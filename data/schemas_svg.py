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


# ---------------------------------------------------------------- 6. DTA vs DAPP
def dta_vs_dapp():
    def carte(x, titre, qui, quoi, coul):
        return (f'<rect x="{x}" y="84" width="340" height="210" fill="#fff"/>'
                f'<rect x="{x}" y="84" width="340" height="5" fill="{coul}"/>'
                f'<text x="{x+24}" y="130" font-size="26" font-weight="700" fill="{coul}">{titre}</text>'
                + _multi(x + 24, 168, qui, 15, V, "600")
                + _multi(x + 24, 226, quoi, 14, GRIS, interligne=24))
    c = f'''<rect width="800" height="400" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">Amiante : qui est responsable de quoi ?</text>
{carte(30, "DTA", "Le syndic|pour les parties communes", "Listes A et B|Tenu à jour, fiche remise|aux occupants et entreprises", V)}
{carte(430, "DAPP", "Chaque propriétaire|pour son logement", "Liste A seulement|Flocages, calorifugeages,|faux-plafonds", OR)}
<text x="30" y="342" font-size="15" font-weight="600" fill="{V}">Deux documents, deux responsables — et aucun ne remplace le repérage avant travaux.</text>
<text x="30" y="368" font-size="13.5" fill="{GRIS}">Avant un chantier, le repérage avant travaux reste obligatoire dans les deux cas.</text>'''
    return _envelope(
        "DTA ou DAPP : qui est responsable de quoi",
        "Deux cartes. Le dossier technique amiante relève du syndic pour les parties "
        "communes : listes A et B, tenu à jour, fiche remise aux occupants et aux "
        "entreprises. Le diagnostic amiante des parties privatives relève de chaque "
        "propriétaire pour son logement : liste A seulement — flocages, calorifugeages, "
        "faux-plafonds. Aucun des deux ne remplace le repérage avant travaux.",
        c, "0 0 800 400", "800/400")


# ---------------------------------------------------------------- 7. calendrier DPE collectif
def calendrier_dpe():
    jalons = [("1er janvier 2024", "Plus de 200 lots"),
              ("1er janvier 2025", "De 51 à 200 lots"),
              ("1er janvier 2026", "50 lots et moins"),
              ("Aujourd'hui", "Toutes concernées")]
    blocs = f'<line x1="70" y1="120" x2="70" y2="384" stroke="{OR}" stroke-width="1.6"/>'
    for i, (d, t) in enumerate(jalons):
        y = 120 + i * 88
        em = (i == 3)
        blocs += (f'<circle cx="70" cy="{y}" r="9" fill="{OR if em else V}"/>'
                  f'<text x="104" y="{y-2}" font-size="17" font-weight="600" fill="{V}">{d}</text>'
                  f'<text x="104" y="{y+22}" font-size="14" fill="{GRIS}">{t}</text>')
    c = f'''<rect width="800" height="440" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">DPE collectif : le calendrier est arrivé à son terme</text>
<text x="30" y="76" font-size="14" fill="{GRIS}">Copropriétés d'habitation dont le permis de construire est antérieur à 2013.</text>
{blocs}
<text x="430" y="200" font-size="15" font-weight="600" fill="{V}">Validité : dix ans,</text>
<text x="430" y="224" font-size="14" fill="{GRIS}">sauf travaux modifiant la performance.</text>
<text x="430" y="266" font-size="15" font-weight="600" fill="{V}">Il porte sur l'immeuble entier,</text>
<text x="430" y="290" font-size="14" fill="{GRIS}">pas sur les lots individuels.</text>'''
    return _envelope(
        "Le calendrier du DPE collectif de copropriété",
        "Frise en quatre jalons. Premier janvier 2024 : copropriétés de plus de 200 "
        "lots. Premier janvier 2025 : de 51 à 200 lots. Premier janvier 2026 : 50 lots "
        "et moins. Aujourd'hui, toutes les copropriétés d'habitation dont le permis est "
        "antérieur à 2013 sont concernées. Validité de dix ans, sauf travaux modifiant "
        "la performance ; il porte sur l'immeuble entier, pas sur les lots.",
        c, "0 0 800 440", "800/440")


