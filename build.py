# -*- coding: utf-8 -*-
"""Générateur statique — pôle copropriété & travaux de DGLM Expertises."""
import json, os, shutil, sys, html, datetime, locale

AUJ = datetime.date.today()
ANNEE = AUJ.year
MOIS_FR = ["janvier","février","mars","avril","mai","juin","juillet","août",
           "septembre","octobre","novembre","décembre"]
MAJ = f"{MOIS_FR[AUJ.month-1]} {ANNEE}"
ISO = AUJ.isoformat()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.communes import COMMUNES as METROPOLE, ZONE_ELARGIE
from data.territoires import GIRONDE_ELARGIE, LANDES
from data.diagnostics_pro import DIAGS_PRO
from data.contenus import charger as charger_contenus, en_attente, md_vers_html, sources_html
from data.quartiers import QUARTIERS_BORDEAUX, QUARTIERS_PAR_VILLE
from data.normes import NORMES, CONSULTE_LE
from data.schemas_svg import rendre as rendre_schema
from data.illustrations import SKYLINE, PICTOS, ECHOPPE, ANIM_MISSION, ANIM_PPPT, ANIM_DPE

COMMUNES = METROPOLE + GIRONDE_ELARGIE + LANDES
SLUG_TO_NOM = {c["slug"]: c["nom"] for c in COMMUNES}
# Priorité d'indexation : la métropole d'abord. Les pages hors métropole restent
# servies (maillage intact) mais en noindex et hors sitemap tant que le domaine
# n'a pas d'autorité — protection contre le classement « scaled content abuse ».
# À rouvrir progressivement une fois le site établi.
METRO_SLUGS = {c["slug"] for c in METROPOLE}
GROUPES = [("Bordeaux Métropole", METROPOLE),
           ("Gironde — bassin, Libournais, Sud-Gironde et Médoc", GIRONDE_ELARGIE),
           ("Landes — côte, Dax et Mont-de-Marsan", LANDES)]
from data.services import SERVICES, SERVICE_BY_SLUG, ENTREPRISE as _DGLM
from data.marque import MARQUE, EQUIPE, FORMULAIRE

E = dict(_DGLM)
E.update(MARQUE)
E["nom"] = MARQUE["nom_long"]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
DOM = E["domaine"]
URLS = []  # (path, priority, changefreq)


# ------------------------------------------------------------------ helpers
def esc(s):
    return html.escape(s, quote=True)


def org_schema():
    return {
        "@type": "ProfessionalService",
        "@id": DOM + "/#organisation",
        "name": E["nom"],
        "legalName": E["societe"],
        "alternateName": E["nom"],
        "description": "Bureau d'études spécialisé en copropriété et travaux : repérage "
                       "amiante avant travaux et avant démolition, diagnostic technique "
                       "global et plan pluriannuel de travaux sur Bordeaux Métropole. "
                       "Ne réalise pas de diagnostic de vente ou de location.",
        "url": DOM + "/",
        "telephone": E["tel_raw"],
        "email": E["email"],
        "foundingDate": E["depuis"],
        "priceRange": "€€",
        "address": {"@type": "PostalAddress", "streetAddress": E["rue"],
                    "postalCode": E["cp"], "addressLocality": E["ville"],
                    "addressRegion": "Nouvelle-Aquitaine", "addressCountry": "FR"},
        "geo": {"@type": "GeoCoordinates", "latitude": E["lat"], "longitude": E["lon"]},
        "areaServed": [{"@type": "City", "name": c["nom"]} for c in COMMUNES],
        "identifier": E["siret"],
        "slogan": E.get("signature", ""),
        "knowsAbout": [
            "Repérage amiante avant travaux", "Repérage amiante avant démolition",
            "Diagnostic technique global", "Plan pluriannuel de travaux",
            "Dossier technique amiante", "Diagnostic amiante des parties privatives",
            "Diagnostic PEMD", "DPE collectif de copropriété", "Constat de risque "
            "d'exposition au plomb", "Copropriété", "Rénovation énergétique"],
        "memberOf": {"@type": "Organization",
                     "name": "FIDI — Fédération Interprofessionnelle du Diagnostic Immobilier"},
        "founder": [{"@type": "Person", "name": "Aude de Gentile"},
                    {"@type": "Person", "name": "Thibault Le Moine"}],
        "sameAs": [E["google_avis"], E["diagadvisor"],
                   "https://www.facebook.com/dglmexpertises/"],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "18:30"}],
    }


def page_schema(url, titre_page):
    return {"@type": "WebPage", "@id": url + "#page", "url": url, "name": titre_page,
            "inLanguage": "fr-FR", "dateModified": ISO,
            "isPartOf": {"@id": DOM + "/#site"},
            "publisher": {"@id": DOM + "/#organisation"}}


def jsonld(*blocks):
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": list(blocks)},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def breadcrumb(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOM + u}
        for i, (n, u) in enumerate(trail)]}


def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def titre(*variantes):
    """Retient la première variante de titre qui tient sous 62 caractères."""
    for v in variantes:
        if len(v) <= 62:
            return v
    return variantes[-1][:59].rsplit(" ", 1)[0] + "…"


def desc_courte(t, limite=158):
    return t if len(t) <= limite else t[:limite].rsplit(" ", 1)[0] + "…"


def crumb_html(trail):
    items = "".join(
        f'<li><a href="{u}">{esc(n)}</a></li>' if u else f"<li>{esc(n)}</li>"
        for n, u in trail)
    return f'<nav class="crumb wrap" aria-label="Fil d\'Ariane"><ol>{items}</ol></nav>'


SILO = ""            # site dédié : les prestations sont à la racine
SILO_NOM = None

NAV = "".join(
    f'<a href="{SILO}/{s["slug"]}/" title="{s["nom_court"]}">{s["sigle"]}</a>' for s in SERVICES)

# Menu tiroir : navigation complète, lisible par un néophyte (sigle + intitulé
# en clair), disponible sur tous les formats — téléphone, tablette, ordinateur.
MENU = ('<a href="/">Accueil</a>'
        + "".join(f'<a href="{SILO}/{s["slug"]}/"><b>{s["sigle"]}</b> — {s["nom_court"]}</a>'
                  for s in SERVICES)
        + '<a href="/diagnostics-copropriete/">Les diagnostics de copropriété</a>'
        + '<a href="/le-tableau-des-diagnostics/">Le tableau des diagnostics</a>'
        + f'<a href="{SILO}/simulateur-obligations-copropriete/">Simulateur : suis-je concerné ?</a>'
        + '<a href="/questions/">Guides pratiques</a>'
        + '<a href="/recherche/">Rechercher dans le site</a>'
        + '<a href="/pack-conseil-syndical/">Le pack du conseil syndical</a>'
        + '<a href="/questions/glossaire-diagnostic-immobilier/">Lexique : les sigles en clair</a>'
        + '<a href="/equipe/">Notre équipe</a>'
        + '<a href="/devis/">Demander un devis</a>'
        + '<a href="/particuliers/">Particuliers — vente &amp; location</a>')


OG = {"reperage-amiante-avant-travaux": "raat", "reperage-amiante-avant-demolition": "raad",
      "diagnostic-technique-global": "dtg", "plan-pluriannuel-de-travaux": "pppt",
      "questions": "questions", "bordeaux": "bordeaux"}


def og_pour(path):
    return OG.get(path.strip("/").split("/")[0], "default")


def shell(*, path, title, desc, body, schema="", robots="index,follow", head_extra=""):
    canon = DOM + path
    head = f"""<!doctype html><html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots},max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{esc(E['nom'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:image" content="{DOM}/assets/og/{og_pour(path)}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{DOM}/assets/og/{og_pour(path)}.png">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta name="theme-color" content="#093F30">
<link rel="icon" href="/assets/logo-dglm-vert.png">
<meta name="geo.region" content="FR-33"><meta name="geo.placename" content="Bordeaux">
<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
{head_extra}
{schema}
{jsonld(page_schema(canon, title))}
</head><body>
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="topbar"><div class="wrap">
<span>Diagnostiqueurs certifiés · Copropriété &amp; travaux · Bordeaux Métropole</span>
<a class="topbar__avis" href="{E['google_avis']}" rel="noopener">★ 4,9/5 — avis Google</a>
<a href="/particuliers/">Particulier pour une vente ou une location ? →</a>
<a href="tel:{E['tel_raw']}">{E['tel']}</a></div></div>
<header class="masthead"><div class="wrap">
<a class="brand" href="/"><img src="/assets/logo-dglm-blanc.png" alt="DGLM Expertises"
width="140" height="44" fetchpriority="high"><span>{E['baseline']}</span></a>
<nav class="nav" aria-label="Navigation principale">{NAV}
<a href="/diagnostics-copropriete/">Diagnostics copro</a>
<a href="/le-tableau-des-diagnostics/">Le tableau</a>
<a href="{SILO}/simulateur-obligations-copropriete/">Simulateur</a>
<a href="/questions/">Guides</a>
<a href="/recherche/">Rechercher</a>
<a class="btn" href="/devis/">Demander un devis</a></nav>
<details class="menu"><summary aria-label="Ouvrir le menu">Menu</summary>
<nav class="menu__list" aria-label="Menu complet">{MENU}</nav></details></div></header>
<main id="contenu" tabindex="-1">"""
    foot = f"""</main>
<footer class="footer"><div class="wrap">
<img class="mark" src="/assets/logo-dglm-blanc.png" alt="" width="164" height="52" loading="lazy">
<div class="grid grid--4">
<div><p class="foot-titre">Prestations</p><ul>{"".join(f'<li><a href="{SILO}/{s["slug"]}/">{s["nom"]}</a></li>' for s in SERVICES)}</ul></div>
<div><p class="foot-titre">Vous êtes</p><ul>
<li><a href="{SILO}/syndics-de-copropriete/">Syndic de copropriété</a></li>
<li><a href="{SILO}/bailleurs-et-maitres-d-ouvrage/">Bailleur ou maître d'ouvrage</a></li>
<li><a href="{SILO}/entreprises-de-travaux/">Entreprise de travaux</a></li></ul></div>
<div><p class="foot-titre">Diagnostics copro</p><ul>
<li><a href="/diagnostics-copropriete/">Les neuf missions collectives</a></li>
<li><a href="/dossier-technique-amiante/">Dossier technique amiante</a></li>
<li><a href="/dpe-collectif-copropriete/">DPE collectif</a></li>
<li><a href="/diagnostic-pemd/">Diagnostic PEMD</a></li></ul></div>
<div><p class="foot-titre">Zones</p><ul>
<li><a href="{SILO}/zones-d-intervention/">56 communes, Gironde et Landes</a></li>
<li><a href="{SILO}/{SERVICES[0]['slug']}/bordeaux/">Bordeaux</a></li>
<li><a href="{SILO}/{SERVICES[0]['slug']}/merignac/">Mérignac</a></li>
<li><a href="{SILO}/{SERVICES[0]['slug']}/pessac/">Pessac</a></li></ul></div>
<div><p class="foot-titre">Contact</p><ul>
<li><a href="tel:{E['tel_raw']}">{E['tel']}</a></li>
<li><a href="mailto:{E['email']}">{E['email']}</a></li>
<li><a href="/equipe/">Notre équipe certifiée</a></li>
<li><a href="{E['google_avis']}" target="_blank" rel="noopener">Nos avis Google ★</a></li>
<li><a href="{E['diagadvisor']}" target="_blank" rel="noopener">Avis DiagAdvisor ★</a></li>
<li>{E['rue']}<br>{E['cp']} {E['ville']}</li></ul></div>
</div>
<p class="legalline">{E['nom']} — {E['endossement']} — {E['federation']} — SIRET {E['siret']} — {E['rcs']} ·
Page à jour au {MAJ} ·
<a href="/plan-du-site/">Plan du site</a> ·
<a href="/mentions-legales/">Mentions légales</a> ·
<a href="/particuliers/">{E['site_a_ancre']}</a> ·
Photos d'architecture : Bétium217, Symac — <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" rel="noopener">CC BY-SA</a>, via Wikimedia Commons</p>
</div></footer></body></html>"""
    write(path, head + body + foot)


def write(path, content):
    rel = path.strip("/")
    d = os.path.join(OUT, rel) if rel else OUT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)


def cta(titre="Un chantier à cadrer ? Parlons-en aujourd'hui.",
        texte="Décrivez votre opération : nous vous rappelons dans la journée et vous "
              "adressons un devis chiffré sous deux heures ouvrées."):
    return f"""<section class="cta"><div class="wrap">
<p class="eyebrow eyebrow--pale">Demander un devis</p>
<h2>{esc(titre)}</h2><p>{esc(texte)}</p>
<div class="actions"><a class="btn btn--light" href="tel:{E['tel_raw']}">Appeler le {E['tel']}</a>
<a class="btn btn--light" href="/devis/">Demander un devis</a></div></div></section>"""


def volet(eyebrow, h2, corps, ouvert=False, pale=False, dark=False, ancre=""):
    """Bandeau de section : titre et contenu visibles — on est sur un site web,
    la lecture se fait au défilement. (L'argument ouvert est conservé pour
    compatibilité, il n'a plus d'effet.)"""
    cls = "band" + (" band--pale" if pale else "") + (" band--dark" if dark else "")
    eb = "eyebrow eyebrow--pale" if dark else "eyebrow"
    aid = f' id="{ancre}"' if ancre else ""
    return (f'<section{aid} class="{cls}"><div class="wrap">'
            f'<p class="{eb}">{eyebrow}</p><h2>{h2}</h2>'
            f'<div class="volet__corps">{corps}</div></div></section>')


def fiche_html(fiche):
    """Fiche pratique : la mission résumée en un tableau lisible en 30 secondes."""
    if not fiche:
        return ""
    lignes = "".join(f"<div><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>" for t, d in fiche)
    return f'<dl class="fiche">{lignes}</dl>'


# Carnets de terrain : photos de nos propres missions, vulgarisées.
# (fichier, largeur, hauteur, légende, ce qu'on voit, pourquoi ça compte)
CARNETS = {
    "reperage-amiante-avant-travaux": [
        ("terrain-conduits.jpg", 960, 1280, "Toiture — conduits en fibres-ciment",
         "des conduits en ciment gris posés avant 1997.",
         "à l'époque, ce ciment était souvent armé d'amiante. Tant qu'on n'y touche "
         "pas, il ne libère rien — mais avant des travaux, on prélève et on fait "
         "analyser en laboratoire. C'est exactement ça, un repérage."),
    ],
    "diagnostic-technique-global": [
        ("terrain-solive.jpg", 1200, 568, "Plancher — solive ancienne, renfort récent",
         "une solive rongée par les insectes du bois, doublée par une pièce neuve.",
         "un plancher qui a souffert raconte l'histoire de l'immeuble. Le diagnostic "
         "technique global objective ce qui porte encore, ce qui doit être renforcé, "
         "et à quel horizon."),
    ],
    "etat-parasitaire-avant-travaux": [
        ("terrain-merule.jpg", 481, 640, "Bois de plancher — attaque fongique",
         "un bois qui se délite dans un angle humide.",
         "les champignons lignivores prospèrent sur l'humidité persistante. Repérés "
         "tôt, ils se traitent ; découverts tard, ils emportent plancher et solives."),
    ],
    "reperage-amiante-avant-demolition": [
        ("terrain-combles.jpg", 960, 1280, "Combles — l'envers du décor",
         "un comble où personne n'est monté depuis des années.",
         "avant une démolition, aucune réserve n'est acceptable : le repérage va "
         "partout, y compris là où personne ne regarde jamais."),
    ],
}


