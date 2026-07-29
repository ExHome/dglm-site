# -*- coding: utf-8 -*-
"""
SCHÉMAS EXPLICATIFS EN SVG.

Pourquoi du SVG plutôt que des images ou de la vidéo :
  - 2 à 6 Ko par schéma contre 200 Ko pour un PNG équivalent
  - net sur tous les écrans, y compris en impression de dossier d'AG
  - le texte à l'intérieur est lu par Google et par les lecteurs d'écran
  - aucune requête réseau : le SVG est inline dans la page
  - se recolore seul en mode sombre

Chaque schéma porte un <title> et un <desc> : c'est ce que restitue un lecteur
d'écran, et ce que Google indexe.
"""

V, VP, OR, ORC, CREME, GRIS, ALERTE = ("#093F30", "#002924", "#C09048",
                                        "#D9B778", "#F7F4EC", "#7C8B84", "#A8321F")

BASE = ('font-family="system-ui,-apple-system,Segoe UI,sans-serif"')


def _envelope(titre, desc, contenu, vb="0 0 800 460", ratio="800/460"):
    return f'''<figure class="schema">
<svg viewBox="{vb}" role="img" aria-labelledby="t{abs(hash(titre))%99999} d{abs(hash(desc))%99999}"
 style="aspect-ratio:{ratio}" {BASE}>
<title id="t{abs(hash(titre))%99999}">{titre}</title>
<desc id="d{abs(hash(desc))%99999}">{desc}</desc>
{contenu}
</svg>
<figcaption>{titre}</figcaption></figure>'''


# ---------------------------------------------------------------- 1. arbre de décision
def arbre_reperage():
    def boite(x, y, w, h, txt, fill, fg=CREME, taille=13, r=3):
        lignes = txt.split("|")
        dy = (h - len(lignes) * (taille + 4)) / 2 + taille
        t = "".join(f'<tspan x="{x+w/2}" dy="{taille+4 if i else 0}">{l}</tspan>'
                    for i, l in enumerate(lignes))
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"/>'
                f'<text x="{x+w/2}" y="{y+dy}" text-anchor="middle" font-size="{taille}" '
                f'fill="{fg}" font-weight="500">{t}</text>')

    def fleche(x1, y1, x2, y2, label=""):
        mid = (y1 + y2) / 2
        d = f"M{x1},{y1} L{x1},{mid} L{x2},{mid} L{x2},{y2-7}"
        lab = (f'<text x="{(x1+x2)/2}" y="{mid-6}" text-anchor="middle" font-size="11" '
               f'fill="{GRIS}">{label}</text>' if label else "")
        return (f'<path d="{d}" fill="none" stroke="{GRIS}" stroke-width="1.4"/>'
                f'<path d="M{x2-4},{y2-9} L{x2},{y2-3} L{x2+4},{y2-9}" fill="{GRIS}"/>{lab}')

    c = f'''<rect width="800" height="460" fill="{CREME}"/>
{boite(300, 18, 200, 46, "Quelle est la nature|de l'opération ?", V, taille=13)}
{fleche(400, 64, 150, 132, "démolition totale")}
{fleche(400, 64, 400, 132, "démolition partielle")}
{fleche(400, 64, 660, 132, "travaux, rénovation")}
{boite(50, 132, 200, 46, "Repérage avant|démolition (RAAD)", OR, VP)}
{boite(300, 132, 200, 46, "Les deux périmètres", ALERTE)}
{boite(560, 132, 200, 46, "Repérage avant|travaux (RAAT)", OR, VP)}
{fleche(150, 178, 150, 250)}
{fleche(400, 178, 400, 250)}
{fleche(660, 178, 660, 250)}
{boite(50, 250, 200, 62, "Bâtiment entier|Fondations, réseaux|Listes A, B et C", "#fff", V, 12)}
{boite(300, 250, 200, 62, "RAAD sur la partie déposée|RAAT sur la partie conservée|Listes A, B et C", "#fff", V, 12)}
{boite(560, 250, 200, 62, "Périmètre du chantier|Sondages destructifs|Listes A, B et C", "#fff", V, 12)}
<rect x="50" y="250" width="4" height="62" fill="{OR}"/>
<rect x="300" y="250" width="4" height="62" fill="{ALERTE}"/>
<rect x="560" y="250" width="4" height="62" fill="{OR}"/>
{fleche(400, 312, 400, 372)}
{boite(215, 372, 370, 52, "Dans tous les cas : diagnostic PEMD si le bâtiment dépasse|1 000 m² ou a accueilli des substances dangereuses", VP, ORC, 12)}
<text x="400" y="446" text-anchor="middle" font-size="11" fill="{GRIS}">Le dossier technique amiante ne dispense d'aucun de ces repérages.</text>'''
    return _envelope(
        "Quel repérage amiante pour quel chantier",
        "Arbre de décision. Démolition totale : repérage avant démolition, portant sur "
        "le bâtiment entier, fondations et réseaux compris. Démolition partielle : les "
        "deux périmètres, repérage avant démolition sur la partie déposée et repérage "
        "avant travaux sur la partie conservée. Travaux ou rénovation : repérage avant "
        "travaux limité au périmètre du chantier, avec sondages destructifs. Dans tous "
        "les cas, les listes A, B et C sont recherchées, et un diagnostic PEMD s'ajoute "
        "au-delà de 1 000 m² ou en présence de substances dangereuses.",
        c)


