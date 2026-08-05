# -*- coding: utf-8 -*-
"""
GÉNÉRATEUR DE PDF, SANS AUCUNE DÉPENDANCE.

Le projet ne tolère aucune bibliothèque tierce : ni pour construire le site,
ni pour l'auditer. Ces fiches de pré-étude ne feront pas exception.

Un PDF est un format simple pour ce qu'on lui demande ici — du texte, des
filets, des aplats de couleur. On écrit donc les objets à la main : un
catalogue, des pages, un flux de contenu par page, et les polices standard
qu'aucun lecteur n'a besoin de télécharger.

Ce que ce module NE fait pas, volontairement : images, transparence,
polices embarquées, formulaires interactifs. Une fiche qui s'imprime et se
remplit au stylo n'en a pas besoin, et chacune de ces fonctions doublerait
la taille du code pour un gain nul.

    p = Pdf("Titre du document")
    p.titre("Repérage amiante avant travaux")
    p.para("Ce qu'il nous faut pour établir votre devis.")
    p.case("L'adresse précise de l'immeuble")
    p.ligne_a_remplir("Adresse")
    p.ecrire("chemin/vers/fichier.pdf")
"""

# --------------------------------------------------------------- constantes
# A4 en points typographiques (72 par pouce).
LARGEUR, HAUTEUR = 595.28, 841.89
MARGE = 48.0

# La charte du site, convertie en composantes de 0 à 1 comme l'exige le format.
VERT = (0x09 / 255, 0x3F / 255, 0x30 / 255)
VERT_PROFOND = (0x00 / 255, 0x29 / 255, 0x24 / 255)
OR = (0xC0 / 255, 0x90 / 255, 0x48 / 255)
OR_PALE = (0xEB / 255, 0xD9 / 255, 0xB8 / 255)
CREME = (0xFA / 255, 0xF8 / 255, 0xF3 / 255)
ENCRE = (0x1E / 255, 0x2E / 255, 0x28 / 255)
GRIS = (0.42, 0.45, 0.44)
FILET = (0.80, 0.82, 0.81)

# Largeur des caractères des polices standard, en millièmes de point. Sans
# elles, impossible de savoir où couper une ligne : le format ne mesure rien
# pour nous. Table réduite aux caractères qu'on écrit réellement.
_LARGEURS_HELV = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, "0": 556, "1": 556, "2": 556, "3": 556, "4": 556,
    "5": 556, "6": 556, "7": 556, "8": 556, "9": 556, ":": 278, ";": 278,
    "<": 584, "=": 584, ">": 584, "?": 556, "@": 1015, "[": 278, "\\": 278,
    "]": 278, "^": 469, "_": 556, "`": 333, "{": 334, "|": 260, "}": 334,
    "~": 584, "…": 1000, "’": 191, "«": 556, "»": 556, "—": 1000, "–": 556,
    "€": 556, "°": 400, "·": 350,
}
for _c, _w in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556,
                   833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667,
                   667, 611]):
    _LARGEURS_HELV[_c] = _w
for _c, _w in zip("abcdefghijklmnopqrstuvwxyz",
                  [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222,
                   833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500,
                   500, 500]):
    _LARGEURS_HELV[_c] = _w
# Les accents français prennent la largeur de leur lettre de base.
for _acc, _base in [("àâä", "a"), ("éèêë", "e"), ("îï", "i"), ("ôö", "o"),
                    ("ùûü", "u"), ("ç", "c"), ("ÀÂÄ", "A"), ("ÉÈÊË", "E"),
                    ("ÎÏ", "I"), ("ÔÖ", "O"), ("ÙÛÜ", "U"), ("Ç", "C"),
                    ("œ", "o"), ("Œ", "O")]:
    for _c in _acc:
        _LARGEURS_HELV[_c] = _LARGEURS_HELV[_base]


def _largeur(texte, taille, gras=False):
    """La largeur d'un texte, en points. Le gras est ~5 % plus large."""
    total = sum(_LARGEURS_HELV.get(c, 556) for c in texte)
    return total / 1000.0 * taille * (1.05 if gras else 1.0)


def _echapper(s):
    """Les parenthèses et l'antislash délimitent les chaînes : à protéger."""
    return s.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


def _encoder(s):
    """WinAnsi accepte les accents français ; le reste devient un point."""
    remplacements = {"’": "'", "‘": "'", "“": '"', "”": '"', "…": "...",
                     "—": "-", "–": "-", " ": " ", " ": " ",
                     "œ": "oe", "Œ": "OE", "€": "EUR", "·": "-"}
    for avant, apres in remplacements.items():
        s = s.replace(avant, apres)
    return s


