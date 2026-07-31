# -*- coding: utf-8 -*-
"""
ILLUSTRATIONS AU TRAIT — registre planche d'architecte.

Des dessins SVG inline, en trait fin, dans les teintes de la marque.
Zéro photo de banque, zéro requête réseau : quelques kilo-octets qui
donnent au site une image sans trahir la charte.
Tous décoratifs : aria-hidden, jamais porteurs d'information.
"""

# ---------------------------------------------------------------- skyline
# Toits bordelais stylisés : échoppe, immeuble en pierre, flèche, chantier.
SKYLINE = """<svg class="skyline" viewBox="0 0 1200 250" aria-hidden="true" focusable="false">
<g fill="none" stroke="#D9B778" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
<!-- échoppe basse -->
<path d="M40,250 L40,170 L200,170 L200,250"/>
<path d="M32,170 L120,138 L208,170"/>
<rect x="66" y="192" width="30" height="58" rx="1"/>
<rect x="126" y="196" width="26" height="34" rx="1"/>
<line x1="120" y1="138" x2="120" y2="120"/><line x1="112" y1="120" x2="128" y2="120"/>
<!-- immeuble pierre 3 niveaux, balcons -->
<path d="M240,250 L240,96 L420,96 L420,250"/>
<line x1="232" y1="96" x2="428" y2="96"/>
<line x1="240" y1="146" x2="420" y2="146"/><line x1="240" y1="198" x2="420" y2="198"/>
<rect x="262" y="110" width="24" height="26"/><rect x="318" y="110" width="24" height="26"/><rect x="374" y="110" width="24" height="26"/>
<rect x="262" y="160" width="24" height="28"/><rect x="318" y="160" width="24" height="28"/><rect x="374" y="160" width="24" height="28"/>
<line x1="254" y1="160" x2="294" y2="160"/><line x1="310" y1="160" x2="350" y2="160"/><line x1="366" y1="160" x2="406" y2="160"/>
<rect x="262" y="212" width="24" height="38"/><rect x="318" y="212" width="24" height="38"/><rect x="374" y="212" width="24" height="38"/>
<!-- flèche (clocher) -->
<path d="M470,250 L470,120 L510,120 L510,250"/>
<path d="M470,120 L490,52 L510,120"/>
<line x1="490" y1="52" x2="490" y2="30"/>
<circle cx="490" cy="150" r="10"/>
<!-- immeuble haussmannien -->
<path d="M550,250 L550,80 L780,80 L780,250"/>
<path d="M550,80 L566,62 L764,62 L780,80"/>
<line x1="550" y1="128" x2="780" y2="128"/><line x1="550" y1="176" x2="780" y2="176"/><line x1="550" y1="222" x2="780" y2="222"/>
<rect x="572" y="94" width="22" height="24"/><rect x="622" y="94" width="22" height="24"/><rect x="672" y="94" width="22" height="24"/><rect x="722" y="94" width="22" height="24"/>
<rect x="572" y="140" width="22" height="26"/><rect x="622" y="140" width="22" height="26"/><rect x="672" y="140" width="22" height="26"/><rect x="722" y="140" width="22" height="26"/>
<rect x="572" y="188" width="22" height="24"/><rect x="622" y="188" width="22" height="24"/><rect x="672" y="188" width="22" height="24"/><rect x="722" y="188" width="22" height="24"/>
<!-- barre moderne -->
<path d="M820,250 L820,130 L980,130 L980,250"/>
<line x1="820" y1="160" x2="980" y2="160"/><line x1="820" y1="190" x2="980" y2="190"/><line x1="820" y1="220" x2="980" y2="220"/>
<line x1="860" y1="130" x2="860" y2="250"/><line x1="900" y1="130" x2="900" y2="250"/><line x1="940" y1="130" x2="940" y2="250"/>
<!-- grue de chantier -->
<line x1="1060" y1="250" x2="1060" y2="70"/>
<line x1="1000" y1="86" x2="1180" y2="86"/>
<path d="M1060,70 L1078,86"/><path d="M1060,70 L1042,86"/>
<line x1="1150" y1="86" x2="1150" y2="128"/><path d="M1140,128 L1160,128 L1150,142 Z"/>
<line x1="1014" y1="86" x2="1014" y2="104"/><rect x="1004" y="104" width="20" height="14"/>
</g></svg>"""