# ---------------------------------------------------------------- 2. listes A B C
def listes_amiante():
    def col(x, lettre, titre, items, doc, coul):
        lis = "".join(
            f'<text x="{x+16}" y="{150+i*22}" font-size="12.5" fill="{V}">• {it}</text>'
            for i, it in enumerate(items))
        return f'''<rect x="{x}" y="60" width="230" height="290" rx="3" fill="#fff"/>
<rect x="{x}" y="60" width="230" height="4" fill="{coul}"/>
<text x="{x+16}" y="97" font-size="30" font-weight="600" fill="{coul}">{lettre}</text>
<text x="{x+16}" y="122" font-size="12.5" font-weight="600" fill="{V}">{titre}</text>
{lis}
<rect x="{x}" y="300" width="230" height="50" fill="{CREME}"/>
<text x="{x+16}" y="322" font-size="10.5" fill="{GRIS}" letter-spacing="1.2">COUVERT PAR</text>
<text x="{x+16}" y="340" font-size="12" font-weight="600" fill="{coul}">{doc}</text>'''

    c = f'''<rect width="800" height="440" fill="{CREME}"/>
<text x="30" y="36" font-size="15" font-weight="600" fill="{V}">Les trois listes, et le document qui les couvre</text>
{col(30, "A", "Libèrent des fibres seules", ["Flocages", "Calorifugeages", "Faux-plafonds"], "DTA · DAPP · RAAT", ALERTE)}
{col(285, "B", "Libèrent si on les sollicite", ["Dalles de sol", "Conduits, canalisations", "Plaques, bardages", "Joints, tresses"], "DTA · RAAT", OR)}
{col(540, "C", "Invisibles sans destruction", ["Colles et mastics", "Enduits, ragréages", "Matériaux noyés", "Derrière cloisons"], "RAAT · RAAD seulement", V)}
<text x="400" y="392" text-anchor="middle" font-size="12.5" fill="{V}" font-weight="600">La liste C n'apparaît jamais dans un dossier technique amiante.</text>
<text x="400" y="414" text-anchor="middle" font-size="11.5" fill="{GRIS}">C'est l'origine de la majorité des chantiers arrêtés en cours d'exécution.</text>'''
    return _envelope(
        "Amiante : ce que couvrent les listes A, B et C",
        "Trois colonnes. Liste A, matériaux qui libèrent des fibres spontanément : "
        "flocages, calorifugeages, faux-plafonds ; couverts par le dossier technique "
        "amiante, le DAPP et le repérage avant travaux. Liste B, matériaux qui libèrent "
        "des fibres si on les sollicite : dalles de sol, conduits, plaques, joints ; "
        "couverts par le dossier technique amiante et le repérage avant travaux. "
        "Liste C, matériaux invisibles sans destruction : colles, mastics, enduits, "
        "matériaux noyés ; couverts uniquement par le repérage avant travaux ou avant "
        "démolition. La liste C n'apparaît jamais dans un dossier technique amiante.",
        c, "0 0 800 440", "800/440")