# ---------------------------------------------------------------- 8. DPE vs audit
def dpe_vs_audit():
    def carte(x, titre, verbe, quoi, coul):
        return (f'<rect x="{x}" y="84" width="340" height="200" fill="#fff"/>'
                f'<rect x="{x}" y="84" width="340" height="5" fill="{coul}"/>'
                + _multi(x + 24, 128, titre, 21, coul, "700")
                + f'<text x="{x+24}" y="182" font-size="16" font-style="italic" fill="{V}">{verbe}</text>'
                + _multi(x + 24, 216, quoi, 14, GRIS, interligne=24))
    c = f'''<rect width="800" height="392" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">DPE collectif ou audit énergétique ?</text>
{carte(30, "DPE collectif", "Il constate.", "L'étiquette de l'immeuble|C'est l'obligation légale", V)}
{carte(430, "Audit énergétique", "Il décide.", "Scénarios de travaux chiffrés|Volontaire — ouvre les aides", OR)}
<text x="30" y="334" font-size="15" font-weight="600" fill="{V}">Le premier vous classe, le second vous fait avancer.</text>
<text x="30" y="360" font-size="13.5" fill="{GRIS}">L'audit alimente directement le plan pluriannuel de travaux.</text>'''
    return _envelope(
        "DPE collectif ou audit énergétique : constater ou décider",
        "Deux cartes. Le DPE collectif constate : c'est l'étiquette énergétique de "
        "l'immeuble entier, et l'obligation légale. L'audit énergétique décide : "
        "scénarios de travaux chiffrés, démarche volontaire qui ouvre l'accès aux aides "
        "et alimente directement le plan pluriannuel de travaux.",
        c, "0 0 800 392", "800/392")


# ---------------------------------------------------------------- 9. CREP avant 1949
def crep_1949():
    def etape(x, n, titre, sub):
        return (f'<circle cx="{x}" cy="140" r="17" fill="{V}"/>'
                f'<text x="{x}" y="146" text-anchor="middle" font-size="14" font-weight="700" fill="{ORC}">{n}</text>'
                + _multi(x - 90, 190, titre, 15.5, V, "600", interligne=22)
                + _multi(x - 90, 240, sub, 13, GRIS, interligne=20))
    c = f'''<rect width="800" height="380" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">Plomb des parties communes : trois questions</text>
<line x1="130" y1="140" x2="670" y2="140" stroke="{OR}" stroke-width="1.6"/>
{etape(130, 1, "L'immeuble date|d'avant 1949 ?", "Peintures au plomb|possibles")}
{etape(400, 2, "On mesure,|sans rien casser", "Appareil à fluorescence X,|unité par unité")}
{etape(670, 3, "On classe|l'état des peintures", "Dégradé = protection|obligatoire avant travaux")}
<text x="30" y="352" font-size="14" fill="{GRIS}">Un constat sans plomb, ou avec revêtements en bon état, n'a pas à être renouvelé.</text>'''
    return _envelope(
        "Le constat plomb des parties communes en trois questions",
        "Trois étapes. Un : l'immeuble date-t-il d'avant 1949 ? Les peintures au plomb "
        "y sont possibles. Deux : on mesure sans rien casser, à l'appareil à "
        "fluorescence X, unité par unité. Trois : on classe l'état des peintures — un "
        "revêtement dégradé impose des protections avant travaux. Un constat sans plomb "
        "ou avec revêtements en bon état n'a pas à être renouvelé.",
        c, "0 0 800 380", "800/380")