def carnets_band(slug):
    items = CARNETS.get(slug)
    if not items:
        return ""
    figs = "".join(
        f'<figure class="photo"><img src="/assets/photos/{f}" alt="{esc(cap)}" '
        f'loading="lazy" decoding="async" width="{w}" height="{h}">'
        f'<figcaption>{esc(cap)}</figcaption>'
        f'<p class="photo__lecon"><b>Ce qu\'on voit :</b> {esc(v)} '
        f'<b>Pourquoi ça compte :</b> {esc(p)}</p></figure>'
        for f, w, h, cap, v, p in items)
    return (f'<section id="terrain" class="band"><div class="wrap">'
            f'<p class="eyebrow">Carnets de terrain</p><h2>Vu en mission</h2>'
            f'<div class="grid grid--2" style="margin-top:1.8rem">{figs}</div></div></section>')


# ------------------------------------------------------------------ accueil
# Site dédié : l'accueil vise directement les requêtes têtes de silo
# (RAAT / RAAD / DTG / PPPT). Aucune requête du site A n'est ciblée.
def page_home(dernier=None):
    actu = (f'<p class="maj">Dernière réponse publiée : '
            f'<a href="/questions/{dernier["slug"]}/">{esc(dernier["titre"])}</a></p>'
            if dernier else "")
    cards = "".join(f"""<a class="card card--link" href="{SILO}/{s['slug']}/">
{PICTOS.get(s['sigle'], '')}<span class="sigle">{s['sigle']}</span><h3>{esc(s['nom'])}</h3>
<p>{esc(s['accroche'])}</p><span class="more">Découvrir la mission →</span></a>""" for s in SERVICES)

    body = f"""<section class="hero hero--photo"><div class="wrap">
<p class="eyebrow eyebrow--pale">RAAT · RAAD · DTG · PPPT — Bordeaux Métropole</p>
<h1>L'expertise du bâti, au service des copropriétés et des maîtres d'ouvrage.</h1>
<p class="lede">Quatre missions techniques déterminent le démarrage d'un chantier et le budget
décennal d'une copropriété : le repérage amiante avant travaux, le repérage avant
démolition, le diagnostic technique global et le plan pluriannuel de travaux. Ce sont les seules que nous exerçons.</p>
<div class="actions">
<a class="btn btn--light" href="{SILO}/simulateur-obligations-copropriete/">Évaluer ma copropriété</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div>
<dl class="refbar">
<div><dt>Spécialité</dt><dd>Copropriété, travaux et démolition</dd></div>
<div><dt>Périmètre</dt><dd>Bordeaux Métropole en priorité — Gironde et Landes sur mission</dd></div>
<div><dt>Intervention</dt><dd>Visite sous 72 heures, rapport sous 48 heures</dd></div>
<div><dt>Analyses</dt><dd>Laboratoire accrédité COFRAC</dd></div>
</dl></div>{SKYLINE}</section>

<section class="parcours"><div class="wrap">
<span class="parcours__label">À chacun son parcours</span>
<a href="{SILO}/syndics-de-copropriete/">Je suis syndic ou conseil syndical</a>
<a href="{SILO}/bailleurs-et-maitres-d-ouvrage/">Je suis bailleur ou maître d'ouvrage</a>
<a href="{SILO}/entreprises-de-travaux/">Je suis une entreprise de travaux</a>
<a href="{SILO}/reperage-amiante-avant-travaux/">Je suis un particulier qui fait des travaux</a>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Quatre missions</p>
<h2>Quatre missions, une même exigence de précision.</h2>
<div class="grid grid--2" style="margin-top:1.8rem">{cards}</div>
{actu}</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Carnets de terrain</p>
<h2>Le terrain, tel que nous le voyons.</h2>
<p class="narrow">Pas de photos de catalogue : nos propres missions, là où le diagnostic
se joue vraiment.</p>
<div class="grid grid--2" style="margin-top:1.8rem">
<figure class="photo"><img src="/assets/photos/terrain-conduits.jpg"
alt="Conduits en fibres-ciment repérés en toiture lors d'une mission amiante"
loading="lazy" decoding="async" width="960" height="1280">
<figcaption>Toiture — conduits en fibres-ciment</figcaption>
<p class="photo__lecon"><b>Ce qu'on voit :</b> des conduits en ciment gris posés avant 1997.
<b>Pourquoi on s'y arrête :</b> à l'époque, ce ciment était souvent armé d'amiante. Tant
qu'on n'y touche pas, il ne libère rien — mais avant des travaux, on prélève et on fait
analyser en laboratoire. C'est exactement ça, un repérage.</p></figure>
<figure class="photo"><img src="/assets/photos/terrain-combles.jpg"
alt="Inspection de combles à la lampe lors d'un repérage"
loading="lazy" decoding="async" width="960" height="1280">
<figcaption>Combles — l'envers du décor</figcaption>
<p class="photo__lecon"><b>Ce qu'on voit :</b> un comble où personne n'est monté depuis des
années. <b>Pourquoi on y va :</b> c'est là que se logent flocages, calorifugeages et
désordres de charpente. Un diagnostic sérieux ne se fait pas depuis le palier :
il va voir.</p></figure>
</div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Le déroulé</p>
<h2>Une mission, quatre temps.</h2>
{ANIM_MISSION}
</div></section>

<section class="band band--dark"><div class="wrap">
<p class="eyebrow eyebrow--pale">Ils nous font confiance</p>
<h2>Notés 4,9 sur 5 par ceux qui nous confient leurs immeubles.</h2>
<p class="narrow" style="color:rgba(248,245,238,.84)">Plus d'une centaine d'avis publics, déposés par des syndics, des conseils
syndicaux et des propriétaires. Nous les lisons tous : c'est la meilleure
relecture de nos rapports.</p>
<div class="actions" style="display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.6rem">
<a class="btn btn--light" href="{E['google_avis']}" rel="noopener">Lire les avis Google</a>
<a class="btn btn--light" href="{E['diagadvisor']}" rel="noopener">Avis certifiés DiagAdvisor</a></div>
</div></section>

<section class="band band--dark"><div class="wrap">
<p class="eyebrow eyebrow--pale">Tout le site, en un clic</p>
<h2>Où voulez-vous aller ?</h2>
<div class="grid grid--3" style="margin-top:1.8rem">
<a class="card card--link" href="/pack-conseil-syndical/"><h3>Le pack du conseil syndical</h3>
<p>Trois check-lists à imprimer pour préparer l'assemblée.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/recherche/"><h3>Rechercher dans le site</h3>
<p>Un sigle, une commune, une question : réponse à la frappe.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/le-tableau-des-diagnostics/"><h3>Le tableau des diagnostics</h3>
<p>Treize missions : qui commande, quand, validité — en une page.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/questions/"><h3>Les guides pratiques</h3>
<p>Toutes nos réponses, classées par thème et mises à jour.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/diagnostics-copropriete/"><h3>Les diagnostics de copropriété</h3>
<p>DTA, DPE collectif, plomb, PEMD, parasitaire, assainissement.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="{SILO}/simulateur-obligations-copropriete/"><h3>Le simulateur d'obligations</h3>
<p>Votre situation établie en six questions, sans inscription.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/bordeaux/"><h3>Bordeaux, quartier par quartier</h3>
<p>Échoppes, pierre, grands ensembles : le bâti tel qu'il est.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="{SILO}/zones-d-intervention/"><h3>Les zones d'intervention</h3>
<p>Bordeaux Métropole en priorité, Gironde et Landes sur mission.</p><span class="more">Ouvrir →</span></a>
</div></div></section>

<section class="band band--pale"><div class="wrap humain">
<div>
<p class="eyebrow">La maison</p>
<h2>Une maison à taille humaine.</h2>
<p class="cite">Nous ne prétendons pas tout savoir d'un immeuble en une visite.
Nous prétendons dire précisément ce que nous avons vu, et ce qu'il reste à vérifier.</p>
<p class="signature">Aude, Thibault et toute l'équipe DGLM</p>
<p><a class="btn btn--ghost" href="/equipe/">Faire connaissance</a></p>
</div>
<ul class="trombine">{"".join(f'<li><picture><source srcset="/assets/equipe/{m["photo"]}.webp" type="image/webp"><img src="/assets/equipe/{m["photo"]}.png" alt="{esc(m["nom"])}" width="76" height="76" loading="lazy" decoding="async"></picture></li>' for m in EQUIPE)}</ul>
</div></section>
{cta()}"""

    shell(path="/", title="RAAT, RAAD, DTG, PPPT à Bordeaux — DGLM Expertises",
          head_extra='<link rel="preload" as="image" href="/assets/photos/hero-immeuble.jpg">',
          desc="Repérage amiante avant travaux et avant démolition, diagnostic technique "
               "global, plan pluriannuel de travaux. Bordeaux Métropole, devis sous 2 h.",
          body=body,
          schema=jsonld(org_schema(),
                        {"@type": "WebSite", "@id": DOM + "/#site", "url": DOM + "/",
                         "name": E["nom"], "inLanguage": "fr-FR",
                         "publisher": {"@id": DOM + "/#organisation"}}))
    URLS.append(("/", "1.0", "weekly"))


# ------------------------------------------------------------------ simulateur
SIM_FAQ = [
    ("Mon immeuble a moins de quinze ans, suis-je concerné par le PPPT ?",
     "Non. L'obligation vise les immeubles à destination totale ou partielle d'habitation "
     "de plus de quinze ans. Le simulateur vous indique l'année exacte à laquelle votre "
     "copropriété entrera dans le champ."),
    ("Un DTG dispense-t-il du plan pluriannuel de travaux ?",
     "Un diagnostic technique global comportant l'ensemble des éléments requis peut tenir "
     "lieu de projet de plan pluriannuel de travaux. C'est souvent la solution la plus "
     "économique : une mission au lieu de deux."),
    ("Le DPE collectif est-il obligatoire dans ma copropriété ?",
     "Il l'est pour les immeubles d'habitation dont le permis de construire est antérieur "
     "à 2013, selon un calendrier échelonné par nombre de lots. Le simulateur applique ce "
     "calendrier à votre situation."),
    ("Qui doit commander le repérage amiante avant travaux dans une copropriété ?",
     "Le syndic, en qualité de donneur d'ordre pour les parties communes. Cette "
     "responsabilité ne se reporte pas sur l'entreprise qui intervient."),
    ("Mes données sont-elles enregistrées ?",
     "Non. Le calcul s'effectue entièrement dans votre navigateur. Aucune information "
     "n'est transmise ni conservée."),
]


def page_simulateur():
    p = SILO + "/simulateur-obligations-copropriete/"
    trail = [("Accueil", "/"), ("Simulateur d'obligations", p)]
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
                  for q, a in SIM_FAQ)
    js = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "build", "simulateur.js"), encoding="utf-8").read()

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Outil gratuit — sans inscription</p>
<h1>Simulateur d'obligations de copropriété</h1>
<p class="lede">PPPT, DTG, DPE collectif, repérage amiante : six questions suffisent à
savoir ce que votre copropriété doit à la réglementation, et depuis quand.</p></div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Échéancier réglementaire</p>
<h2>Le plan pluriannuel de travaux s'applique désormais à l'ensemble du parc.</h2>
<p class="narrow">Issue de la loi Climat et Résilience, l'obligation est entrée en vigueur par
paliers successifs, déterminés par le nombre de lots. Le déploiement est aujourd'hui
achevé : toute copropriété d'habitation de plus de quinze ans y est soumise.</p>
<div class="frise">
<div><b>1<sup>er</sup> janvier 2023</b><span>Copropriétés de plus de 200 lots</span></div>
<div><b>1<sup>er</sup> janvier 2024</b><span>Copropriétés de 51 à 200 lots</span></div>
<div><b>1<sup>er</sup> janvier 2025</b><span>Copropriétés de 50 lots et moins</span></div>
<div><b>Aujourd'hui</b><span>Toutes concernées au-delà de 15 ans d'ancienneté</span></div>
</div></div></section>

