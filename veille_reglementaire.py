#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VEILLE RÉGLEMENTAIRE.

Service Public affiche sur chaque fiche une date « Vérifié le ». Quand cette
date change, c'est que le texte a bougé — et que nos pages qui s'appuient
dessus doivent être relues.

Le script interroge les fiches surveillées, compare la date affichée à celle
enregistrée dans data/normes.py, et signale les écarts avec la liste des pages
du site à reprendre.

Il ne modifie rien : la relecture reste humaine, parce qu'un changement de date
ne dit pas ce qui a changé.

    python3 veille_reglementaire.py            # contrôle
    python3 veille_reglementaire.py --maj      # enregistre les nouvelles dates

Nécessite un accès réseau : il tourne dans l'action GitHub, pas en local hors ligne.
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.normes import FICHES_SURVEILLEES

BASE = "https://www.service-public.gouv.fr/particuliers/vosdroits/"
UA = {"User-Agent": "DGLM-veille-reglementaire/1.0 (+https://www.dglmexpertises.fr)"}

MOIS = {"janvier": "01", "février": "02", "mars": "03", "avril": "04", "mai": "05",
        "juin": "06", "juillet": "07", "août": "08", "septembre": "09",
        "octobre": "10", "novembre": "11", "décembre": "12"}


def date_iso(txt):
    """« Vérifié le 20 février 2026 » -> « 2026-02-20 »"""
    m = re.search(r"(\d{1,2})(?:er)?\s+(" + "|".join(MOIS) + r")\s+(\d{4})", txt)
    if not m:
        return ""
    return f"{m.group(3)}-{MOIS[m.group(2)]}-{int(m.group(1)):02d}"


def lire_fiche(code):
    """Retourne la date de vérification affichée par Service Public."""
    req = urllib.request.Request(BASE + code, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        html = r.read().decode("utf-8", "replace")
    # deux sources concordantes : la métadonnée et le texte visible
    meta = re.search(r'name="dc\.date\.modified"[^>]*content="([\d-]+)"', html)
    if meta:
        return meta.group(1)
    vis = re.search(r"Vérifié le[^<]{0,40}", html)
    return date_iso(vis.group(0)) if vis else ""


def main():
    maj = "--maj" in sys.argv
    ecarts, erreurs, inchange = [], [], 0

    print("\nVeille réglementaire — fiches Service Public")
    print("=" * 62)

    for code, f in FICHES_SURVEILLEES.items():
        try:
            trouvee = lire_fiche(code)
        except Exception as e:
            erreurs.append((code, f["nom"], str(e)[:60]))
            continue

        connue = f.get("verifie_le", "")
        if not connue:
            print(f"  {code}  {f['nom'][:42]:44s} date relevée : {trouvee or '?'}")
            if maj and trouvee:
                enregistrer(code, trouvee)
            continue

        if trouvee and trouvee != connue:
            ecarts.append((code, f, connue, trouvee))
            if maj:
                enregistrer(code, trouvee)
        else:
            inchange += 1

    print()
    for code, f, avant, apres in ecarts:
        print(f"  MISE À JOUR  {code} — {f['nom']}")
        print(f"               {avant}  ->  {apres}")
        if f["pages"]:
            print(f"               à relire : {', '.join(f['pages'])}")
        else:
            print("               aucune page du site ne s'appuie encore dessus")
    for code, nom, e in erreurs:
        print(f"  INJOIGNABLE  {code} — {nom} ({e})")
    if not ecarts and not erreurs:
        print(f"  {inchange} fiche(s) inchangée(s). Rien à relire.")

    print("\n" + "=" * 62)
    print(f"{len(ecarts)} évolution(s), {len(erreurs)} erreur(s) réseau")
    if ecarts and not maj:
        print("Relancer avec --maj pour enregistrer les nouvelles dates,")
        print("après avoir relu les pages concernées.\n")
    return 0 if not ecarts else 2


def enregistrer(code, date):
    """Réécrit la date dans data/normes.py, sans toucher au reste."""
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "normes.py")
    s = open(p, encoding="utf-8").read()
    motif = re.compile(rf'("{code}": dict\([^)]*?verifie_le=")([\d-]*)(")', re.S)
    if motif.search(s):
        s = motif.sub(rf"\g<1>{date}\g<3>", s, count=1)
        open(p, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    sys.exit(main())
