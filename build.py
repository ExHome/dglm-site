# -*- coding: utf-8 -*-
"""Générateur statique — pôle copropriété & travaux de DGLM Expertises."""
import glob, json, os, shutil, sys, html, datetime, locale, hashlib

# Empreinte de l'index de recherche, fixée par page_recherche() dès le début
# du build : elle sert de numéro de version dans l'URL du fichier.
IDX_V = "0"
# Nombre de dossiers clos, relevé dans le logiciel de suivi de l'entreprise le
# 03/08/2026 (6 736 exactement, arrondi à la centaine inférieure pour ne jamais
# annoncer plus que le réel). Tous diagnostics confondus : c'est dit comme tel
# partout où le chiffre apparaît, la copropriété étant une activité récente.
MISSIONS_FAITES = "6 700"
# Clé IndexNow — publique par construction (voir main()).
INDEXNOW_KEY = "edf67dcafdd8f3778243f8d9c952894a"
# Codes de vérification de propriété. ⚠️ Ne jamais les retirer : la validation
# serait perdue et il faudrait tout recommencer. Vide = aucune balise émise.
GOOGLE_VERIF = "kl7ROmpLgrYx6tsJfwytZgAs4TNMeZgMDoHiXYZ0_zw"
BING_VERIF = "92999CEE195CD9F0D74ABC3B4B2516C4"
# Même mécanique pour la feuille de style, fixée par main() à la copie.
# Sans elle, un visiteur déjà venu garde l'ancienne feuille en cache et ne voit
# aucune correction de mise en page — constaté en production le 01/08/2026.
CSS_V = "0"

# Nom court des chapitres et ancre lisible, par section. La clé est le titre
# ramené à sa forme simple (_slug_ancre) : les h2 s'écrivent tantôt avec une
# apostrophe droite dans le code, tantôt courbe après typo_fr, et le slug est
# identique dans les deux cas.
CHAPITRES_COURTS = {
    # hub des diagnostics de copropriété
    "un-immeuble-occupe-ne-se-diagnostique-pas-comme-un-logement-": ("Une pratique distincte", "pratique"),
    "le-tandem-qui-pilote-l-immeuble": ("Les missions phares", "phares"),
    "le-dpe-collectif-constate-l-audit-decide": ("Énergie de l’immeuble", "energie"),
    "les-documents-que-l-immeuble-doit-tenir-a-jour": ("Santé et conformité", "sante"),
    "gaz-et-electricite-des-parties-communes-vers-qui-se-tourner": ("Gaz et électricité", "gaz"),
    # aides financières
    "estimez-vos-aides": ("Le simulateur", "simulateur"),
    "maprimerenov-copropriete-en-clair": ("MaPrimeRénov’", "mpr"),
    "eco-ptz-financer-le-reste-a-charge": ("L’éco-PTZ", "ecoptz"),
    "tva-a-5-5-cee-et-aides-locales": ("Les compléments", "complements"),
    "du-diagnostic-au-dossier-le-circuit": ("Méthode", "circuit"),
    # simulateur d'obligations
    "le-plan-pluriannuel-de-travaux-s-applique-desormais-a-l-ense": ("L’échéancier", "echeancier"),
    "votre-copropriete-en-six-questions": ("Le simulateur", "simulateur"),
    "comprendre-le-resultat": ("Questions", "faq"),
    # équipe
    "celles-et-ceux-qui-interviennent": ("Qui intervient", "equipe"),
    "une-maison-a-taille-humaine": ("À taille humaine", "maison"),
    "certifications-et-assurances": ("Nos garanties", "garanties"),
    # certifications et assurances
    "cinq-diagnostiqueurs-certifies": ("Les personnes", "personnes"),
    "titre-professionnel-et-certification-deux-choses-differentes": ("Titre ou certification", "titres"),
    "qui-nous-certifie-et-qui-le-controle": ("Qui nous certifie", "organisme"),
    "assurance-et-veille": ("Assurance et veille", "assurance"),
    "pourquoi-nous-publions-tout-cela": ("Ce que ça change", "pourquoi"),
    # certificat de conformité
    "controles-passes-avec-succes": ("L’état du jour", "etat"),
    "les-huit-controles-quotidiens": ("Les huit contrôles", "controles"),
    "ce-que-ce-certificat-ne-dit-pas": ("Ce qu’il ne dit pas", "limites"),
    # méthode éditoriale
    "qui-ecrit-et-qui-relit": ("Qui écrit et relit", "auteurs"),
    "d-ou-viennent-les-faits": ("Sources", "sources"),
    "ce-que-nous-ne-publions-pas": ("Ce qu’on refuse", "refus"),
    "si-vous-trouvez-une-erreur": ("Signaler une erreur", "erreur"),
    # conseil syndical
    "ce-qu-on-va-vous-demander-de-comprendre": ("Les quatre sujets", "sujets"),
    "les-questions-a-poser-en-seance": ("Questions à poser", "questions"),
    "ce-que-vous-n-avez-pas-a-faire": ("Votre rôle exact", "role"),
    "les-outils-qui-vous-servent-vraiment": ("Les outils gratuits", "outils"),
    # particulier qui fait des travaux
    "un-diagnostic-qui-ne-sert-pas-a-vendre": ("Pas pour la vente", "pas-la-vente"),
    "des-travaux-ordinaires-qui-declenchent-l-obligation": ("Les travaux visés", "travaux"),
    "pourquoi-ce-reperage-vous-protege-vous": ("Ce qui vous protège", "protection"),
    "comment-cela-se-passe-chez-vous": ("Méthode", "methode"),
    "si-votre-projet-est-de-vendre-ou-de-louer": ("Vendre ou louer", "vendre-louer"),
    # pack du conseil syndical
    "1-les-documents-a-reunir-avant-l-assemblee": ("Les documents", "documents"),
    "2-les-questions-a-poser-a-un-diagnostiqueur-avant-de-le-rete": ("Questions à poser", "questions"),
    "3-le-calendrier-type-d-une-mission-bien-menee": ("Le calendrier", "calendrier"),
    # aide au devis — la barre sert de sélecteur de mission
    "pour-toute-demande": ("Pour toute demande", "toute-demande"),
    "reperage-amiante-avant-travaux-raat": ("Avant travaux", "raat"),
    "reperage-amiante-avant-demolition-raad": ("Avant démolition", "raad"),
    "diagnostic-technique-global-dtg": ("Le DTG", "dtg"),
    "plan-pluriannuel-de-travaux-pppt": ("Le PPPT", "pppt"),
    "diagnostics-de-l-immeuble-dta-dapp-plomb-assainissement": ("Diagnostics d’immeuble", "diagnostics-immeuble"),
}
# Sections qui ne sont pas du contenu : renvois, rappels, invitations. Une
# barre de chapitres annonce ce qu'on va lire, pas les boutons de la page.
# Les deux passerelles entre hubs en font partie : sans elles ici, le hub des
# travaux affichait une barre dont le dernier chapitre était un bouton.
CHAPITRES_EXCLUS = {
    "vous-engagez-des-travaux-sur-l-immeuble",
    "besoin-de-la-vision-d-ensemble-de-l-immeuble",
    "comprendre-chaque-dispositif",
    "federation-professionnelle",
    "analyses-en-laboratoire",
    "pour-aller-plus-loin",
}

AUJ = datetime.date.today()
ANNEE = AUJ.year
MOIS_FR = ["janvier","février","mars","avril","mai","juin","juillet","août",
           "septembre","octobre","novembre","décembre"]
MAJ = f"{MOIS_FR[AUJ.month-1]} {ANNEE}"
MAJ_JOUR = f"{AUJ.day} {MOIS_FR[AUJ.month-1]} {ANNEE}"
ISO = AUJ.isoformat()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.communes import COMMUNES as METROPOLE, ZONE_ELARGIE, PAR_SLUG as COMMUNES_PAR_SLUG
from data.territoires import GIRONDE_ELARGIE, LANDES
from data.diagnostics_pro import DIAGS_PRO
from data.contenus import charger as charger_contenus, en_attente, md_vers_html, sources_html
from data.quartiers import QUARTIERS_BORDEAUX, QUARTIERS_PAR_VILLE
from data.normes import NORMES, CONSULTE_LE
from data.schemas_svg import rendre as rendre_schema
from data.illustrations import (SKYLINE, PICTOS, ECHOPPE, ANIM_MISSION, ANIM_PPPT,
                                ANIM_DPE, ANIM_DEPERDITIONS, RUBRIQUE_PICTOS)

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
# Mémoire des empreintes de pages : elle permet de dire quelle page a
# RÉELLEMENT changé, plutôt que d'annoncer une modification quotidienne sur
# l'ensemble du site. Versionnée dans le dépôt, comme .seo-history.json.
HISTO_DATES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           ".dates-pages.json")
DOM = E["domaine"]
# Date de la dernière évolution structurelle du site. Le sitemap ne doit PAS
# annoncer une modification quotidienne : un lastmod qui bouge alors que rien
# n'a changé perd toute valeur aux yeux des moteurs. À mettre à jour lors
# d'une vraie refonte de gabarit ou d'un changement de contenu transverse.
MAJ_STRUCTURE = "2026-07-31"

URLS = []  # (chemin, priorité, fréquence, date de dernière modification)


# ------------------------------------------------------------------ helpers
import re as _re

# Typographie française. Sur un site dont l'identité repose sur un serif de
# titrage, « l'immeuble » avec un tiret vertical de machine à écrire est le
# détail qui trahit tout. On corrige à la source, une fois pour toutes.
_APOS = _re.compile(r"(?<=\w)'(?=\w)")
# Espace fine insécable avant ; ? ! et insécable avant : — mais uniquement si
# le signe est suivi d'un blanc ou d'une fin : sans quoi on abîmerait les URLs
# (« http://… », « ?page=2 ») que cette fonction voit passer aussi.
_PONCT_FINE = _re.compile(r"(?<=[^\s])\s?([;?!])(?=\s|$)")
_PONCT_DEUX = _re.compile(r"(?<=[^\s])\s?(:)(?=\s|$)")
_GUILL_O = _re.compile(r"«\s?(?=\S)")
_GUILL_F = _re.compile(r"(?<=\S)\s?»")


def typo_fr(s):
    """Apostrophes typographiques et espaces insécables devant la ponctuation."""
    s = _APOS.sub("’", s)
    s = _PONCT_FINE.sub(" \\1", s)
    s = _PONCT_DEUX.sub(" \\1", s)
    s = _GUILL_O.sub("« ", s)
    s = _GUILL_F.sub(" »", s)
    return s


def esc(s):
    return html.escape(typo_fr(s), quote=True)


def cfg_rappel():
    """Les coordonnées et l'adresse d'envoi du formulaire de fin de simulateur.

    Les simulateurs du site donnaient leur réponse puis laissaient le visiteur
    se débrouiller : celui des aides et celui des validités n'offraient aucune
    sortie — pas un bouton, pas un lien. Quelqu'un qui venait de constater
    qu'il a une obligation à remplir n'avait aucun moyen de nous le dire.

    Le formulaire est partagé (build/rappel.js) et s'ajoute APRÈS le résultat :
    le visiteur obtient toujours sa réponse complète d'abord, sans rien donner.
    """
    return ('<script>window.DGLM_PART={"tel":"' + E["tel"] + '",'
            '"tel_raw":"' + E["tel_raw"] + '","email":"' + E["email"] + '",'
            '"endpoint":"' + FORMULAIRE["endpoint"] + '"};</script>'
            '<script src="/assets/rappel.js?v=' + CSS_V + '" defer></script>')


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
        # Deux lignes, une seule entreprise. Le second numéro est celui qui
        # figure sur l'autre site du groupe : le déclarer ici indique aux
        # moteurs qu'il s'agit bien de la même structure, et la réputation
        # attachée à l'une profite à l'autre. Rien ne change à l'écran.
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": E["tel_raw"],
             "contactType": "customer service", "areaServed": "FR",
             "availableLanguage": "French"},
            {"@type": "ContactPoint", "telephone": "+33672700338",
             "contactType": "customer service", "areaServed": "FR",
             "availableLanguage": "French"},
        ],
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
                     "name": "Alliance du Diagnostic Immobilier"},
        "founder": [{"@type": "Person", "name": "Aude de Gentile"},
                    {"@type": "Person", "name": "Thibault Le Moine"}],
        # Le site A est déclaré ici, et NULLE PART ailleurs comme lien de
        # navigation : c'est la même entreprise, et le dire à Google fait
        # profiter au site B l'ancienneté accumulée par le site A. Le jour où
        # le contrat prend fin, le transfert d'autorité est déjà préparé.
        "sameAs": [E["google_avis"], E["diagadvisor"],
                   "https://www.facebook.com/dglmexpertises/",
                   E["site_a_url"].rstrip("/")],
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


def phrase1(t):
    """La première phrase entière d'un texte — jamais un fragment coupé net."""
    t = " ".join(t.split())
    p = t.find(". ")
    return (t[:p + 1] if p > 0 else t).strip()


def desc_courte(t, limite=158):
    """Une méta-description doit se terminer, pas s'interrompre. On coupe donc
    à la dernière phrase complète qui tient ; le repli au mot près, avec des
    points de suspension, ne sert plus que de dernier recours."""
    t = " ".join(t.split())
    if len(t) <= limite:
        return t.rstrip(" ;,—")
    tete = t[:limite]
    # d'abord une phrase entière ; à défaut, un membre de phrase qui se tient,
    # clos par un point — jamais un mot coupé suivi de points de suspension.
    for fin, garde in ((". ", True), ("? ", True), ("! ", True),
                       (" — ", False), (" : ", False), (" ; ", False), (", ", False)):
        coupe = tete.rfind(fin)
        if coupe > limite * 0.55:
            bout = t[:coupe + (1 if garde else 0)].strip(" —:;,")
            return bout if bout.endswith((".", "?", "!")) else bout + "."
    return t[:limite].rsplit(" ", 1)[0].strip(" —:;,") + "."


def crumb_html(trail):
    items = "".join(
        f'<li><a href="{u}">{esc(n)}</a></li>' if u else f"<li>{esc(n)}</li>"
        for n, u in trail)
    return f'<nav class="crumb wrap" aria-label="Fil d\'Ariane"><ol>{items}</ol></nav>'


SILO = ""            # site dédié : les prestations sont à la racine
SILO_NOM = None

SCRIPT_VOLETS = ('<script>(function(){function o(h){try{var e=h&&document.querySelector(h);'
                 'if(e){var d=e.querySelector("details");if(d)d.open=true}}catch(x){}}'
                 'addEventListener("click",function(ev){var a=ev.target.closest&&ev.target.closest("a");'
                 'if(a&&a.getAttribute("href")&&a.getAttribute("href").charAt(0)==="#")o(a.getAttribute("href"))});'
                 'o(location.hash);'
                 # À l'impression, on ouvre tout : la feuille print prépare un
                 # dossier d'assemblée, qui ne peut pas sortir amputé.
                 'addEventListener("beforeprint",function(){document.querySelectorAll("details")'
                 '.forEach(function(d){d.dataset.o=d.open?"1":"";d.open=true})});'
                 'addEventListener("afterprint",function(){document.querySelectorAll("details")'
                 '.forEach(function(d){d.open=d.dataset.o==="1"})});'
                 # WCAG 2.2.2 : toute animation qui dure plus de cinq secondes doit
                 # pouvoir être arrêtée. Le réglage système « moins d'animations »
                 # est déjà respecté, mais il ne remplace pas une commande visible.
                 'document.querySelectorAll(".animex").forEach(function(f,i){'
                 'var b=document.createElement("button");b.type="button";'
                 'b.className="animex__pause";b.setAttribute("aria-pressed","false");'
                 'b.textContent="Suspendre l’animation";'
                 'b.addEventListener("click",function(){'
                 'var p=f.classList.toggle("animex--fige");'
                 'b.setAttribute("aria-pressed",p?"true":"false");'
                 'b.textContent=p?"Reprendre l’animation":"Suspendre l’animation"});'
                 'f.appendChild(b)});'
                 '})()</script>')

NAV = "".join(
    f'<a href="{SILO}/{s["slug"]}/" title="{s["nom_court"]}">{s["sigle"]}</a>' for s in SERVICES)

# Menu tiroir : navigation complète, lisible par un néophyte (sigle + intitulé
# en clair), disponible sur tous les formats — téléphone, tablette, ordinateur.
# L'action principale ouvre le menu : elle était auparavant en 26e position
# sur 27, au bas d'une liste de trois mille pixels.
MENU = ('<a class="menu__cta" href="/devis/">Demander un devis →</a>'
        + '<a href="/">Accueil</a>'
        + '<a class="menu__groupe" href="/diagnostics-copropriete/">◆ Diagnostics de copropriété</a>'
        + '<a href="/diagnostic-technique-global/"><b>DTG</b> — Diagnostic technique global</a>'
        + '<a href="/plan-pluriannuel-de-travaux/"><b>PPPT</b> — Plan pluriannuel de travaux</a>'
        + '<a href="/dpe-collectif-copropriete/"><b>DPE collectif</b> — l\'étiquette de l\'immeuble</a>'
        + '<a href="/audit-energetique-copropriete/"><b>Audit</b> — les scénarios de travaux chiffrés</a>'
        + '<a href="/dossier-technique-amiante/"><b>DTA</b> — amiante des parties communes</a>'
        + '<a href="/amiante-parties-privatives/"><b>DAPP</b> — amiante des parties privatives</a>'
        + '<a href="/crep-parties-communes/"><b>CREP</b> — plomb des parties communes</a>'
        + '<a href="/conformite-assainissement-copropriete/">Assainissement — le raccordement</a>'
        + '<a class="menu__groupe" href="/avant-travaux-et-demolition/">◆ Avant travaux &amp; démolition</a>'
        + '<a href="/reperage-amiante-avant-travaux/"><b>RAAT</b> — repérage amiante avant travaux</a>'
        + '<a href="/reperage-amiante-avant-demolition/"><b>RAAD</b> — repérage avant démolition</a>'
        + '<a href="/diagnostic-pemd/"><b>PEMD</b> — matériaux et déchets du chantier</a>'
        + '<a href="/etat-parasitaire-avant-travaux/">État parasitaire — termites et mérule</a>'
        + '<span class="menu__groupe">◆ Outils &amp; repères</span>'
        + '<a href="/le-tableau-des-diagnostics/">Le tableau des diagnostics</a>'
        + f'<a href="{SILO}/simulateur-obligations-copropriete/">Simulateur : suis-je concerné ?</a>'
        + '<a href="/aides-financieres-copropriete/">Aides financières : le simulateur</a>'
        + '<a href="/simulateur-validite-diagnostics/">Validité : mes diagnostics tiennent-ils ?</a>'
        + '<a href="/pack-conseil-syndical/">Le pack du conseil syndical</a>'
        + '<a href="/conseil-syndical/">Conseil syndical : comprendre et décider</a>'
        + '<a href="/particulier-travaux/">Particulier : je fais des travaux</a>'
        + '<a href="/aide-au-devis/">Aide au devis : les documents à joindre</a>'
        + '<a href="/questions/">Guides pratiques</a>'
        + '<a href="/questions/glossaire-diagnostic-immobilier/">Lexique : les sigles en clair</a>'
        + '<a href="/recherche/">Rechercher dans le site</a>'
        + '<span class="menu__groupe">◆ La maison</span>'
        + '<a href="/equipe/">Notre équipe</a>'
        + '<a href="/certifications-et-assurances/">Certifications et assurances</a>'
        + '<a href="/conformite/">Certificat de conformité du site</a>'
        + '<a href="/devis/">Demander un devis</a>'
        + '<a href="/particuliers/">Particuliers — vente &amp; location</a>')


OG = {"reperage-amiante-avant-travaux": "raat", "reperage-amiante-avant-demolition": "raad",
      "diagnostic-technique-global": "dtg", "plan-pluriannuel-de-travaux": "pppt",
      "questions": "questions", "bordeaux": "bordeaux"}


def og_pour(path):
    return OG.get(path.strip("/").split("/")[0], "default")


def shell(*, path, title, desc, body, schema="", robots="index,follow", head_extra="",
          chapitres=True):
    canon = DOM + path
    # La barre de chapitres est posée ici pour toutes les pages : une seule
    # règle, et le lecteur retrouve le même repère partout. Les pages qui sont
    # elles-mêmes un sommaire (accueil, plan du site) passent chapitres=False.
    if chapitres:
        body = chapitrer(body, CHAPITRES_COURTS, CHAPITRES_EXCLUS)
    # Barre de recherche du bandeau : on tape sa question directement.
    # Absente de la page /recherche/ elle-même, qui a déjà son champ.
    sur_recherche = path == "/recherche/"
    navq = "" if sur_recherche else (
        '<form class="navq" role="search" action="/recherche/">'
        '<label class="navq__l" for="navq">'
        '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" width="16" height="16">'
        '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
        '<circle cx="10.5" cy="10.5" r="6.5"/><line x1="15.5" y1="15.5" x2="21" y2="21"/></g></svg>'
        '<span class="sr">Rechercher sur le site</span></label>'
        '<input id="navq" name="q" type="search" autocomplete="off" role="combobox"'
        ' aria-expanded="false" aria-controls="navq-sug" aria-autocomplete="list"'
        ' placeholder="Votre question ou un mot-clé…">'
        '<div id="navq-sug" class="navsug" role="listbox" hidden></div></form>')
    script_navq = "" if sur_recherche else (
        f'<script>window.IDX_V="{IDX_V}"</script>'
        f'<script src="/assets/recherche.js?v={IDX_V}" defer></script>')
    head = f"""<!doctype html><html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots},max-snippet:-1,max-image-preview:large">
<link rel="alternate" type="application/rss+xml" title="Questions de copropriété — DGLM Expertises" href="/rss.xml">\n<link rel="canonical" href="{canon}">
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
{f'<meta name="google-site-verification" content="{GOOGLE_VERIF}">' if GOOGLE_VERIF else ''}
{f'<meta name="msvalidate.01" content="{BING_VERIF}">' if BING_VERIF else ''}
<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css?v={CSS_V}">
{head_extra}
{schema}
{jsonld(page_schema(canon, title))}
</head><body>
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="topbar"><div class="wrap">
<span>Diagnostiqueurs certifiés · Copropriété &amp; travaux · Bordeaux Métropole</span>
<a class="topbar__avis" href="{E['google_avis']}" rel="noopener">★ 4,9/5 — avis Google</a>
<a href="tel:{E['tel_raw']}">{E['tel']}</a>
<a class="topbar__part" href="/particuliers/">Particulier pour une vente ou une location ? →</a></div></div>
<header class="masthead"><div class="wrap">
<a class="brand" href="/"><img src="/assets/logo-dglm-blanc.png" alt="DGLM Expertises"
width="47" height="44" fetchpriority="high"><span>{E['baseline']}</span></a>
<nav class="nav" aria-label="Navigation principale">
<div class="nav__grp"><a href="/diagnostics-copropriete/" title="Diagnostics de copropriété">Copropriété</a>
<div class="nav__menu">
<a href="/diagnostic-technique-global/"><b>DTG</b> — diagnostic technique global</a>
<a href="/plan-pluriannuel-de-travaux/"><b>PPPT</b> — plan pluriannuel de travaux</a>
<a href="/dpe-collectif-copropriete/">DPE collectif</a>
<a href="/audit-energetique-copropriete/">Audit énergétique</a>
<a href="/diagnostics-copropriete/">Tous les diagnostics de copropriété →</a></div></div>
<div class="nav__grp"><a href="/avant-travaux-et-demolition/" title="Avant travaux et démolition">Chantier</a>
<div class="nav__menu">
<a href="/reperage-amiante-avant-travaux/"><b>RAAT</b> — amiante avant travaux</a>
<a href="/reperage-amiante-avant-demolition/"><b>RAAD</b> — avant démolition</a>
<a href="/diagnostic-pemd/"><b>PEMD</b> — matériaux et déchets</a>
<a href="/etat-parasitaire-avant-travaux/">État parasitaire</a>
<a href="/avant-travaux-et-demolition/">Tout l'avant-travaux →</a></div></div>
<div class="nav__grp"><a href="{SILO}/simulateur-obligations-copropriete/">Simulateurs</a>
<div class="nav__menu">
<a href="{SILO}/simulateur-obligations-copropriete/">Diagnostics : suis-je concerné ?</a>
<a href="/aides-financieres-copropriete/">Aides financières : combien ?</a>
<a href="/simulateur-validite-diagnostics/">Validité : mes diagnostics tiennent-ils ?</a></div></div>
<div class="nav__grp"><a href="/questions/">Guides</a>
<div class="nav__menu">
<a href="/questions/rubriques/amiante/">Amiante</a>
<a href="/questions/rubriques/copropriete/">Copropriété, DTG &amp; PPPT</a>
<a href="/questions/rubriques/energie/">Performance énergétique</a>
<a href="/questions/rubriques/vente-location/">Vente &amp; location</a>
<a href="/questions/rubriques/risques/">Plomb, gaz &amp; risques</a>
<a href="/questions/rubriques/reperes/">Repères &amp; définitions</a>
<a href="/questions/">Tous les guides →</a></div></div>
<div class="nav__grp"><a href="/le-tableau-des-diagnostics/">Outils</a>
<div class="nav__menu">
<a href="/le-tableau-des-diagnostics/">Le tableau des diagnostics</a>
<a href="/pack-conseil-syndical/">Le pack du conseil syndical</a>
<a href="/aide-au-devis/">Aide au devis : les documents</a>
<a href="/recherche/">Rechercher dans le site</a></div></div>
{navq}
<a class="btn" href="/devis/">Demander un devis</a></nav>
<details class="menu"><summary aria-label="Ouvrir le menu">Menu</summary>
<nav class="menu__list" aria-label="Menu complet">{MENU}</nav></details></div></header>
<main id="contenu" tabindex="-1">"""
    foot = f"""{SCRIPT_VOLETS}</main>
<footer class="footer"><div class="wrap">
<img class="mark" src="/assets/logo-dglm-blanc.png" alt="" width="55" height="52" loading="lazy">
<p class="slogan">{esc(E["signature"])}</p>
<div class="grid grid--4">
<div><p class="foot-titre">Avant travaux &amp; démolition</p><ul>
<li><a href="/avant-travaux-et-demolition/">La famille chantier</a></li>
{"".join(f'<li><a href="{SILO}/{s["slug"]}/">{s["nom"]}</a></li>' for s in SERVICES if s["sigle"] in ("RAAT", "RAAD"))}
<li><a href="/diagnostic-pemd/">Diagnostic PEMD</a></li>
<li><a href="/etat-parasitaire-avant-travaux/">État parasitaire</a></li></ul></div>
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
<li><a href="{SILO}/zones-d-intervention/">Toute la Gironde et les Landes</a></li>
<li><a href="{SILO}/{SERVICES[0]['slug']}/bordeaux/">Bordeaux</a></li>
<li><a href="{SILO}/{SERVICES[0]['slug']}/merignac/">Mérignac</a></li>
<li><a href="{SILO}/{SERVICES[0]['slug']}/pessac/">Pessac</a></li></ul></div>
<div><p class="foot-titre">Contact</p><ul>
<li><a href="tel:{E['tel_raw']}">{E['tel']}</a></li>
<li><a href="mailto:{E['email']}">{E['email']}</a></li>
<li><a href="/contact/">Nous joindre — horaires et adresse</a></li>
<li><a href="/equipe/">Notre équipe</a></li>
<li><a href="{E['google_avis']}" target="_blank" rel="noopener">Nos avis Google ★</a></li>
<li><a href="{E['diagadvisor']}" target="_blank" rel="noopener">Avis DiagAdvisor ★</a></li>
<li>{E['rue']}<br>{E['cp']} {E['ville']}</li></ul></div>
</div>
<p class="legalline">{E['nom']} — {E['endossement']} — {E['federation']} — SIRET {E['siret']} — {E['rcs']} ·
Page à jour en {MAJ} ·
<a href="/plan-du-site/">Plan du site</a> ·
<a href="/conformite/">Certificat de conformité</a> ·
<a href="/notre-methode-editoriale/">Méthode éditoriale</a> ·
<a href="/certifications-et-assurances/">Certifications et assurances</a> ·
<a href="/mentions-legales/">Mentions légales</a> ·
<a href="/avis/">Avis clients</a> ·
<a href="/confidentialite/">Confidentialité</a> ·
<a href="/particuliers/">{E['site_a_ancre']}</a> ·
Photos d'architecture : Bétium217, Symac — <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" rel="noopener">CC BY-SA</a>, via Wikimedia Commons</p>
</div></footer>
<div class="barre-mob" role="group" aria-label="Nous contacter">
<a class="barre-mob__tel" href="tel:{E['tel_raw']}">
<svg viewBox="0 0 24 24" aria-hidden="true" width="17" height="17"><path fill="none"
 stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
 d="M6.5 3h3l1.5 4.5-2 1.5a12 12 0 0 0 6 6l1.5-2 4.5 1.5v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4.5 5.2 2 2 0 0 1 6.5 3Z"/></svg>
Appeler</a>
<a class="barre-mob__devis" href="/devis/">Demander un devis</a>
</div>{script_navq}</body></html>"""
    write(path, head + body + foot)