# ---------------------------------------------------------------- 3. coupe d'immeuble
def coupe_immeuble():
    def reperage(x, y, n, txt, ancre="start"):
        # au-dessus de la pastille quand le libellé est centré, à côté sinon
        if ancre == "middle":
            lx, ly = x, y - 16
        else:
            lx, ly = (x + 14, y + 4) if ancre == "start" else (x - 14, y + 4)
        return (f'<circle cx="{x}" cy="{y}" r="9" fill="{OR}"/>'
                f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="11" '
                f'font-weight="700" fill="{VP}">{n}</text>'
                f'<text x="{lx}" y="{ly}" text-anchor="{ancre}" font-size="12" '
                f'fill="{V}">{txt}</text>')

    etages = "".join(
        f'<rect x="250" y="{100+i*58}" width="300" height="54" fill="#fff" '
        f'stroke="{GRIS}" stroke-width=".8"/>'
        f'<rect x="268" y="{114+i*58}" width="38" height="26" fill="{CREME}" stroke="{GRIS}" stroke-width=".6"/>'
        f'<rect x="332" y="{114+i*58}" width="38" height="26" fill="{CREME}" stroke="{GRIS}" stroke-width=".6"/>'
        f'<rect x="430" y="{114+i*58}" width="38" height="26" fill="{CREME}" stroke="{GRIS}" stroke-width=".6"/>'
        f'<rect x="494" y="{114+i*58}" width="38" height="26" fill="{CREME}" stroke="{GRIS}" stroke-width=".6"/>'
        for i in range(4))
    c = f'''<rect width="800" height="440" fill="{CREME}"/>
<text x="30" y="34" font-size="15" font-weight="600" fill="{V}">Où se loge l'amiante dans un immeuble d'avant 1997</text>
<path d="M250,100 L400,52 L550,100 Z" fill="{V}"/>
{etages}
<rect x="250" y="332" width="300" height="56" fill="{VP}"/>
<text x="400" y="365" text-anchor="middle" font-size="12" fill="{ORC}">Sous-sol · chaufferie · caves</text>
<line x1="386" y1="100" x2="386" y2="332" stroke="{GRIS}" stroke-width="1" stroke-dasharray="4 3"/>
{reperage(400, 80, "1", "Plaques de couverture", "middle")}
{reperage(232, 128, "2", "Bardages, allèges", "end")}
{reperage(232, 244, "3", "Mastics de vitrage", "end")}
{reperage(568, 128, "4", "Dalles et colles de sol")}
{reperage(568, 244, "5", "Gaines et conduits")}
{reperage(568, 360, "6", "Calorifugeages de chaufferie")}
{reperage(232, 360, "7", "Faux-plafonds de hall", "end")}
<rect x="30" y="404" width="740" height="1" fill="{OR}"/>
<text x="30" y="428" font-size="11.5" fill="{GRIS}">1, 2, 4, 5 relèvent de la liste B — visibles. 3 relève de la liste C — invisible tant que la menuiserie est en place.</text>'''
    return _envelope(
        "Où se loge l'amiante dans un immeuble d'avant 1997",
        "Coupe schématique d'un immeuble de quatre étages sur sous-sol. Sept "
        "emplacements typiques de matériaux amiantés : plaques de couverture en toiture, "
        "bardages et allèges en façade, mastics de vitrage aux menuiseries, dalles et "
        "colles de sol dans les logements, gaines et conduits techniques, calorifugeages "
        "en chaufferie, faux-plafonds dans le hall. Les mastics de vitrage relèvent de la "
        "liste C : ils restent invisibles tant que la menuiserie est en place.",
        c, "0 0 800 440", "800/440")


# ---------------------------------------------------------------- 4. cycle PPPT
def cycle_pppt():
    etapes = [("Diagnostic", "État réel du bâti"), ("Programmation", "Dix ans, hiérarchisés"),
              ("Vote en AG", "Budget et calendrier"), ("Fonds de travaux", "Cotisation calibrée"),
              ("Travaux", "Exécution échelonnée"), ("Mise à jour", "Avant chaque vote")]
    n = len(etapes)
    seg = 740 / n
    blocs = ""
    for i, (t, s) in enumerate(etapes):
        x = 30 + i * seg
        blocs += (f'<rect x="{x}" y="120" width="{seg-12}" height="86" rx="3" fill="#fff"/>'
                  f'<rect x="{x}" y="120" width="{seg-12}" height="3" fill="{OR}"/>'
                  f'<text x="{x+14}" y="148" font-size="11" fill="{OR}" font-weight="700">0{i+1}</text>'
                  f'<text x="{x+14}" y="172" font-size="12.5" font-weight="600" fill="{V}">{t}</text>'
                  f'<text x="{x+14}" y="192" font-size="11" fill="{GRIS}">{s}</text>')
        if i < n - 1:
            xa = x + seg - 10
            blocs += (f'<path d="M{xa},163 L{xa+6},163" stroke="{OR}" stroke-width="1.5"/>'
                      f'<path d="M{xa+3},160 L{xa+7},163 L{xa+3},166" fill="{OR}"/>')
    c = f'''<rect width="800" height="300" fill="{CREME}"/>
<text x="30" y="40" font-size="15" font-weight="600" fill="{V}">Le cycle du plan pluriannuel de travaux</text>
<text x="30" y="64" font-size="12" fill="{GRIS}">Un cycle de dix ans, avec une mise à jour obligatoire avant chaque vote de travaux.</text>
{blocs}
<path d="M{30+seg*(n-0.5)-6},226 L{30+seg*(n-0.5)-6},252 L{30+seg*0.5},252 L{30+seg*0.5},212"
 fill="none" stroke="{OR}" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M{30+seg*0.5-4},218 L{30+seg*0.5},210 L{30+seg*0.5+4},218" fill="{OR}"/>
<text x="400" y="272" text-anchor="middle" font-size="11.5" fill="{GRIS}">Retour au diagnostic tous les dix ans</text>'''
    return _envelope(
        "Le cycle du plan pluriannuel de travaux",
        "Six étapes en boucle. Diagnostic de l'état réel du bâti, puis programmation "
        "hiérarchisée sur dix ans, vote en assemblée générale du budget et du calendrier, "
        "calibrage de la cotisation au fonds de travaux, exécution échelonnée des travaux, "
        "et mise à jour obligatoire avant chaque nouveau vote. Le cycle recommence au "
        "diagnostic tous les dix ans.",
        c, "0 0 800 300", "800/300")