<section class="band"><div class="wrap sim">
<form class="sim__form" id="sim" novalidate>
<label class="field"><span>Destination de l'immeuble</span>
<select name="destination">
<option value="totale">Habitation en totalité</option>
<option value="partielle">Habitation partielle (commerces en pied d'immeuble)</option>
<option value="aucune">Aucune habitation (bureaux, activité)</option>
</select></label>

<label class="field"><span>Année d'achèvement</span>
<input type="number" name="annee" min="1700" max="{2026}" placeholder="1972" inputmode="numeric">
<em>Ou la date du permis de construire si vous la connaissez.</em></label>

<label class="field"><span>Nombre de lots</span>
<input type="number" name="lots" min="2" max="5000" placeholder="48" inputmode="numeric">
<em>Lots principaux, tels qu'indiqués au règlement de copropriété.</em></label>

<label class="field"><span>Mise en copropriété d'un immeuble de plus de dix ans ?</span>
<select name="misecopro"><option value="non">Non</option><option value="oui">Oui</option></select></label>

<label class="field"><span>Année du dernier plan pluriannuel de travaux</span>
<input type="number" name="anneepppt" min="2020" max="{2026}" placeholder="aucun" inputmode="numeric"></label>

<label class="field"><span>Année du dernier diagnostic technique global</span>
<input type="number" name="anneedtg" min="2014" max="{2026}" placeholder="aucun" inputmode="numeric"></label>

<label class="field"><span>Année du dernier DPE collectif ou audit énergétique</span>
<input type="number" name="anneedpe" min="2010" max="{2026}" placeholder="aucun" inputmode="numeric"></label>

<label class="field"><span>Des travaux sont-ils prévus sur les parties communes ?</span>
<select name="travaux"><option value="non">Non</option><option value="oui">Oui, dans les 12 mois</option></select></label>

<button class="btn" type="submit">Analyser ma copropriété</button>
</form>

<div id="resultat" aria-live="polite" aria-busy="false">
<p class="verdict__empty">Renseignez au minimum l'année d'achèvement et le nombre de lots.
Le résultat s'affiche immédiatement, ici même.</p></div>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Questions fréquentes</p><h2>Comprendre le résultat</h2>
<div style="margin-top:1.5rem;max-width:74ch">{faq}</div>
<p style="margin-top:2rem"><a href="{SILO}/">Voir le détail des quatre missions →</a></p>
</div></section>
{cta(titre="Votre simulateur affiche des missions en retard ?",
     texte="Envoyez-nous le récapitulatif : nous chiffrons l'ensemble en une seule "
           "proposition, prête à inscrire à l'ordre du jour de votre assemblée.")}
<script>{js}</script>"""

    shell(path=p,
          title="Simulateur d'obligations de copropriété — PPPT, DTG, DPE",
          desc="Vérifiez en 6 questions les obligations de votre copropriété : PPPT, "
               "DTG, DPE collectif, repérage amiante. Gratuit, sans inscription.",
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail), faq_schema(SIM_FAQ),
                        {"@type": "WebApplication", "name": "Simulateur d'obligations de copropriété",
                         "url": DOM + p, "applicationCategory": "BusinessApplication",
                         "operatingSystem": "Tout navigateur web", "inLanguage": "fr-FR",
                         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
                         "publisher": {"@id": DOM + "/#organisation"}}))
    URLS.append((p, "0.9", "monthly"))


# ------------------------------------------------------------------ prestation
# À chaque mission, un schéma explicatif SVG (léger, indexable, sans requête réseau).
SCHEMA_SERVICE = {
    "reperage-amiante-avant-travaux": "coupe-immeuble",
    "reperage-amiante-avant-demolition": "arbre-reperage",
    "diagnostic-technique-global": "dtg-vs-pppt",
    "plan-pluriannuel-de-travaux": "cycle-pppt",
}


def page_service(s):
    p = f"{SILO}/{s['slug']}/"
    trail = [("Accueil", "/"), (s["nom"], p)]
    schema = rendre_schema(SCHEMA_SERVICE.get(s["slug"], ""))
    # Le PPPT a droit à la version animée de son cycle — narrable, sonorisable.
    if s["slug"] == "plan-pluriannuel-de-travaux":
        schema = ANIM_PPPT
    cadre = "".join(f"<dt>{esc(t)}</dt><dd>{esc(d)}</dd>" for t, d in s["cadre"])
    etapes = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in s["etapes"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
                  for q, a in s["faq"])
    autres = "".join(
        f'<a class="card card--link" href="{SILO}/{o["slug"]}/"><span class="sigle">{o["sigle"]}</span>'
        f'<h3>{esc(o["nom"])}</h3><p>{esc(o["accroche"])}</p></a>'
        for o in SERVICES if o["slug"] != s["slug"])
    mesh = "".join(f'<li><a href="{p}{c["slug"]}/">{esc(s["sigle"])} {esc(c["nom"])}</a></li>'
                   for c in COMMUNES)
    schema_bloc = (volet("Repère visuel", "Comprendre en un schéma", schema, pale=True,
                         ancre="schema")
                   if schema else "")

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{s['sigle']} — Bordeaux Métropole</p>
<h1>{esc(s['nom'])} à Bordeaux et en Gironde</h1>
<p class="lede">{esc(s['accroche'])}</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<nav class="ancres" aria-label="Chapitres"><div class="wrap">
<a href="#fiche">L'essentiel</a>{'<a href="#terrain">Sur le terrain</a>' if CARNETS.get(s['slug']) else ''}<a href="#reglementation">Réglementation</a><a href="#methode">Méthode</a>{'<a href="#schema">Le schéma</a>' if schema else ''}<a href="#faq">Questions</a><a href="#communes">Votre commune</a>
</div></nav>
<section id="fiche" class="band"><div class="wrap">
<p class="eyebrow">La fiche pratique</p>
<h2>L'essentiel en trente secondes</h2>
{f'<p class="enclair"><span>En français courant</span>{esc(s["clair"])}</p>' if s.get("clair") else ""}
<div class="prose" style="margin-top:1.4rem"><p style="font-size:1.12rem">{esc(s['intro'])}</p></div>
{fiche_html(s.get('fiche'))}
{'<p class="enclair" style="margin-top:1.6rem"><span>Vous êtes un particulier ?</span>Pour des travaux dans votre propre maison ou votre appartement, vous êtes exactement au bon endroit : ce repérage vaut pour tout donneur d\'ordre — y compris vous.</p>' if s['sigle'] in ('RAAT', 'RAAD') else ''}
</div></section>
{carnets_band(s['slug'])}
{volet("Réglementation", "Ce que dit la réglementation",
       f'<dl class="legal">{cadre}</dl>', pale=True, ancre="reglementation")}
{volet("Notre méthode", "Comment nous menons la mission",
       f'<ol class="steps">{etapes}</ol>', ancre="methode")}
{schema_bloc}
<section id="faq" class="band"><div class="wrap">
<p class="eyebrow">Questions fréquentes</p>
<h2>{esc(s['sigle'])} : ce qu'on nous demande le plus souvent</h2>
<div style="margin-top:1.5rem;max-width:74ch">{faq}</div></div></section>
{volet("Par commune", f"{esc(s['nom_court'])} dans votre commune", ancre="communes",
       corps=f'''<p class="narrow">Le parc bâti change de nature d'une commune à l'autre. Chaque page
détaille les typologies rencontrées localement et les points d'attention qui en découlent.</p>
<ul class="mesh">{mesh}</ul>
<p class="mesh--plain" style="margin-top:1.5rem">Également : {esc(", ".join(ZONE_ELARGIE))}.</p>''',
       pale=True)}
{volet("Nos autres missions", "Prestations liées",
       f'<div class="grid grid--3">{autres}</div>')}
{cta()}"""

    shell(path=p,
          title=titre(f"{s['nom']} ({s['sigle']}) Bordeaux | DGLM",
                      f"{s['nom']} Bordeaux | DGLM",
                      f"{s['sigle']} Bordeaux | DGLM Expertises"),
          desc=desc_courte(s["meta"].format(lieu="Bordeaux et en Gironde")),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail), faq_schema(s["faq"]),
                        {"@type": "HowTo",
                         "name": f"Comment se déroule {s['nom_court'].lower()}",
                         "step": [{"@type": "HowToStep", "position": i + 1, "name": t, "text": x}
                                  for i, (t, x) in enumerate(s["etapes"])]},
                        {"@type": "Service", "serviceType": s["nom"],
                         "name": f"{s['nom']} — Bordeaux Métropole",
                         "provider": {"@id": DOM + "/#organisation"},
                         "areaServed": [{"@type": "City", "name": c["nom"]} for c in COMMUNES],
                         "description": s["intro"]}))
    URLS.append((p, "0.9", "monthly"))


# ------------------------------------------------------------------ prestation × commune
# Points d'attention dérivés de la typologie réelle du bâti communal :
# c'est ce qui différencie une page locale d'une page satellite dupliquée.
TYPO = [
    ("échoppe", {
        "RAAT": "Colles de carrelage et revêtements de sol posés lors des restructurations "
                "des années 1960-1980, sous les parquets flottants récents.",
        "RAAD": "Conduits de fumée en fibres-ciment et cloisons de doublage ajoutées "
                "après-guerre, invisibles sans sondage destructif.",
        "DTG": "Structures en pierre et refends porteurs : fissuration, humidité ascensionnelle "
               "et état des planchers bois à objectiver.",
        "PPPT": "Couverture tuile canal et zinguerie en fin de cycle, souvent le premier "
                "poste de dépense sur dix ans.",
    }),
    ("grands ensembles", {
        "RAAT": "Dalles vinyle-amiante et leurs colles bitumineuses, calorifugeages de "
                "réseaux et joints de dilatation.",
        "RAAD": "Flocages résiduels en gaines techniques, conduits de vide-ordures et "
                "panneaux composites de façade.",
        "DTG": "Réseaux collectifs d'origine, sécurité incendie et accessibilité : les trois "
               "points de non-conformité récurrents.",
        "PPPT": "Isolation thermique par l'extérieur, remplacement des menuiseries et "
                "reprise des réseaux : un plan à dix ans structurellement chargé.",
    }),
    ("industriel", {
        "RAAT": "Bardages et couvertures en fibres-ciment, joints de menuiserie, "
                "calorifugeages de tuyauteries et portes coupe-feu.",
        "RAAD": "Matériaux enfouis, dalles semi-rigides et enrobés : le repérage doit "
                "descendre sous le niveau du sol fini.",
        "DTG": "Charpentes métalliques et couvertures de grande portée, à évaluer avec "
               "leurs conditions d'accès.",
        "PPPT": "Peu de collectif d'habitation concerné : la demande porte surtout sur "
                "les copropriétés mixtes en pied d'immeuble.",
    }),
    ("agricole", {
        "RAAT": "Plaques ondulées en fibres-ciment de couverture, très fréquentes sur les "
                "hangars et dépendances antérieurs à 1997.",
        "RAAD": "Bâtiments annexes et abris démolis sans permis : le repérage reste "
                "obligatoire quelle que soit la taille de l'ouvrage.",
        "DTG": "Bâti hétérogène issu d'extensions successives, à décomposer par période "
               "de construction.",
        "PPPT": "Copropriétés peu nombreuses, essentiellement issues de divisions de bâti "
                "ancien.",
    }),
    ("viticole", {
        "RAAT": "Couvertures de chais et de dépendances en fibres-ciment, souvent hors "
                "champ des diagnostics de vente déjà réalisés.",
        "RAAD": "Cuveries et bâtiments techniques anciens : sondages destructifs "
                "indispensables avant démolition.",
        "DTG": "Bâti ancien à structure mixte pierre et bois, avec pathologies d'humidité "
               "spécifiques.",
        "PPPT": "Parc de copropriétés limité, majoritairement récent.",
    }),
]
DEFAUT = {
    "RAAT": "Revêtements de sol souples et leurs colles, conduits, joints de menuiserie et "
            "enduits de rebouchage des bâtiments antérieurs à juillet 1997.",
    "RAAD": "Matériaux non accessibles en exploitation normale : doublages, planchers "
            "intermédiaires, réseaux encastrés.",
    "DTG": "État apparent du clos et du couvert, conformité des équipements communs et "
           "niveau réel d'entretien au regard du carnet.",
    "PPPT": "Couverture, menuiseries et réseaux : le triptyque qui structure la plupart "
            "des plans à dix ans sur ce type de parc.",
}


def vigilance(s, c):
    txt = (c["parc"] + " " + c["enjeu"]).lower()
    out = []
    for cle, table in TYPO:
        if cle in txt and table[s["sigle"]] not in out:
            out.append(table[s["sigle"]])
    if not out:
        out.append(DEFAUT[s["sigle"]])
    out.append(
        f"Contraintes d'accès et de stationnement propres à {c['nom']}, à intégrer au "
        f"planning d'intervention sur {', '.join(c['quartiers'][:2])}.")
    return out


def page_local(s, c):
    p = f"{SILO}/{s['slug']}/{c['slug']}/"
    trail = [("Accueil", "/"), (s["nom"], f"{SILO}/{s['slug']}/"), (c["nom"], p)]
    lieu = f"{c['nom']} ({c['cp']})"
    cadre = "".join(f"<dt>{esc(t)}</dt><dd>{esc(d)}</dd>" for t, d in s["cadre"][:2])
    etapes = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in s["etapes"])

    faq_loc = [
        (f"Intervenez-vous sur tout {c['nom']} ?",
         "Oui, sur l'ensemble de la commune, y compris " +
         ", ".join(c["quartiers"][:4]) +
         f". Notre agence est basée à {E['ville']}, à quelques minutes de {c['nom']}."),
        (f"Quel délai pour un {s['sigle'].lower()} à {c['nom']} ?",
         "Nous intervenons sur site sous 72 heures ouvrées et remettons le rapport sous "
         "48 heures après réception des résultats de laboratoire. Une intervention en "
         "urgence est possible : appelez-nous directement."),
    ] + s["faq"][:3]
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
                  for q, a in faq_loc)

    voisins = "".join(
        f'<li><a href="{SILO}/{s["slug"]}/{v}/">{esc(SLUG_TO_NOM[v])}</a></li>'
        for v in c["voisins"] if v in SLUG_TO_NOM)
    autres = "".join(
        f'<li><a href="{SILO}/{o["slug"]}/{c["slug"]}/">{esc(o["sigle"])} à {esc(c["nom"])}</a></li>'
        for o in SERVICES if o["slug"] != s["slug"])

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{s['sigle']} — {esc(c['nom'])} {c['cp']}</p>
<h1>{esc(s['nom'])} à {esc(c['nom'])}</h1>
<p class="lede">{esc(s['accroche'])} Intervention sur {esc(c['nom'])} et l'ensemble de
Bordeaux Métropole sous 72 heures.</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<section class="band"><div class="wrap prose">
<p style="font-size:1.12rem">{esc(s['intro'])}</p>

<h2>Le parc bâti de {esc(c['nom'])}</h2>
<p>{esc(c['parc'])}</p>
<p>{esc(c['enjeu'])}</p>
<p>Nous intervenons notamment sur {esc(", ".join(c['quartiers']))}, pour des
{esc(s['cible'])}.</p>

<h2>Ce que nous relevons le plus souvent à {esc(c['nom'])}</h2>
<ul>{"".join(f"<li>{esc(x)}</li>" for x in vigilance(s, c))}</ul>

<h2>Cadre réglementaire applicable</h2>
<dl class="legal">{cadre}</dl>
<p>Le déroulé complet de la mission, étape par étape, est détaillé sur la page
<a href="{SILO}/{s['slug']}/">{esc(s['nom'])}</a>.</p>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Questions fréquentes — {esc(c['nom'])}</p>
<h2>Ce que les donneurs d'ordre de {esc(c['nom'])} nous demandent</h2>
<div style="margin-top:1.5rem;max-width:74ch">{faq}</div></div></section>

<section class="band"><div class="wrap grid grid--2">
<div><h2>Nos autres missions à {esc(c['nom'])}</h2>
<ul class="mesh">{autres}</ul></div>
<div><h2>{esc(s['sigle'])} dans les communes voisines</h2>
<ul class="mesh">{voisins}</ul></div>
</div></section>
{cta(titre=f"Un {s['sigle']} à faire à {c['nom']} ?",
     texte="Envoyez-nous le descriptif de l'opération : devis chiffré sous deux heures "
           "ouvrées, intervention sous 72 heures.")}"""

    shell(path=p,
          title=titre(f"{s['nom']} {c['nom']} | DGLM",
                      f"{s['sigle']} {c['nom']} — {s['nom_court']} | DGLM",
                      f"{s['sigle']} {c['nom']} {c['cp']} | DGLM"),
          desc=desc_courte(s["meta"].format(lieu=lieu)),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail), faq_schema(faq_loc),
                        {"@type": "Service", "serviceType": s["nom"],
                         "name": f"{s['nom']} à {c['nom']}",
                         "provider": {"@id": DOM + "/#organisation"},
                         "areaServed": {"@type": "City", "name": c["nom"],
                                        "address": {"@type": "PostalAddress",
                                                    "postalCode": c["cp"],
                                                    "addressLocality": c["nom"],
                                                    "addressCountry": "FR"}},
                         "description": c["enjeu"]}),
          robots="index,follow" if c["slug"] in METRO_SLUGS else "noindex,follow")
    if c["slug"] in METRO_SLUGS:
        URLS.append((p, "0.8", "monthly"))


# ------------------------------------------------------------------ zones
def page_zones():
    p = f"{SILO}/zones-d-intervention/"
    trail = [("Accueil", "/"), ("Zones d'intervention", p)]
    lignes = "".join(f"""<div class="card"><span class="sigle">{c['cp']}</span>