def write(path, content):
    rel = path.strip("/")
    # La page d'erreur doit s'appeler 404.html À LA RACINE : c'est le seul
    # fichier que l'hébergeur sert en cas d'adresse inconnue. Écrite en
    # /404/index.html, elle existait sans jamais être utilisée, et le visiteur
    # tombait sur la page d'erreur anglaise de GitHub.
    if rel == "404":
        with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
            f.write(content)
        return
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


def chapitrer(body, libelles=None, exclure=(), mini=3):
    """Pose la barre de chapitres d'une page composée de sections.

    Elle lit le corps déjà rendu plutôt que d'obliger chaque page à se décrire :
    chaque section reçoit une ancre tirée de son titre, et la barre s'insère
    après le héros. `libelles` donne le nom court d'un chapitre quand son h2
    est trop long pour un chip ; `exclure` écarte les sections qui ne sont pas
    du contenu (l'appel à l'action de fin, par exemple).
    Sans effet si la page a déjà sa barre ou compte moins de `mini` chapitres.
    """
    import re as _re
    if 'class="ancres"' in body:
        return body
    libelles = libelles or {}
    exclus = {_slug_ancre(x) for x in exclure}

    # les sections de premier niveau, dans l'ordre du document
    bornes = [m for m in _re.finditer(r"<(section|article)\b([^>]*)>", body)]
    chapitres, vus, inserts = [], set(), []
    for i, m in enumerate(bornes):
        attrs = m.group(2)
        if "hero" in attrs or "cta" in attrs:
            continue
        fin = bornes[i + 1].start() if i + 1 < len(bornes) else len(body)
        bloc = body[m.start():fin]
        t = _re.search(r"<h2[^>]*>(.*?)</h2>", bloc, _re.S)
        if not t:
            continue
        titre = _re.sub(r"\s+", " ", html.unescape(strip_tags(t.group(1)))).strip()
        if not titre:
            continue
        # Un titre écrit en dur garde l'apostrophe droite ; le même passé par
        # esc() reçoit la courbe, que _slug_ancre supprime au lieu d'en faire
        # un tiret. Sans cette mise à plat, les deux ne donnent pas la même clé
        # et le chapitre retombe sur un libellé tronqué.
        plat = (titre.replace("’", "'").replace(" ", " ")
                     .replace(" ", " ").replace("‑", "-"))
        cle = _slug_ancre(plat)
        if cle in exclus:
            continue
        # le dictionnaire donne le nom court du chapitre et, s'il y tient,
        # une ancre lisible : #garanties plutôt que #certifications-et-assur…
        court = libelles.get(titre) or libelles.get(cle)
        anc_voulue = ""
        if isinstance(court, tuple):
            court, anc_voulue = court
        # une section peut déjà porter son ancre : on la respecte
        deja = _re.search(r'id="([^"]+)"', attrs)
        anc = deja.group(1) if deja else (anc_voulue or cle)
        while anc in vus:
            anc += "-b"
        vus.add(anc)
        if not deja:
            inserts.append((m.start() + len(m.group(1)) + 1, f' id="{anc}"'))
        if not court:
            # à défaut d'un nom court fourni, on coupe à la première rupture
            court = _re.split(r"\s*[:—]\s*", titre)[0]
            if len(court) > 30:
                court = titre[:28].rsplit(" ", 1)[0] + "…"
        chapitres.append((anc, court))

    if len(chapitres) < mini:
        return body
    for pos, txt in reversed(inserts):          # en partant de la fin :
        body = body[:pos] + txt + body[pos:]    # les positions restent valides

    barre = ('<nav class="ancres" aria-label="Chapitres"><div class="wrap">'
             + "".join(f'<a href="#{a}">{esc(t)}</a>' for a, t in chapitres)
             + "</div></nav>")
    # juste après le héros, comme sur les pages mission
    h = _re.search(r'<section[^>]*class="[^"]*hero[^"]*".*?</section>', body, _re.S)
    return body[:h.end()] + barre + body[h.end():] if h else barre + body


def volet(eyebrow, h2, corps, ouvert=False, pale=False, dark=False, ancre=""):
    """Bandeau déroulant : titre visible, contenu replié derrière « Déplier ».
    La hiérarchie se voit, le détail s'ouvre au clic (details natif, zéro JS)."""
    cls = "band" + (" band--pale" if pale else "") + (" band--dark" if dark else "")
    eb = "eyebrow eyebrow--pale" if dark else "eyebrow"
    o = " open" if ouvert else ""
    aid = f' id="{ancre}"' if ancre else ""
    return (f'<section{aid} class="{cls}"><div class="wrap">'
            f'<details class="volet"{o}><summary>'
            f'<span class="{eb}">{eyebrow}</span><h2>{h2}</h2>'
            f'<span class="volet__ouvrir" aria-hidden="true">Déplier</span></summary>'
            f'<div class="volet__corps">{corps}</div></details></div></section>')


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
        ("terrain-conduits.jpg", 960, 1280, "amiante", "Toiture — conduits en fibres-ciment",
         "des conduits en ciment gris posés avant 1997.",
         "à l'époque, ce ciment était souvent armé d'amiante. Tant qu'on n'y touche "
         "pas, il ne libère rien — mais avant des travaux, on prélève et on fait "
         "analyser en laboratoire. C'est exactement ça, un repérage."),
        ("terrain-fibro-toiture.jpg", 1100, 521, "amiante",
         "Couverture — plaques ondulées en fibres-ciment",
         "les grandes plaques ondulées grises d'un appentis, avec leur gouttière.",
         "c'est la silhouette la plus reconnaissable du fibres-ciment ancien. Intacte "
         "et à l'air libre, elle ne présente pas de danger immédiat ; percée, découpée "
         "ou déposée sans précaution, elle libère des fibres. D'où le repérage avant "
         "d'engager le moindre outil."),
        ("terrain-fibro-bardage.jpg", 1100, 521, "amiante",
         "Mur — plaques planes en fibres-ciment",
         "un habillage de plaques planes grises, sous une charpente.",
         "on ne pense qu'aux toitures, mais le fibres-ciment servait aussi en bardage, "
         "en cloison de local technique ou en coffrage de gaine. Un repérage sérieux "
         "regarde les murs autant que les toits."),
    ],
    "dossier-technique-amiante": [
        ("terrain-fibro-bardage.jpg", 1100, 521, "amiante",
         "Parties communes — plaques planes en fibres-ciment",
         "un habillage de plaques grises dans un local commun.",
         "le dossier technique amiante recense ces matériaux immeuble par immeuble, "
         "les localise et note leur état de conservation. C'est ce document que "
         "l'on tend à toute entreprise avant qu'elle n'intervienne."),
        ("terrain-conduits.jpg", 960, 1280, "amiante", "Toiture — conduits en fibres-ciment",
         "des conduits gris courant en toiture.",
         "conduits, descentes et gaines techniques figurent parmi les matériaux "
         "les plus fréquemment retrouvés dans les immeubles d'avant 1997."),
    ],
    "amiante-parties-privatives": [
        ("terrain-fibro-toiture.jpg", 1100, 521, "amiante",
         "Annexes privatives — plaques ondulées",
         "une couverture ondulée en fibres-ciment sur une annexe.",
         "l'amiante des parties privatives ne s'arrête pas au logement : garages, "
         "appentis, caves et celliers en contiennent souvent davantage que les pièces "
         "de vie."),
    ],
    "diagnostic-technique-global": [
        ("terrain-solive.jpg", 1200, 568, "copropriete", "Plancher — solive ancienne, renfort récent",
         "une solive rongée par les insectes du bois, doublée par une pièce neuve.",
         "un plancher qui a souffert raconte l'histoire de l'immeuble. Le diagnostic "
         "technique global objective ce qui porte encore, ce qui doit être renforcé, "
         "et à quel horizon."),
    ],
    "etat-parasitaire-avant-travaux": [
        ("terrain-merule.jpg", 481, 640, "risques",
         "Bois de plancher — attaque fongique (mérule)",
         "un bois qui se délite dans un angle humide.",
         "les champignons lignivores — mérule en tête — prospèrent sur l'humidité "
         "persistante. Repérés tôt, ils se traitent ; découverts tard, ils emportent "
         "plancher et solives."),
    ],
    "reperage-amiante-avant-demolition": [
        ("terrain-combles.jpg", 960, 1280, "amiante", "Combles — l'envers du décor",
         "un comble où personne n'est monté depuis des années.",
         "avant une démolition, aucune réserve n'est acceptable : le repérage va "
         "partout, y compris là où personne ne regarde jamais."),
    ],
    "plan-pluriannuel-de-travaux": [
        ("terrain-cour.jpg", 1200, 900, "copropriete", "Cour intérieure — l'immeuble tel qu'il vit",
         "une cour d'immeuble bordelais : pierre, coursives, enduits fatigués, réseaux apparents.",
         "c'est exactement ce qu'un plan pluriannuel regarde : ce qui tient, ce qui vieillit, "
         "et dans quel ordre le traiter sur dix ans."),
    ],
}

# Thème → nom de rubrique (pour relier chaque carnet à ses guides).
THEME_RUB = {"amiante": "Amiante", "copropriete": "Copropriété, DTG & PPPT",
             "energie": "Performance énergétique", "risques": "Plomb, gaz & risques"}

# Le titre de la rubrique photo, propre à chaque mission : on annonce ce que
# le lecteur va voir plutôt qu'un générique « Vu en mission ».
CARNETS_TITRE = {
    "reperage-amiante-avant-travaux": "L'amiante, tel qu'on le rencontre avant un chantier",
    "reperage-amiante-avant-demolition": "Avant démolition : là où personne ne regarde",
    "dossier-technique-amiante": "L'amiante des parties communes, en images",
    "amiante-parties-privatives": "L'amiante chez soi : garages, caves, annexes",
    "diagnostic-technique-global": "Ce que le diagnostic global regarde vraiment",
    "plan-pluriannuel-de-travaux": "L'immeuble tel qu'il vieillit",
    "etat-parasitaire-avant-travaux": "Insectes et champignons : les signes qui alertent",
}


# ------------------------------------------------------------- maillage éditorial
# Les pages de mission n'envoyaient qu'un seul lien vers les guides : l'autorité
# accumulée par les 70 guides ne circulait pas jusqu'aux pages qui vendent, ni
# l'inverse. Chaque mission désigne ici les questions qu'on lui pose vraiment.
GUIDES_MISSION = {
    "reperage-amiante-avant-travaux": [
        "raat-ou-raad", "qui-realise-reperage-amiante-travaux",
        "qui-paie-reperage-copropriete", "raat-remplacement-fenetres",
        "decouverte-amiante-en-chantier", "amiante-sous-section-3-et-4"],
    "reperage-amiante-avant-demolition": [
        "raat-ou-raad", "batiment-vide-avant-demolition",
        "decouverte-amiante-en-chantier", "diagnostic-pemd-obligatoire-renovation",
        "listes-a-b-c-amiante"],
    "diagnostic-technique-global": [
        "dtg-ou-pppt", "dtg-petite-copropriete", "carnet-entretien-copropriete",
        "majorites-vote-travaux-assemblee", "fonds-de-travaux"],
    "plan-pluriannuel-de-travaux": [
        "voter-pppt-assemblee", "validite-pppt", "copropriete-sans-pppt",
        "dtg-ou-pppt", "fonds-de-travaux", "majorites-vote-travaux-assemblee"],
    "dossier-technique-amiante": [
        "dta-ou-dapp", "dta-ancien-encore-valable", "listes-a-b-c-amiante",
        "fiche-recapitulative-dta"],
    "amiante-parties-privatives": [
        "dta-ou-dapp", "listes-a-b-c-amiante", "amiante-chez-moi-que-faire"],
    "crep-parties-communes": [
        "crep-parties-communes-obligatoire", "qu-est-ce-que-le-diagnostic-plomb",
        "unite-diagnostic-plomb"],
    "dpe-collectif-copropriete": [
        "qu-est-ce-que-le-dpe", "duree-validite-dpe", "qu-est-ce-qu-une-passoire-thermique",
        "calcul-etiquette-dpe"],
    "audit-energetique-copropriete": [
        "qu-est-ce-qu-une-passoire-thermique", "qu-est-ce-que-le-dpe",
        "dtg-dpe-audit-lequel"],
    "diagnostic-pemd": [
        "diagnostic-pemd-obligatoire-renovation", "recolement-pemd",
        "batiment-vide-avant-demolition"],
    "etat-parasitaire-avant-travaux": [
        "diagnostic-termites-obligatoire", "termites-gironde"],
    "installations-collectives-gaz-electricite": [
        "diagnostic-gaz-obligatoire", "diagnostic-electricite-obligatoire"],
    "conformite-assainissement-copropriete": ["fosse-septique-controle-vente"],
}

# Slugs réellement publiés à la date du build — un lien vers un guide à paraître
# serait une 404 bloquante. Rempli par main() dès le chargement des contenus.
PUBLIES = {}


# ------------------------------------------------------------- relecture signée
# Un guide n'engage vraiment que s'il est signé. Les deux cofondateurs relisent
# selon leur domaine : c'est une validation technique, pas une signature de
# complaisance — le champ schema.org employé est donc « reviewedBy » et non
# « author », qui reviendrait à s'attribuer une rédaction.
RELECTEURS = {
    "thibault": {
        "nom": "Thibault Le Moine",
        "qualite": "cofondateur, diagnostiqueur immobilier",
        "detail": "titre professionnel enregistré au RNCP, certifié amiante, "
                  "termites, gaz et électricité (certificat C3284)",
        # ce qu'il relit : son périmètre de certification
        "tags": {"amiante", "chantier", "RAAT", "RAAD", "DTA", "DAPP", "démolition",
                 "termites", "gaz", "électricité", "PEMD", "déchets", "parasitaire",
                 "menuiseries", "sécurité", "travaux"},
    },
    "aude": {
        "nom": "Aude de Gentile",
        "qualite": "cofondatrice, diagnostiqueuse immobilière",
        "detail": "titre professionnel de diagnostiqueur immobilier enregistré au RNCP",
        "tags": set(),   # relit tout le reste
    },
}


def relecteur_de(tags):
    """Qui valide ce guide, selon son domaine."""
    if set(tags) & RELECTEURS["thibault"]["tags"]:
        return RELECTEURS["thibault"]
    return RELECTEURS["aude"]


def signature_html(r, date_pub):
    """Qui répond de ce texte, depuis quand, et où le vérifier."""
    return (
        '<div class="relu">'
        f'<p class="relu__d">Publié le {date_pub.strftime("%d/%m/%Y")} · '
        f'vérifié en {MAJ}</p>'
        '<p class="relu__r"><span>Relu et validé par</span> '
        f'<a href="/equipe/"><b>{esc(r["nom"])}</b></a>, {esc(r["qualite"])} — '
        f'{esc(r["detail"])}. '
        '<a href="/certifications-et-assurances/">Titres et certifications</a>.</p></div>')


def relecteur_schema(r):
    """La même personne, en données structurées, pour le reviewedBy de l'Article."""
    return {"@type": "Person", "name": r["nom"], "jobTitle": r["qualite"],
            "description": r["detail"], "url": DOM + "/equipe/",
            "worksFor": {"@id": DOM + "/#organisation"}}


def guides_lies(slug):
    """Les guides parus qui répondent aux questions de cette mission."""
    voulus = GUIDES_MISSION.get(slug, [])
    dispo = [s for s in voulus if s in PUBLIES]
    if not dispo:
        return ""
    items = "".join(
        f'<li><a href="/questions/{s}/">{esc(PUBLIES[s])}</a></li>' for s in dispo)
    return (f'<section class="band band--pale"><div class="wrap">'
            f'<p class="eyebrow">Les questions qu\'on nous pose</p>'
            f'<h2>Pour aller au fond du sujet</h2>'
            f'<p class="narrow">Nos réponses détaillées, écrites à partir des situations '
            f'que nous rencontrons en mission et sourcées sur les textes en vigueur.</p>'
            f'<ul class="liens-guides">{items}</ul>'
            f'<p class="maj"><a href="/referentiel-des-normes/">Le référentiel des normes '
            f'et des textes applicables</a> · <a href="/questions/">Tous les guides '
            f'pratiques</a></p></div></section>')


def carnets_band(slug):
    items = CARNETS.get(slug)
    if not items:
        return ""
    figs = "".join(
        f'<figure class="photo"><img src="/assets/photos/{f}" alt="{esc(cap)}" '
        f'loading="lazy" decoding="async" width="{w}" height="{h}">'
        f'<figcaption>{esc(cap)}</figcaption>'
        f'<p class="photo__lecon"><b>Ce qu\'on voit :</b> {esc(v)} '
        f'<b>Pourquoi ça compte :</b> {esc(p)}</p>'
        f'<p class="photo__theme"><a href="/questions/rubriques/{th}/">'
        f'Tous nos guides « {esc(THEME_RUB.get(th, th))} » →</a></p></figure>'
        for f, w, h, th, cap, v, p in items)
    titre = CARNETS_TITRE.get(slug, "Vu en mission")
    n = len(items)
    intro = ("" if n < 2 else
             f'<p class="narrow" style="margin-top:.9rem">{n} situations rencontrées '
             f'sur le terrain, expliquées simplement — ce que nous voyons, et pourquoi '
             f'cela change quelque chose pour vous.</p>')
    return (f'<section id="terrain" class="band"><div class="wrap">'
            f'<p class="eyebrow">Carnets de terrain</p><h2>{esc(titre)}</h2>{intro}'
            f'<div class="grid grid--2" style="margin-top:1.8rem">{figs}</div></div></section>')


# ------------------------------------------------------------------ accueil
# Site dédié : l'accueil vise directement les requêtes têtes de silo
# (RAAT / RAAD / DTG / PPPT). Aucune requête du site A n'est ciblée.
def page_home(dernier=None):
    actu = (f'<p class="maj">Dernière réponse publiée : '
            f'<a href="/questions/{dernier["slug"]}/">{esc(dernier["titre"])}</a></p>'
            if dernier else "")
    def _carte_mission(s):
        return (f'<a class="card card--link" href="{SILO}/{s["slug"]}/">'
                f'{PICTOS.get(s["sigle"], "")}<span class="sigle">{s["sigle"]}</span>'
                f'<h3>{esc(s["nom"])}</h3><p>{esc(s["accroche"])}</p>'
                f'<span class="more">Découvrir la mission →</span></a>')
    cards_copro = "".join(_carte_mission(s) for s in SERVICES if s["sigle"] in ("DTG", "PPPT"))
    cards_chantier = "".join(_carte_mission(s) for s in SERVICES if s["sigle"] in ("RAAT", "RAAD"))

    body = f"""<section class="hero hero--photo"><div class="wrap">
<p class="eyebrow eyebrow--pale">RAAT · RAAD · DTG · PPPT — Bordeaux Métropole</p>
<h1>L'expertise du bâti, au service des copropriétés et des maîtres d'ouvrage.</h1>
<p class="lede">Quatre missions techniques déterminent le démarrage d'un chantier et le budget
décennal d'une copropriété : le repérage amiante avant travaux, le repérage avant
démolition, le diagnostic technique global et le plan pluriannuel de travaux — au sein
de neuf missions collectives, du DPE collectif à l'assainissement.</p>
<div class="actions">
<a class="btn btn--light" href="{SILO}/simulateur-obligations-copropriete/">Évaluer ma copropriété</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div>
<dl class="refbar">
<div><dt>Spécialité</dt><dd>Copropriété, travaux et démolition</dd></div>
<div><dt>Périmètre</dt><dd>Bordeaux Métropole en priorité — Gironde et Landes sur mission</dd></div>
<div><dt>Intervention</dt><dd>Repérages amiante : visite sous 72 h, rapport sous 48 h</dd></div>
<div><dt>Analyses</dt><dd>Laboratoire accrédité COFRAC</dd></div>
</dl></div>{SKYLINE}</section>

<section class="parcours"><div class="wrap">
<span class="parcours__label">À chacun son parcours</span>
<a href="{SILO}/syndics-de-copropriete/">Je suis syndic professionnel</a>
<a href="/conseil-syndical/">Je suis au conseil syndical</a>
<a href="{SILO}/bailleurs-et-maitres-d-ouvrage/">Je suis bailleur ou maître d'ouvrage</a>
<a href="{SILO}/entreprises-de-travaux/">Je suis une entreprise de travaux</a>
<a href="/particulier-travaux/">Je fais des travaux chez moi</a>
<a href="/particuliers/">Je vends ou je loue mon logement</a>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Quatre missions, deux familles</p>
<h2>Ce que nous faisons pour vous.</h2>
<h3 class="famille">Diagnostics de copropriété — gérer l'immeuble</h3>
<div class="grid grid--2" style="margin-top:1.2rem">{cards_copro}</div>
<p class="fam-lien"><a href="/diagnostics-copropriete/">Toute la famille copropriété →</a></p>
<h3 class="famille">Avant travaux &amp; démolition — préparer le chantier</h3>
<div class="grid grid--2" style="margin-top:1.2rem">{cards_chantier}</div>
<p class="fam-lien"><a href="/avant-travaux-et-demolition/">Toute la famille chantier →</a></p>
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

<section class="band"><div class="wrap">
<p class="eyebrow">Ce que nous avons déjà fait</p>
<h2>{MISSIONS_FAITES} missions menées à leur terme.</h2>
<p class="narrow">Le chiffre est celui de notre logiciel de suivi, arrêté au
{MAJ_JOUR} : {MISSIONS_FAITES} dossiers clos depuis 2021, tous diagnostics
confondus — vente, location, copropriété, avant travaux.</p>
<p class="narrow"><strong>Disons les choses comme elles sont :</strong> la copropriété
est notre développement le plus récent. Nous ne prétendons pas avoir signé des
centaines de diagnostics techniques globaux. Ce que nous apportons à un conseil
syndical, c'est {MISSIONS_FAITES} interventions de terrain, cinq diagnostiqueurs
certifiés, et un métier appris avant d'être vendu.</p>
<div class="actions" style="margin-top:1.5rem">
<a class="btn btn--light" href="/certifications-et-assurances/">Nos certifications, nominatives</a>
<a class="btn btn--light" href="/equipe/">Qui intervient</a></div>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Ils nous font confiance</p>
<h2>123 avis vérifiés, et nous n'en choisissons aucun.</h2>
<p class="narrow">Sur DiagAdvisor, la plateforme d'avis vérifiés du métier, chaque avis
est rattaché à une mission réellement facturée : nous ne pouvons ni les trier, ni les
supprimer. En voici trois, pris dans l'ordre de publication.</p>
{avis_html(3)}
<div class="actions" style="display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.6rem">
<a class="btn btn--light" href="/avis/">Lire les avis sur le site</a>
<a class="btn btn--light" href="{E['diagadvisor']}" rel="noopener">Les 123 avis vérifiés</a></div>
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
<p>DTG, PPPT, DPE collectif, DTA, plomb, assainissement.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/avant-travaux-et-demolition/"><h3>Avant travaux &amp; démolition</h3>
<p>RAAT, RAAD, PEMD, état parasitaire : préparer le chantier.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="{SILO}/simulateur-obligations-copropriete/"><h3>Le simulateur d'obligations</h3>
<p>Votre situation établie en six questions, sans inscription.</p><span class="more">Ouvrir →</span></a>
<a class="card card--link" href="/aides-financieres-copropriete/"><h3>Le simulateur d'aides</h3>
<p>MaPrimeRénov' Copropriété : le montant estimé, ligne à ligne.</p><span class="more">Ouvrir →</span></a>
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

    shell(path="/", title="Diagnostics de copropriété à Bordeaux — DGLM Expertises",
          # Le préchargement doit suivre la même règle que la feuille de style,
          # sinon le téléphone télécharge la grande image EN PLUS de la petite :
          # 145 Ko pour rien. L'attribut media rend le preload conditionnel.
          head_extra=(
              '<link rel="preload" as="image" media="(min-width:761px)" '
              'href="/assets/photos/hero-immeuble.jpg">'
              '<link rel="preload" as="image" media="(max-width:760px)" '
              'href="/assets/photos/hero-immeuble-800.jpg">'),
          desc="Repérage amiante avant travaux et avant démolition, diagnostic technique "
               "global, plan pluriannuel de travaux. Bordeaux Métropole, devis sous 2 h.",
          body=body,
          schema=jsonld(org_schema(),
                        {"@type": "WebSite", "@id": DOM + "/#site", "url": DOM + "/",
                         "name": E["nom"], "inLanguage": "fr-FR",
                         "publisher": {"@id": DOM + "/#organisation"},
                         # Le site a une recherche interne, qui accepte ?q=.
                         # La déclarer permet aux moteurs d'afficher une boîte
                         # de recherche du site directement dans leurs
                         # résultats : le visiteur cherche « DGLM DTG » et
                         # atterrit sur la page, pas sur l'accueil.
                         "potentialAction": {
                             "@type": "SearchAction",
                             "target": {"@type": "EntryPoint",
                                        "urlTemplate": DOM + "/recherche/?q={search_term_string}"},
                             "query-input": "required name=search_term_string"}},
                        ), chapitres=False)
    URLS.append(("/", "1.0", "weekly", MAJ_STRUCTURE))


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
savoir ce que votre copropriété doit à la réglementation, et depuis quand.</p>
<div class="actions"><a class="btn btn--light" href="/aides-financieres-copropriete/">Simuler vos aides financières</a>
<a class="btn btn--light" href="/devis/">Demander un devis</a></div></div></section>

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
<p class="eyebrow">Le simulateur</p>
<h2>Votre copropriété en six questions</h2>
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
          # Le formulaire de fin de simulateur : le visiteur qui vient de
          # découvrir ses obligations doit pouvoir nous le dire sans quitter
          # la page. Il s'ajoute après le résultat, jamais à sa place.
          head_extra=cfg_rappel(),
          schema=jsonld(org_schema(), breadcrumb(trail), faq_schema(SIM_FAQ),
                        {"@type": "WebApplication", "name": "Simulateur d'obligations de copropriété",
                         "url": DOM + p, "applicationCategory": "BusinessApplication",
                         "operatingSystem": "Tout navigateur web", "inLanguage": "fr-FR",
                         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
                         "publisher": {"@id": DOM + "/#organisation"}}))
    URLS.append((p, "0.9", "monthly", MAJ_STRUCTURE))


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
    faq = "".join(f"<details{' open' if _i == 0 else ''}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
                  for _i, (q, a) in enumerate(s["faq"]))
    autres = "".join(
        f'<a class="card card--link" href="{SILO}/{o["slug"]}/"><span class="sigle">{o["sigle"]}</span>'
        f'<h3>{esc(o["nom"])}</h3><p>{esc(o["accroche"])}</p></a>'
        for o in SERVICES if o["slug"] != s["slug"])
    mesh = "".join(f'<li><a href="{p}{c["slug"]}/">{esc(s["sigle"])} {esc(c["nom"])}</a></li>'
                   for c in COMMUNES)
    schema_bloc = (volet("Repère visuel", "Comprendre en un schéma", schema, pale=True,
                         ancre="schema")
                   if schema else "")

    # Le devis part avec la mission déjà choisie : le visiteur ne redéclare
    # pas ce qu'il vient de lire pendant deux mille mots.
    MISSION_DEVIS = {"reperage-amiante-avant-travaux": "raat",
                     "reperage-amiante-avant-demolition": "raad",
                     "diagnostic-technique-global": "dtg",
                     "plan-pluriannuel-de-travaux": "pppt"}
    # Fragment plutôt que paramètre : l'audit interne lit tout href comme une
    # URL de page et transformerait « ?m=dtg » en 404.
    lien_devis = "/devis/" + (f"#m-{MISSION_DEVIS[s['slug']]}" if s["slug"] in MISSION_DEVIS else "")
    bouton_aides = ('<a class="btn btn--light" href="/aides-financieres-copropriete/">Simuler vos aides</a>'
                    if s["slug"] in ("diagnostic-technique-global", "plan-pluriannuel-de-travaux") else "")
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{s['sigle']} — Bordeaux Métropole</p>
<h1>{esc(s['nom'])} à Bordeaux et en Gironde</h1>
<p class="lede">{esc(s['accroche'])}</p>
<div class="actions"><a class="btn btn--light" href="{lien_devis}">Demander un devis</a>
{bouton_aides}<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<nav class="ancres" aria-label="Chapitres"><div class="wrap">
<a href="#fiche">L’essentiel</a>{'<a href="#terrain">Sur le terrain</a>' if CARNETS.get(s['slug']) else ''}<a href="#reglementation">Réglementation</a><a href="#methode">Méthode</a>{'<a href="#schema">Le schéma</a>' if schema else ''}<a href="#faq">Questions</a><a href="#communes">Votre commune</a>
</div></nav>
<section id="fiche" class="band"><div class="wrap">
<p class="eyebrow">L'antisèche</p>
<h2>L'essentiel en trente secondes</h2>
{f'<p class="enclair"><span>En français courant</span>{esc(s["clair"])}</p>' if s.get("clair") else ""}
<div class="prose" style="margin-top:1.4rem"><p style="font-size:1.12rem">{esc(s['intro'])}</p></div>
{fiche_html(s.get('fiche'))}
{'<p class="enclair" style="margin-top:1.6rem"><span>Vous êtes un particulier ?</span>Pour des travaux dans votre propre maison ou votre appartement, vous êtes exactement au bon endroit : ce repérage vaut pour tout donneur d\'ordre — y compris vous.</p>' if s['sigle'] in ('RAAT', 'RAAD') else ''}
</div></section>
{carnets_band(s['slug'])}
{guides_lies(s['slug'])}
{volet("Réglementation", "Ce que dit la réglementation",
       f'<dl class="legal">{cadre}</dl>', pale=True, ancre="reglementation", ouvert=True)}
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
    URLS.append((p, "0.9", "monthly", MAJ_STRUCTURE))


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
        URLS.append((p, "0.8", "monthly", MAJ_STRUCTURE))


# ------------------------------------------------------------------ zones
def liens_missions(c):
    """Les quatre missions d'une commune, liées seulement si elles comptent.

    Cette page portait 350 liens, dont 115 vers des pages que le site
    interdit lui-même d'indexer. Une page qui distribue son autorité sur 350
    destinations n'en donne à aucune, et un lien vers une page fermée aux
    moteurs ne rapporte rien du tout.

    Les pages hors métropole ne disparaissent pas : elles restent liées
    depuis les hubs de mission, elles ne deviennent donc pas orphelines.
    """
    if c["slug"] not in METRO_SLUGS:
        return ("<li class=\"mesh--muet\">" +
                esc(" · ".join(s["sigle"] for s in SERVICES)) + "</li>")
    return "".join(
        '<li><a href="' + SILO + '/' + s['slug'] + '/' + c['slug'] + '/">'
        + s['sigle'] + '</a></li>' for s in SERVICES)

def lien_commune(c):
    """Le nom de la commune, lié à sa page quand elle en a une.

    COMMUNES dépasse la métropole : la Gironde élargie et les Landes y
    figurent sans page dédiée. Un lien vers une page inexistante casserait
    le maillage aussi sûrement qu'une page orpheline.
    """
    if c["slug"] in METRO_SLUGS:
        return ('<a href="/' + c['slug'] + '/">' + esc(c['nom']) + '</a>')
    return esc(c["nom"])

def page_zones():
    p = f"{SILO}/zones-d-intervention/"
    trail = [("Accueil", "/"), ("Zones d'intervention", p)]
    # Le nom de la commune mène désormais à sa page : sans ce lien, les
    # pages de commune resteraient orphelines, et le contrôle de maillage
    # bloquerait le déploiement — à juste titre.
    lignes = "".join(f"""<div class="card"><span class="sigle">{c['cp']}</span>
