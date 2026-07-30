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
    # RAAT : façade + loupe (on cherche avant d'ouvrir)
    "RAAT": _P.format(
        '<path d="M10,54 L10,22 L34,22 L34,54"/>'
        '<path d="M6,22 L22,10 L38,22"/>'
        '<rect x="16" y="30" width="8" height="9"/>'
        '<circle cx="44" cy="40" r="10"/><line x1="51" y1="47" x2="58" y2="54"/>'),
    # RAAD : bâtiment + boule de démolition
    "RAAD": _P.format(
        '<path d="M14,54 L14,16 L38,16 L38,54"/>'
        '<line x1="14" y1="28" x2="38" y2="28"/><line x1="14" y1="40" x2="38" y2="40"/>'
        '<line x1="50" y1="10" x2="50" y2="30"/><circle cx="50" cy="37" r="7"/>'
        '<path d="M38,16 L50,10"/>'),
    # DTG : immeuble + liste cochée
    "DTG": _P.format(
        '<path d="M10,54 L10,14 L30,14 L30,54"/>'
        '<rect x="15" y="20" width="4" height="5"/><rect x="23" y="20" width="4" height="5"/>'
        '<rect x="15" y="31" width="4" height="5"/><rect x="23" y="31" width="4" height="5"/>'
        '<line x1="40" y1="22" x2="56" y2="22"/><line x1="40" y1="32" x2="56" y2="32"/>'
        '<line x1="40" y1="42" x2="56" y2="42"/><path d="M35,20 L37,23 L40,17"/>'),
    # PPPT : immeuble + calendrier décennal
    "PPPT": _P.format(
        '<path d="M8,54 L8,18 L26,18 L26,54"/>'
        '<line x1="8" y1="30" x2="26" y2="30"/><line x1="8" y1="42" x2="26" y2="42"/>'
        '<rect x="34" y="18" width="24" height="24" rx="2"/>'
        '<line x1="34" y1="26" x2="58" y2="26"/>'
        '<line x1="40" y1="14" x2="40" y2="20"/><line x1="52" y1="14" x2="52" y2="20"/>'
        '<path d="M40,33 L44,37 L52,30"/>'),
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