# ---------------------------------------------------------------- pictos mission
# Un trait, une idée. stroke=currentColor pour hériter de l'or des cartes.
_P = ('<svg class="picto" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
      '<g fill="none" stroke="currentColor" stroke-width="2.2" '
      'stroke-linecap="round" stroke-linejoin="round">{}</g></svg>')

PICTOS = {
    # RAAT : le mur en coupe, la loupe centrée dessus — on regarde DANS le mur
    # avant d'ouvrir. Les deux points : les fibres qu'on cherche.
    "RAAT": _P.format(
        '<line x1="25" y1="9" x2="25" y2="55"/><line x1="39" y1="9" x2="39" y2="55"/>'
        '<line x1="32" y1="9" x2="32" y2="55" stroke-dasharray="2.5 3.5"/>'
        '<circle cx="32" cy="30" r="13"/>'
        '<line x1="41.2" y1="39.2" x2="51" y2="49"/>'
        '<circle cx="28" cy="26" r="1.8" fill="currentColor" stroke="none"/>'
        '<circle cx="36" cy="34" r="1.8" fill="currentColor" stroke="none"/>'),
    # RAAD : la déconstruction bloc à bloc — le coin de l'immeuble est déjà
    # démonté, les blocs partent proprement (pas de boule : on repère AVANT).
    "RAAD": _P.format(
        '<line x1="8" y1="55" x2="56" y2="55"/>'
        '<path d="M12,55 L12,25 L28,25 L28,33 L36,33 L36,55"/>'
        '<line x1="10" y1="25" x2="30" y2="25"/>'
        '<rect x="16" y="31" width="6" height="7"/><rect x="16" y="43" width="6" height="7"/>'
        '<rect x="26" y="43" width="6" height="7"/>'
        '<rect x="33" y="14" width="7" height="7"/><rect x="43" y="20" width="6" height="6"/>'
        '<rect x="48" y="9" width="5" height="5"/>'),
    # DTG : l'immeuble sous la cote d'architecte — on prend la mesure complète
    # du bâti, du sol au toit.
    "DTG": _P.format(
        '<line x1="10" y1="55" x2="44" y2="55"/>'
        '<path d="M14,55 L14,13 L38,13 L38,55"/>'
        '<line x1="12" y1="13" x2="40" y2="13"/>'
        '<rect x="18" y="19" width="5" height="6"/><rect x="29" y="19" width="5" height="6"/>'
        '<rect x="18" y="31" width="5" height="6"/><rect x="29" y="31" width="5" height="6"/>'
        '<rect x="18" y="43" width="5" height="6"/><rect x="29" y="43" width="5" height="6"/>'
        '<line x1="50" y1="13" x2="50" y2="55"/>'
        '<path d="M47,17 L50,13 L53,17"/><path d="M47,51 L50,55 L53,51"/>'),
    # PPPT : l'immeuble au pied de l'escalier du plan — des marches qui montent
    # vers la flèche : les travaux s'échelonnent, l'immeuble progresse.
    "PPPT": _P.format(
        '<path d="M10,55 L10,27 L26,27 L26,55"/>'
        '<line x1="8" y1="27" x2="28" y2="27"/>'
        '<rect x="14" y="33" width="5" height="6"/><rect x="14" y="45" width="5" height="6"/>'
        '<path d="M8,55 L38,55 L38,45 L45,45 L45,35 L52,35 L52,25"/>'
        '<path d="M48,29 L52,25 L56,29"/>'),
}