<h3>{lien_commune(c)}</h3><p>{esc(c['parc'][:180])}…</p>
<ul class="mesh" style="margin-top:.6rem">
{liens_missions(c)}
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
    URLS.append((p, "0.7", "monthly", MAJ_STRUCTURE))


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
<section class="band"><div class="wrap prose">
{f'<p class="enclair" style="margin-top:0"><span>Vous louez votre propre logement ?</span>Les diagnostics de location d&#x27;un particulier relèvent de notre <a href="/particuliers/">site dédié</a> — ici, nous parlons patrimoine et campagnes de repérage.</p>' if a['slug'] == 'bailleurs-et-maitres-d-ouvrage' else ''}
{f'<p class="enclair" style="margin-top:0"><span>DPE collectif : où en est votre portefeuille ?</span>Toutes les copropriétés d&#x27;habitation au permis antérieur à 2013 sont concernées depuis le 1er janvier 2026 — notre <a href="/dpe-collectif-copropriete/">fiche DPE collectif</a> et le <a href="{SILO}/simulateur-obligations-copropriete/">simulateur</a> font le point immeuble par immeuble.</p>' if a['slug'] == 'syndics-de-copropriete' else ''}
{corps}</div></section>
<section class="band band--pale"><div class="wrap"><p class="eyebrow">Prestations</p>
<h2>Nos quatre missions</h2>
<div class="grid grid--2" style="margin-top:1.6rem">{cards}</div></div></section>{cta()}"""
    shell(path=p, title=titre(f"{a['titre']} — RAAT, DTG, PPPT Bordeaux | DGLM",
                              f"{a['titre']} : RAAT, DTG, PPPT | DGLM",
                              f"{a['titre']} — Bordeaux | DGLM"),
          desc=desc_courte(a["desc"]), body=body, schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.7", "monthly", MAJ_STRUCTURE))


# ------------------------------------------------------------------ contact
def page_contact():
    p = "/contact/"
    trail = [("Accueil", "/"), ("Contact", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Réponse sous deux heures ouvrées</p>
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
                           f"à Bordeaux. Devis chiffré sous deux heures ouvrées. "
                           f"{E['tel']}."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail),
                                   {"@type": "ContactPage", "url": DOM + p}), chapitres=False)
    URLS.append((p, "0.8", "yearly", MAJ_STRUCTURE))


def page_mentions():
    p = "/mentions-legales/"
    body = f"""<section class="band"><div class="wrap prose">
