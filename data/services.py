# -*- coding: utf-8 -*-
"""
Contenu des 4 prestations. Les références réglementaires sont à revalider
avant mise en ligne (voir NOTE-JURIDIQUE.md).
"""

SERVICES = [
    dict(
        slug="reperage-amiante-avant-travaux",
        clair="Avant d'ouvrir un mur ou un sol, on vérifie si de l'amiante s'y cache — et on fait analyser en laboratoire. Le chantier démarre en sachant, pas en espérant.",
        sigle="RAAT",
        nom="Repérage amiante avant travaux",
        nom_court="Repérage amiante avant travaux",
        accroche="Le repérage qui conditionne le démarrage de votre chantier.",
        kw="repérage amiante avant travaux",
        meta="Repérage amiante avant travaux à {lieu} : analyses COFRAC, rapport "
             "sous 48 h, intervention sous 72 h. Devis sous 2 h.",
        intro="Le repérage amiante avant travaux est obligatoire avant toute opération "
              "susceptible d'exposer des travailleurs à l'amiante, dans un immeuble bâti "
              "dont le permis de construire a été délivré avant le 1er juillet 1997. "
              "L'obligation pèse sur le donneur d'ordre : maître d'ouvrage, syndic, "
              "bailleur ou propriétaire occupant.",
        cadre=[
            ("Code du travail, art. R.4412-97 et suivants",
             "Impose au donneur d'ordre de faire réaliser un repérage avant toute "
             "opération susceptible d'exposer les travailleurs à l'amiante."),
            ("Arrêté du 16 juillet 2019",
             "Fixe les modalités du repérage amiante avant travaux pour le domaine "
             "immeubles bâtis : compétences de l'opérateur, méthodologie, contenu du "
             "rapport."),
            ("Transmission aux entreprises",
             "Le rapport doit être remis à toutes les entreprises consultées, dès la "
             "phase d'appel d'offres, et annexé aux pièces du marché."),
        ],
        etapes=[
            ("Analyse du programme de travaux",
             "Nous partons de votre périmètre d'intervention réel : plans, CCTP, "
             "descriptif. Le repérage se cale sur ce que vous allez ouvrir, pas sur une "
             "trame standard."),
            ("Repérage sur site avec sondages",
             "Investigation des matériaux et produits susceptibles de contenir de "
             "l'amiante dans le périmètre, avec sondages non destructifs et destructifs "
             "selon l'accord préalable du donneur d'ordre."),
            ("Prélèvements et analyses en laboratoire accrédité",
             "Chaque doute est levé par prélèvement et analyse en laboratoire accrédité "
             "COFRAC. Aucun matériau n'est classé « présumé amianté » par confort."),
            ("Rapport exploitable par les entreprises",
             "Localisation précise, croquis, photographies, conclusions par matériau et "
             "estimation des quantités : le document doit permettre à une entreprise de "
             "chiffrer son retrait sans revenir sur site."),
        ],
        faq=[
            ("Qui est responsable de faire réaliser le RAAT ?",
             "Le donneur d'ordre, c'est-à-dire celui qui commande les travaux : maître "
             "d'ouvrage public ou privé, syndic pour les parties communes, bailleur, ou "
             "propriétaire. Cette responsabilité ne se transfère pas à l'entreprise de "
             "travaux."),
            ("Le diagnostic amiante des parties privatives suffit-il ?",
             "Non. Le DAPP et le dossier technique amiante répondent à une logique de "
             "gestion du bâtiment, pas de préparation de chantier. Ils ne couvrent ni le "
             "périmètre des travaux, ni les sondages destructifs nécessaires."),
            ("Que se passe-t-il si le repérage n'a pas été fait ?",
             "L'inspection du travail peut ordonner l'arrêt du chantier. La "
             "responsabilité pénale du donneur d'ordre peut être engagée, et l'assurance "
             "de l'entreprise intervenante peut refuser sa garantie."),
            ("Faut-il un repérage pour des travaux de faible ampleur ?",
             "Le critère n'est pas l'ampleur des travaux mais l'exposition potentielle "
             "des travailleurs. Percer un mur, déposer un revêtement de sol ou intervenir "
             "sur une gaine technique suffit à déclencher l'obligation."),
            ("Quel délai pour obtenir le rapport ?",
             "Nous intervenons généralement sous 72 heures et remettons le rapport sous "
             "48 heures après réception des résultats d'analyse."),
        ],
        cible="maîtres d'ouvrage, syndics, bailleurs et entreprises générales",
        fiche=[
            ("Pour qui", "Maître d'ouvrage, syndic, bailleur ou propriétaire : "
                         "celui qui commande les travaux."),
            ("Quand", "Avant tous travaux dans un bâtiment dont le permis de "
                      "construire est antérieur au 1er juillet 1997."),
            ("Sur site", "Intervention généralement sous 72 heures."),
            ("Rapport", "Remis sous 48 heures après les résultats d'analyse."),
            ("Analyses", "Laboratoire accrédité COFRAC."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="reperage-amiante-avant-demolition",
        clair="Avant de démolir, on cherche partout, sans exception : tout ce que la pelleteuse va toucher doit être connu d'avance.",
        sigle="RAAD",
        nom="Repérage amiante avant démolition",
        nom_court="Repérage amiante avant démolition",
        accroche="Le repérage exhaustif, sans zone d'ombre, avant de faire tomber le bâtiment.",
        kw="repérage amiante avant démolition",
        meta="Repérage amiante avant démolition à {lieu} : repérage exhaustif, "
             "sondages destructifs, analyses COFRAC. Devis sous 2 h.",
        intro="Le repérage amiante avant démolition est obligatoire avant la démolition "
              "totale ou partielle de tout immeuble bâti dont le permis de construire a "
              "été délivré avant le 1er juillet 1997. Contrairement au repérage avant "
              "travaux, il vise l'exhaustivité : tous les matériaux du bâtiment, y compris "
              "ceux que seuls des sondages destructifs peuvent atteindre.",
        cadre=[
            ("Code de la santé publique, art. R.1334-19",
             "Impose au propriétaire de faire rechercher la présence d'amiante avant la "
             "démolition de tout ou partie d'un immeuble bâti."),
            ("Code du travail, art. R.4412-97",
             "S'applique en parallèle dès lors que l'opération est susceptible d'exposer "
             "des travailleurs."),
            ("Exhaustivité et sondages destructifs",
             "Le bâtiment étant voué à disparaître, aucune réserve de non-accessibilité "
             "n'est acceptable : le repérage doit couvrir l'ensemble des matériaux, "
             "y compris enrobés, remblais et éléments enfouis."),
        ],
        etapes=[
            ("Cadrage du périmètre de démolition",
             "Démolition totale, partielle, curage préalable : le périmètre détermine "
             "l'étendue de la mission et le plan de sondages."),
            ("Repérage exhaustif avec sondages destructifs",
             "Ouverture des structures, dépose d'échantillons, investigation des espaces "
             "non accessibles en exploitation normale. Le bâtiment doit être libéré et "
             "les réseaux consignés."),
            ("Analyses en laboratoire accrédité COFRAC",
             "Volume d'analyses significativement supérieur à un repérage avant travaux, "
             "à intégrer dans le planning et le budget de l'opération."),
            ("Rapport et estimation des quantités",
             "Localisation, nature et quantité estimée par matériau : la base de chiffrage "
             "du lot désamiantage et du plan de retrait de l'entreprise."),
        ],
        faq=[
            ("Quelle différence entre RAAT et RAAD ?",
             "Le repérage avant travaux se limite au périmètre de l'opération projetée. "
             "Le repérage avant démolition couvre l'intégralité du bâtiment, sans "
             "réserve de non-accessibilité, avec sondages destructifs systématiques."),
            ("Le RAAD doit-il être joint à la demande de permis de démolir ?",
             "Il doit être réalisé avant l'engagement de l'opération et transmis aux "
             "entreprises consultées. Nous recommandons de l'anticiper dès la phase de "
             "montage, car ses conclusions déterminent le coût réel de la démolition."),
            ("Le bâtiment doit-il être vide ?",
             "Oui. Les sondages destructifs et l'investigation des espaces techniques "
             "supposent un bâtiment libéré, avec réseaux consignés et accès sécurisés."),
            ("Un RAAD peut-il servir pour un chantier de travaux ?",
             "Oui, dans son périmètre : un repérage avant démolition étant plus étendu, "
             "il couvre les besoins d'un repérage avant travaux sur les mêmes zones."),
        ],
        cible="maîtres d'ouvrage, aménageurs, bailleurs sociaux et entreprises de démolition",
        fiche=[
            ("Pour qui", "Maître d'ouvrage, aménageur, bailleur social ou "
                         "entreprise de démolition."),
            ("Quand", "Avant la démolition totale ou partielle d'un bâtiment "
                      "d'avant le 1er juillet 1997."),
            ("Particularité", "Repérage exhaustif avec sondages destructifs : "
                              "le bâtiment doit être libéré, réseaux consignés."),
            ("Rapport", "Localisation, nature et quantités estimées par matériau."),
            ("Analyses", "Laboratoire accrédité COFRAC."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="diagnostic-technique-global",
        clair="Le bilan de santé complet de l'immeuble : ce qui va, ce qui fatigue, ce que ça coûtera — pour décider en assemblée sur du solide.",
        sigle="DTG",
        nom="Diagnostic technique global",
        nom_court="Diagnostic technique global",
        accroche="L'état réel de la copropriété, avant de voter le moindre budget.",
        kw="diagnostic technique global",
        meta="Diagnostic technique global de copropriété à {lieu} : état du bâti, "
             "chiffrage des travaux, volet énergétique. Devis sous 2 h.",
        intro="Le diagnostic technique global établit une photographie complète de la "
              "copropriété : état apparent des parties communes et des équipements, "
              "situation au regard des obligations réglementaires, améliorations "
              "possibles et estimation du coût des travaux nécessaires sur dix ans.",
        cadre=[
            ("Code de la construction et de l'habitation, art. L.731-1",
             "Définit le contenu du diagnostic technique global, issu de la loi ALUR "
             "du 24 mars 2014."),
            ("Cas d'obligation",
             "Immeuble de plus de dix ans faisant l'objet d'une mise en copropriété, et "
             "immeuble faisant l'objet d'une procédure pour insalubrité. Dans les autres "
             "cas, la réalisation du DTG est soumise au vote de l'assemblée générale."),
            ("Articulation avec le plan pluriannuel de travaux",
             "Un DTG comportant les éléments requis peut tenir lieu de plan pluriannuel "
             "de travaux, ce qui évite de commander deux missions successives."),
        ],
        etapes=[
            ("Collecte documentaire",
             "Carnet d'entretien, règlement de copropriété, procès-verbaux d'assemblée, "
             "contrats d'exploitation, diagnostics existants. Cette phase conditionne la "
             "qualité de l'analyse."),
            ("Visite technique des parties communes",
             "Structure, clos et couvert, réseaux, équipements communs, sécurité "
             "incendie, accessibilité. Relevé d'état apparent et identification des "
             "désordres évolutifs."),
            ("Volet énergétique",
             "Diagnostic de performance énergétique collectif ou audit énergétique selon "
             "la configuration de l'immeuble, intégré à l'analyse d'ensemble."),
            ("Rapport, chiffrage et présentation en assemblée",
             "Liste hiérarchisée des travaux, estimation du coût, échéancier. Nous "
             "présentons les conclusions en assemblée générale pour sécuriser le vote."),
        ],
        faq=[
            ("Le DTG est-il obligatoire pour toutes les copropriétés ?",
             "Non. Il l'est pour les immeubles de plus de dix ans mis en copropriété et "
             "en cas de procédure d'insalubrité. Ailleurs, l'assemblée générale se "
             "prononce sur son inscription à l'ordre du jour."),
            ("Quelle différence avec le plan pluriannuel de travaux ?",
             "Le DTG décrit l'état de l'immeuble et ses obligations. Le PPPT programme "
             "les travaux sur dix ans. Un DTG complet peut tenir lieu de PPPT, mais "
             "l'inverse n'est pas vrai."),
            ("Combien de temps prend un DTG ?",
             "Comptez trois à six semaines selon la taille de l'immeuble et la "
             "disponibilité des documents, dont une à trois journées sur site."),
            ("Le DTG engage-t-il la copropriété à faire les travaux ?",
             "Non. C'est un outil d'aide à la décision. Il éclaire l'assemblée générale, "
             "qui reste souveraine sur le vote des travaux et leur financement."),
        ],
        cible="syndics de copropriété, conseils syndicaux et bailleurs",
        fiche=[
            ("Pour qui", "Syndics, conseils syndicaux, bailleurs."),
            ("Quand", "Mise en copropriété d'un immeuble de plus de 10 ans, "
                      "procédure d'insalubrité, ou sur vote de l'assemblée générale."),
            ("Durée", "Trois à six semaines, dont une à trois journées sur site."),
            ("Livrable", "Rapport chiffré et hiérarchisé, présenté en assemblée "
                         "générale."),
            ("Bon à savoir", "Un DTG complet peut tenir lieu de plan pluriannuel "
                             "de travaux : une mission au lieu de deux."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="plan-pluriannuel-de-travaux",
        clair="Le plan d'entretien des dix prochaines années : quels travaux, dans quel ordre, pour quel budget — et l'épargne qui va avec.",
        sigle="PPPT",
        nom="Plan pluriannuel de travaux",
        nom_court="Projet de plan pluriannuel de travaux",
        accroche="Dix ans de travaux, chiffrés et hiérarchisés, votables en une assemblée.",
        kw="plan pluriannuel de travaux",
        meta="Plan pluriannuel de travaux à {lieu} : copropriétés de plus de 15 ans, "
             "priorités et chiffrage sur 10 ans. Devis sous 2 h.",
        intro="Le projet de plan pluriannuel de travaux est obligatoire dans les "
              "copropriétés à destination totale ou partielle d'habitation de plus de "
              "quinze ans. Il liste les travaux nécessaires sur dix ans, les hiérarchise "
              "par niveau de priorité, en estime le coût et fixe un échéancier. Il "
              "conditionne le dimensionnement du fonds de travaux.",
        cadre=[
            ("Loi Climat et Résilience du 22 août 2021",
             "Introduit l'obligation de projet de plan pluriannuel de travaux à "
             "l'article 14-2 de la loi du 10 juillet 1965."),
            ("Calendrier d'entrée en vigueur",
             "Échelonné selon le nombre de lots : plus de 200 lots depuis le 1er janvier "
             "2023, de 51 à 200 lots depuis le 1er janvier 2024, 50 lots et moins depuis "
             "le 1er janvier 2025. Toutes les copropriétés concernées sont désormais "
             "dans le champ de l'obligation."),
            ("Lien avec le fonds de travaux",
             "Lorsque le plan fait apparaître des travaux nécessaires dans les dix ans, "
             "la cotisation annuelle au fonds de travaux ne peut être inférieure à un "
             "pourcentage du montant des travaux prévus."),
        ],
        etapes=[
            ("Diagnostic de l'état apparent",
             "Structure, enveloppe, couverture, réseaux, équipements communs, sécurité. "
             "Le plan ne vaut que par la qualité du relevé initial."),
            ("Analyse énergétique",
             "Identification des travaux d'amélioration de la performance énergétique et "
             "de leurs gains attendus, en cohérence avec le DPE collectif ou l'audit."),
            ("Hiérarchisation et chiffrage",
             "Chaque poste est classé par priorité, estimé financièrement et positionné "
             "dans l'échéancier décennal."),
            ("Présentation en assemblée générale",
             "Le projet est présenté à la première assemblée qui suit son élaboration. "
             "Nous intervenons pour l'exposer et répondre aux copropriétaires."),
        ],
        faq=[
            ("Quelles copropriétés sont concernées ?",
             "Les copropriétés à destination totale ou partielle d'habitation dont "
             "l'immeuble a plus de quinze ans. Le calendrier d'entrée en vigueur, "
             "échelonné selon le nombre de lots, est aujourd'hui intégralement déployé."),
            ("Quelle validité pour le plan ?",
             "Le projet est établi pour dix ans et doit être actualisé tous les dix ans."),
            ("Que se passe-t-il si la copropriété n'a pas de PPPT ?",
             "L'absence de plan expose le syndic à voir sa responsabilité recherchée, et "
             "prive la copropriété d'un dimensionnement fiable de son fonds de travaux. "
             "En cas de difficulté, l'autorité administrative peut le réclamer."),
            ("Un DTG récent dispense-t-il du PPPT ?",
             "Un diagnostic technique global comportant l'ensemble des éléments requis "
             "peut tenir lieu de projet de plan pluriannuel de travaux. Nous vérifions ce "
             "point avant de vous proposer une mission."),
            ("Le plan doit-il être voté ?",
             "Le projet est présenté à l'assemblée générale, qui se prononce ensuite sur "
             "les travaux à engager et sur leurs modalités de financement."),
        ],
        cible="syndics de copropriété, conseils syndicaux et administrateurs de biens",
        fiche=[
            ("Pour qui", "Syndics, conseils syndicaux, administrateurs de biens."),
            ("Quand", "Copropriété à destination totale ou partielle d'habitation "
                      "de plus de 15 ans."),
            ("Horizon", "Travaux programmés sur 10 ans ; plan actualisé tous les "
                        "10 ans."),
            ("Livrable", "Travaux hiérarchisés, chiffrage et échéancier, présentés "
                         "en assemblée générale."),
            ("Bon à savoir", "Le plan dimensionne la cotisation au fonds de travaux."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

ENTREPRISE = dict(
    nom="DGLM Expertises",
    baseline="Diagnostics techniques du bâtiment — Bordeaux Métropole",
    tel="06 07 35 15 05",
    tel_raw="+33607351505",
    email="contact@dglmexpertises.fr",
    rue="27 ter rue des Sables",
    cp="33320",
    ville="Eysines",
    siret="89128707000017",
    rcs="891 287 070 R.C.S. Bordeaux",
    lat="44.8846",
    lon="-0.6503",
    depuis="2020",
    domaine="https://www.dglmexpertises.fr",
)