# ---------------------------------------------------------------- 10. agents du bois
def agents_bois():
    def col(x, titre, sub, coul):
        return (f'<rect x="{x}" y="90" width="230" height="170" fill="#fff"/>'
                f'<rect x="{x}" y="90" width="230" height="5" fill="{coul}"/>'
                + _multi(x + 20, 132, titre, 17, coul, "700")
                + _multi(x + 20, 176, sub, 13.5, GRIS, interligne=22))
    c = f'''<rect width="800" height="380" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">Ce qui attaque le bois d'un immeuble</text>
{col(30, "Termites", "Galeries invisibles|Gironde et Landes|en zone délimitée", ALERTE)}
{col(285, "Insectes|xylophages", "Capricornes, vrillettes :|trous et sciure|dans les charpentes", OR)}
{col(540, "Mérule et|champignons", "Humidité persistante,|bois qui se délite|en cubes", V)}
<text x="30" y="316" font-size="15" font-weight="600" fill="{V}">L'état parasitaire les cherche tous — pas seulement les termites de la vente.</text>
<text x="30" y="342" font-size="13.5" fill="{GRIS}">Planchers, solives et charpentes sont examinés comme éléments porteurs.</text>'''
    return _envelope(
        "Termites, insectes xylophages, mérule : ce qui attaque le bois",
        "Trois colonnes. Les termites creusent des galeries invisibles — la Gironde et "
        "les Landes sont en zone délimitée par arrêté. Les insectes xylophages, "
        "capricornes et vrillettes, laissent trous et sciure dans les charpentes. La "
        "mérule et les champignons lignivores prospèrent sur l'humidité persistante et "
        "délitent le bois en cubes. L'état parasitaire recherche l'ensemble de ces "
        "agents, au-delà du seul contrôle termites exigé à la vente.",
        c, "0 0 800 380", "800/380")


# ---------------------------------------------------------------- 11. qui fait quoi
def qui_fait_quoi():
    def ligne(y, qui, quoi):
        return (f'<rect x="30" y="{y}" width="4" height="72" fill="{OR}"/>'
                f'<text x="56" y="{y+28}" font-size="17" font-weight="600" fill="{V}">{qui}</text>'
                f'<text x="56" y="{y+54}" font-size="14" fill="{GRIS}">{quoi}</text>')
    c = f'''<rect width="800" height="420" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">Qui contrôle quoi dans votre immeuble ?</text>
{ligne(84, "Le diagnostiqueur certifié — c'est nous", "Amiante, plomb, DTG, PPPT, DPE collectif, état parasitaire")}
{ligne(172, "L'organisme de contrôle agréé", "Installations collectives de gaz et d'électricité, ascenseurs")}
{ligne(260, "Le service public d'assainissement", "Conformité du raccordement au réseau")}
<text x="30" y="382" font-size="15" font-weight="600" fill="{V}">Ce n'est pas notre mission ? Nous vous orientons vers qui de droit.</text>
<text x="30" y="406" font-size="13.5" fill="{GRIS}">Et nous intégrons leurs conclusions au DTG et au plan pluriannuel de travaux.</text>'''
    return _envelope(
        "Qui contrôle quoi : diagnostiqueur, organisme agréé, collectivité",
        "Trois lignes. Le diagnostiqueur certifié — c'est notre métier — réalise "
        "amiante, plomb, diagnostic technique global, plan pluriannuel, DPE collectif "
        "et état parasitaire. L'organisme de contrôle agréé vérifie les installations "
        "collectives de gaz et d'électricité et les ascenseurs. Le service public "
        "d'assainissement contrôle la conformité du raccordement au réseau. Quand ce "
        "n'est pas notre mission, nous vous orientons vers qui de droit et intégrons "
        "leurs conclusions au DTG et au plan pluriannuel.",
        c, "0 0 800 420", "800/420")