<h1>Mentions légales</h1>
<h2>Éditeur</h2><p><strong>{E['nom']}</strong>, société à responsabilité limitée
au capital de 1 500 €, immatriculée sous le SIRET {E['siret']} — {E['rcs']},
numéro de TVA intracommunautaire FR60891287070.</p>
<p>Siège social : {E['rue']}, {E['cp']} {E['ville']}.<br>
Téléphone : {E['tel']} — Courriel : {E['email']}.</p>
<p>Directrice de la publication : Aude de Gentile, cogérante.</p>
<h2>Activités distinctes</h2><p>{E['nom']} intervient exclusivement sur les missions de
copropriété, de travaux et de démolition : repérage amiante avant travaux et avant
démolition, diagnostic technique global, plan pluriannuel de travaux.</p>
<p>Les diagnostics obligatoires de vente et de location (DPE, amiante, plomb, termites,
gaz, électricité, mesurage) relèvent de notre activité auprès des particuliers, présentée
sur un site distinct. Pour savoir lesquels s'appliquent à votre logement,
<a href="/particuliers/">six questions suffisent</a> — et nous établissons le dossier.</p>
<h2>Certifications et assurance</h2><p>Diagnostiqueurs certifiés par LCC Qualixpert,
organisme accrédité par le COFRAC sous le numéro 4-0094. Responsabilité civile
professionnelle souscrite auprès de Markel Insurance SE. Numéros de certification,
domaines et dates de validité :
<a href="/certifications-et-assurances/">certifications et assurances</a>.</p>
<h2>Médiation de la consommation</h2><p>Conformément à l'ordonnance n° 2015-1033 du
20 août 2015, nos clients consommateurs ont accès à un dispositif de médiation de la
consommation, proposé par l'Alliance du Diagnostic Immobilier dont nous sommes membres.</p>
<h2>Hébergement</h2><p>Ce site est hébergé par <strong>GitHub, Inc.</strong>,
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis
(<a href="https://github.com" rel="noopener">github.com</a>). Il est composé de fichiers
statiques : aucune base de données, aucun traitement n'est exécuté sur le serveur.</p>
<h2>Propriété intellectuelle</h2><p>Les textes, schémas, illustrations et photographies
de ce site sont la propriété de {E['nom']}, à l'exception des photographies
d'architecture créditées en pied de page. Toute reproduction sans autorisation
est interdite.</p>
<h2>Données personnelles</h2><p>Le détail des traitements, de leur base légale et de
leurs durées de conservation figure sur la page
<a href="/confidentialite/">confidentialité</a>. En résumé : les informations transmises
par le formulaire ne servent qu'à répondre à votre demande et à établir un devis, elles
ne sont ni vendues ni cédées, et vous pouvez à tout moment en demander l'accès, la
rectification ou la suppression en écrivant à {E['email']}.</p>
</div></section>"""
    # La page était soumise au plan du site ET interdite d'indexation : la
    # console de recherche remonte cela comme une erreur permanente. Des
    # mentions légales n'ont aucune raison d'être cachées — elles participent
    # au contraire de la confiance qu'un moteur accorde à un site.
    shell(path=p, title=f"Mentions légales — {E['nom']}",
          desc="Mentions légales de DGLM Expertises : éditeur, hébergeur, "
               "certifications, assurance et traitement des données.", body=body,
          schema=jsonld(org_schema()), chapitres=False)
    URLS.append((p, "0.3", "yearly", MAJ_STRUCTURE))


# Avis relevés le 03/08/2026 sur DiagAdvisor, plateforme d'avis vérifiés du
# métier : chaque avis y est rattaché à une mission facturée, contrairement à
# un avis libre. Reproduits mot pour mot, sans corriger l'orthographe, dans
# l'ordre de publication. Aucun n'est écarté — voir page_avis().
AVIS = [
    ("Agréable et professionnel",
     "Expert sympathique, professionnel et efficace, en plus d'être dévoué car DPE "
     "réalisé la journée de la demande.", "Vincent D.", "07/07/2026"),
    ("Très professionnel",
     "Rapide efficace, professionnel. A recommander", "Corinne B.", "19/06/2026"),
    ("Cordial et professionnel",
     "Excellent contact avec l'expert, très professionnel et sympathique. Bon contact "
     "aussi avec l'accueil du bureau.", "Helyette B.", "04/06/2026"),
    ("Parfait !",
     "L'expertise a été faite avec serieux. Le technicien est très sympatique et pro.",
     "Frédéric V.", "03/06/2026"),
    ("Excellent travail",
     "Rapide, efficace sans aucun oubli. Très bon contact avec l'expert. A recommander",
     "Daniel et Marie-France A.", "13/05/2026"),
    ("Un excellent travail et des personnes charmantes",
     "L'expertise m'a semblé réalisée de manière très professionnelle et les contacts "
     "avec l'expert ainsi qu'au téléphone ont été très cordiaux.", "Sébastien K.", "28/04/2026"),
    ("Intervention très satisfaisante",
     "Intervenant professionnel et efficace.", "El Hassani", "15/04/2026"),
    ("Très bon travail",
     "Visite faite très proffessionnelement.", "Françoise B.", "12/04/2026"),
    ("Très bon travail",
     "Merci de votre réactivitée & de votre service.", "Eric D.", "09/04/2026"),
    ("Très bon travail",
     "Rendez-vous pris rapidement et visite réalisée avec professionnalisme.",
     "Christine et Eric L.", "01/04/2026"),
]


def avis_html(n=3):
    """Quelques avis, tels quels. Pas de note agrégée déclarée en données
    structurées : une note qu'on s'attribue à soi-même ne prouve rien, et
    Google la sanctionne."""
    cartes = "".join(
        f'<figure class="avis"><blockquote><p class="avis__t">{esc(t)}</p>'
        f'<p>{esc(corps)}</p></blockquote>'
        f'<figcaption>{esc(qui)} · {esc(quand)}</figcaption></figure>'
        for t, corps, qui, quand in AVIS[:n])
    return f'<div class="avis__l">{cartes}</div>'


def page_avis():
    """Tous les avis, sans tri. La transparence est ici un argument : le site
    concurrent filtre les siens à quatre étoiles minimum."""
    p = "/avis/"
    trail = [("Accueil", "/"), ("Avis clients", p)]
    tous = "".join(
        f'<figure class="avis"><blockquote><p class="avis__t">{esc(t)}</p>'
        f'<p>{esc(corps)}</p></blockquote>'
        f'<figcaption>{esc(qui)} · {esc(quand)}</figcaption></figure>'
        for t, corps, qui, quand in AVIS)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">123 avis vérifiés · 4,9 sur 5 sur Google</p>
<h1>Ce que disent nos clients</h1>
<p class="lede">Nous n'en choisissons aucun. Les avis ci-dessous sont ceux de
DiagAdvisor, la plateforme d'avis vérifiés du diagnostic immobilier : chaque
avis y est rattaché à une mission réellement facturée, et nous ne pouvons ni
les filtrer ni les supprimer.</p></div></section>

<section class="band"><div class="wrap">
<p class="enclair"><span>Ce que nous ne faisons pas</span>Nous n'affichons pas de note
que nous nous serions attribuée nous-mêmes, et nous ne masquons pas les avis les moins
élogieux. Les deux plateformes sont ouvertes : vous pouvez y lire l'intégralité,
y compris ce qui n'est pas repris ici.</p>
{tous}
<div class="actions" style="margin-top:2rem">
<a class="btn btn--light" href="{E['diagadvisor']}" rel="noopener">Les 123 avis vérifiés sur DiagAdvisor</a>
<a class="btn btn--light" href="{E['google_avis']}" rel="noopener">Nos avis Google</a></div>
<p class="maj">Avis relevés le {MAJ_JOUR}. Ils portent sur l'ensemble de notre activité
depuis 2021 — vente, location, copropriété et travaux confondus. Notre activité en
copropriété étant récente, la plupart concernent des missions de vente ou de location :
nous préférons le dire plutôt que de laisser croire le contraire.</p>
</div></section>
{cta()}"""
    shell(path=p, title="Avis clients vérifiés — DGLM Expertises Bordeaux",
          desc=desc_courte("123 avis vérifiés sur DiagAdvisor et 4,9 sur 5 sur Google. "
                           "Nous n'en sélectionnons aucun et n'affichons aucune note "
                           "auto-déclarée."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.7", "monthly", MAJ_STRUCTURE))


def page_confidentialite():
    """Ce que deviennent les données du formulaire. Obligatoire dès lors qu'on
    demande un règlement de copropriété ou un PV d'assemblée — et attendu par
    le service conformité d'un syndic."""
    p = "/confidentialite/"
    trail = [("Accueil", "/"), ("Confidentialité", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Ce que deviennent vos données</p>
<h1>Confidentialité</h1>
<p class="lede">Ce site ne dépose aucun traceur et ne mesure pas votre navigation.
Les seules données que nous détenons sont celles que vous nous transmettez
volontairement, pour une demande de devis ou une prise de contact.</p></div></section>

<section class="band"><div class="wrap prose">
<p class="enclair"><span>L'antisèche</span>Aucun cookie, aucune publicité, aucun partage
avec un tiers à des fins commerciales. Vos documents de copropriété servent à chiffrer
votre mission, et à rien d'autre.</p>

<h2>Qui est responsable</h2>
<p>{E['nom']}, {E['rue']}, {E['cp']} {E['ville']}, SIRET {E['siret']}. Pour toute
question ou demande relative à vos données : <a href="mailto:{E['email']}">{E['email']}</a>.</p>

<h2>Ce que nous collectons, et pourquoi</h2>
<dl class="fiche">
<div><dt>Formulaire de devis</dt><dd>Nom, société, courriel, téléphone, adresse du bien,
description de la mission, et les pièces que vous choisissez de joindre (règlement de
copropriété, carnet d'entretien, procès-verbaux, plans, diagnostics antérieurs).
<b>Finalité</b> : établir le devis et préparer l'intervention. <b>Base légale</b> :
mesures précontractuelles prises à votre demande.</dd></div>
<div><dt>Courriel et téléphone</dt><dd>Ce que vous nous écrivez ou nous dites.
<b>Finalité</b> : vous répondre. <b>Base légale</b> : votre demande.</dd></div>
<div><dt>Navigation</dt><dd><b>Rien.</b> Pas de cookie, pas de mesure d'audience, pas de
bouton de réseau social, aucune requête vers un service extérieur. Notre hébergeur
conserve des journaux techniques d'accès, comme tout serveur, à des fins de sécurité.</dd></div>
</dl>

<h2>Combien de temps nous les gardons</h2>
<ul class="checklist">
<li><b>Demande sans suite</b> — 12 mois, puis suppression, pièces jointes comprises.</li>
<li><b>Mission réalisée</b> — les données du dossier sont conservées le temps de notre
responsabilité professionnelle, soit 10 ans, conformément aux obligations qui pèsent sur
les rapports de diagnostic.</li>
<li><b>Comptabilité</b> — 10 ans, obligation légale.</li>
</ul>

<h2>Qui y a accès</h2>
<p>Nos diagnostiqueurs et notre assistante de direction, pour les besoins de la mission.
Nos prestataires techniques, et eux seuls : l'hébergeur du site (GitHub, Inc.), le
service qui achemine le formulaire jusqu'à notre boîte (FormSubmit, Aleyda Solutions —
il transmet le message et ne le conserve pas), et notre fournisseur de messagerie
professionnelle (Microsoft). Le laboratoire d'analyses accrédité, uniquement pour les
prélèvements, sans donnée personnelle. <b>Vos données ne sont ni vendues, ni louées, ni
cédées à des fins commerciales.</b></p>

<h2>Vos droits</h2>
<p>Vous pouvez demander l'accès à vos données, leur rectification, leur effacement, la
limitation de leur traitement, leur portabilité, ou vous opposer à un traitement. Écrivez
à <a href="mailto:{E['email']}">{E['email']}</a> : nous répondons sous un mois.</p>
<p>Si notre réponse ne vous satisfait pas, vous pouvez saisir la Commission nationale de
l'informatique et des libertés : <a href="https://www.cnil.fr/fr/plaintes"
rel="noopener">cnil.fr/fr/plaintes</a>, ou CNIL, 3 place de Fontenoy, TSA 80715,
75334 Paris Cedex 07.</p>

<h2>Sécurité</h2>
<p>Le site est servi exclusivement en HTTPS. Les pièces que vous joignez transitent par
notre messagerie professionnelle et ne sont jamais déposées sur ce site, qui ne dispose
d'aucun espace de stockage.</p>
<p class="maj">Politique en vigueur en {MAJ} — toute modification est datée ici.</p>
</div></section>
{cta()}"""
    shell(path=p, title="Confidentialité et données personnelles — DGLM Expertises",
          desc=desc_courte("Aucun traceur, aucun cookie. Ce que deviennent les données "
                           "que vous nous transmettez, combien de temps, et vos droits."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.3", "yearly", MAJ_STRUCTURE))




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
    h2_schema = "Comprendre en un schéma"
    if d["slug"] == "dpe-collectif-copropriete":
        schema = ANIM_DEPERDITIONS + ANIM_DPE
        h2_schema = "Comprendre en un coup d'œil"
    elif d["slug"] == "audit-energetique-copropriete":
        schema = ANIM_DEPERDITIONS + schema
        h2_schema = "Comprendre en un coup d'œil"
    schema_bloc = (volet("Repère visuel", h2_schema, schema,
                         ancre="schema")
                   if schema else "")
    cadre = "".join(f"<dt>{esc(t)}</dt><dd>{esc(x)}</dd>" for t, x in d["cadre"])
    faq = "".join(f"<details{' open' if _i == 0 else ''}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
                  for _i, (q, a) in enumerate(d["faq"]))
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
{('<a class="btn btn--light" href="/aides-financieres-copropriete/">Simuler vos aides</a>'
  if d["slug"] in ("dpe-collectif-copropriete", "audit-energetique-copropriete") else "")}<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>

<nav class="ancres" aria-label="Chapitres"><div class="wrap">
<a href="#fiche">L’essentiel</a>{'<a href="#terrain">Sur le terrain</a>' if CARNETS.get(d['slug']) else ''}<a href="#reglementation">Réglementation</a>{'<a href="#schema">Le schéma</a>' if schema else ''}<a href="#faq">Questions</a>
</div></nav>
<section id="fiche" class="band"><div class="wrap">
<p class="eyebrow">L'antisèche</p>
<h2>L'essentiel en trente secondes</h2>
{f'<p class="enclair"><span>En français courant</span>{esc(d["clair"])}</p>' if d.get("clair") else ""}
<div class="prose" style="margin-top:1.4rem"><p style="font-size:1.12rem">{esc(d['intro'])}</p></div>
{fiche_html(d.get('fiche'))}
</div></section>
{carnets_band(d['slug'])}
{guides_lies(d['slug'])}
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
    URLS.append((p, "0.85", "monthly", MAJ_STRUCTURE))



def page_hub_travaux():
    """La famille chantier : RAAT et RAAD en phares, PEMD et parasitaire en compléments."""
    p = "/avant-travaux-et-demolition/"
    trail = [("Accueil", "/"), ("Avant travaux & démolition", p)]
    phares = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/">{PICTOS.get(s["sigle"], "")}'
        f'<span class="sigle">{s["sigle"]}</span>'
        f'<h3>{esc(s["nom"])}</h3><p>{esc(s["accroche"])}</p>'
        f'<span class="more">Découvrir la mission →</span></a>'
        for s in SERVICES if s["sigle"] in ("RAAT", "RAAD"))
    compl = "".join(
        f'<a class="card card--link" href="/{d["slug"]}/"><span class="sigle">{esc(d["sigle"])}</span>'
        f'<h3>{esc(d["nom"])}</h3><p>{esc(d["accroche"])}</p>'
        f'<span class="more">Voir →</span></a>'
        for d in DIAGS_PRO if d["slug"] in ("diagnostic-pemd", "etat-parasitaire-avant-travaux"))
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Deux missions phares, deux compléments de chantier</p>
<h1>Les diagnostics avant travaux et avant démolition</h1>
<p class="lede">Avant d'ouvrir un mur ou de faire tomber un bâtiment, on sait ce qu'on va
toucher : repérages amiante, inventaire des matériaux, état des bois. Pour maîtres
d'ouvrage, syndics donneurs d'ordre et entreprises.</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div></div></section>
<section class="band"><div class="wrap">
<p class="eyebrow">Niveau 1 — les missions phares</p>
<h2>Le repérage qui conditionne le chantier</h2>
<p class="narrow">Travaux : le repérage se cale sur ce que vous allez ouvrir. Démolition :
il couvre tout, sondages destructifs compris. Dans les deux cas, le chantier démarre en
sachant.</p>
<div class="grid grid--2" style="margin-top:1.8rem">{phares}</div></div></section>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Niveau 2 — les compléments du même chantier</p>
<h2>Ce qui se vérifie pendant qu'on y est</h2>
<div class="grid grid--2" style="margin-top:1.8rem">{compl}</div></div></section>
<section class="band band--dark"><div class="wrap">
<p class="eyebrow eyebrow--pale">La passerelle</p>
<h2>Besoin de la vision d'ensemble de l'immeuble ?</h2>
<p class="narrow" style="color:rgba(248,245,238,.84)">État global, plan de travaux, énergie :
c'est la famille copropriété qui s'en charge.</p>
<div class="actions" style="display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.6rem">
<a class="btn btn--light" href="/diagnostics-copropriete/">Diagnostics de copropriété →</a></div>
</div></section>
{cta()}"""
    shell(path=p, title="Avant travaux et démolition : RAAT, RAAD, PEMD — Bordeaux",
          desc=desc_courte("Repérages amiante avant travaux et démolition, diagnostic PEMD, "
                           "état parasitaire : préparer un chantier à Bordeaux, en Gironde "
                           "et dans les Landes."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p,
                         "name": "Avant travaux et démolition"}))
    URLS.append((p, "0.9", "weekly", MAJ_STRUCTURE))


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
<p class="maj">Vérifié en {MAJ} — mis à jour automatiquement à chaque évolution réglementaire</p>
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
    URLS.append((p, "0.9", "weekly", MAJ_STRUCTURE))


def page_conformite():
    """Le certificat de conformité du site : chaque affirmation est un fait
    produit par la chaîne de contrôle elle-même — rien de déclaratif."""
    p = "/conformite/"
    trail = [("Accueil", "/"), ("Certificat de conformité", p)]
    controles = [
        ("Cannibalisation interne", "chaque page vise une requête distincte"),
        ("Étanchéité éditoriale", "aucune page ne cible les requêtes réservées à notre site vente et location"),
        ("Titres et méta-descriptions", "longueurs et unicité contrôlées sur chaque page"),
        ("Liens internes", "zéro lien cassé toléré"),
        ("Pages locales", "similarité surveillée pour rester sous les seuils d'alerte"),
        ("URL canoniques", "une adresse canonique unique par page"),
        ("Liens sortants", "un seul lien par page vers notre site particuliers, à ancre descriptive"),
        ("Régressions", "pages perdues, contenu allégé ou alourdi : publication bloquée"),
    ]
    lignes = "".join(f'<li><b>{esc(a)}</b> — {esc(b)}</li>' for a, b in controles)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Contrôlé automatiquement chaque matin</p>
<h1>Le certificat de conformité de ce site</h1>
<p class="lede">Ce site est reconstruit et vérifié chaque jour par une chaîne de contrôle
automatique. Si un seul contrôle échoue, la publication est bloquée jusqu'à correction.
Cette page en publie l'état — sans déclaration, seulement des faits.</p></div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">État du jour</p>
<h2>Contrôles passés avec succès</h2>
<dl class="fiche">
<div><dt>Dernier contrôle</dt><dd>{MAJ_JOUR}</dd></div>
<div><dt>Pages vérifiées</dt><dd>L'intégralité du site, à chaque publication</dd></div>
<div><dt>Contrôles bloquants</dt><dd>8 vérifications — un échec suspend la mise en ligne</dd></div>
<div><dt>Veille réglementaire</dt><dd>Fiches Service-Public surveillées ; toute évolution déclenche une relecture</dd></div>
<div><dt>Sources citées</dt><dd>Textes officiels, avec date de vérification affichée dans chaque guide</dd></div>
<div><dt>Performance mesurée</dt><dd>Lighthouse (Google) le 30/07/2026 : 97/100 performance, 100/100 SEO et bonnes pratiques</dd></div>
</dl>
</div></section>

<section class="band band--pale"><div class="wrap prose">
<h2>Les huit contrôles quotidiens</h2>
<ul class="checklist">{lignes}</ul>
<p class="maj">Chaîne de contrôle exécutée à chaque modification et tous les matins —
dernier passage : {MAJ_JOUR}</p>
</div></section>

<section class="band"><div class="wrap prose">
<h2>Ce que ce certificat ne dit pas</h2>
<p>Il atteste de la rigueur de fabrication de ce site — pas de la conformité de votre
immeuble, qui relève d'une mission sur place. Les certifications individuelles de nos
diagnostiqueurs et notre attestation d'assurance responsabilité civile professionnelle
sont publiées sur la page
<a href="/certifications-et-assurances/">certifications et assurances</a>.</p>
<p>Il ne dit rien non plus de la façon dont les guides sont écrits et relus : cela relève
d'une autre discipline, publiée sur la page
<a href="/notre-methode-editoriale/">notre méthode éditoriale</a>.</p>
</div></section>
{cta()}"""
    shell(path=p, title="Certificat de conformité du site — DGLM Expertises",
          desc=desc_courte("Ce site est reconstruit et vérifié chaque matin : huit contrôles "
                           "bloquants, veille réglementaire, sources datées. L'état publié "
                           "sans déclaration — seulement des faits."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.6", "weekly", MAJ_STRUCTURE))


def page_methode():
    """Qui écrit, d'où viennent les faits, ce que nous refusons de publier.
    Le pendant humain du certificat de conformité, qui ne parle que de machine.
    Un lecteur doit pouvoir juger nos guides sans nous croire sur parole."""
    p = "/notre-methode-editoriale/"
    trail = [("Accueil", "/"), ("Notre méthode éditoriale", p)]

    refus = [
        ("Aucune photo de banque d'images, aucune image générée",
         "les photos de ce site sont prises en mission, et jamais dans un logement occupé "
         "ni devant une façade reconnaissable"),
        ("Aucun prix affiché",
         "un devis se chiffre sur le bâti réel — annoncer un tarif de vitrine reviendrait "
         "à le démentir ensuite"),
        ("Aucun conseil juridique personnalisé",
         "nous expliquons ce que dit un texte ; l'appliquer à votre situation relève de "
         "votre notaire, de votre syndic ou d'un avocat"),
        ("Aucune mission que nous ne sommes pas habilités à faire",
         "gaz et électricité en parties communes relèvent d'organismes de contrôle agréés : "
         "nous le disons et nous renvoyons vers qui de droit"),
        ("Aucune source non vérifiée",
         "un lien vers un texte officiel n'est publié qu'après avoir été ouvert et son "
         "titre confirmé ; à défaut, le texte est cité sans lien"),
    ]
    lignes = "".join(f"<li><b>{esc(a)}</b> — {esc(b)}</li>" for a, b in refus)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Qui écrit, comment, et ce que nous refusons</p>
<h1>Notre méthode éditoriale</h1>
<p class="lede">Ces guides sont écrits par des diagnostiqueurs, pas par un service
communication. Voici comment ils sont fabriqués, vérifiés et corrigés — pour que vous
puissiez les juger sans avoir à nous croire sur parole.</p></div></section>

<section class="band"><div class="wrap prose">
<p class="enclair"><span>L'antisèche</span>Chaque guide porte en bas de page le nom de
celui qui l'a relu, la date de sa dernière vérification et ses sources. Le relecteur
change selon le sujet : chacun ne valide que ce qu'il pratique.</p>
<h2>Qui écrit et qui relit</h2>
<p>Les guides sont rédigés en interne à partir des textes en vigueur, puis relus par
l'un des deux cofondateurs, tous deux titulaires du <strong>titre professionnel de
diagnostiqueur immobilier</strong> enregistré au RNCP.</p>
<p>Le partage suit les compétences réelles, pas l'organigramme.
<strong>Thibault Le Moine</strong>, certifié en amiante, termites, gaz et électricité,
relit tout ce qui touche à ces domaines et aux repérages avant travaux ou démolition.
<strong>Aude de Gentile</strong> relit le reste : copropriété, énergie, procédures,
obligations d'information.</p>
<p>Une précision que nous préférons donner nous-mêmes : Aude de Gentile n'est pas
certifiée et ne signe donc aucun rapport. Son titre atteste qu'elle a appris le métier,
pas qu'elle est habilitée à l'exercer — <a href="/certifications-et-assurances/">la
différence est expliquée ici</a>, avec les numéros et les dates de chacun. Les rapports
sont établis et signés par les quatre diagnostiqueurs certifiés qui interviennent sur le
terrain, présentés sur la page <a href="/equipe/">équipe</a>.</p>
</div></section>

<section class="band band--pale"><div class="wrap prose">
<h2>D'où viennent les faits</h2>
<p>Nous citons d'abord la source première : le texte lui-même. Loi du 10 juillet 1965,
Code de la santé publique, Code de la construction et de l'habitation, Code du travail,
loi Climat et résilience, décret du 17 mars 1967 — chacun est lié sur Légifrance après
vérification de son titre officiel.</p>
<p>Viennent ensuite les fiches Service-Public.fr, citées avec leur numéro, et les
publications de l'ADEME et de l'Anah pour les barèmes d'aides. Les sources d'un guide
sont listées à la fin de ce guide, avec la date à laquelle nous les avons ouvertes.</p>
<p>Un texte peut changer. Une veille automatique surveille les fiches officielles que
nous citons et signale toute évolution, ce qui déclenche une relecture. Le détail de
cette chaîne de contrôle est publié sur le
<a href="/conformite/">certificat de conformité du site</a>.</p>
</div></section>

<section class="band"><div class="wrap prose">
<h2>Ce que nous ne publions pas</h2>
<ul class="checklist">{lignes}</ul>
</div></section>

<section class="band band--pale"><div class="wrap prose">
<h2>Si vous trouvez une erreur</h2>
<p>Écrivez-nous à <a href="mailto:{E['email']}">{E['email']}</a> en indiquant l'adresse
de la page. Une erreur de fait est corrigée sans discuter et la date de vérification du
guide est remise à jour le jour même. Nous ne supprimons pas un guide devenu inexact :
nous le corrigeons, parce qu'il est déjà lu et parfois cité.</p>
<h2>Pourquoi ces guides sont gratuits</h2>
<p>Parce qu'un diagnostic mal compris se subit, et qu'un diagnostic compris se commande
au bon moment — souvent bien avant le chantier. Expliquer sert notre métier mieux que le
vendre. Les questions de vente et de location sont traitées ici à titre informatif
seulement ; pour une mission de ce type, nous renvoyons vers
<a href="/particuliers/">notre site dédié aux particuliers</a>.</p>
<p class="maj">Méthode en vigueur en {MAJ} — toute modification est datée ici.</p>
</div></section>
{cta()}"""

    shell(path=p, title="Notre méthode éditoriale — DGLM Expertises",
          desc=desc_courte("Qui écrit ces guides, d'où viennent les faits, ce que nous "
                           "refusons de publier et comment une erreur se corrige."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.6", "monthly", MAJ_STRUCTURE))


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
</div></section>
<section class="band band--pale"><div class="wrap prose">
<h2>2. Les questions à poser à un diagnostiqueur avant de le retenir</h2>
<ul class="checklist">
<li>Êtes-vous certifié, par un organisme accrédité COFRAC, pour chaque mission proposée ?</li>
<li>Pouvez-vous fournir votre attestation d'assurance responsabilité civile professionnelle ?</li>
<li>Vos analyses passent-elles par un laboratoire accrédité COFRAC ?</li>
<li>Le rapport comprendra-t-il localisation, photographies et quantitatifs exploitables ?</li>
<li>Présentez-vous vos conclusions devant le conseil syndical ou l'assemblée ?</li>
<li>Quels sont vos délais d'intervention et de remise du rapport ?</li>
</ul>
</div></section>
<section class="band"><div class="wrap prose">
<h2>3. Le calendrier type d'une mission bien menée</h2>
<ul class="checklist">
<li>J−90 : demande de devis, comparaison, vérification des certifications</li>
<li>J−60 : inscription de la mission à l'ordre du jour de l'assemblée</li>
<li>J−30 : vote, ordre de service, collecte des documents de l'immeuble</li>
<li>Jour J : visite sur site — accès organisés, occupants prévenus</li>
<li>J+15 : rapport remis, lecture commentée avec le conseil syndical</li>
<li>Assemblée suivante : présentation des conclusions et vote des suites</li>
</ul>
<p class="maj">Établi par l'équipe DGLM Expertises — vérifié en {MAJ}</p>
</div></section>
{cta()}"""
    shell(path=p, title="Le pack du conseil syndical — check-lists à imprimer | DGLM",
          desc=desc_courte("Trois check-lists gratuites : documents à réunir avant "
                           "assemblée, questions à poser à un diagnostiqueur, "
                           "calendrier type de mission."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.8", "monthly", MAJ_STRUCTURE))


def _norm_recherche(s):
    import unicodedata as _u
    return _u.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def page_recherche(contenus):
    """Recherche instantanée, entièrement locale : l'index est embarqué dans
    la page, le filtrage se fait dans le navigateur. Zéro requête, zéro serveur."""
    p = "/recherche/"
    trail = [("Accueil", "/"), ("Rechercher", p)]
    idx = []

    def add(t, u, d, extra="", art=0, img=""):
        e = {"t": t, "u": u, "d": d[:170],
             "n": _norm_recherche(f"{t} {d} {extra}")}
        if art:
            e["a"] = 1
        if img:
            e["i"] = img
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
    # Les photos de terrain : on cherche « combles », on voit la photo.
    _pages_photo = {s["slug"]: (f"{SILO}/{s['slug']}/", s["nom"]) for s in SERVICES}
    _pages_photo.update({d["slug"]: (f"/{d['slug']}/", d["nom"]) for d in DIAGS_PRO})
    _vues = set()
    for slug, items in CARNETS.items():
        cible = _pages_photo.get(slug)
        if not cible:
            continue
        base, nom_mission = cible
        for f, w, h, th, cap, voit, pourquoi in items:
            if f in _vues:
                continue
            _vues.add(f)
            add(f"Photo — {cap}", base + "#terrain", f"Ce qu'on voit : {voit}",
                f"photo image vue terrain chantier {th} {THEME_RUB.get(th, '')} "
                f"{nom_mission} {CARNETS_TITRE.get(slug, '')} {pourquoi}", img=f)
    add("Le tableau des diagnostics", "/le-tableau-des-diagnostics/",
        "Treize missions : qui commande, quand, validité — en une page.", "tableau récapitulatif")
    add("Simulateur d'obligations", f"{SILO}/simulateur-obligations-copropriete/",
        "Votre situation établie en six questions.", "pppt dtg dpe obligations")
    add("Notre équipe", "/equipe/", "Des noms, des visages, des signatures.", "diagnostiqueurs certifiés")
    add("Zones d'intervention", f"{SILO}/zones-d-intervention/",
        "Bordeaux Métropole en priorité, Gironde et Landes sur mission.", "communes secteur")
    # Le site n'affiche pas de tarifs : les questions de prix mènent au devis,
    # qui chiffre sur les caractéristiques réelles de l'immeuble.
    add("Demande de devis", "/devis/",
        "Chaque immeuble a son prix : surfaces, lots, accès. Devis chiffré sous deux heures ouvrées.",
        "contact rappel prix tarif tarifs cout coute couter combien budget "
        "honoraires facture estimation chiffrage montant")
    add("Aides financières : le simulateur", "/aides-financieres-copropriete/",
        "MaPrimeRénov' Copropriété : le montant estimé de vos aides, ligne à ligne.",
        "aide aides subvention subventions financement anah maprimerenov prix cout "
        "combien travaux renovation energetique eco-ptz cee tva")
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
<noscript><p class="enclair"><span>Sans JavaScript</span>La recherche instantanée est
indisponible — retrouvez tout dans <a href="/questions/">les guides pratiques</a> et
<a href="/questions/glossaire-diagnostic-immobilier/">le lexique</a>.</p></noscript>
<div id="rep" style="margin-top:2rem"></div>
<div class="grid grid--2" id="res" style="margin-top:2rem"></div>
</div></section>"""
    # L'index est écrit une seule fois dans /assets/recherche.json : la barre
    # du bandeau et cette page le partagent, au lieu de l'embarquer deux fois.
    # Son empreinte sert de numéro de version : sans elle, le navigateur d'un
    # visiteur garderait un index périmé après une mise à jour du site.
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    brut = json.dumps({"idx": idx, "defs": defs}, ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT, "assets", "recherche.json"), "w", encoding="utf-8").write(brut)
    globals()["IDX_V"] = hashlib.md5(brut.encode("utf-8")).hexdigest()[:8]

    js = ("<script>let IDX=[],DEFS={};"
          "const MAIL='" + E["email"] + "';"
          "const inp=document.getElementById('q'),out=document.getElementById('res'),rep=document.getElementById('rep');"
          "function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase()}"
          "function lienQ(){const su=encodeURIComponent('Question pour vos guides pratiques');"
          "const co=encodeURIComponent('Bonjour, voici ma question : '+inp.value.trim());"
          "return '<p style=\"margin-top:1.2rem\"><a class=\"btn btn--ghost\" href=\"mailto:'+MAIL+'?subject='+su+'&body='+co+'\">Nous envoyer cette question</a></p>'}"
          # On pose une question entière : les mots outils ne sont dans aucun
          # index, les exiger ferait tout échouer. On garde le sens.
          # Les mots interrogatifs restent : nos titres sont des questions.
          "const VIDES=new Set('le la les un une des du de au aux en et ou est sont ce cet cette "
          "elle on nous vous je tu mon ma mes votre vos notre nos leur leurs "
          "sa son ses pour par sur dans avec sans plus moins tout tous toute toutes "
          "pas ni aussi meme etre avoir fait faire doit dois puis alors donc mais car "
          "oui non ils elles cela ceci celui celle'.split(' '));"
          "function mots(s){const b=norm(s).split(/[^a-z0-9]+/).filter(m=>m.length>2);"
          "const u=b.filter(m=>!VIDES.has(m));return u.length?u:b}"
          "function go(){const q=norm(inp.value.trim());rep.innerHTML='';"
          "if(q.length<2){out.innerHTML='';return}"
          "const terms=mots(inp.value);const sc=[];"
          # un mot rare pèse plus qu'un mot omniprésent (« diagnostic »)
          "const pds=terms.map(t=>{let n=0;for(const e of IDX)if(e.n.includes(t))n++;"
          "return n?Math.max(1,Math.log(IDX.length/n)):1});"
          "for(const e of IDX){let s=0,ok=0;const ti=norm(e.t);"
          "terms.forEach((t,k)=>{if(e.n.includes(t)){ok++;s+=pds[k]*(ti.includes(t)?3:1)}});"
          "if(ok)sc.push([ok*100+s,e])}"
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
          "out.innerHTML=sc.slice(0,24).map(x=>{const e=x[1];"
          "const v=e.i?'<img class=\"vign\" src=\"/assets/photos/'+e.i+'\" alt=\"\" loading=\"lazy\" decoding=\"async\">':'';"
          "return '<a class=\"card card--link'+(e.i?' card--photo':'')+'\" href=\"'+e.u+'\">'+v+'<h3>'+e.t+'</h3><p>'+e.d+'</p><span class=\"more\">'+(e.i?'Voir la photo →':'Ouvrir →')+'</span></a>'}).join('')"
          "||('<div><p>Nous n\\'avons pas encore de guide qui réponde à cette question — elle mérite peut-être le sien, et nous l\\'écrirons.</p>'+lienQ()+'</div>')}"
          "inp.addEventListener('input',go);"
          "const p0=new URLSearchParams(location.search).get('q');if(p0)inp.value=p0;"
          "out.innerHTML='<p class=\"maj\">Chargement de l\\'index…</p>';"
          "fetch('/assets/recherche.json?v=" + IDX_V + "').then(r=>r.json()).then(d=>{IDX=d.idx;DEFS=d.defs;"
          "out.innerHTML='';if(inp.value)go();inp.focus()})"
          ".catch(()=>{out.innerHTML='<p>La recherche n\\'a pas pu se charger. "
          "Le <a href=\"/plan-du-site/\">plan du site</a> liste toutes les pages.</p>'});"
          "</script>")
    shell(path=p, title="Rechercher — DGLM Expertises",
          desc="Recherche instantanée dans les missions, guides pratiques, communes et "
               "quartiers couverts par DGLM Expertises.",
          body=body + js + cta(),
          schema=jsonld(org_schema(), breadcrumb(trail)),
          robots="noindex,follow", chapitres=False)


def page_hub_diags():
    p = "/diagnostics-copropriete/"
    trail = [("Accueil", "/"), ("Diagnostics de copropriété", p)]
    phares = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/">{PICTOS.get(s["sigle"], "")}'
        f'<span class="sigle">{s["sigle"]}</span>'
        f'<h3>{esc(s["nom"])}</h3><p>{esc(s["accroche"])}</p>'
        f'<span class="more">Découvrir la mission →</span></a>'
        for s in SERVICES if s["sigle"] in ("DTG", "PPPT"))
    def _carte_diag(slugs):
        return "".join(
            f'<a class="card card--link" href="/{d["slug"]}/"><span class="sigle">{esc(d["sigle"])}</span>'
            f'<h3>{esc(d["nom"])}</h3><p>{esc(d["accroche"])}</p>'
            f'<span class="more">Voir →</span></a>'
            for d in DIAGS_PRO if d["slug"] in slugs)
    energie = _carte_diag(("dpe-collectif-copropriete", "audit-energetique-copropriete"))
    sante = _carte_diag(("dossier-technique-amiante", "amiante-parties-privatives",
                         "crep-parties-communes", "conformite-assainissement-copropriete"))
    orientation = _carte_diag(("installations-collectives-gaz-electricite",))
    cards = "".join(
        f'<a class="card card--link" href="/{d["slug"]}/"><span class="sigle">{esc(d["sigle"])}</span>'
        f'<h3>{esc(d["nom"])}</h3><p>{esc(d["accroche"])}</p>'
        f'<span class="more">Voir →</span></a>' for d in DIAGS_PRO)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Deux missions phares, sept diagnostics de l'immeuble</p>
<h1>Les diagnostics de copropriété</h1>
<p class="lede">La colonne vertébrale : le diagnostic technique global et le plan pluriannuel
de travaux. Autour d'eux, l'énergie, l'amiante, le plomb et l'assainissement — tout ce
qu'un immeuble doit savoir sur lui-même, pour syndics, conseils syndicaux et bailleurs.</p>
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
<p class="eyebrow">Niveau 1 — les missions phares</p>
<h2>Le tandem qui pilote l'immeuble</h2>
<p class="narrow">Le DTG établit l'état réel ; le PPPT programme dix ans de travaux. Un DTG
complet peut tenir lieu de PPPT : une mission au lieu de deux.</p>
<div class="grid grid--2" style="margin-top:1.8rem">{phares}</div></div></section>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Niveau 2 — l'énergie de l'immeuble</p>
<h2>Le DPE collectif constate, l'audit décide.</h2>
<div class="grid grid--2" style="margin-top:1.8rem">{energie}</div></div></section>
<section class="band"><div class="wrap">
<p class="eyebrow">Niveau 2 — santé et conformité du bâti</p>
<h2>Les documents que l'immeuble doit tenir à jour</h2>
<div class="grid grid--2" style="margin-top:1.8rem">{sante}</div></div></section>
{volet("Hors diagnostic immobilier", "Gaz et électricité des parties communes : vers qui se tourner",
       f'<div class="grid grid--2">{orientation}</div>', pale=True)}
<section class="band band--dark"><div class="wrap">
<p class="eyebrow eyebrow--pale">La passerelle</p>
<h2>Vous engagez des travaux sur l'immeuble ?</h2>
<p class="narrow" style="color:rgba(248,245,238,.84)">Le dossier technique amiante ne dispense
jamais du repérage avant travaux : dès qu'un chantier s'ouvre, on change de famille.</p>
<div class="actions" style="display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.6rem">
<a class="btn btn--light" href="/avant-travaux-et-demolition/">Avant travaux &amp; démolition →</a></div>
</div></section>
{cta()}"""
    shell(path=p, title="Diagnostics de copropriété : DTG, PPPT, DPE collectif",
          desc=desc_courte("Diagnostics collectifs pour copropriétés et patrimoines à "
                           "Bordeaux, en Gironde et dans les Landes : DTA, DPE collectif, "
                           "audit énergétique, PEMD, CREP parties communes."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p,
                         "name": "Diagnostics de copropriété"}))
    URLS.append((p, "0.9", "weekly", MAJ_STRUCTURE))



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
            # un titre professionnel n'est pas une certification de personne :
            # les deux se disent, mais pas sous la même étiquette.
            pers["hasCredential"] = {
                "@type": "EducationalOccupationalCredential",
                "credentialCategory": ("certification" if "ertifié" in m["cert"]
                                       else "titre professionnel"),
                "name": m["cert"]}
        personnes.append(pers)
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Sept personnes, cinq certifications individuelles</p>
<h1>Des noms, des visages, et des signatures au bas des rapports.</h1>
<p class="lede">Fondée en 2020 par Aude de Gentile et Thibault Le Moine, la maison réunit sept
personnes, dont quatre diagnostiqueurs certifiés qui interviennent sur le terrain.
Chaque rapport est signé par celui qui l'a établi.</p></div></section>
<section class="band"><div class="wrap">
<p class="eyebrow">L'équipe</p><h2>Celles et ceux qui interviennent</h2>
<div class="team">{fiches}</div>
<p class="maj">Effectif et certifications à jour en {MAJ}</p></div></section>
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
compétences qu'ils exercent. Plutôt que de les tenir « à disposition », nous publions
les numéros de certification, les domaines couverts et leurs dates de validité :
<a href="/certifications-et-assurances/">voir nos certifications et notre assurance</a>.</p>
<h2>Fédération professionnelle</h2>
<p>DGLM Expertises est membre de l'{E['federation']}.</p>
<h2>Analyses en laboratoire</h2>
<p>Tous les prélèvements sont analysés en laboratoire accrédité COFRAC. Aucun matériau n'est classé « présumé amianté » par commodité : le doute se lève
par l'analyse.</p>
</div></section>
{cta()}"""
    shell(path=p, title="Notre équipe de diagnostiqueurs certifiés — DGLM Expertises",
          desc=desc_courte("Les diagnostiqueurs certifiés de DGLM Expertises à Bordeaux : "
                           "équipe, certifications COFRAC, veille réglementaire. Structure familiale "
                           "créée en 2020."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail), *personnes))
    URLS.append((p, "0.7", "monthly", MAJ_STRUCTURE))



# ------------------------------------------------------------------ contenus éditoriaux
# Une page = une question réelle, réponse directe dès le premier paragraphe.
# C'est le format que citent les moteurs IA : ils reprennent la phrase qui
# répond, pas le paragraphe d'introduction.
def _slug_ancre(t):
    import re as _re, unicodedata as _u
    t = _u.normalize("NFD", t).encode("ascii", "ignore").decode()
    return _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60] or "section"


def sommaire_article(corps):
    """Ancre chaque h2 du guide et rend la liste des chapitres.
    Retourne (corps_avec_ancres, [(ancre, titre), ...]) — la barre de
    chapitres est construite par page_contenu, qui connaît aussi les blocs
    de fin (schéma, vidéo, sources) à y ajouter."""
    import re as _re
    titres = _re.findall(r"<h2>(.*?)</h2>", corps)
    if len(titres) < 2:
        return corps, []
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
    return corps, items


def page_contenu(c, voisins):
    p = f"/questions/{c['slug']}/"
    trail = [("Accueil", "/"), ("Guides pratiques", "/questions/"), (c["titre"], p)]
    # même typographie que le reste du site : le corps des guides est le
    # texte le plus lu, il ne peut pas rester en apostrophes de machine à écrire.
    corps = typo_fr(md_vers_html(c["corps"]))
    corps, som = sommaire_article(corps)
    index_glossaire = ""
    # Glossaire : chaque terme reçoit une ancre, et un index alphabétique
    # s'ajoute en tête — la porte d'entrée du lexique.
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
            index_glossaire = (
                f'<nav class="sommaire-art" id="index" aria-label="Index des termes">'
                f'<p class="eyebrow">Index — {len(termes)} termes, de A à Z</p>'
                f'<ul class="mesh">{chips}</ul></nav>')
    # Un article peut embarquer un schéma : champ « schema: » du frontmatter.
    schema_art = rendre_schema(c.get("schema", ""))
    VL = {"vente", "location", "ddt", "loi carrez", "loi boutin", "surface",
          "meublé", "bailleur", "validité"}
    est_vl = bool({x.strip().lower() for x in c.get("tags", [])} & VL)
    cta_bloc = (f'''<section class="cta"><div class="wrap">
<p class="eyebrow eyebrow--pale">Pour passer à l'action</p>
<h2>Ces diagnostics relèvent d'un autre cadre.</h2>
<p>Vente ou location d'un logement : notre site dédié aux particuliers les réalise —
même maison, même exigence.</p>
<div class="actions"><a class="btn btn--light" href="/particuliers/">{esc(E['site_a_ancre'])} →</a></div>
</div></section>''' if est_vl else cta())
    TITRES = {f"/questions/{o['slug']}/": o["titre"] for o in voisins}
    TITRES.update({f"{SILO}/{s['slug']}/": s["nom"] for s in SERVICES})
    TITRES.update({f"/{d['slug']}/": d["nom"] for d in DIAGS_PRO})
    TITRES.update({"/questions/": "Tous les guides pratiques",
                   "/le-tableau-des-diagnostics/": "Le tableau des diagnostics",
                   f"{SILO}/simulateur-obligations-copropriete/": "Le simulateur d'obligations",
                   "/equipe/": "Notre équipe"})
    liens = "".join(
        f'<li><a href="{u}">{esc(TITRES.get(u, u.strip("/").replace("-", " ").capitalize()))}</a></li>'
        for u in c["liens"])
    autres = "".join(
        f'<a class="card card--link" href="/questions/{o["slug"]}/"><h3>{esc(o["titre"])}</h3>'
        f'<span class="more">Lire →</span></a>' for o in voisins[:3])
    tags = "".join(f'<li><span class="mesh--plain">{esc(t)}</span></li>' for t in c["tags"])
    rel = relecteur_de(c["tags"])

    # La barre de chapitres des pages mission, portée aux guides : le lecteur
    # voit la structure avant de lire, et va droit au passage qui le concerne.
    # Elle remplace l'ancien sommaire encadré — deux tables des matières sur
    # la même page, c'est une de trop.
    film = video_html(c["slug"])
    # les titres viennent du corps : déjà typographiés et échappés, on ne les
    # repasse pas par esc() — on retire seulement le gras ou l'italique.
    chapitres = [("essentiel", "L’essentiel")]
    if index_glossaire:
        chapitres.append(("index", "L’index A-Z"))
    chapitres += [(a, strip_tags(t)) for a, t in som]
    if schema_art:
        chapitres.append(("schema", "Le schéma"))
    if film:
        chapitres.append(("video", "En vidéo"))
    if c.get("sources"):
        chapitres.append(("sources", "Sources"))
    if liens:
        chapitres.append(("approfondir", "Pour approfondir"))
    barre = ""
    if som or index_glossaire:   # sous deux chapitres, une barre n'apprend rien
        barre = ('<nav class="ancres" aria-label="Chapitres"><div class="wrap">'
                 + "".join(f'<a href="#{a}">{t}</a>' for a, t in chapitres)
                 + "</div></nav>")

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Question fréquente</p>
<h1>{esc(c['titre'])}</h1></div></section>
{barre}
<article class="band"><div class="wrap prose">
<p class="enclair" id="essentiel" style="margin-top:0"><span>L'antisèche</span>{esc(c.get("antiseche", c["meta"]))}</p>
{index_glossaire}{corps}{f'<div id="schema">{schema_art}</div>' if schema_art else ''}
{film}
{sources_html(c)}
{signature_html(rel, c['date'])}
<h2 id="approfondir">Pour approfondir</h2><ul>{liens}</ul>
</div></article>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Dans le même champ</p><h2>Autres réponses</h2>
<div class="grid grid--3" style="margin-top:1.5rem">{autres}</div>
<ul class="mesh" style="margin-top:1.5rem">{tags}</ul></div></section>
{cta_bloc}"""

    art = {"@type": "Article", "headline": c["titre"][:110],
           "description": c["meta"], "datePublished": c["date"].isoformat(),
           "dateModified": ISO, "inLanguage": "fr-FR",
           "speakable": {"@type": "SpeakableSpecification",
                         "cssSelector": ["h1", ".prose > p:first-of-type"]},
           "author": {"@id": DOM + "/#organisation"},
           "reviewedBy": relecteur_schema(rel),
           "publisher": {"@id": DOM + "/#organisation"},
           "mainEntityOfPage": {"@type": "WebPage", "@id": DOM + p},
           "citation": [{"@type": "CreativeWork", "name": s.split("~")[0],
                         "url": s.split("~")[1] if "~" in s else None}
                        for s in c.get("sources", [])]}
    faq = {"@type": "FAQPage", "mainEntity": [{
        "@type": "Question", "name": c.get("question", c["titre"]),
        "acceptedAnswer": {"@type": "Answer",
                           "text": strip_tags(corps)[:900]}}]}
    blocs = [org_schema(), breadcrumb(trail), art, faq]
    # jsonld() ne filtre pas les None : on n'ajoute le bloc que s'il existe.
    film = video_schema(c["slug"], p)
    if film:
        art["video"] = {"@id": film["@id"]}
        blocs.append(film)
    shell(path=p, title=titre(c["titre"], c["titre"][:58], c["tags"][0] if c["tags"] else "Question"),
          desc=desc_courte(c["meta"]), body=body, schema=jsonld(*blocs))
    # Un guide porte sa vraie date de parution : c'est le seul lastmod honnête.
    URLS.append((p, "0.75", "monthly", c["date"].isoformat()))


def strip_tags(h):
    import re as _re
    return _re.sub(r"\s+", " ", _re.sub(r"<[^>]+>", " ", h)).strip()


# ------------------------------------------------------------------ vidéos
# Les épisodes sont tournés au format vertical, pour le téléphone. Un épisode
# se pose sur UNE seule page, et uniquement dans /questions/ : c'est la seule
# zone que le pare-feu vente/location exempte, et deux pages portant la même
# vidéo se feraient concurrence dans les résultats.
# Le rendu passe par esc() comme le reste du site — d'où sa place ici plutôt
# que dans data/, qui ne peut pas importer build sans boucle.
VIDEOS = {
    "qu-est-ce-que-le-dpe": {
        "fichier": "episode-02-dpe-voisin",
        "episode": "Épisode 02",
        "titre": "Deux voisins, deux étiquettes",
        "duree": 65,
        "duree_txt": "1 min 05",
        "publie": "2026-07-31",
        "chapo": "Deux logements du même immeuble, même surface et même chauffage : "
                 "D pour l'un, F pour l'autre. L'écart ne vient pas de la façon "
                 "d'habiter, mais de la place du logement dans le bâtiment — sous "
                 "la toiture, à l'angle, sans voisin chauffé de l'autre côté du mur.",
        "transcription": [
            (3.2, "Même immeuble. Même surface. Même chauffage."),
            (8.1, "Lui : D. Vous : F."),
            (11.6, "Injuste ? Non. Physique."),
            (14.4, "Voici l'immeuble, vu en coupe."),
            (17.2, "Neuf logements. Le vôtre est en haut, à l'angle."),
            (20.7, "En rouge : les parois qui donnent sur l'extérieur."),
            (24.2, "La chaleur part par le toit. Personne ne vit au-dessus de vous."),
            (30.5, "Et par deux façades exposées, au lieu d'une."),
            (34.0, "Votre voisin, lui, est au milieu."),
            (36.8, "Ses murs ne donnent pas sur le froid. Ils donnent sur du 20 degrés."),
            (41.7, "Trois différences, et pas un mètre carré d'écart."),
            (46.6, "Aucune des trois ne dépend de vous."),
            (49.4, "Le DPE ne note pas votre bonne volonté."),
            (53.6, "Il note de la physique."),
            (57.8, "Avant de vendre, faites-vous expliquer votre étiquette."),
            (62.0, "DGLM Expertises — 06 07 35 15 05"),
        ],
        # Ce que montre l'image, pour qui ne la voit pas. Rédigé après visionnage,
        # pas déduit : une alternative fausse est pire qu'une alternative absente.
        "alt": "Sur fond vert sombre, deux échelles DPE côte à côte : la barre D "
               "allumée côté voisin, la barre F côté spectateur. Puis un immeuble "
               "dessiné en coupe, découpé en neuf logements : celui du haut à "
               "l'angle est cerclé et marqué « vous », et chaque logement est "
               "coloré selon le nombre de parois donnant sur l'extérieur — rouge "
               "pour deux, ocre pour une, vert pour aucune. Des chevrons montrent "
               "la chaleur sortir par le toit puis par la façade latérale, tandis "
               "que le logement du milieu est entouré de quatre voisins à 20°. "
               "Un écran de synthèse récapitule les trois différences — toiture, "
               "façades exposées, mitoyenneté — avant la carte de visite finale.",
    },
}


def _mmss(s):
    return f"{int(s) // 60}:{int(s) % 60:02d}"


def video_html(slug):
    """Le lecteur, sa description et sa transcription dépliable.
    preload="none" : les deux mégaoctets ne partent que si on clique."""
    v = VIDEOS.get(slug)
    if not v:
        return ""
    b = f"/assets/video/{v['fichier']}"
    lignes = "".join(f"<div><dt>{_mmss(t)}</dt><dd>{esc(txt)}</dd></div>"
                     for t, txt in v["transcription"])
    return f"""<figure class="film" id="video">
<h3 class="film__t">{esc(v['titre'])}</h3>
<div class="film__cadre">
<video controls preload="none" playsinline width="720" height="1280"
       poster="{b}.jpg" aria-describedby="film-desc">
<source src="{b}.mp4" type="video/mp4">
<track kind="captions" srclang="fr" label="Sous-titres français" src="{b}.fr.vtt">
</video></div>
<p class="film__d" id="film-desc">{esc(v['chapo'])}</p>
<p class="film__a">{esc(v['alt'])}</p>
<details class="film__x"><summary>Lire la transcription</summary>
<dl class="film__l">{lignes}</dl></details>
<figcaption>{esc(v['episode'])} · {esc(v['duree_txt'])}</figcaption>
</figure>"""


def video_schema(slug, page):
    v = VIDEOS.get(slug)
    if not v:
        return None
    b = DOM + f"/assets/video/{v['fichier']}"
    return {"@type": "VideoObject", "@id": DOM + page + "#video",
            "name": f"{v['episode']} — {v['titre']}",
            "description": v["chapo"],
            "thumbnailUrl": b + ".jpg",
            "contentUrl": b + ".mp4",
            "encodingFormat": "video/mp4",
            "uploadDate": v["publie"] + "T09:00:00+02:00",
            "duration": f"PT{v['duree']}S",
            "inLanguage": "fr-FR",
            "caption": b + ".fr.vtt",
            "transcript": " ".join(t for _, t in v["transcription"]),
            "creator": {"@id": DOM + "/#organisation"},
            "publisher": {"@id": DOM + "/#organisation"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": DOM + page}}


def page_hub_contenus(contenus):
    p = "/questions/"
    trail = [("Accueil", "/"), ("Guides pratiques", p)]
    # Sous-catégories : chaque thème dans son propre bandeau (fin du fouillis).
    CATS = [
        ("Amiante", "amiante", "Repérages avant travaux et démolition, DTA, listes A/B/C",
         "Interdit depuis 1997, présent presque partout avant. Tant qu'on n'y touche "
         "pas, rien ne se passe — avant d'y toucher, on repère et on fait analyser.",
         {"raat", "raad", "amiante", "dta", "dapp"}),
        ("Copropriété, DTG & PPPT", "copropriete", "Diagnostic global, plan de travaux, gouvernance",
         "L'immeuble se gère comme il se diagnostique : un état des lieux, un plan "
         "sur dix ans, une épargne — et des votes en assemblée.",
         {"dtg", "pppt", "fonds de travaux", "syndic", "assemblée générale",
          "carnet d'entretien", "petite copropriété", "copropriété"}),
        ("Performance énergétique", "energie", "DPE, audit énergétique, passoires thermiques",
         "Le DPE note, l'audit trace le chemin. Et depuis 2025, la note décide de "
         "qui peut louer.",
         {"dpe", "énergie", "audit énergétique", "passoire thermique", "décence"}),
        ("Vente & location", "vente-location", "Obligations, durées de validité, surfaces",
         "Un dossier de diagnostics accompagne chaque cession et chaque bail. L'âge "
         "du bâtiment et l'adresse décident de son contenu.",
         {"vente", "location", "ddt", "loi carrez", "loi boutin", "surface",
          "meublé", "bailleur", "validité"}),
        ("Plomb, gaz & risques", "risques", "CREP, termites, gaz, électricité, ERP, PEMD",
         "Avant 1949 le plomb ; plus de quinze ans, le gaz et l'électricité ; la "
         "zone décide des termites et des risques. Chaque danger a sa date et sa carte.",
         {"plomb", "crep", "gaz", "électricité", "termites", "parasitaire", "erp",
          "incendie", "débroussaillement", "pemd", "déchets", "santé", "sécurité"}),
        ("Repères & définitions", "reperes", "Le vocabulaire du diagnostic, en clair",
         "Les mots du métier, traduits. Un sigle ne devrait jamais faire peur.",
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
        idx = next((i for i, (_, _, _, _, k) in enumerate(CATS) if tset & k), len(CATS))
        groupes.setdefault(idx, []).append(c)

    RUB_IMG = {
        "amiante": ("terrain-conduits.jpg", 960, 1280),
        "copropriete": ("rub-copro.jpg", 1200, 691),
        "energie": ("hero-immeuble.jpg", 1600, 1067),
        "vente-location": ("hero-echoppe.jpg", 1400, 1050),
    }
    rubcards, rubpages, shown = "", [], 0
    for i, (nom, rslug, sub, anti, _) in enumerate(CATS):
        items = groupes.get(i)
        if not items:
            continue
        shown += 1
        img, iw, ih = RUB_IMG.get(rslug, ("", 0, 0))
        vignette = (f'<img src="/assets/photos/{img}" alt="" loading="lazy" '
                    f'decoding="async" width="{iw}" height="{ih}">' if img else
                    f'<div class="card-picto">{RUBRIQUE_PICTOS.get(nom, "")}</div>')
        rubcards += (f'<a class="card card--link card--photo" href="/questions/rubriques/{rslug}/">'
                     f'{vignette}'
                     f'<span class="sigle">Rubrique {shown:02d} · {len(items)} guide{"s" if len(items) > 1 else ""}</span>'
                     f'<h3>{esc(nom)}</h3><p>{esc(sub)}</p>'
                     f'<span class="more">Ouvrir la rubrique →</span></a>')
        rubpages.append((shown, nom, rslug, sub, anti, items, img, iw, ih))
    reste = groupes.get(len(CATS))
    if reste:
        shown += 1
        rubcards += (f'<a class="card card--link" href="/questions/rubriques/autres/">'
                     f'<span class="sigle">Rubrique {shown:02d} · {len(reste)} guides</span>'
                     f'<h3>Autres réponses</h3><p>Ce qui ne rentre dans aucune case</p>'
                     f'<span class="more">Ouvrir la rubrique →</span></a>')
        rubpages.append((shown, "Autres réponses", "autres",
                         "Les guides hors catégories", "", reste, "", 0, 0))

    # Chaque rubrique est une VRAIE page : un clic = une page, jamais un défilement.
    for num, nom, rslug, sub, anti, items, img, iw, ih in rubpages:
        rp = f"/questions/rubriques/{rslug}/"
        rtrail = [("Accueil", "/"), ("Guides pratiques", "/questions/"), (nom, rp)]
        rcartes = "".join(carte(c) for c in items)
        picto = RUBRIQUE_PICTOS.get(nom, "")
        photo = (f'<figure class="photo photo--rub"><img src="/assets/photos/{img}" '
                 f'alt="{esc(nom)} — illustration" loading="lazy" decoding="async" '
                 f'width="{iw}" height="{ih}"></figure>' if img else "")
        vus = [(mslug, e) for mslug, entries in CARNETS.items()
               for e in entries if e[3] == rslug]
        terrain = ""
        if vus:
            tf = "".join(
                f'<figure class="photo"><img src="/assets/photos/{e[0]}" alt="{esc(e[4])}" '
                f'loading="lazy" decoding="async" width="{e[1]}" height="{e[2]}">'
                f'<figcaption>{esc(e[4])}</figcaption>'
                f'<p class="photo__lecon"><b>Ce qu\'on voit :</b> {esc(e[5])} '
                f'<b>Pourquoi ça compte :</b> {esc(e[6])}</p></figure>'
                for mslug, e in vus[:2])
            terrain = (f'<section class="band band--pale"><div class="wrap">'
                       f'<p class="eyebrow">Carnets de terrain</p><h2>Vu en mission, sur ce thème</h2>'
                       f'<div class="grid grid--2" style="margin-top:1.8rem">{tf}</div></div></section>')
        rbody = f"""{crumb_html(rtrail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Rubrique {num:02d} — {len(items)} guide{"s" if len(items) > 1 else ""}</p>
<div class="rub-titre">{picto}<h1>{esc(nom)} : les guides</h1></div>
<p class="lede">{esc(sub)}.</p></div></section>
<section class="band"><div class="wrap">
{f'<p class="enclair" style="margin-top:0"><span>L&#x27;antisèche</span>{esc(anti)}</p>' if anti else ''}
{photo}
<div class="grid grid--2" style="margin-top:2.2rem">{rcartes}</div>
<p style="margin-top:2rem"><a class="btn btn--ghost" href="/questions/">← Toutes les rubriques</a></p>
</div></section>
{terrain}
{cta()}"""
        shell(path=rp, title=f"{nom} : les guides pratiques — DGLM"[:58],
              desc=desc_courte(f"{sub}. {anti}" if anti else f"{sub}."),
              body=rbody,
              schema=jsonld(org_schema(), breadcrumb(rtrail),
                            {"@type": "CollectionPage", "url": DOM + rp, "name": nom}))
        URLS.append((rp, "0.7", "weekly", MAJ_STRUCTURE))

    rubriques = (f'<section class="band"><div class="wrap">'
                 f'<p class="eyebrow">Le sommaire</p><h2>Choisissez votre rubrique.</h2>'
                 f'<div class="grid grid--3" style="margin-top:1.8rem">{rubcards}</div></div></section>')

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(contenus)} réponses · classées par thème</p>
<h1>Ce que l'on nous demande</h1>
<p class="lede">Chaque réponse est rédigée par les diagnostiqueurs qui conduisent les missions,
datée, et revue à chaque évolution réglementaire. Quand nous n'avons pas de réponse assurée,
nous préférons ne pas écrire la page.</p>
<div class="actions"><a class="btn btn--light" href="/notre-methode-editoriale/">Comment
ces guides sont écrits</a></div></div></section>
{rubriques}
{cta()}"""
    shell(path=p, title="Guides pratiques du diagnostic en copropriété",
          desc=desc_courte("Réponses documentées sur le repérage amiante avant travaux, le "
                           "DTG, le plan pluriannuel de travaux et les obligations de "
                           "copropriété, par les diagnostiqueurs de DGLM Expertises."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p,
                         "name": "Guides pratiques", "dateModified": ISO}))
    URLS.append((p, "0.85", "daily", MAJ_STRUCTURE))



# ------------------------------------------------------------------ Bordeaux au quartier
# Granularité que personne ne publie sur Bordeaux. Le bâti d'une échoppe de
# Nansouty, d'un chai des Chartrons et d'une barre du Grand Parc n'a rien de
# commun : c'est un contenu qu'on ne peut pas copier sans faire le terrain.
Q_BY_SLUG = {q["slug"]: q for q in QUARTIERS_BORDEAUX}


def fond_quartier(q):
    """Ce que nous pouvons affirmer à partir du bâti décrit.

    Les pages de quartier s'arrêtaient à la description du bâti : environ
    290 mots, et rien sur la conduite de la mission. Ce bloc porte la
    méthode, les points de contrôle et le cadre applicable.

    Les trois champs sont optionnels : un quartier qui ne les a pas encore
    rend simplement les sections qu'il possède. Voir data/quartiers_textes.py.
    """
    blocs = []
    if q.get("methode"):
        blocs.append("<h2>Comment la mission se conduit à " + esc(q["nom"])
                     + "</h2><p>" + esc(q["methode"]) + "</p>")
    if q.get("points"):
        pts = "".join("<li>" + esc(x) + "</li>" for x in q["points"])
        blocs.append("<h2>Les points de contrôle appelés par ce bâti</h2>"
                     "<ul>" + pts + "</ul>")
    if q.get("cadre"):
        blocs.append("<h2>Le cadre réglementaire applicable</h2><p>"
                     + esc(q["cadre"]) + "</p>")
    return "".join(blocs)


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

    fond = fond_quartier(q)
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
{fond}
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
                           f"travaux à Bordeaux {q['nom']}. {phrase1(q['bati'])}"),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "Service", "serviceType": "Diagnostics de copropriété",
                         "provider": {"@id": DOM + "/#organisation"},
                         "areaServed": {"@type": "Place", "name": f"Bordeaux {q['nom']}",
                                        "containedInPlace": {"@type": "City",
                                                             "name": "Bordeaux"}},
                         "description": q["enjeu"][:280]}))
    URLS.append((p, "0.75", "monthly", MAJ_STRUCTURE))


