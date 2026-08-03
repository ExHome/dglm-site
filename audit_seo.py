# -*- coding: utf-8 -*-
"""
Audit SEO du site généré — à relancer après chaque build.

Contrôle principal : la cannibalisation. Deux pages qui visent la même requête
se neutralisent. Ce script détecte les collisions AVANT la mise en ligne, y
compris avec le silo « diagnostics » qui reste à produire.
"""
import glob, html, itertools, os, re, sys, collections

# Une page informationnelle pose une question ou explique. Une page commerciale
# nomme une commune, un prix ou une intention d'achat. Ce ne sont pas les mêmes
# pages de résultats : « combien de temps est valable un DPE » et « DPE Bordeaux »
# ne se disputent rien. Le pare-feu ne doit donc bloquer que le commercial.
INFORMATIONNEL = re.compile(
    r"^(quel|quelle|quels|quelles|comment|pourquoi|combien|qui |que |qu'|quand|"
    r"faut-il|peut-on|doit-on|est-ce|à quoi|à partir de|dans quel|où |ce que|"
    r"tout ce qu)|\?\s*$|\s:\s")
COMMERCIAL = re.compile(
    r"\b(devis|prix|tarif|entreprise|soci[ée]t[ée]|cabinet|prestataire|pas cher|"
    r"meilleur|bordeaux|m[ée]rignac|pessac|talence|b[èe]gles|eysines|gironde|"
    r"pr[èe]s de chez)\b")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.marque import (MARQUE, REQUETES_SITE_A, REQUETES_SITE_B,
                         LIENS_MAX_VERS_SITE_A, QUALIFICATIFS)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# Requêtes réservées au futur silo /diagnostics-immobiliers/.
# Aucune page du silo copropriété ne doit les viser en requête principale.
RESERVE_DIAGNOSTICS = REQUETES_SITE_A


def neutre(s):
    """Une forme comparable, insensible à la typographie.

    Le générateur applique typo_fr() avant de publier : apostrophes
    courbes, espaces insécables, guillemets français. Comparer le texte
    source au texte affiché sans neutraliser cela revient à comparer deux
    alphabets.
    """
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2009", " ")
    s = s.replace("\u00ab", '"').replace("\u00bb", '"')
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", s).strip()

def txt(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))


def mots(h):
    return re.findall(r"[a-zà-ÿ']{3,}", txt(h).lower())


def shingles(w, n=5):
    return {tuple(w[i:i + n]) for i in range(max(0, len(w) - n))}


def requete_principale(title, h1):
    """Approximation de la requête ciblée : titre avant le séparateur."""
    t = re.split(r"[|—–]", title)[0].strip().lower()
    return re.sub(r"[^a-zà-ÿ0-9' ]", " ", t).strip()