# ---------------------------------------------------------------- échoppe
# La façade bordelaise type, en pied d'immeuble — pour le volet couverture.
ECHOPPE = """<svg class="illu-echoppe" viewBox="0 0 320 210" aria-hidden="true" focusable="false">
<g fill="none" stroke="#D9B778" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
<path d="M20,210 L20,74 L300,74 L300,210"/>
<path d="M12,74 L160,26 L308,74"/>
<line x1="160" y1="26" x2="160" y2="10"/><line x1="150" y1="10" x2="170" y2="10"/>
<rect x="44" y="96" width="52" height="114" rx="2"/>
<path d="M44,96 A26,26 0 0 1 96,96"/>
<rect x="130" y="100" width="60" height="64" rx="2"/>
<line x1="160" y1="100" x2="160" y2="164"/><line x1="130" y1="132" x2="190" y2="132"/>
<line x1="122" y1="170" x2="198" y2="170"/>
<rect x="224" y="100" width="52" height="64" rx="2"/>
<line x1="250" y1="100" x2="250" y2="164"/><line x1="224" y1="132" x2="276" y2="132"/>
<line x1="216" y1="170" x2="284" y2="170"/>
<line x1="20" y1="86" x2="300" y2="86"/>
</g></svg>"""


# ---------------------------------------------------------------- explainer animé
# Micro motion-design : quatre temps qui s'enchaînent en boucle (CSS .ax).
# Prefers-reduced-motion : tout s'affiche, rien ne bouge.
_AX_OR, _AX_V, _AX_G = "#C09048", "#093F30", "#7C8B84"

def _ax_temps(classe, num, icone, titre, sous):
    return (f'<g class="{classe}">'
            f'<text x="70" y="90" font-size="64" font-weight="700" fill="{_AX_OR}" opacity=".25">{num}</text>'
            f'{icone}'
            f'<text x="400" y="216" text-anchor="middle" font-size="23" font-weight="600" fill="{_AX_V}">{titre}</text>'
            f'<text x="400" y="247" text-anchor="middle" font-size="15" fill="{_AX_G}">{sous}</text></g>')

_AX_ICONES = [
    # visite : façade + loupe
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<path d="M355,168 L355,110 L415,110 L415,168"/><path d="M347,110 L385,84 L423,110"/>'
    f'<rect x="370" y="128" width="14" height="16"/>'
    f'<circle cx="440" cy="150" r="16"/><line x1="451" y1="161" x2="466" y2="176"/></g>',
    # prélèvement : tube + étiquette
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<path d="M385,86 L385,158 A15,15 0 0 0 415,158 L415,86"/><line x1="377" y1="86" x2="423" y2="86"/>'
    f'<line x1="385" y1="128" x2="415" y2="128"/><rect x="428" y="118" width="34" height="22"/></g>',
    # laboratoire : fiole
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<path d="M388,84 L388,120 L358,170 A12,12 0 0 0 368,188 L432,188 A12,12 0 0 0 442,170 L412,120 L412,84"/>'
    f'<line x1="380" y1="84" x2="420" y2="84"/><line x1="371" y1="152" x2="429" y2="152"/></g>',
    # rapport : document coché
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<path d="M362,80 L418,80 L438,100 L438,190 L362,190 Z"/><path d="M418,80 L418,100 L438,100"/>'
    f'<line x1="376" y1="120" x2="424" y2="120"/><line x1="376" y1="138" x2="424" y2="138"/>'
    f'<path d="M388,160 L398,172 L416,150"/></g>',
]