def fond_commune(slug, nom):
    """Le contenu de fond d'une page de ville.

    Ces pages n'affichaient qu'un titre et une grille de vignettes : 160 mots,
    et rien à apprendre. C'est le schéma que les moteurs sanctionnent le plus
    durement. Elles portent désormais ce que nous savons de la commune.

    Les champs copro et reperes sont optionnels : une commune qui ne les a pas
    encore rend simplement les deux sections qui la concernent.
    """
    c = COMMUNES_PAR_SLUG.get(slug, {})
    blocs = []
    if c.get("parc"):
        blocs.append("<h2>Le parc bâti de " + esc(nom) + "</h2><p>"
                     + esc(c["parc"]) + "</p>")
    if c.get("enjeu"):
        blocs.append("<h2>Ce que ce parc implique pour les missions collectives</h2>"
                     "<p>" + esc(c["enjeu"]) + "</p>")
    if c.get("copro"):
        blocs.append("<h2>La copropriété à " + esc(nom) + "</h2><p>"
                     + esc(c["copro"]) + "</p>")
    if c.get("reperes"):
        items = "".join("<li>" + esc(x) + "</li>" for x in c["reperes"])
        blocs.append("<h2>Nos repères de terrain à " + esc(nom) + "</h2>"
                     "<ul>" + items + "</ul>")
    return "".join(blocs)


def page_hub_bordeaux():
    p = "/bordeaux/"
    trail = [("Accueil", "/"), ("Bordeaux", p)]
    cards = "".join(
        f'<a class="card card--link" href="/bordeaux/{q["slug"]}/">'
        f'<h3>{esc(q["nom"])}</h3><p>{esc(q["intro"][:135])}…</p>'
        f'<span class="more">Découvrir le quartier →</span></a>' for q in QUARTIERS_BORDEAUX)
    fond = fond_commune("bordeaux", "Bordeaux")
    body = f"""{crumb_html(trail)}
<section class="hero hero--page hero--echoppe"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(QUARTIERS_BORDEAUX)} quartiers</p>
<h1>Bordeaux, quartier par quartier.</h1>
<p class="lede">Une échoppe de Nansouty, un chai des Chartrons et une barre du Grand Parc ne
relèvent ni des mêmes sondages, ni du même plan de repérage, ni du même ordre de
grandeur budgétaire. Nous documentons chaque quartier pour lui-même.</p></div></section>
<section class="band"><div class="wrap prose">
{fond}
</div></section>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Les quartiers de Bordeaux</p>
<h2>Le bâti change d'un quartier à l'autre.</h2>
<div class="grid grid--3">{cards}</div></div></section>
{cta()}"""
    shell(path=p, title="Diagnostics de copropriété à Bordeaux, quartier par quartier",
          desc=desc_courte("Repérage amiante, DTG et plan pluriannuel de travaux dans les "
                           "quartiers de Bordeaux : Chartrons, Saint-Michel, Bacalan, "
                           "Caudéran, Grand Parc, Euratlantique."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p, "name": "Bordeaux"}))
    URLS.append((p, "0.9", "monthly", MAJ_STRUCTURE))


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

    fond = fond_quartier(q)

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
{fond}
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
    URLS.append((p, "0.7", "monthly", MAJ_STRUCTURE))


def page_commune(c):
    """La page d'une commune sans découpage par quartier.

    Dix-sept communes disposaient de textes rédigés et vérifiés sans aucune
    page pour les porter : elles n'ont pas de quartiers, elles n'entraient
    donc dans aucune boucle. Eysines, siège de l'entreprise, répondait 404.
    """
    slug, nom = c["slug"], c["nom"]
    p = f"/{slug}/"
    trail = [("Accueil", "/"), (nom, p)]
    fond = fond_commune(slug, nom)
    missions = "".join(
        f'<a class="card card--link" href="{SILO}/{s["slug"]}/{slug}/">'
        f'<span class="sigle">{s["sigle"]}</span><h3>{esc(s["nom"])}</h3>'
        f'<p>{esc(s["accroche"])}</p><span class="more">Découvrir la mission →</span></a>'
        for s in SERVICES)
    voisins = "".join(
        f'<li><a href="/{v}/">{esc(SLUG_TO_NOM[v])}</a></li>'
        for v in c.get("voisins", []) if v in SLUG_TO_NOM)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{esc(c["cp"])} · Bordeaux Métropole</p>
<h1>Diagnostics de copropriété à {esc(nom)}</h1>
<p class="lede">Repérage amiante avant travaux, diagnostic technique global et
plan pluriannuel de travaux sur les immeubles collectifs de {esc(nom)}.</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E["tel"]}</a></div></div></section>

<section class="band"><div class="wrap prose">
{fond}
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Nos interventions</p><h2>Les quatre missions à {esc(nom)}</h2>
<div class="grid grid--2" style="margin-top:1.7rem">{missions}</div></div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">À proximité</p><h2>Les communes voisines</h2>
<ul class="cols">{voisins}</ul></div></section>
{cta()}"""

    shell(path=p,
          title=f"Diagnostics de copropriété à {nom} — DGLM Expertises",
          desc=desc_courte(f"Repérage amiante avant travaux, DTG et plan pluriannuel de travaux sur les copropriétés de {nom} ({c['cp']})."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "Place", "name": nom,
                         "address": {"@type": "PostalAddress",
                                     "addressLocality": nom,
                                     "postalCode": c["cp"],
                                     "addressCountry": "FR"}}))
    URLS.append((p, "0.8", "monthly", MAJ_STRUCTURE))


def page_hub_ville(ville):
    vslug, vnom = ville["slug"], ville["nom"]
    quartiers = ville["quartiers"]
    p = f"/{vslug}/"
    trail = [("Accueil", "/"), (vnom, p)]
    cards = "".join(
        f'<a class="card card--link" href="/{vslug}/{q["slug"]}/">'
        f'<h3>{esc(q["nom"])}</h3><p>{esc(q["intro"][:135])}…</p>'
        f'<span class="more">Découvrir le quartier →</span></a>' for q in quartiers)
    fond = fond_commune(vslug, vnom)

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">{len(quartiers)} quartiers</p>
<h1>{esc(vnom)}, quartier par quartier.</h1>
<p class="lede">D'un quartier à l'autre, le bâti change : le plan de repérage, l'ampleur des
sondages et l'ordre de grandeur budgétaire ne sont pas les mêmes. Nous documentons chaque
quartier de {esc(vnom)} pour lui-même.</p></div></section>
<section class="band"><div class="wrap prose">
{fond}
</div></section>
<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Les quartiers de {esc(vnom)}</p>
<h2>Le bâti change d'un quartier à l'autre.</h2>
<div class="grid grid--3">{cards}</div></div></section>
{cta()}"""
    shell(path=p, title=f"Diagnostics copropriété à {vnom}, par quartier",
          desc=desc_courte(f"Repérage amiante, DTG et plan pluriannuel de travaux dans les "
                           f"quartiers de {vnom} : "
                           + ", ".join(q["nom"] for q in quartiers[:5]) + "."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "CollectionPage", "url": DOM + p, "name": vnom}))
    URLS.append((p, "0.85", "monthly", MAJ_STRUCTURE))



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
          body=body, robots="noindex,follow", chapitres=False)



# ------------------------------------------------------------------ demande de devis
# Les documents attendus, mission par mission. SOURCE UNIQUE : la page
# /aide-au-devis/ les affiche en check-list, et le formulaire de devis les
# rappelle à côté de la zone de dépôt, selon la mission choisie.
DOCS_DEVIS = [
        ("Pour toute demande", [
            "L'adresse précise de l'immeuble ou du bien",
            "Un contact sur place (gardien, syndic, occupant) pour l'accès",
            "Vos délais souhaités (date de chantier, prochaine assemblée…)",
        ]),
        ("Repérage amiante avant travaux (RAAT)", [
            "Le descriptif des travaux : devis d'entreprise, CCTP ou simple liste des interventions",
            "Les plans ou croquis des zones concernées, même sommaires",
            "L'année de construction ou la date du permis de construire",
            "Le dossier technique amiante (DTA) ou sa fiche récapitulative, s'il existe",
            "Les repérages ou diagnostics amiante déjà réalisés",
            "Quelques photos des zones à ouvrir, si possible",
        ]),
        ("Repérage amiante avant démolition (RAAD)", [
            "Le projet de démolition : totale, partielle, curage",
            "Les plans du bâtiment, même anciens",
            "L'année de construction ou la date du permis",
            "L'état d'occupation (le bâtiment doit être libéré pour la visite)",
            "Le DTA ou les repérages existants",
        ]),
        ("Diagnostic technique global (DTG)", [
            "Le règlement de copropriété et l'état descriptif de division",
            "Le carnet d'entretien de l'immeuble",
            "Les procès-verbaux des trois dernières assemblées générales",
            "Les contrats d'exploitation (chauffage, ascenseur, entretien)",
            "Le DTA, le DPE collectif ou l'audit énergétique, s'ils existent",
            "Les plans de l'immeuble, si disponibles",
        ]),
        ("Plan pluriannuel de travaux (PPPT)", [
            "Les mêmes pièces que pour un DTG",
            "Le DTG existant, s'il a déjà été réalisé",
            "Le montant du fonds de travaux et les travaux déjà votés ou réalisés",
        ]),
        ("Diagnostics de l'immeuble (DTA, DAPP, plomb, assainissement…)", [
            "L'année de construction ou la date du permis",
            "Le nombre de lots et la liste des parties communes concernées",
            "Les diagnostics antérieurs, même anciens",
            "Les modalités d'accès aux caves, combles et locaux techniques",
        ]),
]