def main():
    pages = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True)):
        h = open(f, encoding="utf-8").read()
        url = "/" + os.path.relpath(os.path.dirname(f), ROOT).replace(os.sep, "/") + "/"
        url = url.replace("/./", "/")
        pages[url] = dict(
            html=h,
            title=(re.search(r"<title>(.*?)</title>", h, re.S) or [None, ""])[1],
            desc=(re.search(r'name="description" content="(.*?)"', h, re.S) or [None, ""])[1],
            h1=(re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S) or [None, ""])[1],
            canon=(re.search(r'rel="canonical" href="(.*?)"', h) or [None, ""])[1],
            noindex="noindex" in h[:2000],
        )

    err = warn = 0
    print(f"\n{len(pages)} pages analysées\n" + "=" * 62)

    # 1. Cannibalisation interne : requête principale dupliquée
    print("\n[1] Cannibalisation interne")
    par_requete = collections.defaultdict(list)
    for u, p in pages.items():
        if p["noindex"]:
            continue
        par_requete[requete_principale(p["title"], p["h1"])].append(u)
    coll = {k: v for k, v in par_requete.items() if len(v) > 1}
    if coll:
        for k, v in coll.items():
            print(f"    COLLISION « {k} » → {', '.join(v)}")
            err += 1
    else:
        print(f"    OK — {len(par_requete)} requêtes principales, toutes distinctes")

    # 2. Réservation des requêtes du silo diagnostics
    print("\n[2] Étanchéité avec le site A (dglm-expertises.com)")
    fuites = []
    for u, p in pages.items():
        if p["noindex"]:
            continue
        t = p["title"].lower()
        h1 = re.sub(r"<[^>]+>", "", p["h1"]).lower().strip()

        # Les pages de la bible sont informationnelles : elles répondent à une
        # question, elles ne vendent rien. « Combien de temps est valable un DPE »
        # et « DPE Bordeaux » ne partagent aucune page de résultats — il n'y a
        # donc pas de collision avec le site A, qui ne cible que le commercial.
        if u.startswith("/questions/") and INFORMATIONNEL.search(h1) \
                and not COMMERCIAL.search(t + " " + h1):
            continue

        accueil = u.rstrip("/") == ""
        for kw in RESERVE_DIAGNOSTICS:
            for nom, champ in (("titre", t), ("h1", h1)):
                # La requête compte PARTOUT dans le champ, et plus seulement en
                # tête. « Bordeaux : diagnostic immobilier » disputait la même
                # page de résultats qu'un titre commençant par la requête, et
                # passait pourtant sans être vu.
                if kw not in champ:
                    continue
                # Un qualificatif de copropriété rend la requête légitime —
                # SAUF dans le titre de la page d'accueil. C'est la page la
                # plus forte du site : elle concourt sur le générique même
                # qualifiée. Tant que le site A est sous contrat, l'accueil
                # n'a droit à aucune requête réservée dans son titre.
                if not (accueil and nom == "titre")                         and any(q in champ for q in QUALIFICATIFS):
                    continue
                fuites.append((u, f"{kw} — dans le {nom}"))
                break
    if fuites:
        for u, kw in fuites:
            print(f"    FUITE  {u} cible « {kw} », réservé au site A")
            print( "           → reformuler avec un mot de copropriété "
                   "(collectif, parties communes, syndic, avant travaux…)")
            err += 1
    else:
        print(f"    OK — aucune des {len(pages)} pages ne cible une des "
              f"{len(RESERVE_DIAGNOSTICS)} requêtes du site A")

    # 3. Titres et descriptions
    print("\n[3] Titres et méta-descriptions")
    titres = collections.Counter(p["title"] for p in pages.values())
    dupt = [t for t, n in titres.items() if n > 1]
    for t in dupt:
        print(f"    TITRE DUPLIQUÉ  « {t} »")
        err += 1
    longs = [(u, len(p["title"])) for u, p in pages.items() if len(p["title"]) > 65]
    for u, n in longs[:5]:
        print(f"    titre long ({n} car.)  {u}")
        warn += 1
    dlong = [(u, len(p["desc"])) for u, p in pages.items() if len(p["desc"]) > 165]
    for u, n in dlong[:5]:
        print(f"    description longue ({n} car.)  {u}")
        warn += 1
    if not dupt and not longs and not dlong:
        print("    OK — titres uniques, longueurs conformes")
    else:
        print(f"    {len(dupt)} doublon(s), {len(longs)} titre(s) long(s), "
              f"{len(dlong)} description(s) longue(s)")

    # 4. Liens internes cassés
    print("\n[4] Liens internes")
    casses = set()
    for u, p in pages.items():
        for href in re.findall(r'href="(/[^"#]*?)"', p["html"]):
            if href.startswith("/assets") or href.endswith((".xml", ".txt", ".css", ".js")):
                continue
            if not href.endswith("/"):
                href += "/"
            if href not in pages:
                casses.add((u, href))
    for u, h in sorted(casses)[:10]:
        print(f"    404  {h}   (depuis {u})")
    if casses:
        err += len(casses)
    else:
        print("    OK — aucun lien interne cassé")

    # 5. Similarité entre pages communales
    print("\n[5] Similarité entre pages locales (risque « doorway »)")
    profondeur = 3  # /prestation/commune/
    for silo in sorted({u.rsplit("/", 2)[0] + "/" for u in pages
                        if u.count("/") == profondeur}):
        fs = [u for u in pages if u.startswith(silo) and u != silo][:14]
        if len(fs) < 3:
            continue
        S = {u: shingles(mots(pages[u]["html"])) for u in fs}
        sims = [len(S[a] & S[b]) / max(1, len(S[a] | S[b]))
                for a, b in itertools.combinations(fs, 2)]
        moy, mx = 100 * sum(sims) / len(sims), 100 * max(sims)
        etat = "OK" if mx < 55 else ("À SURVEILLER" if mx < 70 else "RISQUE")
        if mx >= 55:
            warn += 1
        print(f"    {etat:14s} {silo:52s} moy {moy:.0f}%  max {mx:.0f}%")

    # 6. Canoniques
    print("\n[6] URL canoniques")
    canons = collections.Counter(p["canon"] for p in pages.values())
    dupc = [c for c, n in canons.items() if n > 1]
    if dupc:
        for c in dupc:
            print(f"    CANONIQUE DUPLIQUÉE  {c}")
            err += 1
    else:
        print(f"    OK — {len(canons)} canoniques uniques")

    # 7. Protocole de cross-linking
    print("\n[7] Cross-linking vers le site A")
    dom_a = MARQUE["site_a_url"].rstrip("/")
    trop = []
    for u, p in pages.items():
        if p["noindex"]:
            continue  # les mentions légales doivent citer l'éditeur
        # On ne compte QUE les liens de navigation. La déclaration
        # d'identité en données structurées (sameAs) n'envoie personne
        # ailleurs : elle dit à Google que c'est la même entreprise.
        sans_ld = re.sub(r'<script[^>]*application/ld+json[^>]*>.*?</script>',
                         "", p["html"], flags=re.S)
        n = len(re.findall(re.escape(dom_a), sans_ld))
        if n > LIENS_MAX_VERS_SITE_A:
            trop.append((u, n))
    ancres = set(re.findall(r'href="' + re.escape(dom_a) + r'[^"]*"[^>]*>(.*?)</a>',
                            "".join(p["html"] for p in pages.values())))
    exact = [a for a in ancres
             if any(a.strip().lower() == kw for kw in REQUETES_SITE_A)]
    if trop:
        for u, n in trop[:5]:
            print(f"    {n} liens vers le site A sur {u} (max {LIENS_MAX_VERS_SITE_A})")
            warn += 1
    if exact:
        print(f"    ANCRE EXACT-MATCH vers le site A : {exact}")
        err += len(exact)
    if not trop and not exact:
        print(f"    OK — 1 lien par page, ancre descriptive « "
              f"{MARQUE['site_a_ancre']} », aucune ancre exact-match")

    # 8. Préparation de la migration
    print("\n[8] Migration — absorption du site A")
    from data.marque import SITE_A_SOUS_CONTRAT
    if SITE_A_SOUS_CONTRAT:
        print("    Pare-feu ACTIF — les 31 requêtes du site A sont réservées.")
        print("    À la sortie de contrat : SITE_A_SOUS_CONTRAT = False dans")
        print("    data/marque.py, relancer le build, puis 301 le site A vers ce site.")
    else:
        print("    Pare-feu LEVÉ — le site peut cibler l'ensemble des requêtes.")
    if not MARQUE["tel_copro"]:
        print("    À FAIRE — ligne dédiée copro acquise mais non renseignée "
              "(MARQUE['tel_copro']), l'attribution des appels n'est pas traçable.")
        warn += 1

    # ------------------------------------------------------------------
    # [9] LIVRAISON DU CONTENU
    # Les huit contrôles précédents vérifient que les pages produites sont
    # correctes. Aucun ne vérifiait qu'elles contiennent bien ce qui avait
    # été écrit pour elles. Le 3 août 2026, 20 687 mots de textes ont été
    # écrits, validés, poussés — et ne sont jamais arrivés dans une page :
    # deux fonctions partageaient un gabarit, l'une affichait un bloc qu'elle
    # ne construisait pas, l'autre construisait un bloc qu'elle n'affichait
    # pas. La chaîne était au vert. Ce contrôle ferme cette faille.
    # ------------------------------------------------------------------
    print("\n[9] Livraison du contenu — les textes écrits arrivent-ils dans les pages ?")
    attendus = []
    try:
        from data.communes_textes import TEXTES as _TC
        for _slug, _t in _TC.items():
            attendus.append((f"/{_slug}/", "commune " + _slug, _t.get("parc", "")))
    except ImportError:
        print("    (pas de textes de communes)")
    try:
        from data.quartiers_textes import TEXTES as _TQ
        for _cle, _t in _TQ.items():
            attendus.append((f"/{_cle}/", "quartier " + _cle, _t.get("methode", "")))
    except ImportError:
        print("    (pas de textes de quartiers)")

    perdus, absents = [], 0
    for _u, _quoi, _texte in attendus:
        if not _texte:
            continue
        p = pages.get(_u)
        if p is None:
            absents += 1
            continue
        # Des deux côtés la même forme neutre : le générateur pose les
        # apostrophes courbes et les espaces insécables au moment de publier.
        frag = neutre(_texte)[:70]
        corps = neutre(html.unescape(txt(p["html"])))
        if frag not in corps:
            perdus.append((_u, _quoi))

    if perdus:
        for _u, _quoi in perdus[:12]:
            print(f"    PERDU  {_quoi} : son texte n'apparaît pas sur {_u}")
        if len(perdus) > 12:
            print(f"    … et {len(perdus) - 12} autres")
        print("           → un gabarit ne rend pas les données qui lui sont "
              "destinées.")
        err += len(perdus)
    else:
        print(f"    OK — les {len(attendus) - absents} textes déclarés arrivent "
              f"tous dans leur page")
    if absents:
        print(f"    {absents} texte(s) sans page correspondante (à vérifier)")
        warn += absents

    print("\n" + "=" * 62)
    print(f"{err} erreur(s) bloquante(s), {warn} avertissement(s)\n")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