class Pdf:
    """Un document. On empile des blocs, la page se coupe toute seule."""

    def __init__(self, titre_doc, sous_titre="", pied=""):
        self.titre_doc = titre_doc
        self.sous_titre = sous_titre
        self.pied = pied
        self.pages = []          # chaque page : liste d'instructions
        self.flux = []
        self.y = 0.0
        self._nouvelle_page()

    # ---------------------------------------------------------------- pages
    def _nouvelle_page(self):
        if self.flux:
            self.pages.append("".join(self.flux))
        self.flux = []
        self._bandeau()

    def _place(self, hauteur):
        """Assure qu'il reste la place demandée, sinon coupe la page."""
        if self.y - hauteur < MARGE + 34:
            self._nouvelle_page()

    # ------------------------------------------------------------ primitives
    def _rect(self, x, y, l, h, couleur):
        r, v, b = couleur
        self.flux.append(f"{r:.3f} {v:.3f} {b:.3f} rg {x:.1f} {y:.1f} "
                         f"{l:.1f} {h:.1f} re f\n")

    def _trait(self, x1, y1, x2, y2, couleur=FILET, epaisseur=0.6):
        r, v, b = couleur
        self.flux.append(f"{r:.3f} {v:.3f} {b:.3f} RG {epaisseur} w "
                         f"{x1:.1f} {y1:.1f} m {x2:.1f} {y2:.1f} l S\n")

    def _texte(self, x, y, s, taille=10, gras=False, couleur=ENCRE):
        r, v, b = couleur
        police = "/F2" if gras else "/F1"
        self.flux.append(
            f"BT {r:.3f} {v:.3f} {b:.3f} rg {police} {taille} Tf "
            f"{x:.1f} {y:.1f} Td ({_echapper(_encoder(s))}) Tj ET\n")

    def _couper(self, s, largeur_max, taille, gras=False):
        """Coupe un texte en lignes qui tiennent dans la largeur donnée."""
        mots, lignes, courante = _encoder(s).split(), [], ""
        for mot in mots:
            essai = (courante + " " + mot).strip()
            if _largeur(essai, taille, gras) <= largeur_max:
                courante = essai
            else:
                if courante:
                    lignes.append(courante)
                courante = mot
        if courante:
            lignes.append(courante)
        return lignes

    # --------------------------------------------------------------- entête
    def _bandeau(self):
        """Le bandeau de marque, en tête de chaque page."""
        h = 92.0
        self._rect(0, HAUTEUR - h, LARGEUR, h, VERT)
        self._rect(0, HAUTEUR - h - 3, LARGEUR, 3, OR)
        self._texte(MARGE, HAUTEUR - 44, "DGLM EXPERTISES", 17, True, CREME)
        self._texte(MARGE, HAUTEUR - 62, "L'expertise en action", 9.5, False, OR_PALE)
        # Coordonnées, alignées à droite
        for i, ligne in enumerate([
                "27 ter rue des Sables - 33320 Eysines",
                "06 07 35 15 05 - contact@dglmexpertises.fr",
                "www.dglmexpertises.fr"]):
            self._texte(LARGEUR - MARGE - _largeur(ligne, 8), HAUTEUR - 40 - i * 11,
                        ligne, 8, False, OR_PALE)
        self.y = HAUTEUR - h - 42

        if self.titre_doc:
            self._texte(MARGE, self.y, self.titre_doc, 15, True, VERT)
            self.y -= 17
        if self.sous_titre:
            for l in self._couper(self.sous_titre, LARGEUR - 2 * MARGE, 10):
                self._texte(MARGE, self.y, l, 10, False, GRIS)
                self.y -= 13
        self.y -= 12
        # Le titre ne se répète pas sur les pages suivantes.
        self.titre_doc = self.sous_titre = ""

    # ----------------------------------------------------------- composition
    def titre(self, s):
        self._place(46)
        self.y -= 8
        self._rect(MARGE, self.y - 5, 3, 17, OR)
        self._texte(MARGE + 11, self.y, s, 12, True, VERT)
        self.y -= 22

    def para(self, s, taille=9.8, couleur=ENCRE):
        for l in self._couper(s, LARGEUR - 2 * MARGE, taille):
            self._place(15)
            self._texte(MARGE, self.y, l, taille, False, couleur)
            self.y -= 13.5
        self.y -= 4

    def encadre(self, s):
        """Un bloc sur fond crème, pour ce qui doit être lu avant le reste."""
        lignes = self._couper(s, LARGEUR - 2 * MARGE - 24, 9.6)
        h = len(lignes) * 13 + 18
        self._place(h + 10)
        self._rect(MARGE, self.y - h + 12, LARGEUR - 2 * MARGE, h, CREME)
        self._rect(MARGE, self.y - h + 12, 3, h, OR)
        yy = self.y
        for l in lignes:
            self._texte(MARGE + 14, yy, l, 9.6, False, ENCRE)
            yy -= 13
        self.y -= h + 6

    def case(self, s):
        """Une case à cocher suivie de son libellé."""
        lignes = self._couper(s, LARGEUR - 2 * MARGE - 22, 9.8)
        self._place(len(lignes) * 13 + 6)
        self._trait(MARGE, self.y - 1, MARGE + 9.5, self.y - 1, GRIS, 0.7)
        self._trait(MARGE, self.y + 8.5, MARGE + 9.5, self.y + 8.5, GRIS, 0.7)
        self._trait(MARGE, self.y - 1, MARGE, self.y + 8.5, GRIS, 0.7)
        self._trait(MARGE + 9.5, self.y - 1, MARGE + 9.5, self.y + 8.5, GRIS, 0.7)
        for i, l in enumerate(lignes):
            self._texte(MARGE + 18, self.y - i * 13, l, 9.8)
        self.y -= len(lignes) * 13 + 3

    def ligne_a_remplir(self, libelle, largeur=None):
        """Un libellé suivi d'un filet, à remplir au stylo."""
        self._place(26)
        self._texte(MARGE, self.y, libelle, 8.6, False, GRIS)
        self.y -= 13
        fin = LARGEUR - MARGE if largeur is None else MARGE + largeur
        self._trait(MARGE, self.y, fin, self.y, FILET, 0.7)
        self.y -= 15

    def deux_lignes(self, gauche, droite):
        """Deux champs côte à côte, pour ne pas gâcher la hauteur."""
        self._place(26)
        mi = (LARGEUR - 2 * MARGE) / 2 - 10
        self._texte(MARGE, self.y, gauche, 8.6, False, GRIS)
        self._texte(MARGE + mi + 20, self.y, droite, 8.6, False, GRIS)
        self.y -= 13
        self._trait(MARGE, self.y, MARGE + mi, self.y, FILET, 0.7)
        self._trait(MARGE + mi + 20, self.y, LARGEUR - MARGE, self.y, FILET, 0.7)
        self.y -= 15

    def espace(self, h=10):
        self.y -= h

    # -------------------------------------------------------------- écriture
    def _pied_de_page(self, flux, num, total):
        r, v, b = GRIS
        y = MARGE - 12
        gauche = self.pied or "DGLM Expertises - SIRET 891 287 070 00025"
        droite = f"Page {num} sur {total}"
        flux += (f"{FILET[0]:.3f} {FILET[1]:.3f} {FILET[2]:.3f} RG 0.6 w "
                 f"{MARGE} {y + 14:.1f} m {LARGEUR - MARGE} {y + 14:.1f} l S\n")
        flux += (f"BT {r:.3f} {v:.3f} {b:.3f} rg /F1 7.5 Tf "
                 f"{MARGE} {y:.1f} Td ({_echapper(_encoder(gauche))}) Tj ET\n")
        flux += (f"BT {r:.3f} {v:.3f} {b:.3f} rg /F1 7.5 Tf "
                 f"{LARGEUR - MARGE - _largeur(droite, 7.5):.1f} {y:.1f} Td "
                 f"({_echapper(droite)}) Tj ET\n")
        return flux

    def ecrire(self, chemin):
        self.pages.append("".join(self.flux))
        total = len(self.pages)
        objets, n_page = [], len(self.pages)

        # 1 catalogue, 2 arbre de pages, puis 2 objets par page, puis 2 polices
        ids_pages = [3 + 2 * i for i in range(n_page)]
        id_f1, id_f2 = 3 + 2 * n_page, 4 + 2 * n_page

        objets.append("<< /Type /Catalog /Pages 2 0 R >>")
        kids = " ".join(f"{i} 0 R" for i in ids_pages)
        objets.append(f"<< /Type /Pages /Kids [{kids}] /Count {n_page} >>")

        for i, contenu in enumerate(self.pages):
            contenu = self._pied_de_page(contenu, i + 1, total)
            octets = contenu.encode("latin-1", "replace")
            objets.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {LARGEUR:.2f} "
                f"{HAUTEUR:.2f}] /Contents {ids_pages[i] + 1} 0 R /Resources "
                f"<< /Font << /F1 {id_f1} 0 R /F2 {id_f2} 0 R >> >> >>")
            objets.append(("STREAM", octets))

        objets.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
                      "/Encoding /WinAnsiEncoding >>")
        objets.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold "
                      "/Encoding /WinAnsiEncoding >>")

        sortie = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        positions = [0]
        for i, obj in enumerate(objets, start=1):
            positions.append(len(sortie))
            if isinstance(obj, tuple):
                octets = obj[1]
                sortie += f"{i} 0 obj\n<< /Length {len(octets)} >>\nstream\n".encode("latin-1")
                sortie += octets
                sortie += b"\nendstream\nendobj\n"
            else:
                sortie += f"{i} 0 obj\n{obj}\nendobj\n".encode("latin-1")

        debut_xref = len(sortie)
        sortie += f"xref\n0 {len(objets) + 1}\n".encode("latin-1")
        sortie += b"0000000000 65535 f \n"
        for pos in positions[1:]:
            sortie += f"{pos:010d} 00000 n \n".encode("latin-1")
        sortie += (f"trailer\n<< /Size {len(objets) + 1} /Root 1 0 R >>\n"
                   f"startxref\n{debut_xref}\n%%EOF\n").encode("latin-1")

        with open(chemin, "wb") as f:
            f.write(bytes(sortie))
        return len(sortie)