<h3>{esc(c['nom'])}</h3><p>{esc(c['parc'][:180])}…</p>
<ul class="mesh" style="margin-top:.6rem">
{"".join(f'<li><a href="{SILO}/{s["slug"]}/{c["slug"]}/">{s["sigle"]}</a></li>' for s in SERVICES)}
</ul></div>""" for c in COMMUNES)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">28 communes</p>
<h1>Nos zones d'intervention sur Bordeaux Métropole</h1>
<p class="lede">Basés à {E['ville']}, nous couvrons l'intégralité de la métropole
bordelaise et une large part de la Gironde.</p></div></section>
<section class="band"><div class="wrap">
<div class="grid grid--3">{lignes}</div>
<h2 style="margin-top:3rem">Au-delà de la métropole</h2>
<p class="narrow">Nous intervenons également, sur devis, dans les communes suivantes :</p>
<p class="mesh--plain">{esc(", ".join(ZONE_ELARGIE))}.</p>
</div></section>{cta()}"""
    shell(path=p, title="Zones d'intervention — Bordeaux Métropole | DGLM",
          desc="RAAT, RAAD, DTG et PPPT dans les 28 communes de Bordeaux Métropole et en "
               "Gironde. Intervention sous 72 h.",
          body=body, schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.7", "monthly"))


# ------------------------------------------------------------------ pages métier
AUDIENCES = [
    dict(slug="syndics-de-copropriete", titre="Syndics de copropriété",
         h1="DTG, PPPT et repérages amiante pour les syndics de Bordeaux Métropole",
         lede="Des rapports votables en assemblée générale, et un interlocuteur qui vient "
              "les défendre devant les copropriétaires.",
         desc="Diagnostic technique global, plan pluriannuel de travaux et repérage amiante "
              "avant travaux pour syndics de copropriété à Bordeaux et en Gironde.",
         corps=[
             ("Le calendrier que vous devez tenir",
              "Toutes les copropriétés d'habitation de plus de quinze ans sont désormais "
              "soumises au projet de plan pluriannuel de travaux. Pour un portefeuille de "
              "plusieurs dizaines d'immeubles, la question n'est plus de savoir s'il faut "
              "les traiter, mais dans quel ordre et à quel rythme."),
             ("Une mission, pas deux",
              "Un diagnostic technique global comportant l'ensemble des éléments requis "
              "peut tenir lieu de projet de plan pluriannuel de travaux. Nous vérifions "
              "systématiquement si votre copropriété peut être traitée en une seule "
              "mission plutôt qu'en deux."),
             ("Le repérage avant travaux sur parties communes",
              "Dès qu'une entreprise intervient sur les parties communes d'un immeuble "
              "antérieur à juillet 1997, le repérage amiante avant travaux s'impose. "
              "C'est le syndic, en qualité de donneur d'ordre, qui en porte la charge."),
             ("Présentation en assemblée générale",
              "Nous nous déplaçons pour présenter nos conclusions et répondre aux "
              "questions des copropriétaires. Un rapport bien expliqué se vote ; un "
              "rapport envoyé par mail se reporte d'un an."),
         ]),
    dict(slug="bailleurs-et-maitres-d-ouvrage", titre="Bailleurs et maîtres d'ouvrage",
         h1="Repérages amiante sur patrimoine occupé et opérations de démolition",
         lede="Des campagnes multi-sites organisées, des rapports annexables directement "
              "aux pièces de marché.",
         desc="Repérage amiante avant travaux et avant démolition pour bailleurs sociaux, "
              "aménageurs et maîtres d'ouvrage à Bordeaux Métropole.",
         corps=[
             ("Le site occupé change tout",
              "Un repérage en logement occupé suppose une organisation : prise de rendez-vous, "
              "information des locataires, taux de pénétration, gestion des refus et des "
              "absences. Nous cadrons ces points avant l'intervention, pas pendant."),
             ("Des pièces exploitables en marché",
              "Nos rapports comportent la localisation précise, les croquis, les "
              "photographies et l'estimation des quantités par matériau. Une entreprise "
              "doit pouvoir chiffrer son lot désamiantage sans revenir sur site."),
             ("Démolition : anticiper le budget réel",
              "Sur une opération de démolition, les conclusions du repérage déterminent "
              "une part significative du coût. Réalisé trop tard, il fait exploser le "
              "budget prévisionnel après attribution des marchés."),
             ("Responsabilité du donneur d'ordre",
              "L'obligation de repérage pèse sur vous, pas sur l'entreprise. Le rapport "
              "doit être remis à toutes les entreprises consultées dès la phase d'appel "
              "d'offres."),
         ]),
    dict(slug="entreprises-de-travaux", titre="Entreprises de travaux",
         h1="Repérage amiante avant travaux et avant démolition pour les entreprises",
         lede="Un repérage rapide, chiffrable, qui ne vous laisse pas découvrir l'amiante "
              "le jour de l'ouverture des cloisons.",
         desc="Repérage amiante avant travaux et avant démolition pour entreprises du "
              "bâtiment et de démolition à Bordeaux et en Gironde. Intervention sous 72 h.",
         corps=[
             ("Réactivité",
              "Nous intervenons sous 72 heures ouvrées et rendons le rapport sous 48 "
              "heures après analyse. Sur les opérations urgentes, appelez-nous : nous "
              "vous disons immédiatement ce qui est faisable."),
             ("Le repérage n'est pas à votre charge — mais il vous protège",
              "L'obligation pèse sur le donneur d'ordre. En pratique, c'est vous qui "
              "subissez l'arrêt de chantier si le repérage manque. Nous vous aidons à "
              "formaliser la demande auprès du maître d'ouvrage."),
             ("Des quantitatifs pour chiffrer",
              "Un rapport qui se contente de dire « présence d'amiante » ne vous sert à "
              "rien. Nous localisons, quantifions et décrivons les matériaux pour que "
              "votre plan de retrait s'appuie sur des données réelles."),
             ("Levée de doute en cours de chantier",
              "Un matériau inattendu apparaît à l'ouverture ? Nous nous déplaçons pour "
              "prélever et faire analyser, afin de limiter la durée d'arrêt."),
         ]),
]


def page_audience(a):
    p = f"{SILO}/{a['slug']}/"
    trail = [("Accueil", "/"), (a["titre"], p)]
    corps = "".join(f"<h2>{esc(t)}</h2><p>{esc(d)}</p>" for t, d in a["corps"])
    cards = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/"><span class="sigle">{s["sigle"]}</span>'
        f'<h3>{esc(s["nom"])}</h3><p>{esc(s["accroche"])}</p></a>' for s in SERVICES)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{esc(a['titre'])}</p>
<h1>{esc(a['h1'])}</h1><p class="lede">{esc(a['lede'])}</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>
<section class="band"><div class="wrap prose">{corps}</div></section>
<section class="band band--pale"><div class="wrap"><p class="eyebrow">Prestations</p>
<h2>Nos quatre missions</h2>
<div class="grid grid--2" style="margin-top:1.6rem">{cards}</div></div></section>{cta()}"""
    shell(path=p, title=titre(f"{a['titre']} — RAAT, DTG, PPPT Bordeaux | DGLM",
                              f"{a['titre']} : RAAT, DTG, PPPT | DGLM",
                              f"{a['titre']} — Bordeaux | DGLM"),
          desc=desc_courte(a["desc"]), body=body, schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.7", "monthly"))


# ------------------------------------------------------------------ contact
def page_contact():
    p = "/contact/"
    trail = [("Accueil", "/"), ("Contact", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Demander un devis ouvrées</p>
<h1>Décrivez votre opération, nous chiffrons.</h1>
<p class="lede">Un appel suffit le plus souvent à cadrer la mission : nature des travaux,
année de construction, surface concernée, échéance.</p>
<div class="actions"><a class="btn btn--light" href="tel:{E['tel_raw']}">Appeler le {E['tel']}</a>
<a class="btn" href="mailto:{E['email']}">{E['email']}</a></div></div></section>
<section class="band"><div class="wrap grid grid--2">
<div class="card"><h3>Nous joindre</h3>
<p><a href="tel:{E['tel_raw']}">{E['tel']}</a><br><a href="mailto:{E['email']}">{E['email']}</a></p>
<p>{E['rue']}<br>{E['cp']} {E['ville']}<br>Sur rendez-vous uniquement</p>
<p>Du lundi au vendredi, 8 h – 18 h 30.</p></div>
<div class="card"><h3>Pour un devis rapide, précisez</h3>
<ul class="prose"><li>La commune et l'adresse du bien</li>
<li>L'année de construction ou la date du permis</li>
<li>La nature exacte des travaux ou de la démolition</li>
<li>La surface ou le nombre de lots concernés</li>
<li>Votre échéance de démarrage</li></ul></div>
</div></section>{cta()}"""
    shell(path=p, title="Contact et devis — DGLM Expertises Bordeaux",
          desc=desc_courte(f"Contactez DGLM Expertises pour un RAAT, RAAD, DTG ou PPPT "
                           f"à Bordeaux. Demander un devis ouvrées. {E['tel']}."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail),
                                   {"@type": "ContactPage", "url": DOM + p}))
    URLS.append((p, "0.8", "yearly"))


def page_mentions():
    p = "/mentions-legales/"
    body = f"""<section class="band"><div class="wrap prose">
<h1>Mentions légales</h1>
<h2>Éditeur</h2><p><strong>{E['nom']}</strong> est une marque exploitée par
{E['societe']}, société immatriculée sous le SIRET {E['siret']} — {E['rcs']}.</p>
<p>Établissement : {E['rue']}, {E['cp']} {E['ville']}.<br>
Téléphone : {E['tel']} — Courriel : {E['email']}.</p>
<h2>Activités distinctes</h2><p>{E['nom']} intervient exclusivement sur les missions de
copropriété, de travaux et de démolition : repérage amiante avant travaux et avant
démolition, diagnostic technique global, plan pluriannuel de travaux.</p>
<p>Les diagnostics obligatoires de vente et de location (DPE, amiante, plomb, termites,
gaz, électricité, mesurage) sont réalisés par {E['site_a_nom']}, sous une marque et un
site distincts : <a href="{E['site_a_url']}">{E['site_a_url']}</a>.</p>
<h2>Certifications</h2><p>Diagnostiqueurs certifiés par un organisme accrédité COFRAC.
Attestations d'assurance responsabilité civile professionnelle et de certification
communiquées sur simple demande.</p>
<h2>Hébergement</h2><p>À compléter avant mise en ligne.</p>
<h2>Données personnelles</h2><p>Les informations transmises via le formulaire de contact
sont utilisées uniquement pour répondre à votre demande et établir un devis. Vous disposez
d'un droit d'accès, de rectification et de suppression en écrivant à {E['email']}.</p>
</div></section>"""
    shell(path=p, title=f"Mentions légales — {E['nom']}",
          desc="Mentions légales de DGLM Expertises.", body=body,
          schema=jsonld(org_schema()), robots="noindex,follow")




# ------------------------------------------------------------------ diagnostics pro
# Chaque titre porte un qualificatif collectif/professionnel : c'est la
# frontière qui empêche la collision avec le site A.
SCHEMA_DIAG = {
    "dossier-technique-amiante": "coupe-immeuble",
    "amiante-parties-privatives": "dta-vs-dapp",
    "diagnostic-pemd": "arbre-reperage",
    "dpe-collectif-copropriete": "calendrier-dpe",
    "audit-energetique-copropriete": "dpe-vs-audit",
    "crep-parties-communes": "crep-1949",
    "etat-parasitaire-avant-travaux": "agents-bois",
    "installations-collectives-gaz-electricite": "qui-fait-quoi",
    "conformite-assainissement-copropriete": "eaux-separatif",
}


