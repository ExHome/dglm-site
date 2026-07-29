#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VEILLE SEO CONTINUE.

audit_seo.py répond à « le site est-il correct aujourd'hui ? ».
veille_seo.py répond à « s'est-il dégradé depuis la dernière fois ? ».

C'est la question qui compte réellement : un site ne perd presque jamais ses
positions d'un coup. Il les perd par érosion — une page orpheline ici, un
contenu qui s'allège là, un titre qui déborde, un poids qui grimpe.

Le script :
  1. calcule un instantané de 12 indicateurs
  2. le compare au dernier instantané enregistré
  3. écrit un rapport daté, consultable
  4. sort en erreur si un indicateur régresse au-delà du seuil toléré

Branché dans l'action GitHub, il empêche un déploiement qui dégraderait le site.

    python3 veille_seo.py            # veille + rapport
    python3 veille_seo.py --init     # première référence, sans blocage
"""
import datetime
import glob
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(RACINE, "site")
HISTO = os.path.join(RACINE, ".seo-history.json")
RAPPORT = os.path.join(SITE, "_veille", "index.html")

# ---------------------------------------------------------------- seuils
BUDGET_HTML_KO = 70          # poids maximum d'une page, hors assets
MOTS_MINIMUM = 300           # en deçà : contenu mince
PROFONDEUR_MAX = 4           # clics depuis l'accueil
TOLERANCE_PAGES = 0          # aucune perte de page tolérée
TOLERANCE_MOTS = -8          # % de baisse du volume rédactionnel moyen
TOLERANCE_POIDS = 15         # % de hausse du poids moyen


def lire_pages():
    pages = {}
    for f in glob.glob(os.path.join(SITE, "**", "index.html"), recursive=True):
        url = "/" + os.path.relpath(f, SITE)[:-10].replace(os.sep, "/")
        url = "/" if url == "/" else url
        if "/_" in url:
            continue
        h = open(f, encoding="utf-8").read()
        texte = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S)
        texte = re.sub(r"<[^>]+>", " ", texte)
        pages[url] = dict(
            html=h,
            octets=len(h.encode("utf-8")),
            mots=len(re.sub(r"\s+", " ", texte).split()),
            titre=(re.search(r"<title>(.*?)</title>", h, re.S) or [None, ""])[1].strip(),
            desc=(re.search(r'name="description" content="(.*?)"', h, re.S) or [None, ""])[1],
            schema=h.count('application/ld+json'),
            noindex="noindex" in h,
            liens={m for m in re.findall(r'href="(/[^"#?]*)"', h)},
        )
    return pages


def graphe(pages):
    """Profondeur de clic depuis l'accueil et pages orphelines."""
    entrants = {u: 0 for u in pages}
    for u, p in pages.items():
        for cible in p["liens"]:
            c = cible if cible.endswith("/") else cible + "/"
            if c in entrants and c != u:
                entrants[c] += 1
    prof, file = {"/": 0}, ["/"]
    while file:
        u = file.pop(0)
        for cible in pages.get(u, {}).get("liens", ()):
            c = cible if cible.endswith("/") else cible + "/"
            if c in pages and c not in prof:
                prof[c] = prof[u] + 1
                file.append(c)
    return entrants, prof