ANIM_MISSION = ('<figure class="animex"><svg viewBox="0 0 800 300" role="img" aria-labelledby="axt">'
    '<title id="axt">Une mission en quatre temps : visite sur site, prélèvements, analyses en '
    'laboratoire accrédité, rapport exploitable</title>'
    '<rect width="800" height="300" fill="#FFFFFF"/>'
    + _ax_temps("ax", "01", _AX_ICONES[0], "La visite, sur site", "On regarde partout — y compris là où personne ne va.")
    + _ax_temps("ax ax2", "02", _AX_ICONES[1], "Les prélèvements", "Chaque doute devient un échantillon référencé.")
    + _ax_temps("ax ax3", "03", _AX_ICONES[2], "Le laboratoire accrédité", "Les analyses tranchent : jamais de « présumé » par confort.")
    + _ax_temps("ax ax4", "04", _AX_ICONES[3], "Le rapport exploitable", "Localisé, chiffré, prêt pour l\u2019assemblée ou le chantier.")
    + f'<g fill="{_AX_G}"><circle cx="370" cy="278" r="4"/><circle cx="390" cy="278" r="4"/>'
    + f'<circle cx="410" cy="278" r="4"/><circle cx="430" cy="278" r="4"/></g>'
    '</svg></figure>')


# ---------------------------------------------------------------- PPPT animé
_PP_ICONES = [
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<path d="M362,180 L362,100 L410,100 L410,180"/><path d="M354,100 L386,78 L418,100"/>'
    f'<rect x="376" y="118" width="12" height="14"/><rect x="376" y="148" width="12" height="14"/>'
    f'<path d="M424,150 L434,162 L452,132"/></g>',
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<rect x="360" y="92" width="80" height="88" rx="3"/><line x1="360" y1="116" x2="440" y2="116"/>'
    f'<line x1="376" y1="84" x2="376" y2="100"/><line x1="424" y1="84" x2="424" y2="100"/>'
    f'<text x="400" y="160" text-anchor="middle" font-size="26" font-weight="700" fill="{_AX_V}" stroke="none">10</text></g>',
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<rect x="362" y="120" width="76" height="60" rx="3"/><line x1="382" y1="120" x2="400" y2="96"/>'
    f'<rect x="392" y="86" width="20" height="14"/><line x1="374" y1="150" x2="426" y2="150"/></g>',
    f'<g fill="none" stroke="{_AX_OR}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    f'<line x1="368" y1="184" x2="452" y2="184"/><line x1="380" y1="184" x2="380" y2="108"/>'
    f'<line x1="352" y1="118" x2="428" y2="98"/><line x1="420" y1="100" x2="420" y2="128"/>'
    f'<path d="M410,128 L430,128 L420,142 Z"/><circle cx="444" cy="164" r="12"/>'
    f'<text x="444" y="170" text-anchor="middle" font-size="13" font-weight="700" fill="{_AX_V}" stroke="none">€</text></g>',
]

ANIM_PPPT = ('<figure class="animex"><svg viewBox="0 0 800 300" role="img" aria-labelledby="axp">'
    '<title id="axp">Le plan pluriannuel de travaux en quatre temps : diagnostic, programme sur dix ans, '
    'vote en assemblée générale, travaux et fonds de travaux — remis à jour tous les dix ans</title>'
    '<rect width="800" height="300" fill="#FFFFFF"/>'
    + _ax_temps("ax", "01", _PP_ICONES[0], "Le diagnostic", "L\u2019état réel du bâti, poste par poste.")
    + _ax_temps("ax ax2", "02", _PP_ICONES[1], "Le programme sur dix ans", "Travaux hiérarchisés, chiffrés, échéancés.")
    + _ax_temps("ax ax3", "03", _PP_ICONES[2], "Le vote en assemblée", "Budget et calendrier décidés ensemble.")
    + _ax_temps("ax ax4", "04", _PP_ICONES[3], "Les travaux et le fonds", "Exécution échelonnée, épargne calibrée.")
    + f'<text x="400" y="284" text-anchor="middle" font-size="12.5" fill="{_AX_G}">Et l\u2019on remet le plan à jour tous les dix ans.</text>'
    '</svg></figure>')