def page_diag_pro(d):
    p = f"/{d['slug']}/"
    trail = [("Accueil", "/"), (d["nom"], p)]
    schema = rendre_schema(SCHEMA_DIAG.get(d["slug"], ""))
    if d["slug"] == "dpe-collectif-copropriete":
        schema = ANIM_DPE
    schema_bloc = (volet("Repère visuel", "Comprendre en un schéma", schema,
                         ancre="schema")
                   if schema else "")
    cadre = "".join(f"<dt>{esc(t)}</dt><dd>{esc(x)}</dd>" for t, x in d["cadre"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
                  for q, a in d["faq"])
    autres = "".join(
        f'<a class="card card--link" href="/{o["slug"]}/"><span class="sigle">{esc(o["sigle"])}</span>'
        f'<h3>{esc(o["nom"])}</h3><p>{esc(o["accroche"])}</p></a>'
        for o in DIAGS_PRO if o["slug"] != d["slug"])[:2400]
    groupes = "".join(
        f'<h3 style="margin-top:1.6rem">{esc(t)}</h3><ul class="mesh">'
        + "".join(f'<li><a href="/{SERVICES[0]["slug"]}/{c["slug"]}/">{esc(c["nom"])}</a></li>'
                  for c in lst) + "</ul>"
        for t, lst in GROUPES)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{esc(d['sigle'])} — copropriétés, bailleurs, maîtres d'ouvrage</p>
<h1>{esc(d['h1'])}</h1>
<p class="lede">{esc(d['accroche'])}</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<nav class="ancres" aria-label="Chapitres"><div class="wrap">
<a href="#fiche">L'essentiel</a>{'<a href="#terrain">Sur le terrain</a>' if CARNETS.get(d['slug']) else ''}<a href="#reglementation">Réglementation</a>{'<a href="#schema">Le schéma</a>' if schema else ''}<a href="#faq">Questions</a>
</div></nav>
<section id="fiche" class="band"><div class="wrap">
<p class="eyebrow">La fiche pratique</p>
<h2>L'essentiel en trente secondes</h2>
{f'<p class="enclair"><span>En français courant</span>{esc(d["clair"])}</p>' if d.get("clair") else ""}
<div class="prose" style="margin-top:1.4rem"><p style="font-size:1.12rem">{esc(d['intro'])}</p></div>
{fiche_html(d.get('fiche'))}
</div></section>
{carnets_band(d['slug'])}
{volet("Réglementation", "Ce que dit la réglementation", ancre="reglementation",
       corps=f'''<dl class="legal">{cadre}</dl>
<h3 style="margin-top:2.2rem;color:var(--vert)">Une pratique distincte du diagnostic de transaction</h3>
<p>Un diagnostic de vente se rend en vingt-quatre heures sur un logement vacant. Une
mission collective se conduit sur un immeuble habité, au rythme d'un conseil syndical
et d'un calendrier d'assemblée. Ce sont deux métiers ; nous exerçons le second.</p>
<p>Nos rapports sont conçus pour être présentés en assemblée générale et annexés à un
marché de travaux, non pour être classés dans un dossier de compromis.</p>''',
       pale=True)}
{schema_bloc}
<section id="faq" class="band band--pale"><div class="wrap">
<p class="eyebrow">Questions fréquentes</p><h2>Les questions les plus fréquentes</h2>
<div style="margin-top:1.5rem;max-width:74ch">{faq}</div></div></section>
{volet("Missions liées", "Missions généralement associées",
       f'<div class="grid grid--3">{autres}</div>')}
{volet("Périmètre", "Où nous intervenons", groupes, dark=True)}
{cta()}"""

    shell(path=p, title=titre(f"{d['nom']} — Bordeaux, Gironde, Landes",
                             f"{d['nom']} | DGLM Expertises",
                             f"{d['sigle']} — {d['nom']}"),
          desc=desc_courte(d["meta"].format(lieu="Bordeaux, en Gironde et dans les Landes")),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail), faq_schema(d["faq"]),
                        {"@type": "Service", "serviceType": d["nom"],
                         "name": d["nom"], "provider": {"@id": DOM + "/#organisation"},
                         "areaServed": [{"@type": "City", "name": c["nom"]} for c in COMMUNES],
                         "description": d["intro"]}))
    URLS.append((p, "0.85", "monthly"))



def page_tableau():
    """La page-bible : chaque mission et diagnostic de copropriété en un tableau."""
    p = "/le-tableau-des-diagnostics/"
    trail = [("Accueil", "/"), ("Le tableau des diagnostics", p)]
    LIGNES = [
        ("RAAT", "Repérage amiante avant travaux", "Le donneur d'ordre : syndic, maître d'ouvrage, bailleur",
         "Avant tous travaux, bâti d'avant juillet 1997", "Rapport sous 48 h après analyses COFRAC",
         f"{SILO}/reperage-amiante-avant-travaux/"),
        ("RAAD", "Repérage amiante avant démolition", "Le maître d'ouvrage",
         "Avant démolition totale ou partielle, bâti d'avant juillet 1997",
         "Exhaustif, sondages destructifs, bâtiment libéré",
         f"{SILO}/reperage-amiante-avant-demolition/"),
        ("DTG", "Diagnostic technique global", "Le syndic, sur vote ou obligation",
         "Mise en copropriété d'un immeuble de plus de 10 ans, insalubrité, ou vote en AG",
         "Un DTG complet peut tenir lieu de PPPT",
         f"{SILO}/diagnostic-technique-global/"),
        ("PPPT", "Plan pluriannuel de travaux", "Le syndic",
         "Copropriété d'habitation de plus de 15 ans",
         "Établi pour 10 ans, actualisé tous les 10 ans",
         f"{SILO}/plan-pluriannuel-de-travaux/"),
        ("DTA", "Dossier technique amiante", "Le syndic",
         "Parties communes, permis d'avant juillet 1997",
         "À tenir à jour à chaque travaux",
         "/dossier-technique-amiante/"),
        ("DAPP", "Amiante des parties privatives", "Chaque propriétaire de lot",
         "Logements en collectif d'avant juillet 1997",
         "Liste A seule — ne remplace pas un repérage avant travaux",
         "/amiante-parties-privatives/"),
        ("PEMD", "Produits, équipements, matériaux, déchets", "Le maître d'ouvrage",
         "Démolition ou rénovation significative : plus de 1 000 m² ou substances dangereuses",
         "Récolement à transmettre après travaux",
         "/diagnostic-pemd/"),
        ("DPE collectif", "DPE de l'immeuble entier", "Le syndic",
         "Copropriété d'habitation, permis antérieur à 2013 — toutes depuis le 1er janvier 2026",
         "Validité 10 ans",
         "/dpe-collectif-copropriete/"),
        ("Audit énergétique", "Scénarios de rénovation chiffrés", "L'assemblée générale (démarche volontaire)",
         "En préparation d'une rénovation",
         "Conditionne l'accès à plusieurs aides",
         "/audit-energetique-copropriete/"),
        ("CREP communes", "Constat plomb des parties communes", "Le syndicat des copropriétaires",
         "Immeubles d'habitation d'avant 1949",
         "Définitif si absence de plomb ou revêtements sains",
         "/crep-parties-communes/"),
        ("État parasitaire", "Termites, mérule, xylophages", "Maître d'ouvrage ou acquéreur",
         "Avant travaux ou acquisition, bâti ancien — Gironde et Landes en zone termites",
         "Expertise contractuelle, au-delà du seul contrôle termites",
         "/etat-parasitaire-avant-travaux/"),
        ("Gaz & électricité collectifs", "Contrôle des installations communes", "Le syndic — auprès d'un organisme agréé",
         "Au titre de l'entretien de l'immeuble et du dossier assureur",
         "Réalisé par un organisme de contrôle agréé, pas par un diagnostiqueur : nous vous orientons",
         "/installations-collectives-gaz-electricite/"),
        ("Assainissement", "Conformité du raccordement", "Le syndicat et chaque copropriétaire",
         "Avant la mise en demeure de la collectivité",
         "À inscrire au plan pluriannuel plutôt qu'à subir en urgence",
         "/conformite-assainissement-copropriete/"),
    ]
    rangs = "".join(
        f'<tr><td data-l="Mission"><a href="{u}"><b>{esc(s)}</b></a><span>{esc(n)}</span></td>'
        f'<td data-l="Qui le commande">{esc(q)}</td>'
        f'<td data-l="Quand">{esc(qd)}</td>'
        f'<td data-l="Le point clé">{esc(pc)}</td></tr>'
        for s, n, q, qd, pc, u in LIGNES)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(LIGNES)} missions et diagnostics · mis à jour {MAJ}</p>
<h1>Tous les diagnostics de copropriété, en un tableau.</h1>
<p class="lede">Qui commande quoi, quand, et le point qui change tout — la page à mettre en
favori et à partager en conseil syndical. Chaque ligne renvoie vers la fiche complète.</p></div></section>
<section class="band"><div class="wrap">
<table class="tabmaitre">
<thead><tr><th>Mission</th><th>Qui le commande</th><th>Quand</th><th>Le point clé</th></tr></thead>
<tbody>{rangs}</tbody></table>
<p class="maj">Vérifié au {MAJ} — mis à jour automatiquement à chaque évolution réglementaire</p>
<p style="margin-top:1.6rem">Vente et location d'un logement : ces diagnostics relèvent d'un autre
cadre — nos <a href="/questions/">réponses détaillées</a> les couvrent, et notre site
<a href="/particuliers/">dédié aux particuliers</a> les réalise.</p>
</div></section>
{cta()}"""
    shell(path=p, title="Le tableau des diagnostics de copropriété — DGLM Expertises",
          desc=desc_courte("Chaque mission et diagnostic de copropriété en un tableau : qui le "
                           "commande, quand, validité et point clé. Vérifié et mis à jour."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "Table", "about": "Diagnostics de copropriété",
                         "name": "Le tableau des diagnostics de copropriété"}))
    URLS.append((p, "0.9", "weekly"))