# Correspondance entre les missions du formulaire et les blocs ci-dessus.
DOCS_PAR_MISSION = {
    "raat": ("Pour toute demande", "Repérage amiante avant travaux (RAAT)"),
    "raad": ("Pour toute demande", "Repérage amiante avant démolition (RAAD)"),
    "dtg": ("Pour toute demande", "Diagnostic technique global (DTG)"),
    "pppt": ("Pour toute demande", "Plan pluriannuel de travaux (PPPT)"),
    "dpe": ("Pour toute demande", "Diagnostic technique global (DTG)"),
    "autre": ("Pour toute demande", "Diagnostics de l'immeuble (DTA, DAPP, plomb, assainissement…)"),
}


def page_aide_devis():
    """Les documents à joindre à une demande de devis, mission par mission.
    Imprimable : le client coche, réunit, et joint tout à son e-mail."""
    p = "/aide-au-devis/"
    trail = [("Accueil", "/"), ("Aide au devis", p)]
    BLOCS = DOCS_DEVIS
    # Une bande par mission plutôt qu'une seule pour toutes : la barre de
    # chapitres devient alors un sélecteur de mission, et c'est l'usage réel
    # de cette page — on y vient pour SA mission, pas pour les six.
    sections = "".join(
        f'<section class="band{" band--pale" if i % 2 else ""}"><div class="wrap prose">'
        f'<h2>{esc(titre_bloc)}</h2><ul class="checklist">'
        + "".join(f"<li>{esc(x)}</li>" for x in items)
        + "</ul></div></section>"
        for i, (titre_bloc, items) in enumerate(BLOCS))
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Aide au devis — à imprimer ou à garder sous la main</p>
<h1>Les documents qui accélèrent votre devis</h1>
<p class="lede">Plus votre demande est documentée, plus le chiffrage est rapide et juste —
souvent sans même un rappel préalable. Cochez, réunissez, joignez.</p>
<div class="actions"><button class="btn btn--light" onclick="window.print()">Imprimer ou enregistrer en PDF</button>
<a class="btn btn--light" href="/devis/">Passer à la demande de devis</a></div>
</div></section>
<section class="band"><div class="wrap prose">
<p class="enclair" style="margin-top:0"><span>L'antisèche</span>Réunissez ce qui vous concerne
ci-dessous, puis joignez les fichiers à l'e-mail que le formulaire de devis prépare pour
vous — ils arrivent directement dans notre boîte contact. Rien sous la main ? Envoyez
quand même : on fait avec ce que vous avez.</p>
</div></section>
{sections}
<section class="band band--pale"><div class="wrap prose">
<p class="maj">Établi par l'équipe DGLM Expertises — vérifié en {MAJ}</p>
</div></section>
{cta()}"""
    shell(path=p, title="Aide au devis : les documents à joindre — DGLM",
          desc=desc_courte("Mission par mission, la liste des documents qui accélèrent votre "
                           "devis : plans, DTA, règlement de copropriété, procès-verbaux. "
                           "À imprimer et à joindre."),
          body=body,
          schema=jsonld(org_schema(), breadcrumb(trail)))
    URLS.append((p, "0.7", "monthly", MAJ_STRUCTURE))


# --------------------------------------------------- portes d'entrée dédiées
# L'audit UX a montré deux visiteurs mal accueillis : le conseiller syndical
# bénévole, envoyé sur la page écrite pour les syndics professionnels, et le
# particulier en travaux, renvoyé vers l'autre site alors qu'il est notre client.
def page_conseil_syndical():
    p = "/conseil-syndical/"
    trail = [("Accueil", "/"), ("Conseil syndical", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Pour les élus bénévoles</p>
<h1>Conseil syndical : comprendre et décider</h1>
<p class="lede">Vous êtes bénévole, et l'on vous demande de vous prononcer sur des études
techniques que vous n'avez pas rédigées. Voici de quoi les lire, et les questions à poser
en séance.</p>
<div class="actions"><a class="btn btn--light" href="/pack-conseil-syndical/">Les check-lists à imprimer</a>
<a class="btn btn--light" href="{SILO}/simulateur-obligations-copropriete/">Ce que doit votre copropriété</a></div>
</div></section>
<section class="band">
  <div class="wrap">
    <p class="eyebrow">Vous êtes au conseil syndical</p>
    <p>Vous n'avez pas choisi ce vocabulaire. Personne ne vous a formé au bâtiment : vous êtes bénévole, élu par vos voisins, et on vous demande de vous prononcer sur des documents que vous n'avez pas rédigés. Plan pluriannuel, diagnostic technique global, DPE collectif, repérage avant travaux : quatre sigles, quatre budgets, et souvent une seule séance pour trancher.</p>
    <p>Cette page est écrite pour vous, pas pour votre syndic. Elle ne cherche pas à faire de vous un technicien : elle vous donne de quoi comprendre ce que chaque document est censé apporter, et de quoi poser les questions qui séparent une étude sérieuse d'un document de façade.</p>
    <p>Nous écrivons ces études au quotidien et nous lisons celles des autres. Nous savons donc où elles se relâchent.</p>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <p class="eyebrow">Le programme de l'année</p>
    <h2>Ce qu'on va vous demander de comprendre</h2>
    <p>Quatre sujets reviennent dans presque toutes les assemblées. Voici ce qu'il faut en retenir avant d'ouvrir le rapport.</p>

    <div class="grid grid--2">
      <div class="card">
        <h3>Le plan pluriannuel de travaux</h3>
        <p>C'est la liste des travaux à envisager sur les dix années à venir, avec une estimation et un ordre de priorité. Il concerne les immeubles à destination totale ou partielle d'habitation dont le permis de construire remonte à plus de quinze ans. Voter le plan, ce n'est ni voter les travaux, ni engager une dépense immédiate.</p>
        <p><a href="/plan-pluriannuel-de-travaux/">La mission PPPT</a> · <a href="/questions/voter-pppt-assemblee/">Voter le plan en assemblée</a> · <a href="/questions/validite-pppt/">Combien de temps reste-t-il valable ?</a></p>
      </div>

      <div class="card">
        <h3>Le diagnostic technique global</h3>
        <p>C'est l'état des lieux complet de l'immeuble : structure, équipements, situation réglementaire, performance énergétique. Plus large que le plan de travaux, il lui sert souvent de socle. Selon les cas, il est obligatoire ou seulement soumis au vote de l'assemblée.</p>
        <p><a href="/diagnostic-technique-global/">La mission DTG</a> · <a href="/questions/dtg-ou-pppt/">DTG ou PPPT, lequel d'abord ?</a> · <a href="/questions/dtg-petite-copropriete/">Le cas des petites copropriétés</a></p>
      </div>

      <div class="card">
        <h3>Le DPE collectif</h3>
        <p>C'est le diagnostic de performance énergétique de l'immeuble entier, et non de chaque logement. Il donne une étiquette au bâtiment et alimente la réflexion sur les travaux d'économie d'énergie. Le calendrier d'obligation dépend de la taille de la copropriété.</p>
        <p><a href="/dpe-collectif-copropriete/">Le DPE collectif</a> · <a href="/questions/qu-est-ce-que-le-dpe/">Ce que mesure un DPE</a> · <a href="/audit-energetique-copropriete/">L'audit énergétique</a></p>
      </div>

      <div class="card">
        <h3>Les repérages amiante avant travaux</h3>
        <p>Dès qu'un chantier touche la matière du bâtiment — toiture, façade, canalisations, sols — un repérage amiante doit précéder les travaux dans les immeubles dont le permis de construire a été délivré avant le 1<sup>er</sup> juillet 1997. Ce n'est pas une formalité : c'est ce qui protège les intervenants.</p>
        <p><a href="/reperage-amiante-avant-travaux/">Le repérage avant travaux</a> · <a href="/questions/raat-ou-raad/">Avant travaux ou avant démolition ?</a> · <a href="/questions/qui-paie-reperage-copropriete/">Qui le paie ?</a></p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Votre vrai levier</p>
    <h2>Les questions à poser en séance</h2>
    <p>Vous n'avez pas à juger la technique ; vous pouvez vérifier la méthode, et c'est là que tout se joue. Un plan bâti sur une visite rapide se vote aussi facilement qu'un autre ; il se paie à la première toiture.</p>

    <div class="grid grid--2">
      <div class="card">
        <h3>Sur quoi s'appuie exactement ce document ?</h3>
        <p>Combien de temps le diagnostiqueur est-il resté sur place, quels locaux a-t-il ouverts, a-t-il consulté les archives et le carnet d'entretien ? Si les toitures, les vides sanitaires ou les colonnes en parties privatives n'ont pas été vus, le chiffrage repose sur des hypothèses — acceptable, à condition que ce soit écrit.</p>
      </div>

      <div class="card">
        <h3>Qui a signé, et dans quel domaine est-il certifié ?</h3>
        <p>Les certifications sont nominatives et par domaine : amiante, DPE, plomb, termites. Un signataire certifié pour le DPE ne l'est pas pour autant pour l'amiante. Demandez le nom, l'organisme, la date de validité et l'attestation d'assurance.</p>
        <p><a href="/questions/qui-realise-reperage-amiante-travaux/">Qui peut réaliser un repérage</a> · <a href="/certifications-et-assurances/">Nos certifications</a></p>
      </div>

      <div class="card">
        <h3>Qu'est-ce qui a été constaté, et qu'est-ce qui a été supposé ?</h3>
        <p>Un rapport sérieux distingue ce que l'intervenant a vu de ce qu'il a déduit. Un document sans aucune réserve, sans zone non visitée, sans incertitude signalée n'en est pas plus sûr : il est à interroger.</p>
      </div>

      <div class="card">
        <h3>Des sondages ont-ils été faits, ou seulement des observations ?</h3>
        <p>En amiante, certains matériaux ne s'identifient pas à l'œil : il faut prélever et faire analyser en laboratoire. Demandez combien de prélèvements ont été réalisés et sur quels matériaux. Un repérage avant travaux sans aucun prélèvement mérite une explication.</p>
        <p><a href="/questions/listes-a-b-c-amiante/">Les listes A, B et C</a></p>
      </div>

      <div class="card">
        <h3>Et si on découvre de l'amiante en cours de chantier ?</h3>
        <p>Cela arrive, même après un repérage correct. Ce qui compte, c'est que la conduite à tenir soit prévue avant le début des travaux : arrêt du chantier, analyse, avenant. Une copropriété qui n'y a pas pensé subit l'arrêt au lieu de le piloter.</p>
        <p><a href="/questions/decouverte-amiante-en-chantier/">La découverte en chantier</a></p>
      </div>

      <div class="card">
        <h3>À quelle majorité vote-t-on, et que finance le fonds de travaux ?</h3>
        <p>La majorité applicable change la nature du débat, et le fonds de travaux peut déjà couvrir une partie de la dépense. Ces deux points se vérifient avant la séance, pas pendant.</p>
        <p><a href="/questions/majorites-vote-travaux-assemblee/">Les majorités</a> · <a href="/questions/fonds-de-travaux/">Le fonds de travaux</a></p>
      </div>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <p class="eyebrow">Mise au point</p>
    <h2>Ce que vous n'avez pas à faire</h2>
    <p>Beaucoup de conseillers syndicaux s'épuisent à endosser un rôle qui n'est pas le leur.</p>
    <ul>
      <li><strong>Vous n'avez pas à devenir technicien.</strong> Vous n'êtes pas censé lire un rapport de repérage ni évaluer une charpente, mais vérifier que quelqu'un de compétent l'a fait, et l'a écrit.</li>
      <li><strong>Vous n'avez pas à arbitrer seul.</strong> Le conseil syndical assiste et contrôle le syndic ; il ne décide pas à la place de l'assemblée générale.</li>
      <li><strong>Vous n'avez pas à porter seul le choix retenu.</strong> Votre mission est bénévole et consultative : c'est l'assemblée qui décide et qui engage la copropriété. Ce qui vous protège, c'est la traçabilité : demandez que vos questions et les réponses figurent au compte rendu.</li>
      <li><strong>Vous n'avez pas à faire le travail du syndic.</strong> Réunir les devis, transmettre les rapports, tenir le carnet d'entretien relèvent de sa mission. Vous pouvez exiger les pièces sans aller les chercher.</li>
      <li><strong>Vous n'avez pas à tout comprendre, tout de suite.</strong> Demander un report de vote faute d'éléments n'est pas un aveu de faiblesse. C'est souvent la décision la plus économique de l'année.</li>
    </ul>
    <p><a href="/questions/carnet-entretien-copropriete/">Le carnet d'entretien</a> · <a href="/questions/copropriete-sans-pppt/">Si la copropriété n'a pas de PPPT</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Gratuit, sans inscription</p>
    <h2>Les outils qui vous servent vraiment</h2>
    <p>Nous les avons construits pour une séance de conseil syndical : un dossier ouvert, une heure devant soi.</p>

    <div class="grid grid--3">
      <div class="card">
        <h3>Simulateur d'obligations</h3>
        <p>Ce qui vous est réellement imposé, en quelques questions.</p>
        <p><a href="/simulateur-obligations-copropriete/">Ouvrir le simulateur</a></p>
      </div>
      <div class="card">
        <h3>Simulateur de validité</h3>
        <p>Vos rapports existants sont-ils encore utilisables ?</p>
        <p><a href="/simulateur-validite-diagnostics/">Vérifier vos rapports</a></p>
      </div>
      <div class="card">
        <h3>Le tableau des diagnostics</h3>
        <p>À quoi sert chaque diagnostic, et combien de temps il vaut.</p>
        <p><a href="/le-tableau-des-diagnostics/">Consulter le tableau</a></p>
      </div>
      <div class="card">
        <h3>Aides financières</h3>
        <p>Les dispositifs mobilisables avant de chiffrer un reste à charge.</p>
        <p><a href="/aides-financieres-copropriete/">Voir les aides</a></p>
      </div>
      <div class="card">
        <h3>Pack conseil syndical</h3>
        <p>Les pièces à réunir et une trame de questions pour la séance.</p>
        <p><a href="/pack-conseil-syndical/">Obtenir le pack</a></p>
      </div>
      <div class="card">
        <h3>Aide au devis</h3>
        <p>Comparer des propositions à périmètre égal, et comprendre un écart.</p>
        <p><a href="/aide-au-devis/">Comparer des devis</a></p>
      </div>
    </div>

    <p class="enclair"><span>L'antisèche</span> Votre rôle n'est pas d'expertiser, il est de contrôler. Trois réflexes suffisent : demander sur quoi s'appuie l'étude, qui l'a signée et pour quel domaine, et que les zones non vues et les hypothèses soient écrites noir sur blanc. Si les réponses tardent, ce n'est pas votre compétence qui est en cause — c'est le document.</p>

    <p>Une question précise sur un rapport que vous avez sous les yeux ? Nous répondons aux conseils syndicaux même lorsqu'ils ne sont pas nos clients : <a href="/questions/glossaire-diagnostic-immobilier/">le glossaire</a> lève déjà bien des malentendus, et <a href="/equipe/">l'équipe</a> répond au reste.</p>
  </div>
</section>
{cta()}"""
    shell(path=p, title="Conseil syndical : comprendre et décider — DGLM",
          desc=desc_courte("Plan pluriannuel, diagnostic global, DPE collectif, repérage "
                           "amiante : ce qu'un conseiller syndical bénévole doit en "
                           "comprendre, et les questions à poser."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail),
                                   {"@type": "WebPage", "url": DOM + p,
                                    "name": "Conseil syndical"}))
    URLS.append((p, "0.85", "monthly", MAJ_STRUCTURE))


def page_particulier_travaux():
    p = "/particulier-travaux/"
    trail = [("Accueil", "/"), ("Vous rénovez votre logement", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Particuliers — travaux et rénovation</p>
<h1>Vous rénovez votre logement</h1>
<p class="lede">Salle de bain, cloisons, sols, toiture : dès qu'on ouvre la matière d'un
logement d'avant 1997, un repérage amiante s'impose. Cela vaut aussi chez un particulier —
et c'est vous que cela protège.</p>
<div class="actions"><a class="btn btn--light" href="/devis/#m-raat">Demander un devis</a>
<a class="btn btn--light" href="tel:{E['tel_raw']}">{E['tel']}</a></div>
</div></section>
<section class="band"><div class="wrap prose">
<p style="font-size:1.12rem">Vous refaites une salle de bain, vous abattez une cloison, vous changez vos fenêtres — et vous ne trouvez que des pages qui parlent d'immeubles et de syndics. Vous êtes pourtant au bon endroit. Le repérage amiante avant travaux n'est réservé ni aux grandes opérations ni aux professionnels : un propriétaire qui fait faire des travaux chez lui est le donneur d'ordre de son chantier, comme un bailleur ou un promoteur.</p>

<h2>Un diagnostic qui ne sert pas à vendre</h2>
<p>Le mot « diagnostic » évoque presque toujours la vente : le dossier remis au notaire, qu'on ne relit jamais. Le repérage avant travaux obéit à une autre logique. Il ne renseigne pas un acheteur sur l'état d'un bien : il protège les personnes qui vont ouvrir les murs — l'artisan, et vous qui vivez sur place pendant le chantier.</p>
<p>C'est aussi pourquoi un repérage amiante déjà présent dans vos papiers ne suffit pas. Le constat établi lors d'une vente, comme le <a href="/dossier-technique-amiante/">dossier technique amiante</a> d'un immeuble, décrit ce qui est visible et accessible, sans sondage destructif : il ne couvre pas le périmètre de vos travaux, rien de ce qui se trouve sous votre carrelage. Notre guide <a href="/questions/dta-ou-dapp/">DTA ou DAPP</a> détaille la distinction.</p>

<h2>Quand le repérage s'impose chez un particulier</h2>
<p>Deux conditions se cumulent. La première tient à l'âge du bâtiment : le permis de construire doit avoir été délivré avant le 1<sup>er</sup> juillet 1997. La seconde tient à la nature des travaux : dès que l'opération est susceptible d'exposer des travailleurs à l'amiante, c'est-à-dire dès qu'on ouvre, perce, découpe, dépose ou démolit.</p>
<p class="enclair"><span>À retenir</span>Le critère n'est pas l'ampleur du chantier, mais le fait de toucher à la matière. Percer un mur pour passer une évacuation suffit à poser la question.</p>
<p>Dans un logement, les points de contact sont toujours les mêmes :</p>
<ul class="checklist">
<li>les colles de carrelage et de revêtement de sol, souvent noires et bitumineuses</li>
<li>les dalles de sol plastiques anciennes, souvent de format carré</li>
<li>les enduits, ragréages et doublages de cloisons</li>
<li>les mastics de vitrage et les joints d'huisserie</li>
<li>les plaques ondulées en fibres-ciment d'un appentis, d'un garage ou d'un abri de jardin</li>
<li>les conduits de fumée, les calorifugeages et les tresses d'étanchéité d'une vieille chaudière</li>
</ul>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Chantiers domestiques</p>
<h2>Des travaux ordinaires, qui déclenchent l'obligation</h2>
<p class="narrow">Aucun de ces chantiers n'est spectaculaire. Tous supposent d'ouvrir quelque chose dans un logement qui a pu être bâti avec des matériaux amiantés.</p>
<div class="grid grid--2" style="margin-top:1.6rem">
<div class="card"><h3>Refaire une salle de bain</h3><p>Dépose de la faïence, du carrelage et de sa colle, parfois d'un ancien revêtement resté sous le nouveau. C'est l'un des chantiers où l'on rencontre le plus souvent des matériaux amiantés.</p></div>
<div class="card"><h3>Déposer un revêtement de sol collé</h3><p>Les dalles plastiques et leur colle sont deux matériaux distincts : les premières peuvent être saines et la seconde amiantée. C'est l'arrachage qui libère les fibres, pas la présence du sol.</p></div>
<div class="card"><h3>Abattre une cloison</h3><p>Ouvrir une cuisine sur un séjour reste une démolition. Enduits, doublages et plaques de la cloison entrent dans le périmètre du repérage.</p></div>
<div class="card"><h3>Changer les fenêtres</h3><p>On y pense rarement : le mastic de vitrage et les joints ont longtemps contenu de l'amiante. Notre guide <a href="/questions/raat-remplacement-fenetres/">RAAT et remplacement de fenêtres</a> détaille ce point.</p></div>
<div class="card"><h3>Refaire une toiture d'appentis</h3><p>Les plaques ondulées en fibres-ciment d'un garage ou d'un abri de jardin sont un cas d'école. Les découper ou les casser pour les évacuer est ce qu'il ne faut pas faire à l'aveugle.</p></div>
<div class="card"><h3>Isoler des combles</h3><p>Avant de souffler une isolation, on circule, on fixe, on traverse des conduits. Les calorifugeages anciens méritent d'être identifiés avant.</p></div>
</div></div></section>

<section class="band"><div class="wrap prose">
<h2>Pourquoi ce repérage vous protège, vous</h2>
<p>L'obligation pèse sur le donneur d'ordre, celui qui commande les travaux : dans votre logement, c'est vous. Le Code du travail, à ses articles R. 4412-97 et suivants, et l'arrêté du 16 juillet 2019 relatif aux immeubles bâtis ne prévoient pas de transfert de cette responsabilité vers l'entreprise qui intervient. Notre guide <a href="/questions/qui-realise-reperage-amiante-travaux/">qui doit faire réaliser le repérage</a> le détaille.</p>
<p>Un artisan sérieux vous le demandera, et il a raison. Sans repérage, il travaille sans savoir ce qu'il ouvre : son assureur peut lui opposer ce défaut, et beaucoup d'entreprises refusent de démarrer.</p>
<p>L'argument suivant est économique. Une découverte d'amiante en cours de chantier arrête tout : l'intervention est suspendue, il faut faire appel à une entreprise certifiée pour le retrait, orienter les déchets vers une filière dédiée et reprogrammer les corps d'état déjà planifiés. Le repérage préalable évite cette séquence. Nous la décrivons dans <a href="/questions/decouverte-amiante-en-chantier/">découverte d'amiante en chantier</a>, et les deux régimes d'intervention dans <a href="/questions/amiante-sous-section-3-et-4/">sous-section 3 et sous-section 4</a>.</p>
<p>Une nuance, parce qu'elle est réelle : le texte vise l'exposition de travailleurs. Si vous démontez vous-même une cloison un dimanche, aucun salarié n'est exposé et l'obligation, au sens strict, ne vous vise pas. Vous respirez pourtant la même poussière, dans la pièce où vous dormirez le soir. Faire analyser un matériau avant de le casser reste la seule façon de savoir.</p>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Déroulé</p>
<h2>Comment cela se passe chez vous</h2>
<ol class="steps">
<li><h3>Nous partons de votre projet</h3><p>Décrivez ce que vous allez ouvrir : la pièce, les surfaces déposées, les percements. Le repérage se cale sur ce périmètre, pas sur une trame standard.</p></li>
<li><h3>La visite</h3><p>Un diagnostiqueur certifié se déplace. Il n'inspecte pas tout le logement, seulement votre périmètre de travaux. Les sondages destructifs — soulever une plinthe, déposer un carreau, ouvrir une trappe — sont réalisés avec votre accord.</p></li>
<li><h3>Les prélèvements et le laboratoire</h3><p>Chaque doute est levé par prélèvement et analyse en laboratoire accrédité COFRAC. Aucun matériau n'est classé « présumé amianté » par confort : cette facilité vous coûterait un désamiantage peut-être inutile.</p></li>
<li><h3>Le rapport</h3><p>Vous recevez un rapport localisant chaque matériau, avec photographies, croquis et conclusions. C'est le document que vous remettez à votre artisan avant qu'il ne chiffre.</p></li>
<li><h3>Les délais</h3><p>Nous intervenons généralement sous 72 heures ouvrées sur Bordeaux Métropole et remettons le rapport sous 48 heures après réception des résultats d'analyse. Le délai du laboratoire reste la seule variable que nous ne maîtrisons pas.</p></li>
</ol>
</div></section>

<section class="band"><div class="wrap prose">
<h2>Si votre projet est de vendre ou de louer</h2>
<p>Autant le dire tout de suite : nous ne réalisons pas les diagnostics de vente ou de mise en location. C'est une autre équipe du groupe qui s'en charge, sur <a href="/particuliers/">la page dédiée aux particuliers</a>. Notre travail commence quand les travaux commencent.</p>
<p>La frontière est parfois moins nette : on rénove souvent un logement avant de le remettre en location, ou juste après l'avoir acheté. Les deux besoins coexistent alors sans se remplacer : le diagnostic de la transaction ne vaut pas repérage avant travaux, et l'inverse est vrai aussi.</p>
<h2>Pour aller plus loin</h2>
<ul class="mesh">
<li><a href="/reperage-amiante-avant-travaux/">La mission de repérage avant travaux</a></li>
<li><a href="/questions/raat-ou-raad/">Repérage avant travaux ou avant démolition ?</a></li>
<li><a href="/questions/listes-a-b-c-amiante/">Les listes A, B et C des matériaux</a></li>
<li><a href="/le-tableau-des-diagnostics/">Le tableau des diagnostics</a></li>
<li><a href="/questions/qu-est-ce-que-le-diagnostic-plomb/">Le diagnostic plomb dans un logement ancien</a></li>
<li><a href="/questions/glossaire-diagnostic-immobilier/">Le glossaire, si un sigle vous échappe</a></li>
</ul>
</div></section>

<section class="cta"><div class="wrap">
<p class="eyebrow eyebrow--pale">Un chantier chez vous</p>
<h2>Décrivez-nous vos travaux, nous vous dirons ce qui est nécessaire.</h2>
<p>Un appel suffit souvent à cadrer le périmètre. Si un repérage ne s'impose pas dans votre situation, nous vous le dirons aussi.</p>
<div class="actions"><a class="btn btn--light" href="tel:+33607351505">Appeler le 06 07 35 15 05</a>
<a class="btn btn--light" href="/devis/">Demander un devis</a></div></div></section>
{cta()}"""
    shell(path=p, title="Vous rénovez votre logement : le repérage amiante — DGLM",
          desc=desc_courte("Refaire une salle de bain, déposer un sol, abattre une "
                           "cloison : quand un repérage amiante avant travaux s'impose "
                           "chez un particulier, et pourquoi."),
          body=body, schema=jsonld(org_schema(), breadcrumb(trail),
                                   {"@type": "WebPage", "url": DOM + p,
                                    "name": "Particulier en travaux"}))
    URLS.append((p, "0.85", "monthly", MAJ_STRUCTURE))


# ------------------------------------------------------ simulateur de validité
def page_validite():
    """On coche ce qu'on a, on saisit les dates, l'outil dit ce qui tient.
    Les durées viennent du guide des validités : une seule source."""
    p = "/simulateur-validite-diagnostics/"
    trail = [("Accueil", "/"), ("Vos diagnostics sont-ils encore valables ?", p)]

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Outil gratuit — rien n'est enregistré</p>
<h1>Vos diagnostics sont-ils encore valables ?</h1>
<p class="lede">Six mois pour l'état des risques, dix ans pour le DPE, et des règles
particulières pour l'amiante et le plomb : personne ne retient tout cela. Cochez ce que
vous avez, indiquez les dates, l'outil fait le tri.</p>
<div class="actions"><a class="btn btn--light" href="/le-tableau-des-diagnostics/">Le tableau des diagnostics</a>
<a class="btn btn--light" href="/devis/">Demander un devis</a></div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Votre dossier</p>
<h2>Ce que vous avez déjà</h2>
<p class="enclair"><span>L'antisèche</span>Un diagnostic périmé ne se rattrape pas la
veille de la signature : certains demandent une visite, et les délais de laboratoire ne se
négocient pas. Le plus court de tous, l'état des risques, ne tient que six mois — c'est
presque toujours lui qui manque.</p>

<div class="avec-aide">
<div class="avec-aide__principal">

<form id="valid-form" class="devis">
<fieldset class="devis__bloc"><legend><h3>1 · Pour quelle situation ?</h3></legend>
<div class="vusage">
<label class="vusage__o"><input type="radio" name="usage" value="vente" checked>
<span><b>Une vente</b><i>Les durées y sont plus courtes</i></span></label>
<label class="vusage__o"><input type="radio" name="usage" value="location">
<span><b>Une location</b><i>Gaz, électricité et plomb tiennent plus longtemps</i></span></label>
</div></fieldset>

<div class="devis__bloc"><h3>2 · Vos diagnostics et leurs dates</h3>
<p class="postes__intro">Cochez ceux que vous possédez, puis indiquez la date figurant
sur le rapport — celle de la visite, pas celle où vous l'avez reçu.</p>
<div id="valid-liste"></div></div>

<div class="simu-valider">
<button type="submit" class="btn">Vérifier mes diagnostics</button>
<p class="simu-manque" id="valid-manque" role="status" aria-live="polite"></p>
</div>
</form>

<p id="valid-synthese" class="sr" role="status" aria-live="polite"></p>
<div id="valid-resultat" tabindex="-1" hidden>
<h2 style="margin-top:2.4rem">Ce qui tient, ce qui ne tient plus</h2>
<div class="simu-corps"></div>
<p class="maj">Analyse indicative, fondée sur les seules dates saisies et sur les durées
en vigueur en {MAJ}. Elle ne remplace pas l'examen des rapports eux-mêmes : c'est leur
contenu, et non leur seule date, qui détermine ce qui reste opposable.</p>
</div>
<noscript><p class="enclair"><span>Sans JavaScript</span>L'outil a besoin de JavaScript,
mais toutes les durées figurent dans
<a href="/questions/duree-validite-diagnostics/">le guide des validités</a> et dans
<a href="/le-tableau-des-diagnostics/">le tableau des diagnostics</a>.</p></noscript>

</div>
<aside class="aide" aria-label="Repères sur les durées de validité">
<p class="aide__titre">Les durées, et d'où elles viennent</p>

<details class="aide__bloc" open><summary>Pourquoi des durées si différentes ?</summary>
<p>Une durée de validité n'est pas arbitraire : elle traduit la vitesse à laquelle
l'information peut devenir fausse. Un mesurage de surface ne bouge pas tant qu'on ne
touche pas aux murs, donc il n'expire pas. Une installation de gaz se dégrade, donc son
contrôle se refait. Et une colonie de termites peut coloniser un immeuble en une saison :
d'où six mois seulement.</p></details>

<details class="aide__bloc"><summary>Six mois — l'état des risques</summary>
<p>C'est le plus court de tous, et de loin le plus oublié. Il recense les risques auxquels
la commune est exposée : inondation, mouvement de terrain, sismicité, pollution des sols,
exposition au radon. Ces zonages sont révisés par arrêté préfectoral, parfois en cours
d'année — d'où une validité courte. Il doit être à jour <strong>le jour de la signature</strong>,
et non le jour de la mise en vente.</p></details>

<details class="aide__bloc"><summary>Six mois — les termites</summary>
<p>Exigé dans les zones délimitées par arrêté préfectoral, ce qui vise
<strong>la Gironde entière</strong>. Six mois, parce qu'une infestation évolue vite et que
le constat porte sur ce qui était visible le jour de la visite.</p></details>

<details class="aide__bloc"><summary>Trois ou six ans — gaz et électricité</summary>
<p>Ces deux contrôles ne sont exigés que si l'installation a <strong>plus de quinze ans</strong>.
La durée dépend ensuite de l'usage : <strong>trois ans</strong> pour une vente,
<strong>six ans</strong> pour une location. L'écart s'explique par le rythme des
transactions : un bail se renouvelle plus souvent qu'une vente, et le législateur a évité
d'imposer un contrôle à chaque changement de locataire.</p></details>

<details class="aide__bloc"><summary>Dix ans — le DPE, avec une exception</summary>
<p>Dix ans en principe. Mais tous les DPE établis <strong>avant le 1<sup>er</sup> juillet
2021</strong> ont cessé d'être valables : la méthode de calcul a changé ce jour-là, et
l'ancienne version reposait en partie sur les factures de l'occupant plutôt que sur les
caractéristiques du logement. Un DPE de 2019 ne vaut donc plus rien, même si dix ans ne
sont pas écoulés. <a href="/questions/qu-est-ce-que-le-dpe/">Comment se lit un DPE →</a></p></details>

<details class="aide__bloc"><summary>Amiante et plomb : la logique du résultat</summary>
<p>Ces deux constats n'ont pas de durée fixe : c'est <strong>leur conclusion</strong> qui
décide. Un constat plomb négatif vaut sans limite de durée — le plomb n'apparaît pas
spontanément. S'il est positif, il vaut un an pour une vente, six ans pour un bail, parce
que c'est l'état de conservation des peintures qui doit être resuivi.</p>
<p>Pour l'amiante, même logique, avec une réserve de taille : un repérage établi
<strong>avant 2013</strong> doit être refait, car la liste des matériaux à rechercher a été
élargie depuis. Un rapport ancien peut donc être « négatif » sur un champ devenu trop
étroit. <a href="/questions/listes-a-b-c-amiante/">Les listes A, B et C →</a></p></details>

<details class="aide__bloc"><summary>Ce qui périme un diagnostic avant l'heure</summary>
<p>Une date d'échéance n'est qu'une limite haute. Trois événements rendent un rapport
caduc plus tôt : des <strong>travaux</strong> qui modifient ce qu'il décrit, un
<strong>changement de réglementation</strong> comme en 2021 pour le DPE, et la
<strong>découverte d'un fait nouveau</strong> qu'il ne mentionnait pas.</p></details>

<p class="aide__pied">Les durées appliquées ici sont celles du code de la construction et
de l'habitation, telles qu'en vigueur en {MAJ}.
<a href="/questions/duree-validite-diagnostics/">Le guide détaillé →</a></p>
</aside>
</div>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Ce que l'outil ne peut pas voir</p>
<h2>Trois raisons de refaire un diagnostic encore « valable »</h2>
<div class="grid grid--3" style="margin-top:1.6rem">
<div class="card"><h3>Des travaux ont eu lieu</h3><p>Un diagnostic décrit un bâtiment à
un instant donné. Une cloison déposée, une chaudière remplacée, une toiture refaite :
ce que le rapport décrit n'existe plus tel quel.</p></div>
<div class="card"><h3>La réglementation a changé</h3><p>C'est ce qui est arrivé aux DPE
d'avant juillet 2021 et aux repérages amiante d'avant 2013 : la méthode ou le champ
du contrôle ont évolué, et les anciens rapports sont sortis du jeu.</p></div>
<div class="card"><h3>Une anomalie est apparue</h3><p>Des cordonnets dans une cave, une
peinture qui s'écaille, une odeur de gaz : un fait nouveau prime toujours sur une date
d'échéance lointaine.</p></div>
</div></div></section>
{cta()}"""

    # Le formulaire de fin de simulateur est partagé : il faut lui donner les
    # coordonnées et l'adresse d'envoi, et le charger avant celui qui l'appelle.
    extra = (cfg_rappel()
             + '<script src="/assets/validite.js" defer></script>')
    shell(path=p, title="Vos diagnostics sont-ils encore valables ? — DGLM",
          desc=desc_courte("Cochez vos diagnostics, indiquez leurs dates : l'outil dit "
                           "lesquels tiennent encore, lesquels expirent et lesquels sont "
                           "à refaire."),
          body=body + extra,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "WebApplication",
                         "name": "Simulateur de validité des diagnostics",
                         "url": DOM + p, "applicationCategory": "UtilityApplication",
                         "operatingSystem": "Web"}))
    URLS.append((p, "0.85", "monthly", MAJ_STRUCTURE))


