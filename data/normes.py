# -*- coding: utf-8 -*-
"""
RÉFÉRENTIEL DES NORMES ET TEXTES.

Pour chaque diagnostic : la norme AFNOR qui fixe la méthode, l'arrêté qui la
rend opposable, et l'article de code qui crée l'obligation. Personne ne publie
ça sous forme lisible — c'est ce que cherchent les maîtres d'ouvrage, les
architectes et les entreprises, et c'est ce qui attire les liens.

Le champ `confiance` pilote l'affichage :
  "verifie"  — source primaire consultée, date de consultation renseignée
  "etabli"   — référence de place, stable, non revérifiée à la source
  "a_verifier" — à confirmer avant publication

Le contrôle veille_reglementaire.py surveille les fiches Service Public et
signale toute mise à jour de leur date « Vérifié le ».
"""

CONSULTE_LE = "28 juillet 2026"

NORMES = [
    dict(
        cle="raat", confiance="verifie",
        nom="Repérage amiante avant travaux",
        sigle="RAAT",
        obligation="Code du travail, articles R. 4412-97 à R. 4412-97-6",
        decret="Décret n° 2017-899 du 9 mai 2017, modifié par le décret "
               "n° 2019-251 du 27 mars 2019",
        arrete="Arrêté du 16 juillet 2019, entré en vigueur le 19 juillet 2019",
        norme="NF X 46-020 : août 2017",
        norme_titre="Repérage amiante — Repérage des matériaux et produits contenant "
                    "de l'amiante dans les immeubles bâtis — Mission et méthodologie",
        note="La mise en œuvre de la norme est réputée satisfaire à l'arrêté, sauf "
             "pour ses articles 4, 7, 11 et 14. La liste minimale des matériaux à "
             "rechercher est fixée par le tableau A1 de la norme, en fonction du "
             "programme détaillé des travaux communiqué par le donneur d'ordre.",
        piege="L'opérateur transmet au donneur d'ordre le périmètre et le programme "
              "de repérage pour avis, avant toute investigation sur site. Un rapport "
              "établi sans cette étape est contestable.",
        lien="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038777498/",
    ),
    dict(
        cle="raad", confiance="verifie",
        nom="Repérage amiante avant démolition",
        sigle="RAAD",
        obligation="Code du travail, articles R. 4412-97 à R. 4412-97-6",
        decret="Décret n° 2017-899 du 9 mai 2017 modifié",
        arrete="Arrêté du 16 juillet 2019",
        norme="NF X 46-020 : août 2017",
        norme_titre="Même référentiel que le repérage avant travaux, appliqué à un "
                    "périmètre exhaustif",
        note="Un repérage avant démolition conduit selon la NF X 46-020 d'août 2017 "
             "vaut repérage avant travaux : son périmètre étant plus large, il couvre "
             "les besoins du repérage ciblé.",
        piege="L'inverse est faux. Un repérage avant travaux ne peut jamais tenir "
              "lieu de repérage avant démolition.",
        lien="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038777498/",
    ),
    dict(
        cle="raat-autres", confiance="verifie",
        nom="Repérage amiante — installations, structures et équipements",
        sigle="NF X 46-100",
        obligation="Code du travail, articles R. 4412-97 et suivants",
        decret="Décret n° 2017-899 du 9 mai 2017 modifié",
        arrete="Arrêté du 22 juillet 2021",
        norme="NF X 46-100",
        norme_titre="Repérage avant travaux sur les installations, structures ou "
                    "équipements concourant à la réalisation d'une activité",
        note="Domaine distinct de l'immeuble bâti. Concerne les process industriels, "
             "les équipements de production, les structures techniques.",
        piege="Sur un site industriel, le bâti et le process relèvent de deux domaines "
              "et de deux référentiels différents. Une seule mission ne couvre pas les "
              "deux.",
        lien="",
    ),
    dict(
        cle="dta", confiance="etabli",
        nom="Dossier technique amiante",
        sigle="DTA",
        obligation="Code de la santé publique, articles R. 1334-14 et suivants",
        decret="—",
        arrete="Arrêtés d'application relatifs au repérage et à l'évaluation "
               "périodique de l'état de conservation",
        norme="NF X 46-020",
        norme_titre="Repérage des matériaux des listes A et B, sans investigation "
                    "destructive",
        note="Document de gestion permanente du bâtiment, tenu à jour par le "
             "propriétaire. Sa fiche récapitulative est remise à toute entreprise "
             "appelée à intervenir.",
        piege="Le DTA ne couvre jamais la liste C. Il ne dispense donc d'aucun "
              "repérage avant travaux.",
        lien="",
    ),
    dict(
        cle="crep", confiance="etabli",
        nom="Constat de risque d'exposition au plomb",
        sigle="CREP",
        obligation="Code de la santé publique, articles L. 1334-5 et suivants",
        decret="—",
        arrete="Arrêtés relatifs au protocole de réalisation du constat",
        norme="NF X 46-030 : avril 2008",
        norme_titre="Diagnostic plomb — Protocole de réalisation du constat de risque "
                    "d'exposition au plomb",
        note="Deux normes complémentaires encadrent les analyses : NF X 46-031 pour "
             "l'analyse chimique des peintures, NF X 46-032 pour la mesure du plomb "
             "dans les poussières au sol.",
        piege="La mesure se fait par fluorescence X sur site. Les prélèvements ne "
              "sont utilisés qu'en cas d'impossibilité de mesure directe.",
        lien="",
    ),
    dict(
        cle="termites", confiance="verifie",
        nom="État relatif à la présence de termites",
        sigle="Termites",
        obligation="Code de la construction et de l'habitation, articles L. 126-4 "
                   "et suivants",
        decret="—",
        arrete="Arrêté du 29 mars 2007, modifié par l'arrêté du 7 mars 2012",
        norme="NF P03-201 : février 2016 (version AFNOR en vigueur)",
        norme_titre="Diagnostic technique — État du bâtiment relatif à la présence "
                    "de termites",
        note="L'obligation ne s'applique que dans les zones délimitées par arrêté "
             "préfectoral. La Gironde fait l'objet d'un arrêté de longue date.",
        piege="Décalage à connaître : l'arrêté du 7 mars 2012 vise nommément la norme "
              "NF P03-201 de mars 2012, alors que l'AFNOR l'a remplacée par la version "
              "de février 2016. Aucun arrêté n'a encore reconnu cette dernière. Les "
              "deux versions coexistent donc en pratique.",
        lien="",
    ),
    dict(
        cle="gaz", confiance="a_verifier",
        nom="État de l'installation intérieure de gaz",
        sigle="Gaz",
        obligation="Code de la construction et de l'habitation, articles L. 134-6 "
                   "et suivants",
        decret="—",
        arrete="Arrêté du 25 juillet 2022, abrogeant l'arrêté du 18 novembre 2013",
        norme="NF P45-500 : janvier 2013",
        norme_titre="Installations de gaz situées à l'intérieur des bâtiments "
                    "d'habitation — État des installations intérieures de gaz",
        note="Le contrôle porte sur la tuyauterie fixe, le raccordement des appareils, "
             "la ventilation des locaux et la combustion.",
        piege="Le diagnostic suppose que l'installation soit alimentée et les appareils "
              "en état de fonctionner. À défaut, le rapport comporte des réserves qui "
              "en limitent la portée.",
        lien="",
    ),
    dict(
        cle="electricite", confiance="etabli",
        nom="État de l'installation intérieure d'électricité",
        sigle="Électricité",
        obligation="Code de la construction et de l'habitation, articles L. 134-7 "
                   "et suivants",
        decret="—",
        arrete="Arrêté « méthode » relatif à l'état de l'installation intérieure "
               "d'électricité",
        norme="NF C16-600 : juillet 2017",
        norme_titre="État des installations électriques des parties privatives des "
                    "locaux à usage d'habitation",
        note="Le contrôle porte sur l'installation située en aval du disjoncteur "
             "général, à l'exclusion du réseau du distributeur.",
        piege="Ne pas confondre avec l'attestation CONSUEL, qui conditionne la mise "
              "sous tension d'une installation neuve. Ce sont deux dispositifs "
              "distincts.",
        lien="",
    ),
    dict(
        cle="assainissement", confiance="etabli",
        nom="Diagnostic assainissement non collectif",
        sigle="ANC",
        obligation="Code de la santé publique, article L. 1331-11-1",
        decret="—",
        arrete="Arrêtés relatifs au contrôle des installations d'assainissement "
               "non collectif",
        norme="NF P15-910 : septembre 2001",
        norme_titre="Lignes directrices pour un diagnostic des installations "
                    "d'assainissement autonome",
        note="Le contrôle relève du service public d'assainissement non collectif de "
             "la commune, et non d'un diagnostiqueur privé.",
        piege="En cas de non-conformité, l'acquéreur dispose d'un délai d'un an après "
              "l'acte pour mettre l'installation en conformité.",
        lien="",
    ),
    dict(
        cle="carrez", confiance="verifie",
        nom="Superficie privative — loi Carrez",
        sigle="Carrez",
        obligation="Loi n° 65-557 du 10 juillet 1965, article 46",
        decret="Décret n° 97-532 du 23 mai 1997",
        arrete="—",
        norme="Aucune norme AFNOR — méthode définie par la loi et son décret",
        norme_titre="Mesurage de la superficie des parties privatives d'un lot de "
                    "copropriété",
        note="Introduite par la loi n° 96-1107 du 18 décembre 1996.",
        piege="Ne pas confondre avec la surface habitable dite loi Boutin, utilisée "
              "en location, ni avec la surface de plancher, notion d'urbanisme. Les "
              "trois se calculent différemment et donnent trois chiffres distincts "
              "pour un même logement.",
        lien="https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006472158/",
    ),
    dict(
        cle="ddt-vente", confiance="verifie",
        nom="Dossier de diagnostic technique — vente",
        sigle="DDT vente",
        obligation="Code de la construction et de l'habitation, article L. 271-4",
        decret="—",
        arrete="—",
        norme="Composition fixée par la loi, non par une norme",
        norme_titre="Diagnostics et informations à communiquer par le propriétaire "
                    "vendeur",
        note="Le dossier se joint à la promesse de vente ou à l'acte de vente.",
        piege="Un dossier incomplet n'annule pas la vente : il prive le vendeur de "
              "l'exonération de la garantie des vices cachés sur le point manquant.",
        lien="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041586781/",
    ),
    dict(
        cle="ddt-location", confiance="verifie",
        nom="Dossier de diagnostic technique — location",
        sigle="DDT location",
        obligation="Loi n° 89-462 du 6 juillet 1989, article 3-3",
        decret="—",
        arrete="—",
        norme="Composition fixée par la loi",
        norme_titre="Contenu du dossier de diagnostic technique annexé au bail",
        note="Le dossier s'annexe au bail à la signature et à chaque renouvellement. "
             "Il se transmet par voie dématérialisée, sauf opposition d'une des parties.",
        piege="Le diagnostic amiante fait partie du dossier mais n'est pas annexé au "
              "bail : il est tenu à la disposition du locataire, sur demande.",
        lien="https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000043978254",
    ),
    dict(
        cle="certification", confiance="verifie",
        nom="Certification des opérateurs de repérage amiante",
        sigle="Certification",
        obligation="Code du travail et code de la santé publique",
        decret="—",
        arrete="Arrêté du 25 juillet 2016 — certification avec mention",
        norme="Référentiel de certification de l'organisme accrédité",
        norme_titre="Compétences exigées de l'opérateur de repérage",
        note="Le repérage avant travaux et avant démolition exige une certification "
             "« avec mention », délivrée par un organisme accrédité. L'opérateur doit "
             "être indépendant du donneur d'ordre et de l'entreprise de travaux.",
        piege="Un opérateur certifié « sans mention » peut établir un DTA, pas un "
              "repérage avant travaux. La vérification se fait sur l'annuaire public "
              "des diagnostiqueurs certifiés.",
        lien="https://www.service-public.gouv.fr/particuliers/vosdroits/F17376",
    ),
]

# Fiches Service Public surveillées par veille_reglementaire.py
FICHES_SURVEILLEES = {
    "F10798": dict(nom="Diagnostics à fournir en cas de vente",
                   verifie_le="2025-03-07",
                   pages=["/questions/diagnostics-obligatoires-vente/"]),
    "F33463": dict(nom="Diagnostics fournis par le bailleur au locataire",
                   verifie_le="2026-02-20",
                   pages=["/questions/diagnostics-obligatoires-location/"]),
    "F16096": dict(nom="Diagnostic de performance énergétique",
                   verifie_le="", pages=[]),
    "F742": dict(nom="État amiante", verifie_le="", pages=[]),
    "F1142": dict(nom="Constat de risque d'exposition au plomb",
                  verifie_le="", pages=[]),
    "F3150": dict(nom="État relatif à la présence de termites",
                  verifie_le="", pages=[]),
    "F17376": dict(nom="Où trouver un diagnostiqueur certifié",
                   verifie_le="", pages=[]),
}