def page_pack():
    """Le pack du conseil syndical : trois check-lists imprimables.
    L'outil que les conseils syndicaux s'échangent — et qui ramène vers nous."""
    p = "/pack-conseil-syndical/"
    trail = [("Accueil", "/"), ("Le pack du conseil syndical", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Outil gratuit — à imprimer et partager</p>
<h1>Le pack du conseil syndical</h1>
<p class="lede">Trois check-lists pour aborder l'assemblée et les diagnostics sans rien
oublier. Imprimez-les, cochez-les, faites-les circuler.</p>
<div class="actions"><button class="btn btn--light" onclick="window.print()">Imprimer ou enregistrer en PDF</button></div>
</div></section>
<section class="band"><div class="wrap prose">
<h2>1. Les documents à réunir avant l'assemblée</h2>
<ul class="checklist">
<li>Le règlement de copropriété et l'état descriptif de division</li>
<li>Le carnet d'entretien, à jour</li>
<li>Le dossier technique amiante (DTA) et sa fiche récapitulative</li>
<li>Le dernier DPE collectif ou audit énergétique, s'il existe</li>
<li>Le plan pluriannuel de travaux ou le DTG existant, avec sa date</li>
<li>Les procès-verbaux des trois dernières assemblées</li>
<li>Les contrats d'exploitation en cours (chauffage, ascenseur, entretien)</li>
</ul>
<h2>2. Les questions à poser à un diagnostiqueur avant de le retenir</h2>
<ul class="checklist">
<li>Êtes-vous certifié, par un organisme accrédité COFRAC, pour chaque mission proposée ?</li>
<li>Pouvez-vous fournir votre attestation d'assurance responsabilité civile professionnelle ?</li>
<li>Vos analyses passent-elles par un laboratoire accrédité COFRAC ?</li>
<li>Le rapport comprendra-t-il localisation, photographies et quantitatifs exploitables ?</li>
<li>Présentez-vous vos conclusions devant le conseil syndical ou l'assemblée ?</li>
<li>Quels sont vos délais d'intervention et de remise du rapport ?</li>
</ul>
<h2>3. Le calendrier type d'une mission bien menée</h2>
<ul class="checklist">
<li>J−90 : demande de devis, comparaison, vérification des certifications</li>
<li>J−60 : inscription de la mission à l'ordre du jour de l'assemblée</li>
<li>J−30 : vote, ordre de service, collecte des documents de l'immeuble</li>
<li>Jour J : visite sur site — accès organisés, occupants prévenus</li>
<li>J+15 : rapport remis, lecture commentée avec le conseil syndical</li>
<li>Assemblée suivante : présentation des conclusions et vote des suites</li>
</ul>
<p class="maj">Établi par l'équipe DGLM Expertises — vérifié au {MAJ}</p>
</div></section>
{cta()}"""
    shell(path=p, title="Le pack du conseil syndical — check-lists à imprimer | DGLM",
          desc=desc_courte("Trois check-lists gratuites : documents à réunir avant "
                           "assemblée, questions à poser à un diagnostiqueur, "
                           "calendrier type de mission."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.8", "monthly"))


def _norm_recherche(s):
    import unicodedata as _u
    return _u.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def page_recherche(contenus):
    """Recherche instantanée, entièrement locale : l'index est embarqué dans
    la page, le filtrage se fait dans le navigateur. Zéro requête, zéro serveur."""
    p = "/recherche/"
    trail = [("Accueil", "/"), ("Rechercher", p)]
    idx = []

    def add(t, u, d, extra="", art=0):
        e = {"t": t, "u": u, "d": d[:170],
             "n": _norm_recherche(f"{t} {d} {extra}")}
        if art:
            e["a"] = 1
        idx.append(e)

    for s in SERVICES:
        add(f"{s['nom']} ({s['sigle']})", f"{SILO}/{s['slug']}/", s["accroche"], s["kw"])
    for d in DIAGS_PRO:
        add(d["nom"], f"/{d['slug']}/", d["accroche"], d["sigle"])
    for c in contenus:
        add(c["titre"], f"/questions/{c['slug']}/", c["meta"], " ".join(c["tags"]), art=1)
    # Définitions des sigles pour la réponse express (uniquement nos données).
    defs = {}
    for s in SERVICES:
        defs[_norm_recherche(s["sigle"])] = f"{s['nom_court']}. {s['accroche']}"
    for d in DIAGS_PRO:
        sig = _norm_recherche(d["sigle"].split()[0])
        if sig not in defs and len(sig) <= 6:
            defs[sig] = f"{d['nom']}. {d['accroche']}"
    add("Le tableau des diagnostics", "/le-tableau-des-diagnostics/",
        "Treize missions : qui commande, quand, validité — en une page.", "tableau récapitulatif")
    add("Simulateur d'obligations", f"{SILO}/simulateur-obligations-copropriete/",
        "Votre situation établie en six questions.", "pppt dtg dpe obligations")
    add("Notre équipe", "/equipe/", "Des noms, des visages, des signatures.", "diagnostiqueurs certifiés")
    add("Zones d'intervention", f"{SILO}/zones-d-intervention/",
        "Bordeaux Métropole en priorité, Gironde et Landes sur mission.", "communes secteur")
    add("Demande de devis", "/devis/", "Devis chiffré sous deux heures ouvrées.", "contact rappel")
    add("Normes et textes", "/referentiel-des-normes/",
        "Norme, arrêté et article de code applicables à chaque diagnostic.", "afnor réglementation")
    add("Bordeaux, quartier par quartier", "/bordeaux/",
        "Échoppes, pierre, grands ensembles : le bâti tel qu'il est.", "quartiers")
    for q in QUARTIERS_BORDEAUX:
        add(f"{q['nom']} — Bordeaux", f"/bordeaux/{q['slug']}/", q["intro"][:110], "quartier")
    for ville in QUARTIERS_PAR_VILLE:
        add(f"{ville['nom']}, quartier par quartier", f"/{ville['slug']}/", ville.get("intro", "")[:110] if isinstance(ville, dict) else "", "quartiers")
    for s in SERVICES:
        for c in METROPOLE:
            add(f"{s['sigle']} à {c['nom']}", f"{SILO}/{s['slug']}/{c['slug']}/",
                f"{s['nom_court']} à {c['nom']} ({c['cp']}).", "commune")

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(idx)} pages indexées — recherche instantanée</p>
<h1>Que cherchez-vous ?</h1>
<p class="lede">Un sigle, une commune, une question : les résultats s'affichent à la frappe.
Tout reste dans votre navigateur, rien n'est transmis.</p></div></section>
<section class="band"><div class="wrap">
<label class="field" style="max-width:34rem"><span>Votre recherche</span>
<input type="search" id="q" placeholder="dtg, amiante, Mérignac, fonds de travaux…" autofocus autocomplete="off"></label>
<div id="rep" style="margin-top:2rem"></div>
<div class="grid grid--2" id="res" style="margin-top:2rem"></div>
</div></section>"""
    js = ("<script>const IDX=" + json.dumps(idx, ensure_ascii=False) + ";"
          "const DEFS=" + json.dumps(defs, ensure_ascii=False) + ";"
          "const MAIL='" + E["email"] + "';"
          "const inp=document.getElementById('q'),out=document.getElementById('res'),rep=document.getElementById('rep');"
          "function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase()}"
          "function lienQ(){const su=encodeURIComponent('Question pour vos guides pratiques');"
          "const co=encodeURIComponent('Bonjour, voici ma question : '+inp.value.trim());"
          "return '<p style=\"margin-top:1.2rem\"><a class=\"btn btn--ghost\" href=\"mailto:'+MAIL+'?subject='+su+'&body='+co+'\">Nous envoyer cette question</a></p>'}"
          "function go(){const q=norm(inp.value.trim());rep.innerHTML='';"
          "if(q.length<2){out.innerHTML='';return}"
          "const terms=q.split(/\\s+/).filter(Boolean);const sc=[];"
          "for(const e of IDX){let s=0;for(const t of terms){if(e.n.includes(t))s+=(norm(e.t).includes(t)?3:1)}"
          "if(s>=terms.length)sc.push([s,e])}"
          "sc.sort((a,b)=>b[0]-a[0]);"
          "let defs='';for(const k in DEFS){if(terms.includes(k)){defs+='<p><b>'+k.toUpperCase()+'</b> — '+DEFS[k]+'</p>'}}"
          "if(!sc.length){const VOC=[...new Set(IDX.flatMap(e=>e.n.split(/[^a-z0-9]+/g)))].filter(w=>w.length>3);"
          "function lev(a,b){if(Math.abs(a.length-b.length)>2)return 9;let pr=[...Array(b.length+1).keys()];"
          "for(let i=1;i<=a.length;i++){const c=[i];for(let j=1;j<=b.length;j++){c[j]=Math.min(pr[j]+1,c[j-1]+1,pr[j-1]+(a[i-1]===b[j-1]?0:1))}pr=c}return pr[b.length]}"
          "const sugg=terms.map(tm=>{if(tm.length<4)return tm;let best=tm,bd=3;for(const w of VOC){const d=lev(tm,w);if(d<bd){bd=d;best=w}}return best}).join(' ');"
          "if(sugg&&norm(sugg)!==q){rep.innerHTML='<div class=\"repexp\"><p><b>Vouliez-vous dire « </b><a href=\"#\" id=\"sug\">'+sugg+'</a><b> » ?</b></p></div>';"
          "const sg=document.getElementById('sug');if(sg)sg.onclick=ev=>{ev.preventDefault();inp.value=sugg;go()}}}"
          "const arts=sc.filter(x=>x[1].a);"
          "if(arts.length||defs){const best=arts.length?arts[0][1]:null;"
          "let h='<p class=\"eyebrow\">Réponse express — assemblée depuis nos guides, sans rien inventer</p>'+defs;"
          "if(best){h+='<h3>'+best.t+'</h3><p>'+best.d+'</p>'"
          "+'<p><a class=\"btn btn--ghost\" href=\"'+best.u+'\">Lire la réponse complète</a></p>';"
          "const plus=arts.slice(1,3).map(x=>'<li><a href=\"'+x[1].u+'\">'+x[1].t+'</a></li>').join('');"
          "if(plus)h+='<p style=\"margin-top:1rem\"><b>Pour aller plus loin :</b></p><ul>'+plus+'</ul>'}"
          "rep.innerHTML='<div class=\"repexp\">'+h+'</div>'}"
          "out.innerHTML=sc.slice(0,24).map(x=>{const e=x[1];return '<a class=\"card card--link\" href=\"'+e.u+'\"><h3>'+e.t+'</h3><p>'+e.d+'</p><span class=\"more\">Ouvrir →</span></a>'}).join('')"
          "||('<div><p>Nous n\\'avons pas encore de guide qui réponde à cette question — elle mérite peut-être le sien, et nous l\\'écrirons.</p>'+lienQ()+'</div>')}"
          "inp.addEventListener('input',go);"
          "const p0=new URLSearchParams(location.search).get('q');if(p0){inp.value=p0;go()}"
          "</script>")
    shell(path=p, title="Rechercher — DGLM Expertises",
          desc="Recherche instantanée dans les missions, guides pratiques, communes et "
               "quartiers couverts par DGLM Expertises.",
          body=body + js + cta(),
          schema=jsonld(org_schema(), breadcrumb(trail)),
          robots="noindex,follow")


def page_hub_diags():
    p = "/diagnostics-copropriete/"
    trail = [("Accueil", "/"), ("Diagnostics de copropriété", p)]
    phares = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/">{PICTOS.get(s["sigle"], "")}'
        f'<span class="sigle">{s["sigle"]}</span>'
        f'<h3>{esc(s["nom"])}</h3><p>{esc(s["accroche"])}</p>'
        f'<span class="more">Découvrir la mission →</span></a>' for s in SERVICES)
    cards = "".join(
        f'<a class="card card--link" href="/{d["slug"]}/"><span class="sigle">{esc(d["sigle"])}</span>'
        f'<h3>{esc(d["nom"])}</h3><p>{esc(d["accroche"])}</p>'
        f'<span class="more">Voir →</span></a>' for d in DIAGS_PRO)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Quatre missions phares, neuf diagnostics complémentaires</p>
<h1>Les diagnostics de copropriété et de patrimoine</h1>
<p class="lede">D'abord nos quatre spécialités — repérages amiante, diagnostic technique
global, plan pluriannuel. Puis les diagnostics collectifs qui complètent la gestion d'un
immeuble, pour syndics, bailleurs et maîtres d'ouvrage.</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>
<section class="band"><div class="wrap">
<p class="eyebrow">Une pratique distincte</p>
<h2>Un immeuble occupé ne se diagnostique pas comme un logement à vendre</h2>
<p class="narrow">Le diagnostic de transaction répond à une échéance : un délai court, un bien le
plus souvent vacant, un décideur unique. La mission collective suppose un conseil
syndical, un calendrier d'assemblée, un budget voté et des occupants sur place. Nous n'exerçons que la seconde.</p>
<p style="margin-top:1.4rem"><a class="btn btn--ghost" href="/le-tableau-des-diagnostics/">Tout voir en un tableau</a></p>
</div></section>
<section class="band"><div class="wrap">
<p class="eyebrow">Niveau 1 — nos spécialités</p>
<h2>Les quatre missions phares</h2>
<div class="grid grid--2" style="margin-top:1.8rem">{phares}</div></div></section>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Niveau 2 — les compléments</p>
<h2>Les neuf diagnostics collectifs</h2>
<div class="grid grid--3" style="margin-top:1.8rem">{cards}</div></div></section>
{cta()}"""
    shell(path=p, title="Diagnostics de copropriété : DTA, DPE collectif, PEMD, plomb",
          desc=desc_courte("Diagnostics collectifs pour copropriétés et patrimoines à "
                           "Bordeaux, en Gironde et dans les Landes : DTA, DPE collectif, "
                           "audit énergétique, PEMD, CREP parties communes."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p,
                         "name": "Diagnostics de copropriété"}))
    URLS.append((p, "0.9", "weekly"))



# ------------------------------------------------------------------ équipe (E-E-A-T)
def page_equipe():
    p = "/equipe/"
    trail = [("Accueil", "/"), ("Notre équipe", p)]
    fiches = "".join(
        f'<article><picture><source srcset="/assets/equipe/{m["photo"]}.webp" type="image/webp">'
        f'<img class="portrait" src="/assets/equipe/{m["photo"]}.png" '
        f'alt="{esc(m["nom"])}, {esc(m["role"].split(chr(8212))[0].strip())}" '
        f'width="112" height="112" loading="lazy" decoding="async"></picture>'
        f'<h3>{esc(m["nom"])}</h3><p class="role">{esc(m["role"])}</p>'
        f'<p>{esc(m["bio"])}</p>'
        + (f'<p class="cert">{esc(m["cert"])}</p>' if m["cert"] else "")
        + "</article>" for m in EQUIPE)
    personnes = []
    for m in EQUIPE:
        pers = {"@type": "Person", "@id": DOM + "/equipe/#" + m["photo"],
                "name": m["nom"], "jobTitle": m["role"],
                "worksFor": {"@id": DOM + "/#organisation"},
                "image": DOM + f"/assets/equipe/{m['photo']}.png"}
        if m.get("cert"):
            pers["hasCredential"] = {"@type": "EducationalOccupationalCredential",
                                     "credentialCategory": "certification",
                                     "name": m["cert"]}
        personnes.append(pers)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Sept personnes, quatre diagnostiqueurs certifiés</p>
<h1>Des noms, des visages, et des signatures au bas des rapports.</h1>
<p class="lede">Fondée en 2020 par Aude de Gentile et Thibault Le Moine, la maison réunit sept
personnes, dont quatre diagnostiqueurs certifiés. Chaque rapport est signé par celui
qui l'a établi.</p></div></section>
<section class="band"><div class="wrap">
<p class="eyebrow">L'équipe</p><h2>Celles et ceux qui interviennent</h2>
<div class="team">{fiches}</div>
<p class="maj">Effectif et certifications à jour au {MAJ}</p></div></section>
<section class="band"><div class="wrap prose">
<h2>Une maison à taille humaine</h2>
<p>DGLM Expertises a été fondée en 2020 par Aude de Gentile et Thibault Le Moine.
Structure familiale et indépendante, elle le demeure par choix : celui de connaître les
immeubles dont on nous confie la charge, et les personnes qui nous les confient.</p>
<p>Nos rapports portent la signature de diagnostiqueurs certifiés, joignables pour en
commenter les conclusions devant un conseil syndical. Lorsque la mission le justifie,
nous nous déplaçons en assemblée générale.</p></div></section>
<section class="band band--pale"><div class="wrap prose">
<h2>Certifications et assurances</h2>
<p>Nos diagnostiqueurs sont certifiés par un organisme accrédité COFRAC pour chacune des
compétences qu'ils exercent. Les attestations de certification et l'attestation de
responsabilité civile professionnelle sont communiquées sur simple demande, et jointes
à chaque dossier de consultation.</p>
<h2>Fédération professionnelle</h2>
<p>DGLM Expertises est membre de la {E['federation']}.</p>
<h2>Analyses en laboratoire</h2>
<p>Tous les prélèvements sont analysés en laboratoire accrédité COFRAC. Aucun matériau n'est classé « présumé amianté » par commodité : le doute se lève
par l'analyse.</p>
</div></section>
{cta()}"""
    shell(path=p, title="Notre équipe de diagnostiqueurs certifiés — DGLM Expertises",
          desc=desc_courte("Les diagnostiqueurs certifiés de DGLM Expertises à Bordeaux : "
                           "équipe, certifications COFRAC, membre FIDI. Structure familiale "
                           "créée en 2020."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail), *personnes))
    URLS.append((p, "0.7", "monthly"))



# ------------------------------------------------------------------ contenus éditoriaux
# Une page = une question réelle, réponse directe dès le premier paragraphe.
# C'est le format que citent les moteurs IA : ils reprennent la phrase qui
# répond, pas le paragraphe d'introduction.
def _slug_ancre(t):
    import re as _re, unicodedata as _u
    t = _u.normalize("NFD", t).encode("ascii", "ignore").decode()
    return _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60] or "section"


def sommaire_article(corps):
    """Ancre chaque h2 et rend un sommaire cliquable (navigation au clic).
    Retourne (corps_avec_ancres, html_du_sommaire)."""
    import re as _re
    titres = _re.findall(r"<h2>(.*?)</h2>", corps)
    if len(titres) < 3:
        return corps, ""
    vus, items = set(), []
    def _remp(m):
        t = m.group(1)
        a = _slug_ancre(strip_tags(t))
        while a in vus:
            a += "-b"
        vus.add(a)
        items.append((a, t))
        return f'<h2 id="{a}">{t}</h2>'
    corps = _re.sub(r"<h2>(.*?)</h2>", _remp, corps)
    liens = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in items)
    som = (f'<nav class="sommaire-art" aria-label="Sommaire">'
           f'<p class="eyebrow">Dans cette page</p><ol>{liens}</ol></nav>')
    return corps, som