def instantane():
    pages = lire_pages()
    indexables = {u: p for u, p in pages.items() if not p["noindex"]}
    entrants, prof = graphe(pages)

    orphelines = sorted(u for u, n in entrants.items()
                        if n == 0 and u != "/" and not pages[u]["noindex"])
    profondes = sorted(u for u, d in prof.items() if d > PROFONDEUR_MAX)
    inatteignables = sorted(u for u in indexables if u not in prof)
    lourdes = sorted(((p["octets"] // 1024, u) for u, p in pages.items()
                      if p["octets"] > BUDGET_HTML_KO * 1024), reverse=True)
    minces = sorted(((p["mots"], u) for u, p in indexables.items()
                     if p["mots"] < MOTS_MINIMUM))
    sans_schema = sorted(u for u, p in indexables.items() if p["schema"] == 0)

    titres, desc = {}, {}
    for u, p in indexables.items():
        titres.setdefault(p["titre"], []).append(u)
        desc.setdefault(p["desc"], []).append(u)

    mots = [p["mots"] for p in indexables.values()] or [0]
    octets = [p["octets"] for p in pages.values()] or [0]

    return dict(
        date=datetime.date.today().isoformat(),
        pages=len(pages),
        indexables=len(indexables),
        mots_moyen=round(sum(mots) / len(mots)),
        mots_total=sum(mots),
        poids_moyen_ko=round(sum(octets) / len(octets) / 1024, 1),
        poids_max_ko=round(max(octets) / 1024, 1),
        profondeur_max=max(prof.values()) if prof else 0,
        orphelines=orphelines,
        profondes=profondes,
        inatteignables=inatteignables,
        lourdes=lourdes[:10],
        minces=minces[:10],
        sans_schema=sans_schema[:10],
        titres_doublons=[v for v in titres.values() if len(v) > 1][:5],
        desc_doublons=[v for v in desc.values() if len(v) > 1][:5],
    )


def comparer(now, avant):
    """Retourne (bloquants, avertissements)."""
    err, warn = [], []

    if avant:
        d = now["pages"] - avant["pages"]
        if d < -TOLERANCE_PAGES:
            err.append(f"{-d} page(s) ont disparu depuis le {avant['date']} "
                       f"({avant['pages']} → {now['pages']})")
        elif d > 0:
            warn.append(f"+{d} page(s) depuis le {avant['date']} — croissance normale")

        if avant["mots_moyen"]:
            var = (now["mots_moyen"] - avant["mots_moyen"]) / avant["mots_moyen"] * 100
            if var < TOLERANCE_MOTS:
                err.append(f"Volume rédactionnel moyen en baisse de {abs(var):.0f} % "
                           f"({avant['mots_moyen']} → {now['mots_moyen']} mots)")

        if avant["poids_moyen_ko"]:
            var = (now["poids_moyen_ko"] - avant["poids_moyen_ko"]) / avant["poids_moyen_ko"] * 100
            if var > TOLERANCE_POIDS:
                err.append(f"Poids moyen des pages en hausse de {var:.0f} % "
                           f"({avant['poids_moyen_ko']} → {now['poids_moyen_ko']} Ko)")

    if now["orphelines"]:
        err.append(f"{len(now['orphelines'])} page(s) orpheline(s) — aucun lien interne "
                   f"n'y mène : {', '.join(now['orphelines'][:3])}")
    if now["inatteignables"]:
        err.append(f"{len(now['inatteignables'])} page(s) inatteignable(s) depuis l'accueil")
    if now["titres_doublons"]:
        err.append(f"{len(now['titres_doublons'])} titre(s) en double")
    if now["sans_schema"]:
        err.append(f"{len(now['sans_schema'])} page(s) sans données structurées")

    if now["lourdes"]:
        warn.append(f"{len(now['lourdes'])} page(s) au-dessus de {BUDGET_HTML_KO} Ko "
                    f"(plus lourde : {now['lourdes'][0][0]} Ko)")
    if now["minces"]:
        warn.append(f"{len(now['minces'])} page(s) sous {MOTS_MINIMUM} mots "
                    f"(plus courte : {now['minces'][0][0]} mots)")
    if now["profondes"]:
        warn.append(f"{len(now['profondes'])} page(s) à plus de {PROFONDEUR_MAX} clics")
    if now["desc_doublons"]:
        warn.append(f"{len(now['desc_doublons'])} méta-description(s) en double")

    return err, warn


def ecrire_rapport(now, histo, err, warn):
    os.makedirs(os.path.dirname(RAPPORT), exist_ok=True)
    serie = (histo + [now])[-30:]
    lignes = "".join(
        f"<tr><td>{s['date']}</td><td>{s['pages']}</td><td>{s['mots_moyen']}</td>"
        f"<td>{s['poids_moyen_ko']} Ko</td><td>{len(s.get('orphelines', []))}</td></tr>"
        for s in reversed(serie))
    bloc = lambda t, items, cls: (
        f'<h2 class="{cls}">{t}</h2><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
        if items else f'<h2 class="ok">{t} — rien à signaler</h2>')
    html = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="robots" content="noindex,nofollow">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Veille SEO — {now['date']}</title>
<style>
 body{{font:15px/1.6 system-ui,sans-serif;max-width:60rem;margin:2rem auto;padding:0 1.2rem;
   background:#F7F4EC;color:#1E2E28}}
 h1{{font-size:1.6rem}} h2{{font-size:1.05rem;margin-top:2rem}}
 .ko{{color:#A8321F}} .warn{{color:#8A6320}} .ok{{color:#093F30}}
 table{{border-collapse:collapse;width:100%;margin-top:.8rem;background:#fff}}
 th,td{{border:1px solid #ddd;padding:.45rem .6rem;text-align:left;font-size:.9rem}}
 th{{background:#093F30;color:#fff}}
 .kpi{{display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0}}
 .kpi div{{background:#fff;border-top:3px solid #C09048;padding:.9rem 1.1rem;flex:1 1 8rem}}
 .kpi b{{display:block;font-size:1.5rem;color:#093F30}}
 .kpi span{{font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:#7C8B84}}
 code{{background:#fff;padding:.1rem .3rem}}
</style></head><body>
<h1>Veille SEO — {now['date']}</h1>
<div class="kpi">
 <div><span>Pages</span><b>{now['pages']}</b></div>
 <div><span>Indexables</span><b>{now['indexables']}</b></div>
 <div><span>Mots / page</span><b>{now['mots_moyen']}</b></div>
 <div><span>Poids moyen</span><b>{now['poids_moyen_ko']} Ko</b></div>
 <div><span>Profondeur max</span><b>{now['profondeur_max']}</b></div>
 <div><span>Mots au total</span><b>{now['mots_total']:,}</b></div>
</div>
{bloc("Régressions bloquantes", err, "ko")}
{bloc("Points de vigilance", warn, "warn")}
<h2>Historique</h2>
<table><tr><th>Date</th><th>Pages</th><th>Mots/page</th><th>Poids moyen</th><th>Orphelines</th></tr>
{lignes}</table>
<p style="margin-top:2rem;font-size:.85rem;color:#7C8B84">
Page non indexée. Générée par <code>veille_seo.py</code> à chaque build.</p>
</body></html>""".replace("{:,}".format(0), "")
    open(RAPPORT, "w", encoding="utf-8").write(html)


def main():
    init = "--init" in sys.argv
    histo = json.load(open(HISTO, encoding="utf-8")) if os.path.exists(HISTO) else []
    now = instantane()
    avant = histo[-1] if histo else None
    err, warn = comparer(now, None if init else avant)

    print(f"\nVeille SEO — {now['date']}")
    print("=" * 62)
    print(f"  {now['pages']} pages · {now['indexables']} indexables · "
          f"{now['mots_moyen']} mots/page · {now['poids_moyen_ko']} Ko/page · "
          f"profondeur max {now['profondeur_max']}")
    if avant:
        print(f"  Référence du {avant['date']} : {avant['pages']} pages · "
              f"{avant['mots_moyen']} mots/page · {avant['poids_moyen_ko']} Ko/page")
    print()
    for e in err:
        print(f"  RÉGRESSION  {e}")
    for w in warn:
        print(f"  vigilance   {w}")
    if not err and not warn:
        print("  Aucune régression, aucun point de vigilance.")

    ecrire_rapport(now, histo, err, warn)
    histo.append(now)
    json.dump(histo[-60:], open(HISTO, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    print("\n" + "=" * 62)
    print(f"{len(err)} régression(s), {len(warn)} vigilance(s) — "
          f"rapport dans site/_veille/\n")
    return 1 if (err and not init) else 0


if __name__ == "__main__":
    sys.exit(main())