# ---------------------------------------------------------------- 5. DTG vs PPPT
def dtg_vs_pppt():
    def face(x, titre, question, points, obligatoire, coul):
        lis = "".join(f'<text x="{x+18}" y="{158+i*24}" font-size="12.5" fill="{V}">— {p}</text>'
                      for i, p in enumerate(points))
        return f'''<rect x="{x}" y="66" width="340" height="270" rx="3" fill="#fff"/>
<rect x="{x}" y="66" width="340" height="4" fill="{coul}"/>
<text x="{x+18}" y="100" font-size="17" font-weight="600" fill="{coul}">{titre}</text>
<text x="{x+18}" y="128" font-size="12.5" font-style="italic" fill="{GRIS}">{question}</text>
{lis}
<rect x="{x+18}" y="286" width="304" height="34" fill="{CREME}"/>
<text x="{x+30}" y="308" font-size="11.5" fill="{V}">{obligatoire}</text>'''
    c = f'''<rect width="800" height="420" fill="{CREME}"/>
<text x="30" y="40" font-size="15" font-weight="600" fill="{V}">Diagnostic technique global ou plan pluriannuel de travaux</text>
{face(30, "DTG", "Dans quel état est notre immeuble ?", ["État apparent des parties communes", "État des équipements communs", "Analyse des améliorations possibles", "Estimation sommaire des coûts", "Situation au regard des obligations"], "Obligatoire : mise en copropriété, insalubrité", V)}
{face(430, "PPPT", "Que fait-on, dans quel ordre, avec quel argent ?", ["Liste des travaux sur dix ans", "Hiérarchisation par urgence", "Échéancier de réalisation", "Estimation du coût de chaque poste", "Calibrage du fonds de travaux"], "Obligatoire : toute copropriété de plus de 15 ans", OR)}
<text x="400" y="368" text-anchor="middle" font-size="12.5" font-weight="600" fill="{V}">Un DTG complet, comportant le volet de programmation, vaut PPPT.</text>
<text x="400" y="392" text-anchor="middle" font-size="11.5" fill="{GRIS}">Les faire réaliser séparément coûte sensiblement plus cher.</text>'''
    return _envelope(
        "Diagnostic technique global ou plan pluriannuel de travaux",
        "Comparaison en deux colonnes. Le diagnostic technique global répond à la "
        "question de l'état de l'immeuble : état apparent des parties communes et des "
        "équipements, analyse des améliorations possibles, estimation sommaire des coûts, "
        "situation au regard des obligations. Il est obligatoire en cas de mise en "
        "copropriété ou de procédure d'insalubrité. Le plan pluriannuel de travaux répond à la "
        "question du programme : liste des travaux sur dix ans, hiérarchisation, "
        "échéancier, estimation par poste, calibrage du fonds de travaux. Il est "
        "obligatoire pour toute copropriété de plus de quinze ans. Un diagnostic technique "
        "global complet, comportant le volet de programmation, vaut plan pluriannuel.",
        c, "0 0 800 420", "800/420")


SCHEMAS = {
    "arbre-reperage": arbre_reperage,
    "listes-amiante": listes_amiante,
    "coupe-immeuble": coupe_immeuble,
    "cycle-pppt": cycle_pppt,
    "dtg-vs-pppt": dtg_vs_pppt,
}


def rendre(cle):
    return SCHEMAS[cle]() if cle in SCHEMAS else ""