def page_contenu(c, voisins):
    p = f"/questions/{c['slug']}/"
    trail = [("Accueil", "/"), ("Guides pratiques", "/questions/"), (c["titre"], p)]
    corps = md_vers_html(c["corps"])
    corps, som = sommaire_article(corps)
    # Glossaire : chaque terme reçoit une ancre, et un index cliquable
    # remplace le sommaire — la porte d'entrée du lexique.
    if c["slug"].startswith("glossaire"):
        import re as _re
        termes = []

        def _anc(m):
            terme = strip_tags(m.group(1)).split(" — ")[0].strip().rstrip(".")
            a = "t-" + _slug_ancre(terme)
            termes.append((terme, a))
            return f'<li id="{a}"><strong>{m.group(1)}</strong>'
        corps = _re.sub(r"<li><strong>(.*?)</strong>", _anc, corps)
        if termes:
            chips = "".join(f'<li><a href="#{a}">{esc(t)}</a></li>'
                            for t, a in sorted(termes, key=lambda x: x[0].lower()))
            som = (f'<nav class="sommaire-art" aria-label="Index des termes">'
                   f'<p class="eyebrow">Index — {len(termes)} termes, de A à Z</p>'
                   f'<ul class="mesh">{chips}</ul></nav>')
    # Un article peut embarquer un schéma : champ « schema: » du frontmatter.
    schema_art = rendre_schema(c.get("schema", ""))
    liens = "".join(f'<li><a href="{u}">{esc(u.strip("/").replace("-", " ").capitalize())}</a></li>'
                    for u in c["liens"])
    autres = "".join(
        f'<a class="card card--link" href="/questions/{o["slug"]}/"><h3>{esc(o["titre"])}</h3>'
        f'<span class="more">Lire →</span></a>' for o in voisins[:3])
    tags = "".join(f'<li><span class="mesh--plain">{esc(t)}</span></li>' for t in c["tags"])

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Question fréquente</p>
<h1>{esc(c['titre'])}</h1></div></section>
<article class="band"><div class="wrap prose">{som}{corps}{schema_art}
<p class="maj">Publié le {c['date'].strftime('%d/%m/%Y')} · vérifié au {MAJ} ·
rédigé par l'équipe technique de {E['nom']}</p>
<h2>Pour approfondir</h2><ul>{liens}</ul>
</div></article>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Dans le même champ</p><h2>Autres réponses</h2>
<div class="grid grid--3" style="margin-top:1.5rem">{autres}</div>
<ul class="mesh" style="margin-top:1.5rem">{tags}</ul></div></section>
{cta()}"""

    schema = jsonld(
        org_schema(), breadcrumb(trail),
        {"@type": "Article", "headline": c["titre"][:110],
         "description": c["meta"], "datePublished": c["date"].isoformat(),
         "dateModified": ISO, "inLanguage": "fr-FR",
         "speakable": {"@type": "SpeakableSpecification",
                       "cssSelector": ["h1", ".prose > p:first-of-type"]},
         "author": {"@id": DOM + "/#organisation"},
         "publisher": {"@id": DOM + "/#organisation"},
         "mainEntityOfPage": {"@type": "WebPage", "@id": DOM + p},
         "citation": [{"@type": "CreativeWork", "name": s.split("~")[0],
                       "url": s.split("~")[1] if "~" in s else None}
                      for s in c.get("sources", [])]},
        {"@type": "FAQPage", "mainEntity": [{
            "@type": "Question", "name": c.get("question", c["titre"]),
            "acceptedAnswer": {"@type": "Answer",
                               "text": strip_tags(corps)[:900]}}]})
    shell(path=p, title=titre(c["titre"], c["titre"][:58], c["tags"][0] if c["tags"] else "Question"),
          desc=desc_courte(c["meta"]), body=body, schema=schema)
    URLS.append((p, "0.75", "monthly"))


def strip_tags(h):
    import re as _re
    return _re.sub(r"\s+", " ", _re.sub(r"<[^>]+>", " ", h)).strip()


def page_hub_contenus(contenus):
    p = "/questions/"
    trail = [("Accueil", "/"), ("Guides pratiques", p)]
    # Sous-catégories : chaque thème dans son propre bandeau (fin du fouillis).
    CATS = [
        ("Amiante", "Repérages avant travaux et démolition, DTA, listes A/B/C",
         {"raat", "raad", "amiante", "dta", "dapp"}),
        ("Copropriété, DTG & PPPT", "Diagnostic global, plan de travaux, gouvernance",
         {"dtg", "pppt", "fonds de travaux", "syndic", "assemblée générale",
          "carnet d'entretien", "petite copropriété", "copropriété"}),
        ("Performance énergétique", "DPE, audit énergétique, passoires thermiques",
         {"dpe", "énergie", "audit énergétique", "passoire thermique", "décence"}),
        ("Vente & location", "Obligations, durées de validité, surfaces",
         {"vente", "location", "ddt", "loi carrez", "loi boutin", "surface",
          "meublé", "bailleur", "validité"}),
        ("Plomb, gaz & risques", "CREP, termites, gaz, électricité, ERP, PEMD",
         {"plomb", "crep", "gaz", "électricité", "termites", "parasitaire", "erp",
          "incendie", "débroussaillement", "pemd", "déchets", "santé", "sécurité"}),
        ("Repères & définitions", "Le vocabulaire du diagnostic, en clair",
         {"glossaire", "définitions", "pédagogie"}),
    ]

    def carte(c):
        return (f'<a class="card card--link" href="/questions/{c["slug"]}/">'
                f'<span class="sigle">{esc(" · ".join(c["tags"][:2]))}</span>'
                f'<h3>{esc(c["titre"])}</h3><p>{esc(c["meta"][:150])}</p>'
                f'<span class="more">Lire →</span></a>')

    groupes = {}
    for c in contenus:
        tset = {t.strip().lower() for t in c.get("tags", [])}
        idx = next((i for i, (_, _, k) in enumerate(CATS) if tset & k), len(CATS))
        groupes.setdefault(idx, []).append(c)

    sections, shown = "", 0
    for i, (nom, sub, _) in enumerate(CATS):
        items = groupes.get(i)
        if not items:
            continue
        cartes = "".join(carte(c) for c in items)
        sections += volet(f"{esc(nom)} · {len(items)}", esc(sub),
                          f'<div class="grid grid--2">{cartes}</div>',
                          ouvert=(shown == 0), pale=bool(shown % 2))
        shown += 1
    reste = groupes.get(len(CATS))
    if reste:
        cartes = "".join(carte(c) for c in reste)
        sections += volet(f"Autres réponses · {len(reste)}", "Autres questions fréquentes",
                          f'<div class="grid grid--2">{cartes}</div>',
                          pale=bool(shown % 2))

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(contenus)} réponses · classées par thème</p>
<h1>Ce que l'on nous demande</h1>
<p class="lede">Chaque réponse est rédigée par les diagnostiqueurs qui conduisent les missions,
datée, et revue à chaque évolution réglementaire. Quand nous n'avons pas de réponse assurée,
nous préférons ne pas écrire la page.</p></div></section>
{sections}
{cta()}"""
    shell(path=p, title="Guides pratiques du diagnostic en copropriété",
          desc=desc_courte("Réponses documentées sur le repérage amiante avant travaux, le "
                           "DTG, le plan pluriannuel de travaux et les obligations de "
                           "copropriété, par les diagnostiqueurs de DGLM Expertises."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p,
                         "name": "Guides pratiques", "dateModified": ISO}))
    URLS.append((p, "0.85", "daily"))



# ------------------------------------------------------------------ Bordeaux au quartier
# Granularité que personne ne publie sur Bordeaux. Le bâti d'une échoppe de
# Nansouty, d'un chai des Chartrons et d'une barre du Grand Parc n'a rien de
# commun : c'est un contenu qu'on ne peut pas copier sans faire le terrain.
Q_BY_SLUG = {q["slug"]: q for q in QUARTIERS_BORDEAUX}


def page_quartier(q):
    p = f"/bordeaux/{q['slug']}/"
    trail = [("Accueil", "/"), ("Bordeaux", "/bordeaux/"), (q["nom"], p)]
    missions = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/bordeaux/">'
        f'<span class="sigle">{s["sigle"]}</span><h3>{esc(s["nom"])}</h3>'
        f'<p>{esc(s["accroche"])}</p><span class="more">Découvrir la mission →</span></a>'
        for s in SERVICES)
    voisins = "".join(
        f'<li><a href="/bordeaux/{v}/">{esc(Q_BY_SLUG[v]["nom"])}</a></li>'
        for v in q["voisins"] if v in Q_BY_SLUG)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Bordeaux · {esc(q['nom'])}</p>
<h1>Repérage amiante, DTG et plan pluriannuel de travaux à {esc(q['nom'])}</h1>
<p class="lede">{esc(q['intro'])}</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<section class="band"><div class="wrap prose">
<h2>Le bâti du quartier</h2><p>{esc(q['bati'])}</p>
<h2>Ce que cela implique pour nos missions</h2><p>{esc(q['enjeu'])}</p>
<dl class="legal"><dt>Point de vigilance à {esc(q['nom'])}</dt>
<dd>{esc(q['vigilance'])}</dd></dl>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Nos interventions</p><h2>Les quatre missions</h2>
<div class="grid grid--2" style="margin-top:1.7rem">{missions}</div></div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">À proximité</p><h2>À proximité immédiate</h2>
<ul class="mesh">{voisins}</ul>
<p style="margin-top:1.4rem"><a href="/bordeaux/">Tous les quartiers de Bordeaux →</a> ·
<a href="{SILO}/reperage-amiante-avant-travaux/bordeaux/">Bordeaux, toutes zones</a></p>
</div></section>
{cta()}"""
    shell(path=p,
          title=titre(f"Amiante, DTG et PPPT à Bordeaux {q['nom']}",
                      f"Diagnostics copropriété — Bordeaux {q['nom']}",
                      f"Bordeaux {q['nom']}"),
          desc=desc_courte(f"Repérage amiante avant travaux, DTG et plan pluriannuel de "
                           f"travaux à Bordeaux {q['nom']}. {q['bati'][:70]}"),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "Service", "serviceType": "Diagnostics de copropriété",
                         "provider": {"@id": DOM + "/#organisation"},
                         "areaServed": {"@type": "Place", "name": f"Bordeaux {q['nom']}",
                                        "containedInPlace": {"@type": "City",
                                                             "name": "Bordeaux"}},
                         "description": q["enjeu"][:280]}))
    URLS.append((p, "0.75", "monthly"))


def page_hub_bordeaux():
    p = "/bordeaux/"
    trail = [("Accueil", "/"), ("Bordeaux", p)]
    cards = "".join(
        f'<a class="card card--link" href="/bordeaux/{q["slug"]}/">'
        f'<h3>{esc(q["nom"])}</h3><p>{esc(q["intro"][:135])}…</p>'
        f'<span class="more">Découvrir le quartier →</span></a>' for q in QUARTIERS_BORDEAUX)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page hero--echoppe"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(QUARTIERS_BORDEAUX)} quartiers</p>
<h1>Bordeaux, quartier par quartier.</h1>
<p class="lede">Une échoppe de Nansouty, un chai des Chartrons et une barre du Grand Parc ne
relèvent ni des mêmes sondages, ni du même plan de repérage, ni du même ordre de
grandeur budgétaire. Nous documentons chaque quartier pour lui-même.</p></div></section>
<section class="band"><div class="wrap">
<div class="grid grid--3">{cards}</div></div></section>
{cta()}"""
    shell(path=p, title="Diagnostics de copropriété à Bordeaux, quartier par quartier",
          desc=desc_courte("Repérage amiante, DTG et plan pluriannuel de travaux dans les "
                           "quartiers de Bordeaux : Chartrons, Saint-Michel, Bacalan, "
                           "Caudéran, Grand Parc, Euratlantique."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p, "name": "Bordeaux"}))
    URLS.append((p, "0.9", "monthly"))


# --- Quartiers hors Bordeaux (Mérignac, Pessac) : mêmes gabarits, ville paramétrée ---
def page_quartier_ville(q, ville):
    vslug, vnom = ville["slug"], ville["nom"]
    qmap = {x["slug"]: x for x in ville["quartiers"]}
    p = f"/{vslug}/{q['slug']}/"
    trail = [("Accueil", "/"), (vnom, f"/{vslug}/"), (q["nom"], p)]
    missions = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/{vslug}/">'
        f'<span class="sigle">{s["sigle"]}</span><h3>{esc(s["nom"])}</h3>'
        f'<p>{esc(s["accroche"])}</p><span class="more">Découvrir la mission →</span></a>'
        for s in SERVICES)
    voisins = "".join(
        f'<li><a href="/{vslug}/{v}/">{esc(qmap[v]["nom"])}</a></li>'
        for v in q["voisins"] if v in qmap)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{esc(vnom)} · {esc(q['nom'])}</p>
<h1>Repérage amiante, DTG et plan pluriannuel de travaux à {esc(q['nom'])}</h1>
<p class="lede">{esc(q['intro'])}</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<section class="band"><div class="wrap prose">
<h2>Le bâti du quartier</h2><p>{esc(q['bati'])}</p>
<h2>Ce que cela implique pour nos missions</h2><p>{esc(q['enjeu'])}</p>
<dl class="legal"><dt>Point de vigilance à {esc(q['nom'])}</dt>
<dd>{esc(q['vigilance'])}</dd></dl>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Nos interventions</p><h2>Les quatre missions</h2>
<div class="grid grid--2" style="margin-top:1.7rem">{missions}</div></div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">À proximité</p><h2>À proximité immédiate</h2>
<ul class="mesh">{voisins}</ul>
<p style="margin-top:1.4rem"><a href="/{vslug}/">Tous les quartiers de {esc(vnom)} →</a> ·
<a href="{SILO}/reperage-amiante-avant-travaux/{vslug}/">{esc(vnom)}, toutes zones</a></p>
</div></section>
{cta()}"""
    shell(path=p,
          title=titre(f"Amiante, DTG et PPPT à {vnom} {q['nom']}",
                      f"Diagnostics copropriété — {vnom} {q['nom']}",
                      f"{vnom} {q['nom']}"),
          desc=desc_courte(f"Repérage amiante avant travaux, DTG et plan pluriannuel de "
                           f"travaux à {vnom} {q['nom']}. {q['bati'][:52]}"),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "Service", "serviceType": "Diagnostics de copropriété",
                         "provider": {"@id": DOM + "/#organisation"},
                         "areaServed": {"@type": "Place", "name": f"{vnom} {q['nom']}",
                                        "containedInPlace": {"@type": "City",
                                                             "name": vnom}},
                         "description": q["enjeu"][:280]}))
    URLS.append((p, "0.7", "monthly"))


def page_hub_ville(ville):
    vslug, vnom = ville["slug"], ville["nom"]
    quartiers = ville["quartiers"]
    p = f"/{vslug}/"
    trail = [("Accueil", "/"), (vnom, p)]
    cards = "".join(
        f'<a class="card card--link" href="/{vslug}/{q["slug"]}/">'
        f'<h3>{esc(q["nom"])}</h3><p>{esc(q["intro"][:135])}…</p>'
        f'<span class="more">Découvrir le quartier →</span></a>' for q in quartiers)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(quartiers)} quartiers</p>
<h1>{esc(vnom)}, quartier par quartier.</h1>
<p class="lede">D'un quartier à l'autre, le bâti change : le plan de repérage, l'ampleur des
sondages et l'ordre de grandeur budgétaire ne sont pas les mêmes. Nous documentons chaque
quartier de {esc(vnom)} pour lui-même.</p></div></section>
<section class="band"><div class="wrap">
<div class="grid grid--3">{cards}</div></div></section>
{cta()}"""
    shell(path=p, title=f"Diagnostics copropriété à {vnom}, par quartier",
          desc=desc_courte(f"Repérage amiante, DTG et plan pluriannuel de travaux dans les "
                           f"quartiers de {vnom} : "
                           + ", ".join(q["nom"] for q in quartiers[:5]) + "."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p, "name": vnom}))
    URLS.append((p, "0.85", "monthly"))



def page_404():
    body = f"""<section class="band err404"><div class="wrap">
<p class="code">ERREUR 404</p>
<h1>Cette page n'existe pas ou a été déplacée.</h1>
<p class="narrow" style="margin:1.2rem auto 0">Elle a peut-être changé d'adresse. Les
quatre missions restent accessibles depuis le menu, et le simulateur d'obligations
répond en six questions.</p>
<div class="actions" style="justify-content:center;display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.8rem">
<a class="btn" href="/">Retour à l'accueil</a>
<a class="btn btn--ghost" href="{SILO}/simulateur-obligations-copropriete/">Simulateur d'obligations</a>
<a class="btn btn--ghost" href="/questions/">Guides pratiques</a>
<a class="btn btn--ghost" href="/recherche/">Rechercher dans le site</a></div>
</div></section>"""
    shell(path="/404", title="Page introuvable — DGLM Expertises",
          desc="La page demandée n'existe pas ou a été déplacée.",
          body=body, robots="noindex,follow")