# ---------------------------------------------------------------- 12. eaux séparées
def eaux_separatif():
    c = f'''<rect width="800" height="380" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">Assainissement : deux eaux, deux tuyaux</text>
<rect x="30" y="90" width="360" height="180" fill="#fff"/>
<rect x="30" y="90" width="360" height="5" fill="{V}"/>
<text x="54" y="132" font-size="17" font-weight="700" fill="{V}">Eaux usées</text>
{_multi(54, 168, "Cuisines, salles d'eau, WC|→ réseau public d'assainissement", 14, GRIS, interligne=24)}
<rect x="410" y="90" width="360" height="180" fill="#fff"/>
<rect x="410" y="90" width="360" height="5" fill="{OR}"/>
<text x="434" y="132" font-size="17" font-weight="700" fill="{OR}">Eaux pluviales</text>
{_multi(434, 168, "Toitures, cours, gouttières|→ jamais dans le même tuyau", 14, GRIS, interligne=24)}
<text x="30" y="316" font-size="15" font-weight="600" fill="{V}">Le contrôle vérifie que rien ne se mélange — et l'état des branchements.</text>
<text x="30" y="342" font-size="13.5" fill="{GRIS}">Sur le bâti d'avant 1970, les réseaux mélangés sont la règle plus que l'exception.</text>'''
    return _envelope(
        "Assainissement : eaux usées et eaux pluviales, deux réseaux séparés",
        "Deux cartes. Les eaux usées — cuisines, salles d'eau, WC — vont au réseau "
        "public d'assainissement. Les eaux pluviales — toitures, cours, gouttières — "
        "ne doivent jamais emprunter le même tuyau. Le contrôle de conformité vérifie "
        "que rien ne se mélange, et l'état des branchements. Sur le bâti d'avant 1970, "
        "les réseaux mélangés sont la règle plus que l'exception.",
        c, "0 0 800 380", "800/380")


# ---------------------------------------------------------------- 13. étiquette DPE
def etiquette_dpe():
    # Couleurs conventionnelles de l'étiquette énergie : repère universel.
    barres = [("A", "#00873C"), ("B", "#4CAF39"), ("C", "#AFCA31"),
              ("D", "#F5D520"), ("E", "#F0A029"), ("F", "#E2661B"), ("G", "#D02B1E")]
    blocs = ""
    for i, (l, coul) in enumerate(barres):
        y = 84 + i * 44
        w = 170 + i * 42
        blocs += (f'<rect x="40" y="{y}" width="{w}" height="36" fill="{coul}"/>'
                  f'<text x="{40+w-26}" y="{y+25}" font-size="19" font-weight="700" fill="#fff">{l}</text>')
    c = f'''<rect width="800" height="440" fill="{CREME}"/>
<text x="30" y="48" font-size="20" font-weight="600" fill="{V}">L'étiquette énergie, et ce qu'elle déclenche</text>
{blocs}
{_multi(520, 116, "A à C|le parc performant", 15, V, "600", interligne=22)}
{_multi(520, 208, "D et E|le milieu du parc", 15, V, "600", interligne=22)}
{_multi(520, 300, "F et G : « passoires »|G exclu de la location|depuis 2025, F en 2028,|E en 2034", 15, ALERTE, "600", interligne=22)}
<text x="30" y="420" font-size="13.5" fill="{GRIS}">En copropriété, le DPE collectif classe l'immeuble entier — et guide le plan de travaux.</text>'''
    return _envelope(
        "L'étiquette énergie de A à G, et ce qu'elle déclenche",
        "Étiquette énergie en sept barres, de A en vert à G en rouge. A à C : le parc "
        "performant. D et E : le milieu du parc. F et G, les « passoires thermiques » : "
        "les logements classés G sont exclus de la location depuis 2025, F le seront en "
        "2028 et E en 2034. En copropriété, le DPE collectif classe l'immeuble entier "
        "et guide le plan de travaux.",
        c, "0 0 800 440", "800/440")


SCHEMAS = {
    "arbre-reperage": arbre_reperage,
    "listes-amiante": listes_amiante,
    "coupe-immeuble": coupe_immeuble,
    "cycle-pppt": cycle_pppt,
    "dtg-vs-pppt": dtg_vs_pppt,
    "dta-vs-dapp": dta_vs_dapp,
    "calendrier-dpe": calendrier_dpe,
    "dpe-vs-audit": dpe_vs_audit,
    "crep-1949": crep_1949,
    "agents-bois": agents_bois,
    "qui-fait-quoi": qui_fait_quoi,
    "eaux-separatif": eaux_separatif,
    "etiquette-dpe": etiquette_dpe,
}


def rendre(cle):
    f = SCHEMAS.get(cle)
    return f() if f else ""