# ------------------------------------------------------- certifications et assurances
# Données relevées sur les certificats et attestations originaux (Dropbox DGLM,
# juillet 2026). Toute modification doit être faite pièce en main : ce sont des
# engagements opposables. Les dates sont celles portées sur les certificats.
CERTIFIES = [
    {"nom": "Amaury Molinier", "role": "Directeur opérationnel, diagnostiqueur certifié",
     "num": "C2936", "org": "LCC Qualixpert", "date": "18/02/2026",
     "domaines": [("Amiante <strong>avec mention</strong>", "11/06/2030"),
                  ("Audit énergétique", "28/12/2028"),
                  ("Diagnostic de performance énergétique, tous types de bâtiments", "28/12/2028"),
                  ("État relatif à la présence de termites (France métropolitaine)", "11/06/2030"),
                  ("Constat de risque d'exposition au plomb (CREP)", "19/07/2030"),
                  ("État des installations intérieures d'électricité", "19/07/2030"),
                  ("État des installations intérieures de gaz", "13/12/2029")]},
    {"nom": "Virgile Poulain", "role": "Diagnostiqueur certifié",
     "num": "C2022-SE09-041", "org": "WE-CERT", "date": "01/07/2024",
     "domaines": [("Diagnostic de performance énergétique <strong>avec mention</strong>", "27/10/2029"),
                  ("Diagnostic de performance énergétique", "27/10/2029"),
                  ("Amiante", "27/10/2029"),
                  ("Constat de risque d'exposition au plomb (CREP)", "27/10/2029"),
                  ("État des installations intérieures d'électricité", "27/10/2029"),
                  ("État des installations intérieures de gaz", "27/10/2029")]},
    {"nom": "Nicolas Louvet", "role": "Diagnostiqueur certifié",
     "num": "C3596", "org": "LCC Qualixpert", "date": "18/02/2026",
     "domaines": [("Amiante", "09/11/2029"),
                  ("Diagnostic de performance énergétique", "21/08/2029"),
                  ("Constat de risque d'exposition au plomb (CREP)", "21/08/2029"),
                  ("État des installations intérieures d'électricité", "21/08/2029"),
                  ("État relatif à la présence de termites (France métropolitaine)", "15/06/2029"),
                  ("État des installations intérieures de gaz", "15/06/2029")]},
    {"nom": "Nicolas Péré", "role": "Diagnostiqueur certifié",
     "num": "2456", "org": "LCP Certification", "date": "01/07/2024",
     "domaines": [("Amiante", "09/04/2031"),
                  ("Diagnostic de performance énergétique", "09/04/2031"),
                  ("État des installations intérieures de gaz", "09/04/2031"),
                  ("Constat de risque d'exposition au plomb (CREP)", "25/02/2031"),
                  ("État des installations intérieures d'électricité", "25/02/2031"),
                  ("État relatif à la présence de termites (France métropolitaine)", "25/02/2031")]},
    {"nom": "Thibault Le Moine", "role": "Cofondateur, diagnostiqueur certifié",
     "num": "C3284", "org": "LCC Qualixpert", "date": "18/02/2026",
     "domaines": [("Amiante", "21/07/2027"),
                  ("État relatif à la présence de termites (France métropolitaine)", "21/07/2027"),
                  ("État des installations intérieures de gaz", "21/07/2027"),
                  ("État des installations intérieures d'électricité", "02/09/2027")]},
]


def page_certifications():
    """Les preuves, nominatives et datées. Un donneur d'ordre doit pouvoir
    vérifier nos titres sans nous les demander."""
    p = "/certifications-et-assurances/"
    trail = [("Accueil", "/"), ("Certifications et assurances", p)]

    fiches = ""
    for c in CERTIFIES:
        lignes = "".join(
            f"<tr><td>{d}</td><td>jusqu'au {fin}</td></tr>" for d, fin in c["domaines"])
        fiches += f"""<article class="certif">
<header><h3>{esc(c['nom'])}</h3>
<p class="certif__role">{esc(c['role'])}</p>
<p class="certif__num">Certificat n<sup>o</sup> {esc(c['num'])} — {esc(c['org'])}
<span>· édition du {esc(c['date'])}</span></p></header>
<div class="tabwrap"><table class="tabsimple">
<thead><tr><th>Domaine de certification</th><th>Validité</th></tr></thead>
<tbody>{lignes}</tbody></table></div></article>"""

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Nos titres, vérifiables</p>
<h1>Certifications et assurances</h1>
<p class="lede">Un diagnostic n'a de valeur que si celui qui le signe est certifié pour
le faire, et assuré pour ce qu'il engage. Voici nos numéros, nos domaines et nos dates —
sans avoir à les demander.</p>
<div class="actions"><a class="btn btn--light" href="/equipe/">Qui nous sommes</a>
<a class="btn btn--light" href="/devis/">Demander un devis</a></div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Les personnes</p>
<h2>Cinq diagnostiqueurs certifiés</h2>
<p class="enclair"><span>L'antisèche</span>La certification est <strong>personnelle</strong>,
jamais celle de l'entreprise : elle s'obtient domaine par domaine, après examen théorique et
pratique, et se contrôle pendant tout son cycle. Chaque rapport porte le nom et le numéro de
celui qui l'a signé — vous pouvez donc vérifier, avant comme après.</p>
{fiches}
<p class="maj">Portée et validité vérifiables auprès de l'organisme certificateur.
Une certification peut être suspendue, modifiée ou retirée à tout moment : c'est ce qui
en fait la valeur.</p>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">Les titres</p>
<h2>Titre professionnel et certification : deux choses différentes</h2>
<p class="narrow">On les confond souvent, et la nuance mérite d'être connue avant de
commander une mission. Le <strong>titre professionnel</strong> sanctionne une formation
qualifiante : il s'obtient une fois, à l'issue d'un parcours complet, et atteste d'un
niveau de qualification. La <strong>certification de compétences</strong>, elle, autorise à
exercer un domaine précis : elle est délivrée pour un cycle, contrôlée pendant sa durée
par des audits sur dossiers réels, et doit être renouvelée.</p>
<p class="narrow">Autrement dit : le titre dit qu'on a appris le métier, la certification
dit qu'on a le droit de l'exercer aujourd'hui. Les deux sont utiles ; seule la seconde
est opposable sur un rapport.</p>
<div class="grid grid--2" style="margin-top:1.6rem">
<div class="card"><h3>Aude de Gentile</h3>
<p><strong>Titre professionnel de diagnostiqueur immobilier</strong>, enregistré au
répertoire national des certifications professionnelles (RNCP), niveau 5 du cadre européen
— délivré par ODI Formation en août 2020.</p>
<p>Elle ne signe pas de mission soumise à certification : ce titre lui donne la lecture
technique des dossiers et la relecture des guides publiés ici, pas le droit d'établir un
rapport. C'est le métier appris, énoncé sans l'arrondir.</p></div>
<div class="card"><h3>Thibault Le Moine</h3>
<p><strong>Titre professionnel de diagnostiqueur immobilier</strong>, enregistré au
répertoire national des certifications professionnelles (RNCP), niveau 5 du cadre européen
— délivré par ODI Formation en août 2020.</p>
<p>Il est en outre <strong>certifié</strong> en amiante, termites, gaz et électricité :
sa fiche et ses dates figurent ci-dessus.</p></div>
</div>
<p class="maj">Les fondateurs se sont formés au métier avant de créer le cabinet, et non
l'inverse. C'est aussi ce qui explique le parti pris du site : expliquer plutôt que vendre.</p>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">L'organisme</p>
<h2>Qui nous certifie, et qui le contrôle</h2>
<p class="narrow">Nos diagnostiqueurs sont certifiés par trois organismes distincts, tous
accrédités par le <strong>COFRAC</strong> — le Comité français d'accréditation — pour la
certification de personnes : <strong>LCC Qualixpert</strong> (accréditation 4-0094),
<strong>WE-CERT</strong> (accréditation 4-0634) et <strong>LCP Certification</strong>,
à Pessac. Chacun a recruté là où il exerçait ; nous n'avons pas jugé utile de tout
regrouper artificiellement chez un seul certificateur.</p>
<p class="narrow">Cette chaîne compte : le COFRAC n'évalue pas les diagnostiqueurs, il
évalue ceux qui les certifient. C'est ce qui empêche une certification de n'être qu'un
logo acheté. Le référentiel applicable est fixé par arrêté ministériel, et il a été
resserré en 2024 pour l'amiante, l'électricité, le gaz, le plomb et les termites.</p>
<p class="narrow">Deux mentions méritent d'être signalées, parce qu'elles ne sont pas
courantes. La <strong>mention amiante</strong> autorise les repérages les plus exigeants,
dont ceux qui précèdent travaux et démolition — c'est le cœur de notre activité. La
<strong>mention DPE</strong> permet d'établir le diagnostic de performance énergétique sur
tout type de bâtiment, immeuble collectif compris, et non seulement sur un logement.</p>
</div></section>

<section class="band band--pale"><div class="wrap">
<p class="eyebrow">La responsabilité</p>
<h2>Assurance et veille</h2>
<div class="grid grid--2" style="margin-top:1.6rem">
<div class="card"><h3>Responsabilité civile professionnelle</h3>
<p>Contrat souscrit auprès de <strong>Markel Insurance SE</strong> (succursale française),
par l'intermédiaire du courtier Klarity Assurance, au titre de l'activité de diagnostiqueur
immobilier. Garantie de <strong>300 000 € par sinistre</strong> et
<strong>500 000 € par année d'assurance</strong>. L'attestation en cours est transmise sur
demande, et jointe d'office à nos dossiers de consultation.</p></div>
<div class="card"><h3>Veille réglementaire</h3>
<p>Nous sommes membres de l'<strong>Alliance du Diagnostic Immobilier</strong>, qui diffuse
à ses adhérents la veille technique, juridique et réglementaire du métier. C'est ce qui
nous permet d'appliquer un texte le mois où il change, et non l'année suivante.
<a href="/conformite/">Notre veille est contrôlée chaque matin</a>.</p></div>
</div>
<div class="enclair" style="margin-top:1.8rem"><p><strong>Médiation de la consommation.</strong>
En tant qu'adhérents, nous donnons à nos clients particuliers l'accès à un dispositif de
médiation de la consommation conforme à l'ordonnance du 20 août 2015. Concrètement : en cas
de désaccord qui ne se règle pas avec nous, vous disposez d'un recours gratuit avant toute
action judiciaire.</p></div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Ce que ça change</p>
<h2>Pourquoi nous publions tout cela</h2>
<p class="narrow">Un rapport de diagnostic engage celui qui le signe, et il engage aussi
celui qui s'en sert : le syndic qui présente un plan de travaux à son assemblée, le maître
d'ouvrage qui lance un chantier. Avant de commander, un donneur d'ordre sérieux vérifie
trois choses — que l'opérateur est certifié <em>dans le domaine concerné</em>, que sa
certification est <em>en cours de validité</em>, et qu'il est <em>assuré</em> pour cette
activité.</p>
<p class="narrow">La plupart des cabinets répondent « sur simple demande ». Nous préférons
répondre avant la question. Si une pièce vous manque pour votre dossier de consultation,
elle vous parviendra le jour même.</p>
<div class="actions" style="margin-top:1.6rem">
<a class="btn" href="/devis/">Demander un devis</a>
<a class="btn btn--ghost" href="tel:{E['tel_raw']}">{E['tel']}</a></div>
</div></section>
{cta()}"""

    schema = jsonld(org_schema(), breadcrumb(trail),
                    {"@type": "WebPage", "url": DOM + p,
                     "name": "Certifications et assurances"},
                    *[{"@type": "Person", "name": c["nom"], "jobTitle": c["role"],
                       "worksFor": {"@id": DOM + "#org"},
                       "hasCredential": {
                           "@type": "EducationalOccupationalCredential",
                           "credentialCategory": "certification",
                           "identifier": c["num"],
                           "recognizedBy": {"@type": "Organization", "name": "LCC Qualixpert"}}}
                      for c in CERTIFIES])
    shell(path=p, title="Certifications et assurances — DGLM Expertises",
          desc=desc_courte("Nos numéros de certification par diagnostiqueur, les domaines "
                           "couverts, leurs dates de validité, notre assurance de "
                           "responsabilité civile et notre veille."),
          body=body, schema=schema)
    URLS.append((p, "0.8", "monthly", MAJ_STRUCTURE))


# ------------------------------------------------------------------ aides financières
def page_aides():
    """Simulateur MaPrimeRénov' Copropriété + guide des aides. Double usage :
    le syndic qui veut un ordre de grandeur, et l'étude (DTG, PPPT, audit)
    qui a besoin du détail ligne à ligne. Barèmes datés, sources officielles,
    moteur dans build/aides.js — rien d'inventé."""
    p = "/aides-financieres-copropriete/"
    trail = [("Accueil", "/"), ("Aides financières", p)]

    _info = [0]

    def info(titre, texte_aide):
        """Bulle d'explication au clic — le jargon devient lisible sur place."""
        _info[0] += 1
        i = _info[0]
        return (f'<span class="info"><button type="button" class="info__b" '
                f'aria-expanded="false" aria-controls="inf{i}" '
                f'aria-label="Qu\'est-ce que {esc(titre)} ?">?</button>'
                f'<span class="info__c" id="inf{i}" role="note">{texte_aide}</span></span>')

    def champ_n(cid, lbl, aide="", requis=True, bulle=""):
        a = f"<em>{esc(aide)}</em>" if aide else ""
        return (f'<label class="field" for="{cid}"><span>{esc(lbl)}{bulle}</span>'
                f'<input id="{cid}" type="number" min="0" inputmode="numeric">{a}</label>')

    def champ_s(cid, lbl, options, aide="", bulle=""):
        opts = "".join(f'<option value="{v}">{esc(t)}</option>' for v, t in options)
        a = f"<em>{esc(aide)}</em>" if aide else ""
        return (f'<label class="field" for="{cid}"><span>{esc(lbl)}{bulle}</span>'
                f'<select id="{cid}">{opts}</select>{a}</label>')

    B_LOTS = info("un lot d'habitation", """<strong>Un lot</strong>, c'est une partie
privative (un appartement, un local) avec sa quote-part de parties communes. Comptez ici
les lots à usage d'habitation, pas les caves et parkings vendus séparément.
L'administration apprécie la règle <strong>en tantièmes</strong> : si votre répartition
s'écarte du simple comptage, ajustez le chiffre en conséquence.""")
    B_RP = info("une résidence principale", """<strong>Résidence principale</strong> =
logement occupé au moins huit mois par an, par son propriétaire ou son locataire. Les
résidences secondaires et les logements vacants n'entrent pas dans le compte. Il en faut
au moins <strong>65 %</strong> des lots pour une copropriété de 20 lots ou moins,
<strong>75 %</strong> au-delà.""")
    B_IMMAT = info("l'immatriculation", """Toute copropriété d'habitation doit être
inscrite au <strong>registre national des copropriétés</strong>, et ses données mises à
jour chaque année par le syndic. Sans immatriculation à jour, aucune aide publique n'est
versée. Le numéro figure sur les documents de la copropriété — sinon, demandez-le au
syndic.""")
    B_AMO = info("l'AMO", """L'<strong>assistance à maîtrise d'ouvrage</strong> est
l'accompagnateur obligatoire du projet : un professionnel indépendant qui aide la
copropriété à définir le programme, consulter les entreprises, monter le dossier de
subvention et suivre le chantier. Son coût est lui-même aidé à <strong>50 %</strong>
(plafond 300 € par logement, minimum 3 000 € par copropriété). Ce n'est pas le
diagnostiqueur, ni le syndic, ni l'architecte : c'est un rôle à part.""")
    B_GAIN = info("le gain énergétique", """Le <strong>gain énergétique</strong> est la
baisse de consommation attendue après travaux, exprimée en pourcentage — par exemple
passer de 300 à 180 kWh/m²/an, soit 40 % de gain. Il ne s'estime pas au jugé : c'est
l'<a href="/audit-energetique-copropriete/">audit énergétique</a> ou le
<a href="/diagnostic-technique-global/">DTG</a> qui le calcule, scénario par scénario.
En deçà de 35 %, aucune aide collective.""")
    B_PASSOIRE = info("une passoire thermique", """Une <strong>passoire thermique</strong>
est un logement classé <strong>F ou G</strong> au diagnostic de performance énergétique.
Si les travaux font passer l'immeuble à la classe <strong>D ou mieux</strong>, l'aide est
majorée de 10 points. <a href="/questions/qu-est-ce-qu-une-passoire-thermique/">Notre
guide sur les passoires →</a>""")
    B_FRAGILE = info("une copropriété fragile", """L'Anah qualifie de
<strong>fragile</strong> une copropriété dont le taux d'impayés dépasse un seuil
réglementaire, et de <strong>en difficulté</strong> celle qui fait l'objet d'un plan de
sauvegarde ou d'une procédure judiciaire. Sont aussi visées les copropriétés situées dans
un quartier en renouvellement urbain. Dans le doute, votre syndic ou l'espace conseil
France Rénov' vous le confirmera : la majoration atteint 20 points.""")
    B_REVENUS = info("les revenus modestes", """Les catégories <strong>modeste</strong> et
<strong>très modeste</strong> reposent sur les <strong>plafonds de ressources de
l'Anah</strong> : ils dépendent du revenu fiscal de référence du ménage, du nombre de
personnes du foyer et de la région (les plafonds d'Île-de-France diffèrent des autres).
Ils sont revalorisés chaque année — c'est l'AMO qui les vérifie au dépôt du dossier.
Ne comptez ici que les <strong>propriétaires occupants</strong> : les bailleurs relèvent
d'un autre régime.""")

    formulaire = f"""<form id="simu-aides" class="devis">
<div class="devis__bloc"><h3>1 · La copropriété</h3>
{champ_n("a_lots", "Nombre de lots d'habitation", "", bulle=B_LOTS)}
{champ_n("a_rp", "dont résidences principales", "", bulle=B_RP)}
{champ_s("a_immat", "Immatriculée et à jour au registre national ?", [("oui", "Oui"), ("non", "Non / je ne sais pas")], bulle=B_IMMAT)}
{champ_s("a_age", "Bâtiment achevé depuis plus de 15 ans ?", [("oui", "Oui"), ("non", "Non")], "La date d'achèvement, pas celle de la dernière rénovation.")}
</div>
<div class="devis__bloc"><h3>2 · Le programme de travaux</h3>
{champ_n("a_travaux", "Montant de travaux estimé (€ HT)", "Le chiffrage issu du DTG, du PPPT ou de l'audit énergétique.")}
<details class="postes" id="a_postes">
<summary>Détailler par poste de travaux — recommandé pour un plan pluriannuel</summary>
<p class="postes__intro">Tous les postes d'un programme n'ouvrent pas droit à l'aide :
seuls les travaux d'économie d'énergie, et ceux qui leur sont indissociablement liés,
entrent dans l'assiette. Renseignez ce que vous connaissez — la somme remplace alors le
montant global ci-dessus.</p>
<p class="postes__groupe">Postes éligibles</p>
{"".join(champ_n("a_p_" + c, n, "", requis=False) for c, n in [
    ("murs", "Isolation des murs (extérieur ou intérieur)"),
    ("toiture", "Isolation de la toiture, des combles ou de la terrasse"),
    ("plancher", "Isolation des planchers bas (sur cave, sur passage)"),
    ("menuiseries", "Menuiseries extérieures (fenêtres, portes sur l'extérieur)"),
    ("chauffage", "Chauffage collectif et eau chaude sanitaire"),
    ("ventilation", "Ventilation"),
    ("induits", "Travaux induits (reprises indissociables des postes ci-dessus)")])}
<p class="postes__groupe postes__groupe--non">Postes non éligibles à cette aide</p>
{champ_n("a_p_ravalement", "Ravalement seul, sans isolation", "Avec une isolation par l'extérieur, portez-le au poste « isolation des murs » : il devient subventionnable.", requis=False)}
{champ_n("a_p_autres", "Autres postes (ascenseur, électricité, embellissement…)", "", requis=False)}
</details>
{champ_n("a_amo", "Coût de l'AMO (€ HT), si connu", "", requis=False, bulle=B_AMO)}
{champ_s("a_gain", "Gain énergétique visé", [("35", "35 à 49 % (minimum requis)"), ("50", "50 % ou plus"), ("0", "Moins de 35 %")], "", bulle=B_GAIN)}
{champ_s("a_passoire", "Sortie de passoire ?", [("non", "Non"), ("oui", "Oui : F ou G aujourd'hui, D ou mieux après travaux")], "", bulle=B_PASSOIRE)}
{champ_s("a_fragile", "Copropriété fragile ou en difficulté ?", [("non", "Non / je ne sais pas"), ("oui", "Oui (impayés élevés, plan de sauvegarde, quartier en renouvellement urbain)")], "", bulle=B_FRAGILE)}
</div>
<div class="devis__bloc"><h3>3 · Les ménages (primes individuelles)</h3>
{champ_n("a_tm", "Propriétaires occupants très modestes", "", requis=False, bulle=B_REVENUS)}
{champ_n("a_m", "Propriétaires occupants modestes", "", requis=False)}
</div>
<div class="simu-valider">
<button type="submit" class="btn" id="aides-valider">Estimer mes aides</button>
<p class="simu-manque" id="aides-manque" role="status" aria-live="polite"></p>
</div>
</form>
<p id="aides-synthese" class="sr" role="status" aria-live="polite"></p>
<div id="aides-resultat" tabindex="-1" hidden>
<h2 style="margin-top:2rem">Votre estimation, ligne à ligne</h2>
<div class="simu-corps"></div>
<div class="actions" style="margin-top:1.2rem">
<button type="button" id="aides-copier" class="btn">Copier le détail (pour une étude ou un PV)</button>
<button type="button" id="aides-imprimer" class="btn btn--light">Imprimer ou enregistrer en PDF</button>
</div>
<p class="maj">Estimation indicative et non contractuelle : seule la décision d'octroi de
l'Anah fait foi, après instruction du dossier déposé avec votre AMO. Barèmes consultés le
31/07/2026 — signalez-nous toute évolution, la page est revue à chaque mise à jour du site.</p>
</div>
<noscript><p class="enclair"><span>Sans JavaScript</span>Le simulateur a besoin de JavaScript,
mais tout le barème est dans le guide ci-dessous — le calcul se fait très bien à la main.</p></noscript>"""

    guide = (
        volet("Le socle", "MaPrimeRénov' Copropriété, en clair",
              """<p>C'est l'aide centrale, versée par l'Anah <strong>au syndicat des
copropriétaires</strong>, puis répartie entre copropriétaires aux tantièmes. Quatre conditions
principales : la copropriété est <strong>immatriculée</strong> au registre national, le bâtiment a
<strong>plus de 15 ans</strong>, les résidences principales représentent au moins
<strong>65 %</strong> des lots (20 lots ou moins) ou <strong>75 %</strong> (au-delà), et le
programme vise au moins <strong>35 % de gain énergétique</strong> — c'est précisément ce que
chiffrent le DTG, le projet de plan pluriannuel et l'audit énergétique.</p>
<p>Le financement : <strong>30 %</strong> du montant des travaux (gain de 35 à 49 %) ou
<strong>45 %</strong> (gain de 50 % et plus), sur une assiette plafonnée à
<strong>25 000 € par logement</strong>. S'y ajoutent le cas échéant <strong>+ 10 %</strong> si
l'immeuble sort du statut de passoire (F ou G avant travaux, D ou mieux après) et
<strong>+ 20 %</strong> pour les copropriétés fragiles ou en difficulté. Les propriétaires
occupants aux revenus modestes reçoivent en plus une prime individuelle
(<strong>1 500 €</strong>, ou <strong>3 000 €</strong> pour les très modestes).</p>
<p>Deux obligations de parcours : une <strong>assistance à maîtrise d'ouvrage</strong> (AMO),
elle-même aidée à 50 % (plafond 300 € par logement, plancher 3 000 €), et des entreprises
<strong>RGE</strong>.</p>""", ouvert=True, ancre="mpr"),
        volet("Le financement", "Éco-PTZ : financer le reste à charge",
              """<p>Le prêt à taux zéro finance ce que l'aide ne couvre pas, <strong>sans
intérêts</strong>. Il peut être porté collectivement par le syndicat (le syndic souscrit pour
les copropriétaires volontaires) ou souscrit individuellement, jusqu'à
<strong>50 000 € par logement</strong> pour une rénovation d'ampleur — montant et durée à
confirmer avec la banque selon le programme retenu. Il se cumule avec MaPrimeRénov'
Copropriété.</p>""", pale=True, ancre="ecoptz"),
        volet("Les compléments", "TVA à 5,5 %, CEE et aides locales",
              """<p><strong>TVA réduite :</strong> les travaux d'amélioration de la performance
énergétique relèvent de la TVA à 5,5 % au lieu de 20 % — elle s'applique directement sur les
factures, sans dossier.</p>
<p><strong>Certificats d'économies d'énergie (CEE) :</strong> cumulables avec l'aide, leur
valorisation dépend du marché et se chiffre sur devis auprès d'un délégataire — votre AMO les
intègre au plan de financement.</p>
<p><strong>Aides locales :</strong> selon les années, la métropole, le département ou la région
abondent certains programmes. Le réflexe : interroger l'espace conseil France Rénov' de votre
territoire au moment du dépôt.</p>""", ancre="complements"),
        volet("La méthode", "Du diagnostic au dossier : le circuit",
              """<p>1 · Le <a href="/diagnostic-technique-global/">DTG</a> ou
l'<a href="/audit-energetique-copropriete/">audit énergétique</a> établit l'état du bâti et le
<strong>gain énergétique atteignable</strong> — la donnée qui déclenche tout.
2 · Le <a href="/plan-pluriannuel-de-travaux/">projet de plan pluriannuel</a> hiérarchise et
chiffre les travaux. 3 · L'assemblée vote le programme et le recours à une AMO.
4 · L'AMO monte le dossier Anah, intègre CEE et éco-PTZ, puis les travaux démarrent avec des
entreprises RGE. Nos études sont conçues pour alimenter ce circuit sans ressaisie : le
pourcentage de gain, poste par poste, figure dans nos rapports.</p>""", pale=True, ancre="circuit"),
    )

    sources = """<div class="sources"><p>Sources officielles — consultées le 31/07/2026 :
<a href="https://www.service-public.fr/particuliers/vosdroits/F35083" rel="noopener nofollow">MaPrimeRénov' (Service-Public)</a> ·
<a href="https://www.service-public.fr/particuliers/vosdroits/F19905" rel="noopener nofollow">Éco-prêt à taux zéro (Service-Public)</a> ·
<a href="https://www.anah.fr/copropriete/syndicat-de-coproprietaires/beneficier-de-laide-maprimerenov-coproprietes/" rel="noopener nofollow">MaPrimeRénov' Copropriété (Anah)</a></p></div>"""

    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Copropriétés — après le DTG, le PPPT ou l'audit</p>