# ------------------------------------------------------------------ demande de devis
def page_devis():
    p = "/devis/"
    trail = [("Accueil", "/"), ("Demande de devis", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Réponse sous deux heures ouvrées</p>
<h1>Demander un devis</h1>
<p class="lede">Le questionnaire s'adapte à la mission. En le remplissant
complètement, vous nous évitez un rappel préalable : nous chiffrons directement.</p>
</div></section>

<section class="band"><div class="wrap">
<form id="devis" class="devis" novalidate>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true"
 style="position:absolute;left:-9999px">

<div class="devis__bloc"><h3>1 · Quelle mission ?</h3>
<div id="devis-choix" class="missions" role="group" aria-label="Choix de la mission"></div></div>

<div class="devis__bloc" style="padding:0;border:0"><h3 style="margin-top:2rem">Vos coordonnées</h3>
{"".join(f'<label class="field" for="c_{c}"><span>{l}</span><input id="c_{c}" name="{c}" type="{t}" required{extra}></label>' for c, l, t, extra in [("nom", "Nom et prénom", "text", ""), ("email", "Courriel", "email", ' inputmode="email" autocomplete="email"'), ("tel", "Téléphone", "tel", ' inputmode="tel" autocomplete="tel"')])}
<label class="field" for="c_qualite"><span>Vous êtes</span>
<select id="c_qualite" name="qualite" required><option value="">— choisir —</option>
{"".join(f"<option>{o}</option>" for o in ["Syndic professionnel", "Conseil syndical ou syndic bénévole", "Bailleur ou administrateur de biens", "Maître d'ouvrage", "Entreprise de travaux", "Architecte ou maître d'œuvre", "Collectivité ou bailleur social", "Particulier"])}
</select></label>
<label class="field" for="c_societe"><span>Société ou copropriété</span>
<input id="c_societe" name="societe" type="text" required></label></div>

<div id="devis-mission" hidden></div>

<div id="devis-envoi" hidden>
<p id="devis-etat" class="devis__etat" role="status" aria-live="polite"></p>
<button type="submit" id="devis-submit" class="btn">Envoyer la demande</button>
<p class="devis__rgpd">Les informations transmises servent uniquement à établir votre
devis. Elles ne sont ni cédées ni exploitées à d'autres fins. Vous pouvez demander leur
suppression à <a href="mailto:{E['email']}">{E['email']}</a>.</p>
</div>
</form>

<div id="devis-succes" class="devis__succes" hidden tabindex="-1">
<h2>Demande transmise.</h2>
<p>Nous revenons vers vous sous deux heures ouvrées. Si votre demande est urgente,
appelez directement le <a href="tel:{E['tel_raw']}">{E['tel']}</a>.</p>
</div>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Avant d'écrire</p>
<h2>Ce qui accélère le chiffrage</h2>
<div class="grid grid--3" style="margin-top:1.6rem">
<div class="card"><h3>L'année de construction</h3><p>C'est elle qui détermine si un
repérage amiante est dû. À défaut, la date du permis de construire.</p></div>
<div class="card"><h3>Le nombre de lots</h3><p>Pour un DTG ou un plan pluriannuel,
c'est la donnée qui structure tout le chiffrage.</p></div>
<div class="card"><h3>Les documents existants</h3><p>Un dossier technique amiante,
même ancien, ou des plans, réduisent le temps d'intervention — et le prix.</p></div>
</div></div></section>
{cta()}"""
    schema = jsonld(org_schema(), breadcrumb(trail),
                    {"@type": "ContactPage", "url": DOM + p, "name": "Demande de devis"})
    extra = (f'<script>window.DEVIS_CFG={{endpoint:"{FORMULAIRE["endpoint"]}",'
             f'cle:"{FORMULAIRE["cle"]}",destinataire:"{FORMULAIRE["destinataire"]}",'
             f'objet:"{FORMULAIRE["objet"]}"}};</script>'
             f'<script src="/assets/devis.js" defer></script>')
    shell(path=p, title="Demander un devis — DGLM Expertises",
          desc=desc_courte("Demande de devis pour un repérage amiante avant travaux, un "
                           "DTG ou un plan pluriannuel de travaux. Réponse sous deux "
                           "heures ouvrées."),
          body=body + extra, schema=schema)
    URLS.append((p, "0.95", "monthly"))



# ------------------------------------------------------------------ référentiel des normes
# Norme AFNOR, arrêté, article de code, pour chaque diagnostic. Contenu de
# référence : c'est ce qui attire les liens de la part des architectes, des
# maîtres d'ouvrage et des écoles du bâtiment.
def page_normes():
    p = "/referentiel-des-normes/"
    trail = [("Accueil", "/"), ("Référentiel des normes", p)]
    BADGE = {"verifie": ("Source primaire consultée", "ok"),
             "etabli": ("Référence de place", "neutre"),
             "a_verifier": ("À confirmer", "attention")}

    fiches = ""
    for n in NORMES:
        lib, cls = BADGE[n["confiance"]]
        lignes = [("Obligation", n["obligation"]), ("Décret", n["decret"]),
                  ("Arrêté", n["arrete"]), ("Norme", n["norme"])]
        dl = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>"
                     for k, v in lignes if v and v != "—")
        lien = (f'<p><a href="{n["lien"]}" rel="noopener nofollow">Consulter le texte '
                f'sur Légifrance</a></p>' if n["lien"] else "")
        fiches += f"""<article class="norme" id="{n['cle']}">
<header><span class="sigle">{esc(n['sigle'])}</span>
<h3>{esc(n['nom'])}</h3>
<span class="badge badge--{cls}">{lib}</span></header>
<p class="norme__titre">{esc(n['norme_titre'])}</p>
<dl class="norme__refs">{dl}</dl>
<p>{esc(n['note'])}</p>
<div class="norme__piege"><strong>Point de vigilance</strong><p>{esc(n['piege'])}</p></div>
{lien}</article>"""

    sommaire = "".join(f'<li><a href="#{n["cle"]}">{esc(n["nom"])}</a></li>'
                       for n in NORMES)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(NORMES)} dispositifs</p>
<h1>Référentiel des normes et des textes</h1>
<p class="lede">Pour chaque diagnostic : la norme AFNOR qui fixe la méthode,
l'arrêté qui la rend opposable, l'article de code qui crée l'obligation — et le
point de vigilance que l'on rencontre sur le terrain.</p>
</div></section>

<section class="band band--nonum"><div class="wrap">
<nav class="sommaire" aria-label="Sommaire du référentiel">
<p class="eyebrow">Sommaire</p><ol>{sommaire}</ol></nav>
</div></section>

<section class="band"><div class="wrap normes">{fiches}
<p class="maj">Références consultées le {CONSULTE_LE}. Les normes et arrêtés
évoluent : ce référentiel est un point de départ documenté, non un avis
juridique. Pour une situation précise, faites-la confirmer.</p>
</div></section>
{cta()}"""

    shell(path=p,
          title="Normes des diagnostics immobiliers — DGLM Expertises",
          desc=desc_courte("Norme AFNOR, arrêté et article de code applicables à chaque "
                           "diagnostic : NF X 46-020, NF C16-600, NF P45-500, NF P03-201, "
                           "NF X 46-030."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "TechArticle", "headline": "Référentiel des normes "
                         "des diagnostics immobiliers", "dateModified": ISO,
                         "inLanguage": "fr-FR",
                         "author": {"@id": DOM + "/#organisation"},
                         "publisher": {"@id": DOM + "/#organisation"},
                         "mainEntityOfPage": {"@type": "WebPage", "@id": DOM + p}}))
    URLS.append((p, "0.9", "monthly"))


# ------------------------------------------------------------------ plan du site
# Accès direct à tout, depuis une seule page : « moins de trois clics vers tout ».
def page_plan(contenus):
    p = "/plan-du-site/"
    trail = [("Accueil", "/"), ("Plan du site", p)]

    def liste(items):
        return "".join(f'<li><a href="{href}">{esc(lbl)}</a></li>' for href, lbl in items)

    prestations = [(f"{SILO}/{s['slug']}/", s["nom"]) for s in SERVICES]
    diags = ([("/diagnostics-copropriete/", "Les neuf diagnostics collectifs")]
             + [(f"/{d['slug']}/", d["nom"]) for d in DIAGS_PRO])
    pourqui = [(f"{SILO}/{a['slug']}/", a["titre"]) for a in AUDIENCES]
    outils = [("/simulateur-obligations-copropriete/", "Simulateur d'obligations"),
              ("/devis/", "Demander un devis"),
              ("/referentiel-des-normes/", "Référentiel des normes"),
              ("/equipe/", "Notre équipe certifiée"),
              ("/contact/", "Contact"),
              ("/questions/", "Toutes les questions fréquentes")]
    zones = [("/zones-d-intervention/", "Toutes les zones — 56 communes"),
             ("/bordeaux/", "Bordeaux et ses quartiers")]
    zones += [(f"/{v['slug']}/", f"{v['nom']} et ses quartiers") for v in QUARTIERS_PAR_VILLE]

    groupes = {}
    for c in contenus:
        tag = (c["tags"][0] if c.get("tags") else "Divers").capitalize()
        groupes.setdefault(tag, []).append((f"/questions/{c['slug']}/", c["titre"]))
    bible = "".join(f'<h3>{esc(t)}</h3><ul class="mesh">{liste(v)}</ul>'
                    for t, v in sorted(groupes.items()))
    bible = bible or "<p>La bibliothèque se remplit au fil des publications.</p>"

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Plan du site</p>
<h1>Accès direct à toute la ressource</h1>
<p class="lede">Toutes nos prestations, tous les diagnostics et toute la bibliothèque
de questions, en un coup d'œil. Un clic pour trouver ce que vous cherchez.</p>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Prestations</p><h2>Nos quatre missions</h2>
<ul class="mesh">{liste(prestations)}</ul></div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Diagnostics de copropriété</p><h2>Les diagnostics collectifs</h2>
<ul class="mesh">{liste(diags)}</ul></div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Pour qui</p><h2>Selon votre profil</h2>
<ul class="mesh">{liste(pourqui)}</ul></div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Outils &amp; ressources</p><h2>Simulateur, devis, référentiel</h2>
<ul class="mesh">{liste(outils)}</ul></div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Zones d'intervention</p><h2>Où nous intervenons</h2>
<ul class="mesh">{liste(zones)}</ul></div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">La bibliothèque</p><h2>Toutes les questions, par thème</h2>
{bible}</div></section>
{cta()}"""

    shell(path=p, title="Plan du site — DGLM Expertises",
          desc=desc_courte("Plan du site DGLM Expertises : prestations, diagnostics de "
                           "copropriété, simulateur, zones et bibliothèque de questions."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.5", "monthly"))


# ------------------------------------------------------------------ pont vers le site particuliers
# Page-relais (noindex) : les particuliers atterrissant ici sont redirigés vers le
# site de vente/location. Un seul point du site référence le domaine A ; le pare-feu
# reste intact car la page n'est pas indexée.
def page_particuliers():
    p = "/particuliers/"
    body = f"""<section class="band"><div class="wrap prose" style="min-height:44vh">
<p class="eyebrow">Vous êtes un particulier ?</p>
<h1>Diagnostics de vente et de location</h1>
<p>Ce site est dédié à la <strong>copropriété, aux travaux et à la démolition</strong>.
Pour un diagnostic destiné à une <strong>vente ou une location</strong> — performance
énergétique, amiante, plomb, gaz, électricité, mesurage — nous vous orientons vers notre
site dédié aux particuliers.</p>
<p><a class="btn" href="{E['site_a_url']}">Continuer vers le site particuliers →</a></p>
<p class="mesh--plain" style="margin-top:1.4rem">Redirection automatique en cours…</p>
</div></section>
<script>window.location.replace("{E['site_a_url']}");</script>"""
    shell(path=p,
          title="Particuliers, vente et location — DGLM Expertises",
          desc="Vous êtes un particulier ? Accédez à notre site dédié aux diagnostics de "
               "vente et de location.",
          body=body, schema="", robots="noindex,follow")


# ------------------------------------------------------------------ build
def sitemap():
    items = "".join(
        f"<url><loc>{DOM}{u}</loc><lastmod>{ISO}</lastmod>"
        f"<changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
        for u, pr, cf in URLS)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           + items + "</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n"
        f"Disallow: /mentions-legales/\nDisallow: /_veille/\nDisallow: /_source/\n"
        f"\nSitemap: {DOM}/sitemap.xml\n")


# llms.txt : carte du site pensée pour les moteurs de réponse (ChatGPT, Claude,
# Perplexity, Gemini). Un index lisible qui aide l'IA à citer les bonnes pages.
def ecrire_llms(contenus):
    def li(url, label, note=""):
        note = " ".join(note.split())
        return f"- [{esc_md(label)}]({DOM}{url})" + (f": {esc_md(note)}\n" if note else "\n")

    md = f"# {E['nom']} — diagnostics de copropriété et travaux\n\n"
    md += ("> Cabinet de diagnostics techniques du bâtiment à Bordeaux Métropole, "
           "spécialisé en copropriété, travaux et démolition : repérage amiante avant "
           "travaux (RAAT) et avant démolition (RAAD), diagnostic technique global (DTG), "
           "plan pluriannuel de travaux (PPPT) et diagnostics collectifs. Ne réalise pas "
           "de diagnostics de vente ni de location.\n\n")
    md += "## Prestations\n"
    for s in SERVICES:
        md += li(f"{SILO}/{s['slug']}/", s["nom"], s["accroche"])
    md += "\n## Diagnostics de copropriété\n"
    for d in DIAGS_PRO:
        md += li(f"/{d['slug']}/", d["nom"])
    md += "\n## Guides pratiques\n"
    for c in contenus:
        md += li(f"/questions/{c['slug']}/", c["titre"], c.get("meta", ""))
    md += "\n## Ressources\n"
    md += li("/simulateur-obligations-copropriete/", "Simulateur d'obligations de copropriété")
    md += li("/referentiel-des-normes/", "Référentiel des normes et des textes")
    md += li("/equipe/", "Notre équipe de diagnostiqueurs certifiés")
    md += li("/plan-du-site/", "Plan du site")
    open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write(md)


def esc_md(s):
    return s.replace("[", "(").replace("]", ")")


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    src = os.path.join(os.path.dirname(OUT), "build")
    shutil.copy(os.path.join(src, "style.css"), os.path.join(OUT, "assets", "style.css"))
    for js in ("simulateur.js", "devis.js"):
        if os.path.exists(os.path.join(src, js)):
            shutil.copy(os.path.join(src, js), os.path.join(OUT, "assets", js))
    shutil.copytree(os.path.join(src, "assets"), os.path.join(OUT, "assets"),
                    dirs_exist_ok=True)
    contenus = charger_contenus()
    page_home(contenus[0] if contenus else None)
    page_simulateur()
    page_hub_diags()
    page_tableau()
    page_recherche(contenus)
    page_pack()
    for d in DIAGS_PRO:
        page_diag_pro(d)
    for s in SERVICES:
        page_service(s)
        for c in COMMUNES:
            page_local(s, c)
    page_zones()
    for a in AUDIENCES:
        page_audience(a)
    page_hub_bordeaux()
    for q in QUARTIERS_BORDEAUX:
        page_quartier(q)
    for ville in QUARTIERS_PAR_VILLE:
        page_hub_ville(ville)
        for q in ville["quartiers"]:
            page_quartier_ville(q, ville)
    if contenus:
        page_hub_contenus(contenus)
        for i, c in enumerate(contenus):
            page_contenu(c, contenus[i+1:] + contenus[:i])
    page_plan(contenus)
    page_particuliers()
    page_normes()
    page_devis()
    page_equipe()
    page_contact()
    page_mentions()
    page_404()
    sitemap()
    ecrire_llms(contenus)
    # Domaine personnalisé GitHub Pages : réécrit à chaque build pour ne pas être perdu.
    open(os.path.join(OUT, "CNAME"), "w", encoding="utf-8").write("www.dglmexpertises.fr\n")
    # Fichier-clé IndexNow (déposé à la racine si le secret est fourni en CI),
    # nécessaire pour la soumission en masse des URLs aux moteurs.
    _cle = os.environ.get("INDEXNOW_KEY", "").strip()
    if _cle:
        open(os.path.join(OUT, _cle + ".txt"), "w", encoding="utf-8").write(_cle)
    print(f"{len(URLS)} URL indexables générées dans {OUT}")


if __name__ == "__main__":
    main()