# ---------------------------------------------------------------- DPE animé
_DPE_BARRES = [("A", "#00873C"), ("B", "#4CAF39"), ("C", "#AFCA31"),
               ("D", "#F5D520"), ("E", "#F0A029"), ("F", "#E2661B"), ("G", "#D02B1E")]

def _dpe_anim():
    b = ""
    for i, (l, coul) in enumerate(_DPE_BARRES):
        y = 78 + i * 27
        w = 150 + i * 40
        b += (f'<rect class="grow g{i}" x="60" y="{y}" width="{w}" height="21" fill="{coul}"/>'
              f'<text x="{60+w+14}" y="{y+16}" font-size="15" font-weight="700" fill="{coul}">{l}</text>')
    return b

ANIM_DPE = ('<figure class="animex"><svg viewBox="0 0 800 300" role="img" aria-labelledby="axd">'
    '<title id="axd">L\u2019étiquette énergie se remplit de A à G ; les logements G sont exclus de la '
    'location depuis 2025, F en 2028, E en 2034</title>'
    '<rect width="800" height="300" fill="#FFFFFF"/>'
    f'<text x="60" y="48" font-size="19" font-weight="600" fill="{_AX_V}">L\u2019étiquette de votre immeuble, de A à G</text>'
    + _dpe_anim()
    + f'<g class="axin"><text x="520" y="110" font-size="15" font-weight="600" fill="{_AX_V}">A à C — le parc performant</text>'
    + f'<text x="520" y="150" font-size="15" font-weight="600" fill="{_AX_V}">D et E — le milieu du parc</text>'
    + f'<text x="520" y="196" font-size="15" font-weight="700" fill="#D02B1E">F et G — « passoires »</text>'
    + f'<text x="520" y="220" font-size="13.5" fill="{_AX_G}">G exclu de la location depuis 2025,</text>'
    + f'<text x="520" y="240" font-size="13.5" fill="{_AX_G}">F en 2028, E en 2034.</text></g>'
    + f'<text x="60" y="286" font-size="12.5" fill="{_AX_G}">Le DPE collectif classe l\u2019immeuble entier — et guide le plan de travaux.</text>'
    '</svg></figure>')


