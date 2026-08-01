# -*- coding: utf-8 -*-
"""
FILE D'ATTENTE ÉDITORIALE.

Principe : chaque fichier de /contenus/*.md porte une date de publication.
Le build ne rend que les contenus dont la date est atteinte. L'action GitHub
tourne tous les matins : un nouveau contenu apparaît seul, le sitemap se met
à jour, le maillage interne se recalcule.

Le réservoir se remplit en une session, il se vide sur plusieurs mois.
Pour recharger : ajouter des fichiers .md, rien d'autre à toucher.
"""
import datetime, os, re

DOSSIER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "contenus")


def _parse(chemin):
    brut = open(chemin, encoding="utf-8").read()
    if not brut.startswith("---"):
        return None
    _, entete, corps = brut.split("---", 2)
    meta = {}
    for ligne in entete.strip().splitlines():
        if ":" in ligne:
            k, v = ligne.split(":", 1)
            meta[k.strip()] = v.strip()
    meta["corps"] = corps.strip()
    # le préfixe numérique sert à l'ordre des fichiers, pas à l'URL
    defaut = re.sub(r"^\d+-", "", os.path.basename(chemin)[:-3])
    meta["slug"] = meta.get("slug") or defaut
    for champ in ("liens", "tags", "sources"):
        meta[champ] = [x.strip() for x in meta.get(champ, "").split("|") if x.strip()]
    return meta


def sources_html(meta):
    """Bloc de sources. Format attendu : Nom~URL~date de vérification"""
    if not meta.get("sources"):
        return ""
    lis = []
    for s in meta["sources"]:
        p = [x.strip() for x in s.split("~")]
        nom, url = p[0], p[1] if len(p) > 1 else ""
        verif = f" — vérifié le {p[2]}" if len(p) > 2 else ""
        lis.append(f'<li><a href="{url}" rel="noopener">{nom}</a>{verif}</li>'
                   if url else f"<li>{nom}{verif}</li>")
    # id="sources" : cible de la barre de chapitres des guides
    return ('<div class="sources" id="sources"><h2>Sources</h2><ul>' + "".join(lis) +
            "</ul><p>Cette page s'appuie sur les textes en vigueur à la date "
            "indiquée. La réglementation évolue : en cas de doute sur une "
            "situation particulière, faites-la confirmer.</p></div>")


def charger(aujourdhui=None):
    """Contenus publiés à ce jour, du plus récent au plus ancien."""
    aujourdhui = aujourdhui or datetime.date.today()
    out = []
    if not os.path.isdir(DOSSIER):
        return out
    for f in sorted(os.listdir(DOSSIER)):
        if not f.endswith(".md"):
            continue
        m = _parse(os.path.join(DOSSIER, f))
        if not m:
            continue
        try:
            d = datetime.date.fromisoformat(m.get("publication", "1970-01-01"))
        except ValueError:
            continue
        if d <= aujourdhui:
            m["date"] = d
            out.append(m)
    return sorted(out, key=lambda x: x["date"], reverse=True)


def en_attente(aujourdhui=None):
    aujourdhui = aujourdhui or datetime.date.today()
    n = 0
    for f in os.listdir(DOSSIER) if os.path.isdir(DOSSIER) else []:
        if not f.endswith(".md"):
            continue
        m = _parse(os.path.join(DOSSIER, f))
        if m and datetime.date.fromisoformat(m.get("publication", "1970-01-01")) > aujourdhui:
            n += 1
    return n


def md_vers_html(texte):
    """Markdown minimal : titres, listes, gras, paragraphes. Zéro dépendance."""
    html, bloc = [], []

    def vider():
        if bloc:
            html.append("<p>" + " ".join(bloc) + "</p>")
            bloc.clear()

    liste = False
    tableau = False
    for ligne in texte.splitlines():
        l = ligne.rstrip()
        if not l.strip():
            vider()
            if liste:
                html.append("</ul>"); liste = False
            if tableau:
                html.append("</tbody></table></div>"); tableau = False
            continue
        if l.startswith("## "):
            vider()
            if liste: html.append("</ul>"); liste = False
            html.append(f"<h2>{l[3:].strip()}</h2>")
        elif l.startswith("### "):
            vider()
            if liste: html.append("</ul>"); liste = False
            html.append(f"<h3>{l[4:].strip()}</h3>")
        elif l.startswith("|"):
            vider()
            if liste:
                html.append("</ul>"); liste = False
            if set(l) <= set("|-: \t"):
                continue
            cellules = [c.strip() for c in l.strip("|").split("|")]
            if not tableau:
                html.append('<div class="tabwrap"><table class="tabsimple"><thead><tr>'
                            + "".join(f"<th>{c}</th>" for c in cellules)
                            + "</tr></thead><tbody>")
                tableau = True
            else:
                html.append("<tr>" + "".join(f"<td>{c}</td>" for c in cellules) + "</tr>")
        elif l.startswith("- "):
            vider()
            if not liste:
                html.append("<ul>"); liste = True
            html.append(f"<li>{l[2:].strip()}</li>")
        else:
            bloc.append(l.strip())
    vider()
    if liste:
        html.append("</ul>")
    if tableau:
        html.append("</tbody></table></div>")
    s = "\n".join(html)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s
