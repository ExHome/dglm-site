# -*- coding: utf-8 -*-
"""
SCHÉMAS EXPLICATIFS EN SVG — version épurée.

Règle de dessin : un schéma = UNE idée, cinq à huit textes maximum,
police 14 minimum dans un cadre de 800 (lisible une fois réduit
sur téléphone). Tout détail supplémentaire appartient à l'article,
pas au schéma.

Pourquoi du SVG plutôt que des images :
  - 2 à 6 Ko par schéma, net sur tous les écrans, imprimable en dossier d'AG
  - le texte est lu par Google et par les lecteurs d'écran
  - aucune requête réseau : le SVG est inline dans la page

Chaque schéma porte un <title> et un <desc> : restitués par les lecteurs
d'écran, indexés par les moteurs.
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


def _multi(x, y, lignes, taille, fill, poids="400", ancre="start", interligne=None):
    """Texte multiligne : lignes séparées par |."""
    it = interligne or taille + 7
    return "".join(
        f'<text x="{x}" y="{y + i*it}" text-anchor="{ancre}" font-size="{taille}" '
        f'font-weight="{poids}" fill="{fill}">{l}</text>'
        for i, l in enumerate(lignes.split("|")))


# ---------------------------------------------------------------- 1. quel repérage ?
def arbre_reperage():
    def ligne(y, question, sigle, reponse):
        return (
            f'<rect x="30" y="{y}" width="300" height="96" fill="#fff"/>'
            f'<rect x="30" y="{y}" width="4" height="96" fill="{OR}"/>'
            + _multi(56, y + 42, question, 17, V, "600")
            + f'<path d="M340,{y+48} L382,{y+48}" stroke="{OR}" stroke-width="2"/>'
            f'<path d="M376,{y+42} L386,{y+48} L376,{y+54}" fill="{OR}"/>'
            f'<rect x="396" y="{y}" width="374" height="96" fill="{V}"/>'
            f'<text x="422" y="{y+42}" font-size="21" font-weight="700" fill="{ORC}">{sigle}</text>'
            + _multi(422, y + 68, reponse, 14, "#F2EEE4"))

    c = f'''<rect width="800" height="460" fill="{CREME}"/>
<text x="30" y="46" font-size="20" font-weight="600" fill="{V}">Quel repérage pour votre chantier ?</text>
{ligne(76, "Travaux, rénovation", "RAAT", "Repérage sur le périmètre du chantier")}
{ligne(192, "Démolition totale", "RAAD", "Repérage exhaustif du bâtiment entier")}
{ligne(308, "Démolition partielle", "RAAD + RAAT", "L'un sur la partie déposée, l'autre sur le reste")}
<text x="30" y="442" font-size="14" fill="{GRIS}">Le dossier technique amiante (DTA) ne remplace aucun de ces repérages.</text>'''
    return _envelope(
        "Quel repérage amiante pour quel chantier",
        "Trois cas. Travaux ou rénovation : repérage amiante avant travaux, limité au "
        "périmètre du chantier. Démolition totale : repérage avant démolition, exhaustif, "
        "sur le bâtiment entier. Démolition partielle : repérage avant démolition sur la "
        "partie déposée et repérage avant travaux sur la partie conservée. Le dossier "
        "technique amiante ne remplace aucun de ces repérages.",
        c)


# ---------------------------------------------------------------- 2. listes A B C
def listes_amiante():
    def col(x, lettre, titre, exemples, doc, coul):
        return (
            f'<rect x="{x}" y="80" width="230" height="250" fill="#fff"/>'
            f'<rect x="{x}" y="80" width="230" height="5" fill="{coul}"/>'
            f'<text x="{x+22}" y="146" font-size="46" font-weight="700" fill="{coul}">{lettre}</text>'
            + _multi(x + 22, 184, titre, 15, V, "600")
            + _multi(x + 22, 236, exemples, 13.5, GRIS)
            + f'<rect x="{x}" y="284" width="230" height="46" fill="{CREME}"/>'
            f'<text x="{x+22}" y="312" font-size="14" font-weight="600" fill="{coul}">{doc}</text>')

    c = f'''<rect width="800" height="440" fill="{CREME}"/>
<text x="30" y="46" font-size="20" font-weight="600" fill="{V}">Amiante : les trois listes, en clair</text>
{col(30, "A", "Libèrent des fibres|tout seuls", "flocages,|calorifugeages", "DTA · RAAT", ALERTE)}
{col(285, "B", "Libèrent des fibres|si on y touche", "dalles de sol,|conduits, plaques", "DTA · RAAT", OR)}
{col(540, "C", "Invisibles|sans démonter", "colles, enduits,|matériaux noyés", "RAAT · RAAD seuls", V)}
<text x="30" y="384" font-size="15" font-weight="600" fill="{V}">La liste C n'apparaît jamais dans un dossier technique amiante.</text>
<text x="30" y="410" font-size="13.5" fill="{GRIS}">C'est la première cause de chantiers arrêtés en cours de route.</text>'''
    return _envelope(
        "Amiante : ce que couvrent les listes A, B et C",
        "Trois colonnes. Liste A, matériaux qui libèrent des fibres spontanément, comme "
        "les flocages et calorifugeages ; couverts par le dossier technique amiante et le "
        "repérage avant travaux. Liste B, matériaux qui libèrent des fibres si on les "
        "sollicite : dalles de sol, conduits, plaques ; mêmes documents. Liste C, "
        "matériaux invisibles sans démontage : colles, enduits, matériaux noyés ; couverts "
        "uniquement par les repérages avant travaux ou avant démolition. La liste C "
        "n'apparaît jamais dans un dossier technique amiante.",
        c, "0 0 800 440", "800/440")


# ---------------------------------------------------------------- 3. coupe d'immeuble
def coupe_immeuble():
    def point(y, n, titre, detail):
        return (
            f'<circle cx="316" cy="{y}" r="13" fill="{OR}"/>'
            f'<text x="316" y="{y+5}" text-anchor="middle" font-size="14" font-weight="700" fill="{VP}">{n}</text>'
            f'<text x="346" y="{y-2}" font-size="16.5" font-weight="600" fill="{V}">{titre}</text>'
            f'<text x="346" y="{y+20}" font-size="13.5" fill="{GRIS}">{detail}</text>')

    def badge(x, y, n):
        return (f'<circle cx="{x}" cy="{y}" r="11" fill="{OR}"/>'
                f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="12" '
                f'font-weight="700" fill="{VP}">{n}</text>')

    c = f'''<rect width="800" height="480" fill="{CREME}"/>
<text x="30" y="46" font-size="20" font-weight="600" fill="{V}">Où se loge l'amiante avant 1997</text>
<path d="M60,150 L155,92 L250,150 Z" fill="{V}"/>
<rect x="60" y="150" width="190" height="80" fill="#fff" stroke="{GRIS}" stroke-width=".8"/>
<rect x="60" y="230" width="190" height="80" fill="#fff" stroke="{GRIS}" stroke-width=".8"/>
<rect x="60" y="310" width="190" height="80" fill="#fff" stroke="{GRIS}" stroke-width=".8"/>
<rect x="60" y="390" width="190" height="52" fill="{VP}"/>
{badge(155, 118, 1)}{badge(78, 190, 2)}{badge(232, 270, 3)}{badge(78, 350, 4)}{badge(155, 416, 5)}
{point(120, 1, "Toiture", "plaques de couverture en fibres-ciment")}
{point(192, 2, "Façade", "bardages, mastics de vitrage")}
{point(264, 3, "Logements", "dalles de sol et leurs colles")}
{point(336, 4, "Gaines techniques", "conduits, flocages")}
{point(408, 5, "Sous-sol", "calorifugeages de chaufferie")}
<text x="30" y="466" font-size="13.5" fill="{GRIS}">Le mastic de vitrage (liste C) reste invisible tant que la fenêtre est en place.</text>'''
    return _envelope(
        "Où se loge l'amiante dans un immeuble d'avant 1997",
        "Coupe schématique d'un immeuble. Cinq emplacements typiques de matériaux "
        "amiantés : plaques de couverture en toiture, bardages et mastics de vitrage en "
        "façade, dalles de sol et colles dans les logements, conduits et flocages dans "
        "les gaines techniques, calorifugeages de chaufferie au sous-sol. Le mastic de "
        "vitrage, en liste C, reste invisible tant que la menuiserie est en place.",
        c, "0 0 800 480", "800/480")


# ---------------------------------------------------------------- 4. cycle PPPT
def cycle_pppt():
    etapes = [("Diagnostic", "l'état réel du bâti"),
              ("Programme", "dix ans de travaux, hiérarchisés et chiffrés"),
              ("Vote en assemblée générale", "budget et calendrier"),
              ("Travaux et fonds de travaux", "exécution échelonnée")]
    blocs = f'<line x1="66" y1="112" x2="66" y2="400" stroke="{OR}" stroke-width="1.6"/>'
    for i, (t, s) in enumerate(etapes):
        y = 112 + i * 96
        blocs += (
            f'<circle cx="66" cy="{y}" r="17" fill="{V}"/>'
            f'<text x="66" y="{y+5}" text-anchor="middle" font-size="14" font-weight="700" fill="{ORC}">{i+1}</text>'
            f'<text x="104" y="{y-1}" font-size="18" font-weight="600" fill="{V}">{t}</text>'
            f'<text x="104" y="{y+23}" font-size="14" fill="{GRIS}">{s}</text>')
    c = f'''<rect width="800" height="500" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">Le plan pluriannuel de travaux, en quatre temps</text>
{blocs}
<path d="M66,436 L66,458 L740,458 L740,112 L716,112" fill="none" stroke="{OR}"
 stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M724,106 L712,112 L724,118" fill="{OR}"/>
<text x="104" y="463" font-size="13.5" fill="{GRIS}">On remet le plan à jour tous les dix ans.</text>'''
    return _envelope(
        "Le cycle du plan pluriannuel de travaux",
        "Quatre temps en boucle. Un, le diagnostic de l'état réel du bâti. Deux, le "
        "programme : dix ans de travaux hiérarchisés et chiffrés. Trois, le vote en "
        "assemblée générale du budget et du calendrier. Quatre, les travaux et le fonds "
        "de travaux, avec une exécution échelonnée. Le plan est remis à jour tous les "
        "dix ans.",
        c, "0 0 800 500", "800/500")


# ---------------------------------------------------------------- 5. DTG vs PPPT
def dtg_vs_pppt():
    def face(x, titre, question, points, oblig, coul):
        return (
            f'<rect x="{x}" y="84" width="340" height="240" fill="#fff"/>'
            f'<rect x="{x}" y="84" width="340" height="5" fill="{coul}"/>'
            f'<text x="{x+24}" y="132" font-size="26" font-weight="700" fill="{coul}">{titre}</text>'
            f'<text x="{x+24}" y="162" font-size="14" font-style="italic" fill="{GRIS}">{question}</text>'
            + _multi(x + 24, 200, points, 14.5, V, interligne=27)
            + f'<rect x="{x}" y="278" width="340" height="46" fill="{CREME}"/>'
            + f'<text x="{x+24}" y="306" font-size="13" fill="{V}">{oblig}</text>')

    c = f'''<rect width="800" height="440" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">DTG ou PPPT : deux questions différentes</text>
{face(30, "DTG", "Dans quel état est l'immeuble ?",
      "— État des parties communes|— Équipements et obligations|— Estimation sommaire des coûts",
      "Obligatoire : mise en copropriété, insalubrité", V)}
{face(430, "PPPT", "Que fait-on, quand, avec quel argent ?",
      "— Travaux sur dix ans, hiérarchisés|— Échéancier et coût par poste|— Calibre le fonds de travaux",
      "Obligatoire : habitation de plus de 15 ans", OR)}
<text x="30" y="376" font-size="15" font-weight="600" fill="{V}">Un DTG complet vaut PPPT : une mission au lieu de deux.</text>
<text x="30" y="402" font-size="13.5" fill="{GRIS}">Les commander séparément coûte sensiblement plus cher.</text>'''
    return _envelope(
        "Diagnostic technique global ou plan pluriannuel de travaux",
        "Deux cartes. Le diagnostic technique global répond à la question : dans quel "
        "état est l'immeuble ? État des parties communes, équipements et obligations, "
        "estimation sommaire des coûts ; obligatoire en cas de mise en copropriété ou "
        "d'insalubrité. Le plan pluriannuel de travaux répond à la question : que "
        "fait-on, quand, avec quel argent ? Travaux sur dix ans hiérarchisés, échéancier "
        "et coût par poste, calibrage du fonds de travaux ; obligatoire pour toute "
        "copropriété d'habitation de plus de quinze ans. Un diagnostic technique global "
        "complet vaut plan pluriannuel de travaux : une mission au lieu de deux.",
        c, "0 0 800 440", "800/440")


SCHEMAS = {
    "arbre-reperage": arbre_reperage,
    "listes-amiante": listes_amiante,
    "coupe-immeuble": coupe_immeuble,
    "cycle-pppt": cycle_pppt,
    "dtg-vs-pppt": dtg_vs_pppt,
}


def rendre(cle):
    f = SCHEMAS.get(cle)
    return f() if f else ""