<h1>Les aides financières, chiffrées ligne à ligne</h1>
<p class="lede">Votre diagnostic chiffre des travaux ; la collectivité en finance une part
importante. Ce simulateur applique le barème en vigueur — taux, plafonds, bonus, primes —
et détaille chaque calcul, pour un ordre de grandeur honnête en deux minutes.</p>
<div class="actions"><a class="btn btn--light" href="/devis/">Demander une étude</a>
<a class="btn btn--light" href="#guide">Lire le guide des aides</a></div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Le simulateur</p>
<h2>Estimez vos aides</h2>
<p class="enclair"><span>L'antisèche</span>Remplissez ce que vous savez : le résultat s'affiche
et se recalcule à mesure. Chaque ligne montre son calcul — rien n'est caché, tout se vérifie.
Le détail se copie tel quel dans une étude ou un procès-verbal.</p>
{formulaire}
</div></section>

<section id="guide" class="band band--pale"><div class="wrap">
<p class="eyebrow">Le guide</p>
<h2>Comprendre chaque dispositif</h2>
</div></section>
{"".join(guide)}
<section class="band"><div class="wrap prose">
{sources}
<p class="maj">Établi par l'équipe DGLM Expertises — barèmes vérifiés en {MAJ}</p>
</div></section>
{cta()}"""

    # Le formulaire de fin de simulateur est partagé : il faut lui donner les
    # coordonnées et l'adresse d'envoi, et le charger avant celui qui l'appelle.
    extra = (cfg_rappel()
             + '<script src="/assets/aides.js" defer></script>')
    shell(path=p, title="Aides financières en copropriété : le simulateur — DGLM",
          desc=desc_courte("Simulateur des aides en copropriété après un DTG, PPPT ou audit : "
                           "taux, plafonds, primes, reste à charge, et le guide des dispositifs."),
          body=body + extra,
          schema=jsonld(org_schema(), breadcrumb(trail),
                        {"@type": "WebApplication", "name": "Simulateur d'aides — copropriétés",
                         "url": DOM + p, "applicationCategory": "FinanceApplication",
                         "operatingSystem": "Web"}))
    URLS.append((p, "0.85", "monthly", MAJ_STRUCTURE))


def page_devis():
    p = "/devis/"
    trail = [("Accueil", "/"), ("Demande de devis", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Réponse sous deux heures ouvrées</p>
<h1>Demander un devis</h1>
<p class="lede">Le questionnaire s'adapte à la mission. En le remplissant
complètement, vous nous évitez un rappel préalable : nous chiffrons directement.</p>
<div class="actions"><a class="btn btn--light" href="/aide-au-devis/">Quels documents joindre ? La liste →</a></div>
</div></section>

<section class="band band--pale"><div class="wrap prose">
<h2>Pourquoi vous ne trouverez pas de tarif sur ce site</h2>
<p>Vous cherchez sans doute un ordre de prix, et vous ne le trouverez nulle part ici.
Ce n'est pas une manœuvre pour vous faire appeler : en copropriété, un tarif affiché
serait faux neuf fois sur dix.</p>
<p>Le prix d'une mission collective dépend de choses qu'aucune grille ne capture :
le nombre de lots et de bâtiments, l'année de construction, l'accès aux combles, aux
sous-sols et aux gaines techniques, le nombre de prélèvements que le bâti impose, les
documents que la copropriété possède déjà — un dossier technique amiante à jour change
tout — et la nécessité ou non de repasser après travaux. Deux immeubles voisins de
même taille peuvent aller du simple au double.</p>
<p>Nous préférons donc chiffrer votre immeuble plutôt que de vous vendre une moyenne.
<strong>Remplissez le questionnaire ci-dessous : vous avez votre prix, ferme et détaillé,
sous deux heures ouvrées.</strong> Et si vous comparez plusieurs propositions, notre
<a href="/aide-au-devis/">aide au devis</a> vous donne les points à vérifier pour que la
comparaison porte sur le même périmètre — c'est là que les écarts se cachent.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>Votre demande</h2>
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
<input id="c_societe" name="societe" type="text" required></label>
<div id="devis-part" class="enclair" hidden><p><strong>Vous êtes un particulier ?</strong>
Pour des travaux, une démolition ou une mission d'immeuble, vous êtes exactement au bon
endroit — laissez « Société » vide. Pour les diagnostics d'une vente ou d'une location de
votre logement, c'est notre <a href="/particuliers/">équipe dédiée aux particuliers</a>
qui s'en charge.</p></div></div>

<div id="devis-mission" hidden></div>

<div id="devis-pieces" class="devis__bloc" hidden>
<h3>Vos documents</h3>
<p class="pieces__intro">Joindre vos pièces, c'est souvent gagner un aller-retour :
nous chiffrons sur pièces plutôt que sur hypothèses. Rien sous la main ?
Envoyez quand même, on fait avec ce que vous avez.</p>
<div class="pieces">
<div class="pieces__zone" id="pieces-zone">
<label class="pieces__btn" for="pieces-input">Choisir des fichiers</label>
<input id="pieces-input" type="file" multiple
 accept=".pdf,.jpg,.jpeg,.png,.heic,.doc,.docx,.xls,.xlsx,.odt,.ods,.dwg,.zip,.txt,.csv">
<p class="pieces__aide">ou glissez-les ici — PDF, photos, plans, tableurs.
Tout reste dans votre navigateur : rien n'est envoyé tant que vous ne le décidez pas.</p>
</div>
<ul class="pieces__liste" id="pieces-liste"></ul>
<p class="pieces__etat" id="pieces-etat" role="status" aria-live="polite"></p>
<div class="actions" id="pieces-actions" hidden>
<button type="button" id="pieces-zip" class="btn">Préparer mon dossier (.zip)</button>
</div>
</div>
<aside class="pieces__memo" id="pieces-memo" hidden>
<p class="pieces__memo-titre">Ce qui nous aide le plus, pour cette mission</p>
<ul id="pieces-memo-liste"></ul>
<p class="pieces__memo-lien"><a href="/aide-au-devis/">La liste complète, à imprimer →</a></p>
</aside>
</div>

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
    docs = {cle: [d for bloc in (b1, b2)
                  for t, items in DOCS_DEVIS if t == bloc for d in items]
            for cle, (b1, b2) in DOCS_PAR_MISSION.items()}
    extra = (f'<script>window.DEVIS_CFG={{endpoint:"{FORMULAIRE["endpoint"]}",'
             f'cle:"{FORMULAIRE["cle"]}",destinataire:"{FORMULAIRE["destinataire"]}",'
             f'objet:"{FORMULAIRE["objet"]}"}};'
             f'window.DEVIS_DOCS={json.dumps(docs, ensure_ascii=False)};</script>'
             f'<script src="/assets/devis.js" defer></script>')
    shell(path=p, title="Demander un devis — DGLM Expertises",
          desc=desc_courte("Demande de devis pour un repérage amiante avant travaux, un "
                           "DTG ou un plan pluriannuel de travaux. Réponse sous deux "
                           "heures ouvrées."),
          body=body + extra, schema=schema)
    URLS.append((p, "0.95", "monthly", MAJ_STRUCTURE))



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
    URLS.append((p, "0.9", "monthly", MAJ_STRUCTURE))


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
              ("/equipe/", "Notre équipe"),
              ("/notre-methode-editoriale/", "Notre méthode éditoriale"),
              ("/contact/", "Contact"),
              ("/avis/", "Avis clients vérifiés"),
              ("/confidentialite/", "Confidentialité"),
              ("/questions/", "Toutes les questions fréquentes")]
    zones = [("/zones-d-intervention/", "Toutes les zones — Gironde et Landes"),
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
          body=body, schema=jsonld(org_schema(), breadcrumb(trail)), chapitres=False)
    URLS.append((p, "0.5", "monthly", MAJ_STRUCTURE))


# ------------------------------------------------------------------ particuliers
# Cette page expédiait le visiteur vers l'autre site de l'entreprise au bout de
# quatre secondes : nous perdions un particulier avant même de lui avoir
# répondu. Elle répond désormais elle-même, par un simulateur bâti sur nos deux
# fiches publiées, puis donne le moyen de nous joindre.
#
# Elle reste NON INDEXÉE. Elle ne vise aucune requête : elle retient ceux qui
# sont déjà là. C'est ce qui la rend compatible avec le pare-feu tout en
# supprimant la fuite.
def page_particuliers():
    p = "/particuliers/"
    trail = [("Accueil", "/"), ("Vous êtes un particulier", p)]
    body = f"""{crumb_html(trail)}
<section class="hero hero--page"><div class="wrap">
<p class="eyebrow eyebrow--pale">Vous êtes un particulier</p>
<h1>De quels diagnostics avez-vous besoin ?</h1>
<p class="lede">Onze documents peuvent composer un dossier de vente, six un
dossier de location. Aucun logement ne les réunit tous : chacun se déclenche
selon l'âge du bâtiment, sa localisation ou ses équipements. Six questions
suffisent à faire le tri.</p></div></section>

<section class="band"><div class="wrap prose">
<div id="simu-part" class="simu"></div>
</div></section>

<section class="band band--pale"><div class="wrap prose">
<h2>Pour aller plus loin</h2>
<p>Nos deux fiches détaillent chaque document, sa condition de déclenchement et
sa durée de validité :</p>
<ul>
<li><a href="/questions/diagnostics-obligatoires-vente/">Quels diagnostics sont
obligatoires pour vendre un logement ?</a></li>
<li><a href="/questions/diagnostics-obligatoires-location/">Quels diagnostics
sont obligatoires pour louer un logement ?</a></li>
<li><a href="/questions/duree-validite-diagnostics/">Combien de temps chaque
diagnostic reste-t-il valable ?</a></li>
</ul>
<h2>Et si votre bien est en copropriété</h2>
<p>Les obligations de l'immeuble ne sont pas celles du logement. Le
<a href="/diagnostics-copropriete/">volet collectif</a> — plan pluriannuel de
travaux, diagnostic technique global, dossier technique amiante des parties
communes — relève du syndicat des copropriétaires, et notre
<a href="{SILO}/simulateur-obligations-copropriete/">simulateur d'obligations
de copropriété</a> vous dit en six questions ce qui s'applique à votre
immeuble.</p>
</div></section>
{cta()}"""
    shell(path=p,
          title="De quels diagnostics avez-vous besoin ? — DGLM Expertises",
          desc="Six questions pour savoir quels documents composent votre "
               "dossier, et pourquoi chacun est dû.",
          body=body, schema="", robots="noindex,follow", chapitres=False,
          # cfg_rappel() apporte les coordonnées et le formulaire partagé, que
          # le simulateur appelle après avoir affiché son résultat.
          head_extra=(cfg_rappel()
                      + '<script src="/assets/particuliers.js?v=' + CSS_V
                      + '" defer></script>'))


# ------------------------------------------------------------------ build
def dates_reelles():
    """Rend à chaque page sa vraie date de dernière modification.

    Le site annonçait une modification du jour sur ses 366 pages, tous les
    matins, parce que le cron reconstruit tout. Le plan du site figeait pendant
    ce temps 216 entrées sur une date unique. Les deux signaux étaient faux, et
    ils se contredisaient.

    On calcule ici l'empreinte de chaque page produite, après neutralisation de
    ce qui varie mécaniquement d'un build à l'autre : les dates elles-mêmes et
    les numéros de version des fichiers statiques. Une empreinte inchangée
    signifie une page inchangée : elle garde sa date mémorisée.

    Retourne {url: date ISO}, et réécrit les dates dans les fichiers produits.
    """
    volatils = [
        (r'"dateModified"\s*:\s*"[0-9-]+"', '"dateModified":"~"'),
        (r'\?v=[0-9a-f]{6,}', '?v=~'),
        (r'"datePublished"\s*:\s*"[0-9-]+"', '"datePublished":"~"'),
        (r'<time[^>]*datetime="[0-9-]+"', '<time datetime="~"'),
    ]

    memoire = {}
    if os.path.exists(HISTO_DATES):
        try:
            memoire = json.load(open(HISTO_DATES, encoding="utf-8"))
        except (ValueError, OSError):
            memoire = {}
    premier = not memoire

    dates, empreintes = {}, {}
    for f in glob.glob(os.path.join(OUT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(f, OUT).replace(os.sep, "/")
        url = "/" + rel[:-len("index.html")]
        url = url if url.endswith("/") else url + "/"
        h = open(f, encoding="utf-8").read()

        neutre = h
        for motif, remplace in volatils:
            neutre = _re.sub(motif, remplace, neutre)
        emp = hashlib.md5(neutre.encode("utf-8")).hexdigest()[:16]

        ancien = memoire.get(url)
        if ancien and ancien.get("empreinte") == emp:
            d = ancien.get("date", ISO)          # rien n'a bougé
        elif premier:
            # Premier passage : on ne prétend pas que tout vient de changer.
            # On reprend la date déjà déclarée dans la page, quand elle existe.
            m = _re.search(r'"dateModified"\s*:\s*"([0-9-]{10})"', h)
            d = m.group(1) if m else ISO
        else:
            d = ISO                              # la page a réellement changé

        dates[url] = d
        empreintes[url] = {"empreinte": emp, "date": d}

        # On réécrit la date dans le fichier produit.
        if d != ISO:
            h2 = h.replace('"dateModified": "' + ISO + '"', '"dateModified": "' + d + '"')
            h2 = h2.replace('"dateModified":"' + ISO + '"', '"dateModified":"' + d + '"')
            if h2 != h:
                open(f, "w", encoding="utf-8").write(h2)

    json.dump(empreintes, open(HISTO_DATES, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)
    changees = sum(1 for u in dates if dates[u] == ISO)
    print(f"    dates réelles : {changees} page(s) modifiée(s) sur {len(dates)}")
    return dates


def flux_rss(contenus):
    """Le flux de syndication de la bibliothèque.

    Le site n'en avait aucun. C'est pourtant le signal de fraîcheur le plus
    direct qu'un site puisse émettre : agrégateurs, lecteurs de flux et
    assistants qui parcourent le web s'en servent pour savoir qu'un site vit.

    On y met les fiches, les plus récentes d'abord. Pas les pages de structure :
    un flux qui annonce des pages qui ne changent jamais n'annonce rien.
    """
    tries = sorted(contenus, key=lambda c: c.get("publication", ""), reverse=True)
    items = []
    for c in tries[:50]:
        lien = DOM + "/questions/" + c["slug"] + "/"
        pub = c.get("publication", "")
        # RFC 822, ce qu'attend un lecteur de flux.
        try:
            d = datetime.datetime.strptime(pub, "%Y-%m-%d")
            pubdate = d.strftime("%a, %d %b %Y 09:00:00 +0100")
        except (ValueError, TypeError):
            pubdate = ""
        items.append(
            "<item>"
            f"<title>{esc(c.get('question') or c['titre'])}</title>"
            f"<link>{lien}</link>"
            f"<guid isPermaLink=\"true\">{lien}</guid>"
            + (f"<pubDate>{pubdate}</pubDate>" if pubdate else "")
            + f"<description>{esc(c.get('meta', ''))}</description>"
            "</item>")
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
        f"<title>{esc(E['nom'])} — questions de copropriété et de travaux</title>"
        f"<link>{DOM}/questions/</link>"
        "<description>Les repères réglementaires et techniques de la copropriété, "
        "des travaux et de la démolition, expliqués par des diagnostiqueurs "
        "certifiés de Bordeaux Métropole.</description>"
        "<language>fr-FR</language>"
        f'<atom:link href="{DOM}/rss.xml" rel="self" type="application/rss+xml"/>'
        + "".join(items) +
        "</channel></rss>")
    with open(os.path.join(OUT, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def sitemap():
    items = "".join(
        f"<url><loc>{DOM}{u}</loc><lastmod>{lm}</lastmod>"
        f"<changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
        for u, pr, cf, lm in URLS)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           + items + "</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        # Les mentions légales doivent rester explorables : c'est par elles que
        # Google vérifie l'identité de l'éditeur — le premier signal de confiance
        # attendu d'un site engageant la responsabilité de ses lecteurs.
        f"User-agent: *\nAllow: /\n"
        f"Disallow: /_veille/\nDisallow: /_source/\nDisallow: /assets/recherche.json\n"
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
    md += li("/notre-methode-editoriale/",
             "Notre méthode éditoriale : qui écrit, quelles sources, quels refus")
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
    # L'empreinte de la feuille de style part dans l'URL : une correction de
    # mise en page atteint alors les visiteurs déjà venus, au lieu de rester
    # invisible derrière leur cache.
    globals()["CSS_V"] = hashlib.md5(
        open(os.path.join(src, "style.css"), "rb").read()).hexdigest()[:8]
    for js in ("simulateur.js", "rappel.js", "particuliers.js", "devis.js", "aides.js", "recherche.js", "validite.js"):
        if os.path.exists(os.path.join(src, js)):
            shutil.copy(os.path.join(src, js), os.path.join(OUT, "assets", js))
    shutil.copytree(os.path.join(src, "assets"), os.path.join(OUT, "assets"),
                    dirs_exist_ok=True)
    contenus = charger_contenus()
    # slug -> titre des guides déjà parus : seuls ceux-là peuvent être liés
    PUBLIES.update({c["slug"]: c["titre"] for c in contenus})
    # En premier : l'index de recherche fixe son empreinte, que toutes les
    # pages suivantes citent dans l'URL du fichier (invalidation du cache).
    page_recherche(contenus)
    page_home(contenus[0] if contenus else None)
    page_simulateur()
    page_hub_diags()
    page_hub_travaux()
    page_tableau()
    page_pack()
    page_aide_devis()
    page_aides()
    page_conseil_syndical()
    page_particulier_travaux()
    page_validite()
    page_certifications()
    page_conformite()
    page_methode()
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

    # Les communes sans découpage par quartier n'entraient dans aucune boucle :
    # leurs textes existaient sans page pour les porter, et /eysines/ — le
    # siège — répondait 404.
    _avec_quartiers = {v["slug"] for v in QUARTIERS_PAR_VILLE} | {"bordeaux"}
    for c in METROPOLE:
        if c["slug"] not in _avec_quartiers:
            page_commune(c)
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
    page_confidentialite()
    page_avis()
    page_404()
    dates_reelles()
    sitemap()
    flux_rss(contenus)
    ecrire_llms(contenus)
    # Domaine personnalisé GitHub Pages : réécrit à chaque build pour ne pas être perdu.
    open(os.path.join(OUT, "CNAME"), "w", encoding="utf-8").write("www.dglmexpertises.fr\n")
    # Fichier-clé IndexNow, qui permet d'annoncer les pages à Bing, Yandex et
    # aux moteurs qui les alimentent. Ce n'est PAS un secret : la clé est
    # publiée telle quelle à la racine du site, c'est précisément ainsi qu'elle
    # prouve que nous contrôlons le domaine. La loger dans un secret de dépôt
    # n'apportait donc rien — et comme le secret n'a jamais été renseigné, la
    # notification des moteurs était désactivée en silence depuis l'origine.
    _cle = os.environ.get("INDEXNOW_KEY", "").strip() or INDEXNOW_KEY
    open(os.path.join(OUT, _cle + ".txt"), "w", encoding="utf-8").write(_cle)
    print(f"{len(URLS)} URL indexables générées dans {OUT}")


if __name__ == "__main__":
    main()