# ------------------------------------------------- déperditions & ponts thermiques
# Coupe d'immeuble auto-suffisante : on comprend sans lire le texte de la page.
# Flèches rouges proportionnelles aux pertes (échelle 1,1 px par %), loupe sur le
# nez de dalle du balcon (LE pont thermique des copropriétés). Ordres de grandeur
# ADEME, immeuble collectif d'avant 1975 non isolé. Pulsation .depflux discrète,
# coupée par prefers-reduced-motion : le dessin statique est complet.
ANIM_DEPERDITIONS = '''<figure class="animex"><svg viewBox="0 0 800 560" role="img" aria-labelledby="axdp">
<title id="axdp">Coupe d’un immeuble collectif non isolé : la chaleur s’échappe par la toiture (30 %), les murs (25 %), le renouvellement d’air et les fuites (20 %), les fenêtres (13 %), les ponts thermiques — la dalle du balcon qui traverse le mur — (7 %) et le plancher bas (5 %)</title>
<rect width="800" height="560" fill="#FFFFFF"/>
<g fill="none" stroke="#C09048" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<path d="M140,470 L280,470 M480,470 L585,470"/>
<path d="M280,146 L280,180 M280,220 L280,288 M280,328 L280,396 M280,436 L280,512"/>
<path d="M290,146 L290,180 M290,220 L290,288 M290,328 L290,396 M290,436 L290,512"/>
<path d="M470,146 L470,198 M470,256 L470,512"/>
<path d="M480,146 L480,198 M480,256 L480,512"/>
<path d="M290,150 L470,150 M290,158 L470,158"/>
<path d="M290,248 L536,248 M290,256 L536,256 M536,248 L536,256"/>
<path d="M290,356 L470,356 M290,364 L470,364"/>
<path d="M290,464 L470,464 M290,472 L470,472"/>
<path d="M280,512 L480,512"/>
<path d="M266,144 L375,98 L494,144"/>
<path d="M436,121 L436,92 M452,128 L452,92 M431,92 L457,92"/>
<path d="M285,182 L285,218 M285,290 L285,326 M285,398 L285,434"/>
<path d="M278,180 L292,180 M278,220 L292,220 M278,288 L292,288 M278,328 L292,328 M278,396 L292,396 M278,436 L292,436"/>
<path d="M475,200 L475,240 M468,198 L482,198"/>
<path d="M534,246 L534,214 M482,214 L534,214 M508,214 L508,242"/>
</g>
<g fill="none" stroke="#C09048" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="490" cy="252" r="18"/>
<circle cx="665" cy="395" r="75"/>
<path d="M500,266 L612,342 M482,268 L596,370"/>
<path d="M648,330 L648,386 M648,404 L648,460 M664,330 L664,386 M664,404 L664,460"/>
<path d="M612,386 L724,386 M612,404 L724,404 M724,386 L724,404"/>
</g>
<g class="depflux" fill="#D02B1E">
<path d="M313.5,116 L313.5,78 L300,78 L330,50 L360,78 L346.5,78 L346.5,116 Z"/>
<path d="M433,92 L433,66 L425,66 L444,52 L463,66 L455,66 L455,92 Z"/>
<path d="M278,146.25 L230,146.25 L230,135 L204,160 L230,185 L230,173.75 L278,173.75 Z"/>
<path d="M278,300.85 L240,300.85 L240,295 L222,308 L240,321 L240,315.15 L278,315.15 Z"/>
<path d="M445.25,472 L445.25,492 L441.5,492 L448,505 L454.5,492 L450.75,492 L450.75,472 Z"/>
<path d="M538,248.15 L560,248.15 L560,244 L572,252 L560,260 L560,255.85 L538,255.85 Z"/>
<path d="M620,389 L700,389 L700,384 L716,395 L700,406 L700,401 L620,401 Z"/>
</g>
<text x="40" y="36" font-size="21" font-weight="700" fill="#093F30">Par où l’immeuble perd sa chaleur ?</text>
<text x="296" y="72" text-anchor="end" font-size="14" fill="#093F30">Toiture <tspan font-size="17" font-weight="700">30 %</tspan></text>
<text x="482" y="66" font-size="14" fill="#093F30">Air renouvelé et fuites <tspan font-size="17" font-weight="700">20 %</tspan></text>
<text x="188" y="165" text-anchor="end" font-size="14" fill="#093F30">Murs <tspan font-size="17" font-weight="700">25 %</tspan></text>
<text x="214" y="313" text-anchor="end" font-size="14" fill="#093F30">Fenêtres <tspan font-size="17" font-weight="700">13 %</tspan></text>
<text x="436" y="500" text-anchor="end" font-size="14" fill="#093F30">Plancher bas <tspan font-size="17" font-weight="700">5 %</tspan></text>
<text x="578" y="247" font-size="17" font-weight="700" fill="#093F30">7 %</text>
<text x="665" y="492" text-anchor="middle" font-size="14" fill="#093F30">Ponts thermiques <tspan font-size="17" font-weight="700">7 %</tspan></text>
<text x="665" y="513" text-anchor="middle" font-size="13" fill="#5B6A62">Le béton du balcon traverse le mur</text>
<text x="665" y="531" text-anchor="middle" font-size="13" fill="#5B6A62">et laisse filer la chaleur dehors.</text>
<text x="616" y="370" text-anchor="middle" font-size="13" fill="#5B6A62">dedans</text>
<text x="708" y="370" text-anchor="middle" font-size="13" fill="#5B6A62">dehors</text>
<text x="40" y="548" font-size="13" fill="#5B6A62">L’immeuble est vu en coupe · ordres de grandeur ADEME, immeuble collectif d’avant 1975 non isolé.</text>
</svg></figure>'''


# ---------------------------------------------------------------- pictos rubriques
# Un dessin au trait par rubrique des guides — même geste que les PICTOS missions.
_R = ('<svg class="picto picto--rub" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
      '<g fill="none" stroke="currentColor" stroke-width="2.2" '
      'stroke-linecap="round" stroke-linejoin="round">{}</g></svg>')

RUBRIQUE_PICTOS = {
    # Amiante : la plaque de fibrociment cadrée + l'étiquette d'échantillon
    # (chaque doute devient un prélèvement référencé).
    "Amiante": _R.format(
        '<path d="M10,26 L54,26 L54,50 L10,50 Z"/>'
        '<path d="M10,34 Q14,29 18,34 T26,34 T34,34 T42,34 T50,34"/>'
        '<path d="M10,43 Q14,38 18,43 T26,43 T34,43 T42,43 T50,43"/>'
        '<rect x="41" y="9" width="12" height="8"/>'
        '<line x1="47" y1="17" x2="51" y2="26"/>'),
    # Copropriété, DTG & PPPT : l'immeuble entier, un lot allumé — votre lot
    # dans la copropriété, parties communes autour.
    "Copropriété, DTG & PPPT": _R.format(
        '<line x1="8" y1="55" x2="56" y2="55"/>'
        '<path d="M14,55 L14,11 L50,11 L50,55"/>'
        '<line x1="12" y1="11" x2="52" y2="11"/>'
        '<path d="M28,55 L28,46 L36,46 L36,55"/>'
        '<rect x="19" y="17" width="6" height="7"/><rect x="30" y="17" width="6" height="7"/>'
        '<rect x="41" y="17" width="6" height="7"/>'
        '<rect x="19" y="29" width="6" height="7"/><rect x="41" y="29" width="6" height="7"/>'
        '<rect x="19" y="40" width="6" height="7"/><rect x="41" y="40" width="6" height="7"/>'
        '<rect x="30" y="29" width="6" height="7" fill="currentColor" stroke="none"/>'),
    # Performance énergétique : les trois flèches d'étiquette, de plus en plus
    # longues — la silhouette DPE reconnaissable entre toutes.
    "Performance énergétique": _R.format(
        '<path d="M10,12 L30,12 L36,17 L30,22 L10,22 Z"/>'
        '<path d="M10,27 L38,27 L44,32 L38,37 L10,37 Z"/>'
        '<path d="M10,42 L48,42 L54,47 L48,52 L10,52 Z"/>'),
    # Vente & location : le contrat au coin plié + la clé du logement.
    "Vente & location": _R.format(
        '<path d="M16,8 L38,8 L46,16 L46,56 L16,56 Z"/>'
        '<path d="M38,8 L38,16 L46,16"/>'
        '<circle cx="27" cy="28" r="5"/>'
        '<line x1="27" y1="33" x2="27" y2="46"/>'
        '<line x1="27" y1="42" x2="31" y2="42"/><line x1="27" y1="46" x2="32" y2="46"/>'),
    # Plomb, gaz & risques : le triangle de vigilance, exclamation affirmée.
    "Plomb, gaz & risques": _R.format(
        '<path d="M32,10 L55,50 L9,50 Z"/>'
        '<line x1="32" y1="24" x2="32" y2="37"/>'
        '<circle cx="32" cy="44" r="2.4" fill="currentColor" stroke="none"/>'),
    # Repères & définitions : le livre ouvert, marque-page dans la page.
    "Repères & définitions": _R.format(
        '<path d="M32,17 C27,12 17,12 11,15 L11,49 C17,46 27,46 32,51 C37,46 47,46 53,49 L53,15 C47,12 37,12 32,17 Z"/>'
        '<line x1="32" y1="17" x2="32" y2="51"/>'
        '<path d="M44,14 L44,25 L47.5,21.5 L51,25 L51,15"/>'),
}
