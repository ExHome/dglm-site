# -*- coding: utf-8 -*-
"""
TEXTES DE FOND DES QUARTIERS.

Les pages de quartier s'arrêtaient à la description du bâti : environ 290 mots,
et rien sur la conduite de la mission. Ces textes leur ajoutent ce qu'un
diagnostiqueur peut affirmer à partir de ce bâti — comment la mission se
conduit, quels points se contrôlent, quel cadre s'applique.

RÈGLE DE RÉDACTION, tenue à la lettre : aucun fait local nouveau. Pas un nom de
rue, pas une date de construction, pas un chiffre qui ne figure déjà dans
data/quartiers.py. Ce qui est développé, ce sont les conséquences techniques et
réglementaires du bâti déjà décrit — vérifiables sans rien savoir de plus du
quartier.

Deux contrôles successifs ont relevé 101 défauts, dont 26 faits locaux ajoutés
et 11 erreurs de droit. 62 phrases ont été supprimées.

INTERDIT ABSOLU : aucune phrase ne doit laisser entendre qu'un bâtiment échappe
au repérage amiante du fait de son âge. Le code du travail ne connaît aucune
date d'exclusion.
"""

TEXTES = {
    "bordeaux/chartrons": dict(
        methode="Sur ce bâti, la mission commence avant la visite, par la reconstitution "
                "des couches de travaux : les autorisations d'urbanisme de la "
                "reconversion, les marchés d'entretien et le règlement de copropriété "
                "avec son état descriptif de division. Dans un immeuble issu de la "
                "division d'un chai, la limite entre parties communes et parties "
                "privatives ne se lit pas sur place, et c'est elle qui borne le périmètre "
                "du constat plomb comme celui du repérage. La visite se conduit ensuite "
                "en deux registres dans le même immeuble : les ouvrages d'origine en "
                "pierre et en bois d'un côté, la couche rapportée par la reconversion de "
                "l'autre, chacun appelant ses propres sondages. C'est ce dédoublement qui "
                "fait durer l'intervention, bien plus que la surface. À préparer : "
                "l'accès aux locaux communs et aux volumes techniques, et les rapports "
                "déjà établis sur l'immeuble.",
        cadre="Le repérage amiante avant travaux relève du code du travail, articles R. "
              "4412-97 et suivants, et de l'arrêté du 16 juillet 2019 : il pèse sur le "
              "donneur d'ordre, préalablement à toute opération, et ne connaît aucune "
              "date d'exclusion — un règlement de copropriété récent n'y change rien. "
              "Le dossier technique amiante des parties communes, régi par les articles "
              "R. 1334-14 et suivants du code de la santé publique, ne couvre que les "
              "listes A et B : il ne dispense d'aucun repérage avant travaux. Le "
              "constat de risque d'exposition au plomb vise les immeubles d'habitation "
              "construits avant le 1er janvier 1949 et porte alors sur tous les "
              "revêtements des parties communes, quelle que soit leur date de pose. "
              "Enfin, la mise en copropriété d'un immeuble construit depuis plus de dix "
              "ans appelle un diagnostic technique global (articles L. 731-1 et "
              "suivants du code de la construction et de l'habitation).",
        points=[
            "Sous le revêtement actuel des sols de circulation commune, la dalle "
                "semi-rigide et sa colle posées lors de la reconversion se sondent sur "
                "toute l'épaisseur du complexe, avant toute reprise de sol.",
            "Les cloisons de distribution rapportées dans les volumes reconvertis se "
                "sondent en parement avant toute dépose ou tout percement : leur date de "
                "pose ne se déduit pas de l'âge des murs qui les entourent.",
            "Les conduits et gaines ajoutés lors de la reconversion se contrôlent "
                "avant toute reprise de colonne, y compris lorsqu'ils sont habillés et "
                "hors de vue.",
            "Dans un immeuble d'habitation antérieur à 1949, les peintures des cages "
                "d'escalier et des menuiseries communes se mesurent par fluorescence X, "
                "unité de diagnostic par unité de diagnostic, avant tout ponçage ou "
                "décapage.",
            "Les planchers bois d'origine se reconnaissent en appui et en about de "
                "solive lors du diagnostic technique global, avant que la copropriété ne "
                "chiffre une reprise de structure.",
        ],
    ),

    "bordeaux/saint-michel-capucins": dict(
        methode="Ici, la mission commence par une question administrative : qui commande. "
                "Sans syndic professionnel, le donneur d'ordre reste le syndicat des "
                "copropriétaires, et il faut qu'un copropriétaire soit désigné pour "
                "ouvrir, accompagner et recevoir le rapport. Vient ensuite le périmètre : "
                "sans carnet d'entretien ni diagnostic antérieur, aucun historique ne "
                "permet de préparer le repérage sur plan. Le nombre et l'emplacement des "
                "sondages se décident sur site, ce qui allonge la visite et interdit "
                "d'annoncer un forfait de sondages à la commande. Les divisions "
                "successives obligent à traiter chaque niveau comme un ouvrage distinct : "
                "un sondage ne vaut que pour l'ouvrage qu'il traverse. La configuration "
                "pèse aussi. Sous procédure administrative enfin, la date de remise "
                "commande tout, et le calendrier de visite se cale d'abord sur le délai "
                "imparti.",
        cadre="Le constat de risque d'exposition au plomb des parties communes n'est "
              "pas une obligation nouvelle : le code de la santé publique, articles L. "
              "1334-5 et suivants, l'impose dans les immeubles d'habitation construits "
              "avant le 1er janvier 1949. Il porte sur tous les revêtements des parties "
              "communes, quelle que soit leur date de pose. Sous police de la sécurité "
              "et de la salubrité des immeubles (articles L. 511-1 et suivants du code "
              "de la construction et de l'habitation), l'autorité administrative peut "
              "demander au syndic la production d'un diagnostic technique global "
              "(articles L. 731-1 et suivants du même code). Une copropriété de moins "
              "de dix lots sans syndic professionnel reste un syndicat soumis à la loi "
              "du 10 juillet 1965 : le plan pluriannuel de travaux lui est dû dès lors "
              "que le permis de construire a été délivré depuis plus de quinze ans, "
              "l'échéance du 1er janvier 2025 étant passée.",
        points=[
            "Les peintures des cages d'escalier, des paliers et des menuiseries "
                "communes se mesurent par fluorescence X unité de diagnostic par unité de "
                "diagnostic, avant tout ponçage ou décapage.",
            "Les cloisons et doublages posés lors des divisions successives se "
                "sondent avant toute ouverture : faute d'archive, rien ne permet de dater "
                "leur pose autrement que par l'analyse.",
            "Les revêtements de sol superposés des paliers se sondent sur toute "
                "l'épaisseur du complexe avant toute réfection, la couche visible ne "
                "disant rien de celles qui la précèdent.",
            "Les réseaux ajoutés au fil des travaux successifs — traversées, "
                "habillages, calfeutrements — se contrôlent avant tout percement, y "
                "compris pour une intervention ponctuelle.",
            "L'état apparent des planchers et des circulations communes se relève "
                "lors du diagnostic technique global, avant toute inscription d'une "
                "reprise de structure au programme de travaux.",
        ],
    ),

    "bordeaux/bacalan-bassins-a-flot": dict(
        methode="Sur une emprise destinée à disparaître, la mission se conduit bâtiment "
                "libéré et mis hors énergie : c'est la condition des sondages destructifs "
                "et de la recherche sous chapes et derrière habillages qu'impose un "
                "repérage avant démolition. La commande se prépare donc avec le maître "
                "d'ouvrage sur trois points. Le phasage d'abord : sur une opération "
                "mixte, les zones démolies et les zones conservées ne relèvent ni du même "
                "périmètre ni du même rapport, et le découpage doit être arrêté avant la "
                "visite, non pendant. Les moyens d'accès ensuite : sur charpente "
                "métallique, les matériaux à contrôler sont en hauteur et masqués, et la "
                "reconnaissance suppose une nacelle ou un accès sur corde, poste qui "
                "commande le délai plus que le repérage lui-même. Les autorisations "
                "d'accès enfin, qui se traitent dès la commande.",
        cadre="Le repérage avant démolition relève du code du travail, articles R. "
              "4412-97 et suivants, et de l'arrêté du 16 juillet 2019 : périmètre "
              "exhaustif, liste C comprise, sondages destructifs sur bâtiment libéré. "
              "Conduit selon la norme NF X 46-020 d'août 2017, il vaut repérage avant "
              "travaux ; l'inverse n'est jamais vrai. L'opérateur doit être certifié "
              "avec mention (arrêté du 25 juillet 2016) et indépendant du donneur "
              "d'ordre comme de l'entreprise de travaux. S'y ajoute le diagnostic "
              "portant sur les produits, équipements, matériaux et déchets (articles L. "
              "126-34 et suivants du code de la construction et de l'habitation, décret "
              "n° 2021-821 du 25 juin 2021), dû en démolition comme en rénovation "
              "significative au-delà de mille mètres carrés de surface de plancher, ou "
              "dès lors que le bâtiment a accueilli une activité industrielle, agricole "
              "ou commerciale mettant en œuvre des substances dangereuses. Il précède "
              "la demande de permis de démolir ou l'acceptation des devis.",
        points=[
            "Les protections projetées sur charpente métallique échappent à tout "
                "examen conduit depuis le sol : leur reconnaissance en hauteur figure au "
                "programme de la visite, avant toute intervention sur la structure.",
            "Sous le revêtement des sols d'atelier, la dalle semi-rigide et sa colle "
                "bitumineuse se sondent sur toute l'épaisseur avant curage.",
            "Sur les immeubles récents en béton, le repérage avant travaux reste dû : "
                "aucune date ne l'exclut, et l'absence de matériau s'établit sur les "
                "ouvrages que le programme va toucher, jamais par déduction à partir de "
                "l'année de construction.",
            "En limite de zone conservée, les ouvrages coupés par la démolition — "
                "planchers, murs de refend, réseaux traversants — relèvent du repérage "
                "avant travaux, distinct du repérage avant démolition mené sur la partie "
                "déposée.",
        ],
    ),

    "bordeaux/cauderan": dict(
        methode="Sur un immeuble de dix à quarante lots, les parties communes tiennent en "
                "peu de volumes : hall, cage, circulations et locaux techniques. La "
                "visite est courte ; l'essentiel du travail est ailleurs. Faute "
                "d'historique technique, la mission commence par une reconstitution "
                "documentaire — autorisations d'urbanisme, contrats d'entretien et de "
                "maintenance, procès-verbaux d'assemblée générale — puis par un relevé de "
                "l'état apparent, ouvrage par ouvrage, qui servira de base au chiffrage. "
                "Le diagnostic technique global n'est pas une visite de plus : il "
                "produit, pour une copropriété sans mémoire technique, le premier état "
                "d'ensemble sur lequel une assemblée puisse délibérer — état apparent des "
                "parties communes et des équipements, situation du syndicat au regard de "
                "ses obligations, volet énergétique et évaluation sommaire des travaux à "
                "dix ans. Il se prépare avec le conseil syndical, qui fournit les pièces "
                "et arbitre les priorités. Sur une maison, la logique change : le donneur "
                "d'ordre est le propriétaire, et le repérage précède la consultation de "
                "l'entreprise, jamais l'inverse.",
        cadre="Le plan pluriannuel de travaux s'impose aux copropriétés à destination "
              "totale ou partielle d'habitation dont le permis de construire a été "
              "délivré depuis plus de quinze ans — c'est ce critère, et non la date de "
              "réception. Le calendrier d'entrée en vigueur est intégralement échu : la "
              "dernière échéance, celle des copropriétés d'au plus cinquante lots, "
              "court depuis le 1er janvier 2025. Le syndic inscrit le projet à l'ordre "
              "du jour de l'assemblée générale, qui se prononce, et le plan s'actualise "
              "tous les dix ans. Le diagnostic technique global (articles L. 731-1 et "
              "suivants du code de la construction et de l'habitation) peut être décidé "
              "par l'assemblée et sert de base à ce projet. Sur une maison, enfin, le "
              "repérage avant travaux relève du code du travail, articles R. 4412-97 et "
              "suivants : l'obligation pèse sur le donneur d'ordre, particulier "
              "compris, sans condition d'âge du bâtiment.",
        points=[
            "Sur les extensions et vérandas rapportées, les plaques de couverture en "
                "fibres-ciment se repèrent avant la dépose, dès la commande des travaux : "
                "découvertes en cours de chantier, elles imposent l'arrêt de "
                "l'intervention.",
            "Dans les halls et paliers des petits collectifs, le revêtement de sol et "
                "sa colle se sondent sur toute l'épaisseur du complexe avant toute "
                "réfection, la couche visible ne préjugeant pas des couches inférieures.",
            "Lorsque l'immeuble dispose d'un local technique collectif, "
                "calorifugeages, joints et garnitures s'y contrôlent avant toute "
                "intervention d'un mainteneur : le donneur d'ordre est alors le syndicat "
                "des copropriétaires.",
            "Les mastics de vitrage et les calfeutrements des menuiseries de parties "
                "communes se repèrent avant dépose, poste que les programmes de "
                "rénovation énergétique chiffrent souvent sans l'avoir fait contrôler.",
            "L'état apparent des façades, des couvertures et des descentes d'eaux "
                "pluviales se relève lors du diagnostic technique global, avant que le "
                "plan pluriannuel n'en fixe l'ordre et le calendrier.",
        ],
    ),

    "bordeaux/nansouty-saint-genes": dict(
        methode="Sur une échoppe ou un immeuble de rapport divisé en deux ou trois lots, "
                "la première tâche n'est pas technique : c'est d'établir ce qui est "
                "commun. Couloir, escalier, cour, couverture, murs — le périmètre du "
                "constat plomb comme celui du repérage se lit dans l'état descriptif de "
                "division, pièce à réunir avant la visite. La mitoyenneté impose une "
                "seconde limite. Toute intervention sur un mur séparatif ou en jonction "
                "de couverture touche un ouvrage partagé, et la mission s'arrête à la "
                "limite de propriété : ce que le programme prévoit au-delà relève d'un "
                "autre donneur d'ordre, à identifier en amont. Vient ensuite la datation "
                "des couches : surélévations et divisions postérieures se repèrent par "
                "les autorisations d'urbanisme, seul moyen de séparer l'ouvrage d'origine "
                "de ce qui a été rapporté. Enfin, l'examen parasitaire suppose un accès "
                "réel aux pieds de mur : plinthes déposées, mobilier écarté, planchers "
                "dégagés en rive. C'est la préparation la plus souvent négligée, et celle "
                "qui décide de la valeur du relevé.",
        cadre="Le constat de risque d'exposition au plomb (code de la santé publique, "
              "articles L. 1334-5 et suivants) vise les immeubles d'habitation "
              "construits avant le 1er janvier 1949 et porte, dans les parties "
              "communes, sur tous les revêtements, quelle que soit leur date de pose : "
              "un couloir repeint n'y échappe pas. La mérule ne fait l'objet d'aucun "
              "diagnostic normalisé : l'état parasitaire est une mission contractuelle, "
              "mais sa présence dans un immeuble bâti doit être déclarée en mairie. Le "
              "plan pluriannuel de travaux, enfin, se déclenche sur le permis de "
              "construire délivré depuis plus de quinze ans, quelle que soit la taille "
              "du syndicat.",
        points=[
            "En pied de mur, les abouts de solive encastrés dans la maçonnerie sont "
                "le point de sondage prioritaire de l'état parasitaire : ils se "
                "contrôlent plinthe déposée, avant toute reprise de sol ou de doublage.",
            "Les doublages et cloisons ajoutés lors des divisions et des "
                "surélévations postérieures se sondent avant dépose : l'âge des murs ne "
                "présume rien de la date de pose de ce qui les habille.",
            "Dans les circulations communes d'un immeuble antérieur à 1949, les "
                "peintures de couloir, d'escalier et de menuiseries se mesurent par "
                "fluorescence X unité par unité, avant tout décapage — un repeint "
                "n'écarte pas la sous-couche.",
            "Sur une couverture en tuiles canal, ce sont les ouvrages de rive et les "
                "éléments de raccord mis à nu par la dépose qui appellent le repérage, "
                "avant l'intervention du couvreur.",
            "Le mur mitoyen et la jonction de couverture avec la construction voisine "
                "se relèvent avant tout devis de ravalement ou de couverture : ils "
                "déterminent ce qui, du programme, sort du périmètre du syndicat.",
        ],
    ),

    "bordeaux/grand-parc": dict(
        methode="Tout part du programme détaillé des travaux. C'est lui qui fixe la liste "
                "des matériaux à rechercher et le périmètre du repérage ; l'opérateur "
                "soumet l'un et l'autre au donneur d'ordre pour avis avant la moindre "
                "investigation, et un rapport établi sans cette étape est contestable. "
                "Sur un parc occupé, la difficulté suivante est l'accès. Le repérage ne "
                "s'arrête pas aux parties communes : dès que le programme touche "
                "menuiseries, gaines ou sols des logements, il faut entrer chez les "
                "occupants. L'échantillonnage couvre chaque typologie de logement et "
                "chaque cage — un sondage ne vaut que pour l'ouvrage qu'il traverse — et "
                "le calendrier de visite se construit avec celui du relogement "
                "temporaire, pas après lui. Les sondages étant destructifs, chaque point "
                "ouvert se rebouche dans la journée : la remise en état fait partie de la "
                "prestation et se chiffre à la commande. Enfin, les campagnes de "
                "réhabilitation déjà conduites laissent des rapports et des attestations "
                "de retrait : les intégrer évite de redécouvrir ce qui a déjà été traité.",
        cadre="Le repérage avant travaux relève du code du travail, articles R. 4412-97 "
              "et suivants, et de l'arrêté du 16 juillet 2019. L'opérateur doit être "
              "certifié avec mention (arrêté du 25 juillet 2016). Aucune date n'exclut "
              "cette obligation. Le dossier technique amiante des parties communes "
              "(articles R. 1334-14 et suivants du code de la santé publique) ne couvre "
              "que les listes A et B et n'en dispense jamais. Selon les matériaux "
              "touchés, les travaux relèveront ensuite du retrait ou encapsulage, "
              "réservé aux entreprises certifiées, ou de l'intervention sur matériaux "
              "susceptibles d'émettre des fibres.",
        points=[
            "Dans les halls, les paliers et les caves, le revêtement de sol et sa "
                "colle se sondent sur toute l'épaisseur du complexe avant toute reprise, "
                "les couches successives se traversant jusqu'au support.",
            "Les gaines techniques et leurs trappes de visite s'ouvrent et se sondent "
                "avant tout remplacement de colonne : l'habillage ne dit rien de ce qu'il "
                "couvre.",
            "Aux menuiseries, ce sont les calfeutrements, les mastics et les tableaux "
                "de baie qui se repèrent avant dépose, et non le châssis lui-même.",
            "Dans les locaux techniques, calorifugeages, joints de brides et "
                "garnitures se contrôlent avant toute intervention d'un mainteneur : le "
                "donneur d'ordre est le maître d'ouvrage de l'immeuble, pas l'entreprise "
                "qui intervient.",
            "En logement occupé, le point de sondage se choisit pour pouvoir être "
                "rebouché le jour même : un ouvrage traversé sans remise en état "
                "immédiate bloque la poursuite de la campagne.",
        ],
    ),

    "bordeaux/saint-seurin": dict(
        methode="Sur ce bâti, la mission se prépare bâtiment par bâtiment plutôt que par "
                "adresse : un immeuble de pierre et un collectif inséré dans le même "
                "patrimoine n'appellent ni le même programme de sondages ni les mêmes "
                "locaux à ouvrir. Le repérage commence par le haut, parce que c'est "
                "l'accès qui commande : couverture en ardoise ou en zinc, noues, solins "
                "et combles supposent une trappe dégagée, une échelle ou une nacelle, et "
                "parfois une autorisation d'occupation du domaine public lorsque le "
                "montage se prend depuis la rue. Vient ensuite la cage d'escalier, où la "
                "mesure du plomb des parties communes se conduit unité de diagnostic par "
                "unité de diagnostic — chaque menuiserie, chaque garde-corps, chaque "
                "paroi : la durée y tient au nombre de niveaux, pas à la surface. Les "
                "locaux techniques ferment le parcours, machinerie d'ascenseur et caves "
                "n'étant le plus souvent accessibles qu'avec la clé du prestataire "
                "d'entretien, à réclamer dès la commande.",
        cadre="1334-5 et suivants) et porte alors sur tous leurs revêtements, quelle "
              "que soit la date de pose. Le dossier technique amiante des parties "
              "communes (articles R. 1334-14 et suivants) s'impose aux immeubles dont "
              "le permis de construire a été délivré avant le 1er juillet 1997 : listes "
              "A et B, jamais la liste C, donc aucune dispense de repérage avant "
              "travaux. Ce dernier procède du code du travail (articles R. 4412-97 et "
              "suivants, arrêté du 16 juillet 2019) et ne connaît aucune date "
              "d'exclusion. Le plan pluriannuel de travaux s'applique enfin, depuis le "
              "1er janvier 2025, aux syndicats d'au plus cinquante lots dont le permis "
              "de construire a été délivré depuis plus de quinze ans.",
        points=[
            "Dans une cage d’escalier d’immeuble d’habitation antérieur à 1949, les "
                "revêtements des parties communes — peintures de rampe, de plinthes, de "
                "portes palières — relèvent tous du constat, quelle que soit la date du "
                "dernier repeint. Le contrôle précède la consultation des peintres, pas "
                "leur arrivée sur place.",
            "Sur une couverture en ardoise ou en zinc, mastics de solin, "
                "calfeutrements de noue et enduits de raccord se sondent avant la reprise "
                ": ce sont des ouvrages ponctuels, que le devis chiffre au mètre linéaire "
                "sans les avoir fait contrôler.",
            "La gaine et la machinerie d’un ascenseur ancien concentrent joints, "
                "garnitures de frein et habillages de câblage. Ces éléments se font "
                "repérer avant toute modernisation de cabine ou remplacement de treuil, "
                "l’entreprise d’ascenseurs intervenant au titre du code du travail.",
            "Sur un plancher associant solives bois et poutrelles métalliques, le "
                "remplissage entre solives et le doublage rapporté lors d’une rénovation "
                "se sondent avant toute reprise de sol ou création de trémie : "
                "l’épaisseur réelle du complexe ne se lit pas depuis la surface.",
            "Sur une façade en pierre de taille, les mastics de calfeutrement des "
                "menuiseries et les enduits de rebouchage des reprises anciennes se "
                "prélèvent avant le montage de l’échafaudage, faute de quoi les sondages "
                "imposent un second passage et une seconde immobilisation de voirie.",
        ],
    ),

    "bordeaux/la-bastide": dict(
        methode="Deux missions cohabitent ici, avec deux donneurs d'ordre et deux "
                "calendriers, et la première décision consiste à ne pas les confondre. "
                "Sur un atelier ou un entrepôt voué à disparaître, le repérage se conduit "
                "bâtiment libéré : investigations destructives autorisées, reconnaissance "
                "en hauteur des charpentes, bardages et sous-faces de couverture inscrite "
                "au programme de la visite, périmètre arrêté avec le maître d'ouvrage "
                "phase par phase avant l'émission du devis. Enfin, le rapport énonce ce "
                "qu'il ne couvre pas : un repérage de matériaux ne renseigne ni la "
                "qualité des sols ni la mémoire industrielle d'une parcelle, qui relèvent "
                "d'une étude commandée en parallèle à un bureau spécialisé.",
        cadre="Sur les opérations de rénovation, le repérage amiante avant travaux "
              "procède du code du travail (articles R. 4412-97 et suivants, décret n° "
              "2017-899 du 9 mai 2017 modifié, arrêté du 16 juillet 2019). Il incombe "
              "au donneur d’ordre et se remet aux entreprises dès leur consultation, "
              "non au marché signé ; aucune date de construction n’en dispense. Le "
              "diagnostic portant sur les produits, équipements, matériaux et déchets "
              "s’y ajoute en rénovation significative — dès que l’opération détruit ou "
              "remplace au moins deux éléments de second œuvre — sous condition de "
              "surface de plancher cumulée ou d’activité passée ayant mis en œuvre des "
              "substances dangereuses. Dans les immeubles d’habitation construits avant "
              "le 1er janvier 1949, le constat de risque d’exposition au plomb des "
              "parties communes reste dû et porte sur l’ensemble de leurs revêtements. "
              "Un repérage de matériaux ne vaut en revanche aucune investigation sur "
              "les sols.",
        points=[
            "Lorsqu’un atelier est couvert ou bardé en fibres-ciment, les plaques ne "
                "sont qu’une part du poste : closoirs, faîtières, costières et fixations "
                "se comptent au même titre. Ce relevé se fait pendant le repérage, jamais "
                "au pied de la benne.",
            "Sous la dalle d’un atelier, regards, caniveaux et fourreaux traversant "
                "le plancher bas portent des joints et des mortiers de scellement à "
                "contrôler avant le curage : une fois la dalle attaquée, la localisation "
                "d’origine n’est plus reconstituable.",
            "Ils se mesurent avant la pose d'une isolation intérieure ou d'un "
                "habillage, qui les rendent inaccessibles.",
            "Avant une isolation par l’extérieur, les mastics de calfeutrement des "
                "menuiseries et les appuis de baie se sondent façade par façade : ce sont "
                "les ouvrages que la dépose des menuiseries met à nu, et ils sortent du "
                "champ du dossier technique amiante des parties communes.",
            "Les remblais et les terres excavées d’une ancienne emprise ne relèvent "
                "d’aucun repérage de matériaux : leur caractérisation se commande au "
                "moment du montage du dossier d’opération, pas à l’ouverture du chantier.",
        ],
    ),

    "bordeaux/belcier-euratlantique": dict(
        methode="Ici la mission se planifie à rebours de l’opération : la date qui compte "
                "n’est pas celle de la visite mais celle du dépôt de la demande "
                "d’autorisation et de la consultation des entreprises, et tout ce qui "
                "remonte en amont doit tenir dans cet intervalle. Le repérage avant "
                "démolition se conduit sur bâtiment libéré, à périmètre exhaustif : liste "
                "C comprise, ouverture des ouvrages, dépose ponctuelle des habillages et "
                "des revêtements superposés pour atteindre ce que la surface masque. "
                "C’est ce poste qui fait la durée, et il ne se comprime pas. Sur les "
                "maisons de faubourg conservées au milieu d’une opération, la logique "
                "change : bâti occupé ou en attente, visites sur rendez-vous, mesure du "
                "plomb des parties communes et sondages amiante groupés dans un même "
                "passage. Trois pièces réclamées à la commande décident du reste : le "
                "phasage réel du chantier, qui borne les périmètres ; les autorisations "
                "d’urbanisme successives, qui datent les couches de travaux ; les "
                "rapports et attestations de retrait antérieurs, sans lesquels on "
                "redécouvre ce qui a déjà été traité. Un matériau non repéré ne coûte pas "
                "un sondage, il coûte un arrêt et un avenant.",
        cadre="Le repérage avant démolition et le repérage avant travaux partagent le "
              "même socle — code du travail, articles R. 4412-97 et suivants, arrêté du "
              "16 juillet 2019, norme NF X 46-020 d’août 2017 — mais pas le même "
              "périmètre. Conduit selon cette norme, un repérage avant démolition vaut "
              "repérage avant travaux, sa recherche étant plus large ; l’inverse est "
              "faux, et un repérage avant travaux ne peut jamais tenir lieu de repérage "
              "avant démolition. Ni l’un ni l’autre ne connaît de date d’exclusion. S’y "
              "ajoute le diagnostic portant sur les produits, équipements, matériaux et "
              "déchets, établi avant le dépôt de la demande de permis de démolir ou, à "
              "défaut, avant l’acceptation des devis, et dont le formulaire de "
              "récolement se transmet à l’organisme désigné une fois les travaux "
              "achevés. Les immeubles d’habitation construits avant le 1er janvier 1949 "
              "relèvent en outre du constat de risque d’exposition au plomb des parties "
              "communes.",
        points=[
            "Sur une maison de faubourg conservée et construite avant 1949, les "
                "peintures de l’escalier et des menuiseries des parties communes se "
                "mesurent avant le curage : les revêtements arrachés, l’unité de "
                "diagnostic n’existe plus et le constat ne peut plus être établi.",
            "Dans un entrepôt ou une emprise ferroviaire, les enduits et mortiers de "
                "scellement des ouvrages traversants — fourreaux, réservations, socles de "
                "machines — se sondent pendant le repérage avant démolition et non au "
                "curage, la liste C n’étant atteinte qu’en investigation destructive.",
            "Dans un local réaménagé, le sol se relève par carottage sur toute son "
                "épaisseur : un sondage arrêté à la première couche laisse hors rapport "
                "les revêtements et les colles qui subsistent en dessous.",
            "Les cloisons et faux-plafonds déposés lors d’une restructuration de "
                "bureaux relèvent du repérage avant travaux, y compris sur un immeuble "
                "récent : le code du travail ne fixe aucune date en deçà de laquelle le "
                "donneur d’ordre en serait dispensé.",
            "Sur une opération mixte, la limite entre partie démolie et partie "
                "conservée se matérialise sur plan avant la visite : une zone laissée "
                "dans l’intervalle sort du périmètre des deux missions et ressort en "
                "cours d’exécution.",
        ],
    ),

    "bordeaux/le-lac-aubiers": dict(
        methode="La commande émane d’un maître d’ouvrage public ou d’un bailleur, et le "
                "rapport partira en pièce annexe d’un marché : cette destination organise "
                "la mission avant même la technique. Le repérage se structure local par "
                "local, sur le plan qui servira à la consultation et avec la numérotation "
                "du dossier : des repères qui ne coïncident pas avec les plans du marché "
                "obligent l’entreprise à refaire le travail de localisation, et se paient "
                "en questions pendant la consultation. La deuxième décision se prend à la "
                "commande : sur un hall ou un bâtiment technique, l’immeuble bâti et les "
                "équipements concourant à une activité ne relèvent pas du même "
                "référentiel, et une seule mission ne couvre pas les deux ; le périmètre "
                "se tranche par écrit. Vient ensuite l’accès : les volumes de grande "
                "hauteur imposent une reconnaissance depuis une nacelle et une "
                "coordination avec l’exploitant, qui se réservent, tandis que les "
                "logements supposent un calendrier de visites. À réunir avant "
                "l’intervention : plans cotés, inventaire des locaux, rapports et "
                "attestations de retrait antérieurs, et le phasage "
                "démolition-conservation.",
        cadre="Le repérage relève du code du travail (articles R. 4412-97 et suivants) "
              "et, pour les immeubles bâtis, de l’arrêté du 16 juillet 2019, dont la "
              "mise en œuvre s’appuie sur la norme NF X 46-020 d’août 2017 : la liste "
              "minimale des matériaux à rechercher est fixée par son tableau A1, en "
              "fonction du programme détaillé des travaux communiqué par le donneur "
              "d’ordre. Les installations, structures et équipements concourant à la "
              "réalisation d’une activité relèvent d’un autre référentiel, la norme NF "
              "X 46-100, encadrée par l’arrêté du 22 juillet 2021 : deux domaines, deux "
              "missions distinctes. L’opérateur doit être certifié avec mention (arrêté "
              "du 25 juillet 2016) et indépendant du donneur d’ordre comme de "
              "l’entreprise de travaux, vérification que l’acheteur public opère sur "
              "l’annuaire des diagnostiqueurs certifiés. Aucune de ces obligations "
              "n’est bornée par une date de construction.",
        points=[
            "Chaque matériau repéré est reporté avec son local, son ouvrage et sa "
                "quantité. Une mention « présence d’amiante dans les circulations », sans "
                "métré ni report sur plan, n’est pas exploitable par une entreprise de "
                "retrait et revient en question de consultation.",
            "Dans un volume de grande hauteur, sous-faces de couverture, chéneaux et "
                "lanterneaux se reconnaissent depuis une nacelle : un repérage conduit "
                "depuis le sol laisse hors rapport les matériaux les plus volumineux du "
                "bâtiment.",
            "En local technique, calorifugeages de réseaux, joints de brides et "
                "tresses de robinetterie se relèvent avant l’arrêt d’exploitation : ce "
                "sont des éléments démontables, qui disparaissent au premier curage et ne "
                "se retrouvent plus au métré.",
            "Les faux-plafonds et habillages de circulation se déposent "
                "ponctuellement pendant la visite : ce qu’ils masquent n’entre au rapport "
                "que s’il a été vu, et une réserve de non-accès se lit comme une zone à "
                "re-repérer en cours de chantier.",
            "Les locaux de faible surface — annexes, réserves, locaux techniques — se "
                "relèvent au même passage que les logements : conduits, coudes et "
                "descentes y courent en plafond, et ce sont les volumes que les "
                "inventaires établis sur plan oublient.",
        ],
    ),

    "bordeaux/saint-augustin": dict(
        methode="La mission commence au bureau : on reprend le dossier technique amiante "
                "des parties communes, sa date, les matériaux qu’il liste et les "
                "évaluations périodiques de leur état de conservation. Un dossier ancien "
                "et jamais réévalué n’est pas un document à jour ; la visite sert d’abord "
                "à vérifier ce qu’il affirme. Sur site, l’ordre est dicté par "
                "l’exploitation. La chaufferie d’abord : local fermé, clé détenue par le "
                "prestataire d’entretien, visite à caler hors période de chauffe et à "
                "réserver plusieurs semaines à l’avance. Les gaines techniques ensuite, "
                "trappe par trappe, en montant les niveaux. Les halls et les caves enfin, "
                "où les revêtements superposés imposent un sondage sur toute l’épaisseur. "
                "Deux points allongent l’intervention : évaluer l’état de conservation "
                "suppose d’atteindre physiquement chaque matériau déjà identifié, non de "
                "recopier un inventaire ; et dès qu’un programme de travaux est arrêté, "
                "le dossier technique ne suffit plus, un repérage avant travaux se "
                "conduit en complément. À réunir avant la visite : plans de réseaux, "
                "contrats d’exploitation, rapports antérieurs, et la fiche "
                "récapitulative, qui doit être remise à toute entreprise appelée à "
                "intervenir.",
        cadre="Le dossier technique amiante des parties communes est dû pour les "
              "immeubles bâtis dont le permis de construire a été délivré avant le 1er "
              "juillet 1997 (code de la santé publique, articles R. 1334-14 et "
              "suivants). Il porte sur les listes A et B, sans investigation "
              "destructive, se tient à jour au fil des évaluations périodiques de "
              "l’état de conservation et des travaux réalisés, et sa fiche "
              "récapitulative se remet à toute entreprise appelée à intervenir. Ses "
              "limites sont nettes : il ne couvre pas la liste C et ne dispense d’aucun "
              "repérage avant travaux. Ce dernier procède du code du travail (articles "
              "R. 4412-97 et suivants, arrêté du 16 juillet 2019) et ne connaît aucune "
              "date d’exclusion. S’ajoutent le plan pluriannuel de travaux — permis de "
              "construire délivré depuis plus de quinze ans — et le DPE collectif, "
              "applicable depuis le 1er janvier 2026 aux syndicats d’au plus cinquante "
              "lots.",
        points=[
            "En chaufferie, les extrémités de calorifugeage — coudes, piquages, "
                "brides — sont les zones dégradées et empoussiérées : ce sont elles qui "
                "se contrôlent, l’état d’un tronçon droit ne préjugeant jamais de celui "
                "d’un raccord.",
            "Sous un sol de hall refait, l’ancien revêtement et sa colle n’ont "
                "presque jamais été déposés : le sondage se fait par carottage jusqu’au "
                "support, et il se répète au droit des seuils et des plinthes, où "
                "l’épaisseur du complexe change.",
            "En cave, conduits, coudes et descentes en amiante-ciment courent en "
                "plafond au-dessus des stockages : le repérage suppose des allées "
                "dégagées, à faire libérer par le syndic avant la date d’intervention.",
        ],
    ),

    "merignac/arlac": dict(
        methode="Sur une copropriété issue de division, la mission commence avant la "
                "visite : identifier le donneur d'ordre, puis reconstituer le périmètre "
                "des parties communes à partir du règlement et de l'état descriptif de "
                "division. La visite s'ordonne ensuite du plus contraint au plus simple : "
                "cage d'escalier et couloirs d'accès d'abord, où le constat plomb des "
                "parties communes et la recherche des matériaux amiantés apportés "
                "après-guerre se conduisent dans le même passage ; caves, combles et "
                "local des compteurs ensuite, parce que c'est là que se logent les "
                "réseaux ajoutés au fil des travaux. Ce qui fait durer l'intervention "
                "n'est pas la technique, c'est l'absence d'interlocuteur unique et de "
                "plans, qui oblige à reconstituer les couches de travaux sur place. À "
                "préparer avant la venue : la désignation d'un représentant du syndicat, "
                "les clés de tous les locaux communs, et l'accord écrit sur les sondages "
                "destructifs et leur remise en état.",
        cadre="Trois régimes se superposent ici. Sur les immeubles d’habitation "
              "construits avant le 1er janvier 1949, le constat de risque d’exposition "
              "au plomb des parties communes porte sur tous les revêtements, quelle que "
              "soit leur date de pose (code de la santé publique, articles L. 1334-5 et "
              "suivants ; protocole NF X 46-030). Le repérage amiante avant travaux "
              "relève du code du travail — articles R. 4412-97 et suivants, arrêté du "
              "16 juillet 2019, norme NF X 46-020 : il pèse sur le donneur d’ordre et "
              "ne connaît aucune date d’exclusion, y compris sur une construction "
              "récente. Le plan pluriannuel de travaux, enfin, vise les immeubles à "
              "destination partielle ou totale d’habitation dont le permis de "
              "construire a été délivré depuis plus de quinze ans ; le diagnostic "
              "technique global en constitue l’état des lieux préalable.",
        points=[
            "Dans une cage d’escalier antérieure à 1949, les peintures des portes "
                "palières, des embrasures et de la rampe relèvent du constat plomb des "
                "parties communes : la mesure se fait unité de diagnostic par unité de "
                "diagnostic, avant tout ponçage ou décapage.",
            "Les conduits de fumée et de ventilation en amiante-ciment traversant les "
                "niveaux d’un immeuble de rapport se contrôlent avant toute reprise de "
                "colonne ou modification de sortie en toiture.",
            "Les mastics et joints des menuiseries de cage d’escalier se prélèvent "
                "avant dépose, dans toute opération de remplacement engagée au titre "
                "d’une rénovation énergétique.",
            "Dans les caves et les locaux de compteurs, les habillages isolants des "
                "canalisations ajoutées au fil des travaux se repèrent avant "
                "l’intervention d’un plombier ou d’un mainteneur, l’analyse en "
                "laboratoire étant seule concluante.",
        ],
    ),

    "merignac/capeyron": dict(
        methode="Sur ces petits collectifs, la mission part rarement de zéro : un dossier "
                "technique amiante des parties communes existe, mais il a été établi sans "
                "investigation destructive et n’a le plus souvent jamais été réévalué. Le "
                "premier travail est donc documentaire — relire ce dossier, ses annexes "
                "et ses éventuelles attestations de retrait, cerner ce qu’il ne couvre "
                "pas — avant d’arrêter le programme de la visite. Sur le terrain, l’ordre "
                "est dicté par les locaux qui ferment : local chaufferie, local des "
                "compteurs, caves et gaines techniques se visitent en premier, parce "
                "qu’ils concentrent les matériaux et parce qu’ils supposent une clé que "
                "personne n’a le jour dit. Halls et paliers suivent. Ce qui allonge "
                "l’intervention, ici, c’est la chaufferie maintenue en service et les "
                "trappes de gaine condamnées par des travaux antérieurs. À préparer : le "
                "dossier existant et les rapports antérieurs, les plans de réseaux s’ils "
                "subsistent, l’accès à tous les locaux techniques, et, si le programme "
                "touche les sols ou les menuiseries des logements, l’organisation en "
                "amont de l’accès aux parties privatives.",
        cadre="Deux textes se répondent sans se remplacer. Le dossier technique amiante "
              "des parties communes procède du code de la santé publique (articles R. "
              "1334-14 et suivants) : il porte sur les matériaux des listes A et B, "
              "sans investigation destructive, s’actualise au fil des évaluations "
              "périodiques de l’état de conservation, et sa fiche récapitulative se "
              "remet à toute entreprise appelée à intervenir. Il ne couvre jamais la "
              "liste C et ne dispense donc d’aucun repérage avant travaux. Celui-ci "
              "relève du code du travail (articles R. 4412-97 et suivants, arrêté du 16 "
              "juillet 2019, norme NF X 46-020), s’impose au donneur d’ordre avant "
              "toute opération, sans condition d’âge du bâtiment, et suppose un "
              "opérateur certifié avec mention, indépendant du donneur d’ordre comme de "
              "l’entreprise de travaux. Le plan pluriannuel de travaux, lui, vise les "
              "immeubles dont le permis de construire a été délivré depuis plus de "
              "quinze ans.",
        points=[
            "Conduits de ventilation en amiante-ciment logés dans les gaines : "
                "contrôlés avant tout remplacement d’extracteur ou reprise de colonne.",
            "Habillages isolants des canalisations et garnitures de robinetterie du "
                "local chaufferie : repérés à l’arrêt de chauffe, avant l’intervention du "
                "mainteneur, le syndicat des copropriétaires étant alors le donneur "
                "d’ordre.",
            "Mastics de vitrage et joints des menuiseries des parties communes : "
                "prélevés avant dépose, au moment de l’étude de la rénovation énergétique "
                "et non après l’attribution du marché.",
            "Plaques ondulées de couverture des garages et dépendances : le repérage "
                "précède la dépose, y compris pour une intervention ponctuelle, "
                "l’obligation pesant sur celui qui commande les travaux.",
        ],
    ),

    "merignac/le-burck": dict(
        methode="Le premier point à trancher n’est pas technique : en gestion mixte, "
                "plusieurs maîtres d’ouvrage peuvent intervenir sur un même bâtiment, et "
                "le repérage avant travaux pèse sur le donneur d’ordre de chaque "
                "opération. Le périmètre se fixe donc par écrit avant la visite — quels "
                "bâtiments, quelles cages, quels ouvrages, pour quel programme — faute de "
                "quoi deux missions se recouvrent ou, plus grave, laissent un vide. Vient "
                "ensuite l’échantillonnage : sur des immeubles répétitifs, un sondage ne "
                "vaut que pour l’ouvrage qu’il traverse, et le plan doit couvrir chaque "
                "typologie de logement et chaque configuration de cage. Le reste est une "
                "affaire de calendrier. Les sondages sont destructifs et les immeubles "
                "occupés : information des occupants, plages d’intervention, rebouchage "
                "et remise en état se calent avec le maître d’ouvrage, et le phasage du "
                "repérage suit celui du relogement temporaire. À préparer : le programme "
                "détaillé des travaux, les rapports et attestations de retrait des "
                "campagnes antérieures, les plans de cage, et la liste des logements "
                "accessibles par typologie.",
        cadre="Le repérage amiante avant travaux procède du code du travail : articles "
              "R. 4412-97 à R. 4412-97-6, arrêté du 16 juillet 2019, norme NF X 46-020 "
              "d’août 2017. Il incombe au donneur d’ordre de chaque opération — "
              "syndicat des copropriétaires ou bailleur selon le maître d’ouvrage — et "
              "se remet aux entreprises dès leur consultation, non à la signature du "
              "marché. Le périmètre et le programme de repérage sont transmis au "
              "donneur d’ordre pour avis avant toute investigation sur site ; un "
              "rapport établi sans cette étape est contestable. L’opérateur doit être "
              "certifié avec mention. Côté copropriété, le plan pluriannuel de travaux "
              "vise les immeubles dont le permis de construire a été délivré depuis "
              "plus de quinze ans, se projette sur dix ans, s’adopte en assemblée "
              "générale, et sert de référence au calcul de la cotisation annuelle au "
              "fonds de travaux.",
        points=[
            "Colles de dalles de sol des halls, paliers et logements : le sondage "
                "descend sous les revêtements ajoutés par les réhabilitations "
                "successives, avant toute reprise de sol.",
            "Habillages isolants des canalisations de chauffage, en sous-sol et en "
                "chaufferie : repérés à l’arrêt de chauffe, avant toute reprise de "
                "réseau.",
            "Plaques d’habillage et trappes de gaine palière : ouvertes pendant la "
                "visite de repérage et non le jour du chantier, avant toute intervention "
                "sur les colonnes.",
            "Enduits et rebouchages des traversées de plancher autour des "
                "canalisations : sondés avant percement, chaque sondage ne valant que "
                "pour l’ouvrage traversé.",
        ],
    ),

    "merignac/centre": dict(
        methode="Deux missions cohabitent ici et ne se conduisent pas de la même façon. "
                "Sur l’habitat voué à disparaître, le repérage se fait bâtiment libéré et "
                "fluides coupés : sondages destructifs sans réserve, déposes partielles "
                "pour atteindre colles, calorifugeages et matériaux masqués, recherche "
                "étendue à la liste C. La date de visite se cale donc sur la libération "
                "effective des lieux, préalable qui se planifie avec le maître d’ouvrage "
                "dès la commande. Sur les copropriétés conservées, la logique est inverse "
                ": le diagnostic technique global établit l’état apparent des parties "
                "communes et des équipements, le plan pluriannuel s’en sert pour "
                "hiérarchiser les postes, et chaque poste appelle ensuite son propre "
                "repérage au moment du chiffrage. Sur une opération mixte, tout se joue "
                "sur le phasage : le périmètre du repérage se découpe par phase et par "
                "lot de travaux, avec des plans cotés, sinon des zones se découvrent hors "
                "périmètre en cours de chantier. À préparer : autorisations d’urbanisme, "
                "calendrier de libération, plans, et le programme détaillé des travaux "
                "phase par phase.",
        cadre="Le repérage avant démolition et le repérage avant travaux partagent le "
              "même socle — code du travail, articles R. 4412-97 et suivants, arrêté du "
              "16 juillet 2019, norme NF X 46-020 — mais pas le même périmètre. Conduit "
              "selon cette norme, un repérage avant démolition vaut repérage avant "
              "travaux, son champ étant plus large ; l’inverse n’est jamais vrai. S’y "
              "ajoute le diagnostic portant sur les produits, équipements, matériaux et "
              "déchets, dû en démolition comme en rénovation significative dès que le "
              "bâtiment dépasse mille mètres carrés de surface de plancher ou qu’il a "
              "accueilli une activité mettant en œuvre des substances dangereuses ; il "
              "s’établit avant le dépôt de la demande de permis de démolir ou, à "
              "défaut, avant l’acceptation des devis. Sur les copropriétés conservées, "
              "le plan pluriannuel de travaux vise les immeubles dont le permis de "
              "construire a été délivré depuis plus de quinze ans.",
        points=[
            "Dans un logement libéré avant démolition, les colles de dalles de sol se "
                "recherchent sous chaque revêtement rapporté : le sondage descend "
                "jusqu’au support, la dépose partielle étant possible sur bâtiment vidé.",
            "Les enduits, mastics et rebouchages des traversées de plancher et de "
                "gaine relèvent de la liste C : ils se sondent au repérage avant "
                "démolition, pas au moment du curage.",
            "Dans les copropriétés conservées, les dalles et colles de sol des halls, "
                "caves et locaux communs se contrôlent avant toute reprise de sol "
                "inscrite au plan pluriannuel.",
            "À l’interface entre partie conservée et partie démolie, calfeutrements, "
                "solins et habillages de joint se repèrent avant le sciage de séparation, "
                "sur les deux faces de la limite.",
            "Dans les caves et vides sanitaires d’un immeuble à démolir, les "
                "calorifugeages de réseaux abandonnés restent en place : le repérage "
                "descend dans ces volumes avant la coupure des accès.",
        ],
    ),

    "merignac/beutre": dict(
        methode="Sur un bâtiment d'activité destiné à la déconstruction, le repérage se "
                "conçoit d'emblée comme un quantitatif, puisque c'est le métré des "
                "matériaux amiantés qui commande le budget et le phasage. Cela change la "
                "façon de visiter : les surfaces se relèvent façade par façade et pan par "
                "pan, les linéaires se comptent, et chaque quantité se rattache à un "
                "local identifié sur un plan coté, de sorte que le rapport soit "
                "exploitable en pièce annexe de consultation. L'accès en hauteur est le "
                "premier point à régler avant la venue : une couverture en plaques de "
                "fibres-ciment ne se parcourt pas, la reconnaissance se fait depuis "
                "l'intérieur du volume ou depuis un moyen d'accès mis à disposition, à "
                "prévoir dans la commande. Le bâtiment doit être libéré et les "
                "installations à l'arrêt. À préparer : plans, historique d'activité du "
                "site, autorisations d'accès.",
        cadre="Le repérage avant travaux comme avant démolition relève du code du "
              "travail (articles R. 4412-97 et suivants, arrêté du 16 juillet 2019, "
              "norme NF X 46-020) : aucune date de construction n’en dispense un "
              "bâtiment, fût-il récent. Attention au domaine : les installations, "
              "structures et équipements concourant à une activité relèvent d’un autre "
              "référentiel — norme NF X 46-100, arrêté du 22 juillet 2021 — et forment "
              "une mission distincte de celle du bâti. Le diagnostic portant sur les "
              "produits, équipements, matériaux et déchets s’ajoute dès mille mètres "
              "carrés de surface de plancher, ou dès lors que le bâtiment a abrité une "
              "activité mettant en œuvre des substances dangereuses. Le constat de "
              "risque d’exposition au plomb des parties communes, enfin, ne vise que "
              "les immeubles d’habitation construits avant le 1er janvier 1949 ; hors "
              "de ce champ, le risque plomb des peintures se traite au titre de la "
              "protection des salariés.",
        points=[
            "Bardages en plaques planes de fibres-ciment : métrés façade par façade, "
                "accessoires de fixation et cornières compris, avant tout chiffrage de "
                "déconstruction.",
            "Plaques ondulées de couverture : reconnues depuis l’intérieur du volume "
                "ou depuis un moyen d’accès en hauteur, jamais en charge sur la plaque, "
                "au moment de la visite de repérage.",
            "Descentes d’eaux pluviales et conduits en amiante-ciment : comptés en "
                "mètres linéaires au même titre que la couverture, faute de quoi le métré "
                "remis au marché est sous-évalué.",
            "Dans les ateliers, joints, tresses et habillages isolants des réseaux et "
                "des appareils fixes : repérés installation à l’arrêt, avant dépose des "
                "équipements.",
            "Sur les dépendances du pavillonnaire, plaques et conduits en "
                "fibres-ciment : leur évacuation se prépare dès l’étude, l’exutoire et le "
                "bordereau de suivi des déchets d’amiante conditionnant la dépose.",
        ],
    ),

    "merignac/chemin-long": dict(
        methode="Ici, la difficulté n’est pas le sondage, c’est le périmètre. Sur un bâti "
                "dont l’histoire est mixte — corps principal d’une époque, extensions et "
                "annexes d’une autre —, le repérage ne se cale pas sur le bâtiment mais "
                "sur le programme détaillé des travaux : on liste ouvrage par ouvrage ce "
                "que l’opération va toucher, puis on remonte aux autorisations "
                "d’urbanisme successives pour dater chaque couche. Une extension ou une "
                "annexe laissée hors de cette liste ne sera pas repérée, et se découvrira "
                "en cours de chantier. Le périmètre et le programme de repérage sont "
                "ensuite transmis au donneur d’ordre pour avis, avant toute investigation "
                "sur site : cette étape conditionne la solidité du rapport et se traite "
                "au moment de la commande, pas de la visite. Sur les copropriétés "
                "récentes, le raisonnement ne change pas : l’obligation demeure, seul "
                "varie le nombre de sondages que la présomption justifie. À préparer : le "
                "programme détaillé des travaux, permis et déclarations préalables, plans "
                "des extensions, clés des annexes et des locaux techniques.",
        cadre="Le repérage amiante avant travaux relève du code du travail — articles "
              "R. 4412-97 et suivants, arrêté du 16 juillet 2019, norme NF X 46-020 — "
              "et l’obligation pèse sur le donneur d’ordre préalablement à toute "
              "opération, sans qu’aucune date de construction n’écarte un bâtiment du "
              "champ. La date du 1er juillet 1997 borne le champ du code de la santé "
              "publique, celui du dossier technique amiante des parties communes ; elle "
              "fonde une présomption qui guide le plan de sondage, elle ne dispense de "
              "rien. La liste minimale des matériaux à rechercher est fixée par le "
              "tableau A1 de la norme, en fonction du programme détaillé des travaux "
              "communiqué par le donneur d’ordre. Le plan pluriannuel de travaux vise, "
              "lui, les immeubles dont le permis de construire a été délivré depuis "
              "plus de quinze ans : les copropriétés récentes y entrent à mesure que "
              "leur permis franchit ce seuil.",
        points=[
            "Dalles de sol et colles bitumineuses : le sondage se répète dans chaque "
                "partie de bâtiment d’époque différente, une couche déposée dans le corps "
                "principal pouvant subsister dans l’extension.",
            "Joints et mastics de menuiserie, y compris ceux des baies d’extension : "
                "prélevés avant dépose, sur chaque type de châssis rencontré.",
            "Aux jonctions entre corps principal et extension, calfeutrements, solins "
                "et habillages se sondent avant tout percement ou reprise de liaison.",
            "Dans les parties communes des résidences, les enduits et rebouchages des "
                "percements de réseaux se sondent avant toute reprise de distribution ou "
                "pose d’équipement en applique.",
        ],
    ),

    "pessac/centre": dict(
        methode="La mission commence par une qualification du syndicat : nombre de lots, "
                "existence ou non d’un syndic professionnel, et définition des parties "
                "communes telle que le règlement la fixe. Sur un immeuble issu d’une "
                "division, cette étape borne le périmètre, car un ouvrage que le "
                "règlement qualifie de privatif sort du champ de la commande passée par "
                "le syndicat. Vient ensuite le dépouillement des autorisations "
                "d’urbanisme et des factures d’entretien disponibles : elles datent les "
                "couches de travaux et permettent d’arrêter le nombre de sondages sur "
                "plan, avant la visite. Sur site, le repérage suit le cheminement d’une "
                "entreprise : hall, cage d’escalier, paliers, puis caves et combles, "
                "volumes que le conseil syndical n’a parfois jamais ouverts. Ce qui fait "
                "durer l’intervention n’est pas la surface, mais le nombre d’ouvrages à "
                "traiter séparément et la recherche des clés des locaux communs. À réunir "
                "avant notre venue : un référent joignable, les clés de tous les communs, "
                "et la liste des travaux engagés depuis la division.",
        cadre="Trois régimes se croisent sur un même immeuble. Le repérage amiante "
              "avant travaux et avant démolition relève du code du travail, articles R. "
              "4412-97 et suivants, et de l’arrêté du 16 juillet 2019 : il pèse sur le "
              "donneur d’ordre — ici le syndicat des copropriétaires — préalablement à "
              "toute opération, et ne connaît aucune date d’exclusion. La borne du 1er "
              "juillet 1997 ne concerne que le dossier technique amiante des parties "
              "communes, relevant du code de la santé publique. Le constat de risque "
              "d’exposition au plomb vise les immeubles d’habitation construits avant "
              "le 1er janvier 1949 et porte alors sur tous les revêtements des parties "
              "communes, quelle que soit leur date de pose. Enfin le plan pluriannuel "
              "de travaux s’impose lorsque le permis de construire a été délivré depuis "
              "plus de quinze ans : pour les syndicats d’au plus cinquante lots, "
              "l’échéance est passée depuis le 1er janvier 2025.",
        points=[
            "Dans une cage d’escalier d’immeuble d’habitation antérieur à 1949, la "
                "mesure du plomb porte sur chaque unité de diagnostic — mur, plinthe, "
                "garde-corps, porte palière — et sur tous les revêtements des parties "
                "communes, quelle que soit leur date de pose. Elle précède tout ponçage "
                "et tout décapage.",
            "Dans une échoppe divisée en deux ou trois lots, la limite entre ouvrage "
                "commun et ouvrage privatif se lit dans le règlement avant le premier "
                "sondage : un plancher séparatif reste commun quand le revêtement qui le "
                "couvre ne l’est pas.",
            "Les panneaux support de tableau électrique et les cloisons du local "
                "technique de rez-de-chaussée se contrôlent avant toute intervention d’un "
                "mainteneur : ce sont les premiers ouvrages ouverts en chantier et les "
                "moins documentés.",
            "Dans les caves et les combles d’un immeuble divisé, les réseaux se "
                "relèvent au fur et à mesure de leur cheminement, faute de plan de "
                "recollement : ces volumes se visitent éclairés et dégagés, sans quoi la "
                "mission se conclut par une réserve.",
        ],
    ),

    "pessac/saige": dict(
        methode="Sur un ensemble de cette taille, l’ordre des opérations décide du coût. "
                "La visite s’ouvre par ce qui s’atteint sans occupant : sous-sols, "
                "chaufferie, locaux de colonnes, gaines palières, halls et circulations. "
                "Cette première passe arrête la nature et le nombre des sondages "
                "destructifs, donc le budget, avant que la campagne en logement ne soit "
                "engagée. L’accès aux logements se planifie ensuite par cage et par "
                "niveau plutôt que par bâtiment entier : une équipe couvre un nombre "
                "limité de logements par jour, chaque sondage destructif imposant une "
                "protection ponctuelle et une remise en état immédiate. La durée d’une "
                "mission tient au taux de présence des occupants, jamais au métré. Deux "
                "points se règlent à la commande : la désignation du donneur d’ordre "
                "bâtiment par bâtiment, un même ensemble pouvant relever du syndicat pour "
                "l’un et d’un bailleur pour l’autre ; et le sort des logements vacants, "
                "dont les clés doivent être disponibles le jour dit. La hauteur des "
                "immeubles impose enfin de traiter les façades depuis des moyens d’accès "
                "dédiés, à programmer avec le repérage et non après lui.",
        cadre="Le repérage avant travaux relève du code du travail, articles R. 4412-97 "
              "et suivants, et de l’arrêté du 16 juillet 2019, dont la norme NF X "
              "46-020 d’août 2017 fixe la méthode, sauf pour ses articles 4, 7, 11 et "
              "14. Deux conséquences pratiques : la liste minimale des matériaux "
              "recherchés se déduit du programme détaillé des travaux communiqué par le "
              "donneur d’ordre, et le périmètre de repérage lui est soumis pour avis "
              "avant toute investigation sur site — un rapport établi sans cette étape "
              "est contestable. La mission suppose un opérateur certifié avec mention, "
              "indépendant du donneur d’ordre comme de l’entreprise de travaux, et le "
              "rapport se remet aux entreprises dès leur consultation. Côté "
              "copropriété, les trois échéances du plan pluriannuel de travaux — 1er "
              "janvier 2023, 2024 et 2025 — sont aujourd’hui passées, quelle que soit "
              "la taille du syndicat.",
        points=[
            "Sur un remplacement de menuiseries, le mastic de vitrage, le "
                "calfeutrement en pied de dormant et l’enduit de rebouchage du tableau se "
                "sondent avant dépose : le matériau se loge à la jonction entre la "
                "menuiserie et le gros œuvre, non dans la menuiserie elle-même.",
            "Avant reprise d’une colonne d’alimentation ou d’évacuation, la traversée "
                "de plancher et son calfeutrement se contrôlent à chaque niveau : "
                "l’ouvrage se répète sur toute la hauteur du bâtiment et se révèle "
                "rarement identique d’un étage à l’autre.",
            "Le logement retenu comme témoin dans chaque cage se choisit sur plan "
                "avant la visite, et non parmi ceux dont l’occupant a répondu le premier "
                ": un échantillon constitué par disponibilité produit une couverture "
                "inégale d’un bâtiment à l’autre.",
            "Dans les circulations, le joint de dilatation entre corps de bâtiment et "
                "son mastic se contrôlent avant toute reprise de sol ou de cloison : "
                "ouvrage linéaire et souvent recouvert, il se traite comme un poste de "
                "métré distinct.",
        ],
    ),

    "pessac/cite-fruges": dict(
        methode="La mission se prépare sur pièces avant toute visite. Le programme "
                "détaillé des travaux est communiqué d'abord : il détermine les matériaux "
                "à rechercher et, sur un bâti protégé, il détermine aussi ce qu'il sera "
                "possible de sonder. Le périmètre et le programme de repérage sont soumis "
                "pour avis au donneur d'ordre, puis le plan de sondage est présenté aux "
                "services du patrimoine, chaque point de prélèvement étant localisé, "
                "justifié par le programme et assorti de son mode de remise en état. Sur "
                "site, l'ordre s'inverse par rapport à un chantier ordinaire : on épuise "
                "d'abord les méthodes non destructives — mesure du plomb par fluorescence "
                "X, examen des ouvrages déjà déposés ou dégradés — avant d'engager le "
                "moindre sondage, et les prélèvements se concentrent sur les zones que le "
                "programme prévoit de déposer, jamais sur une partie conservée.",
        cadre="La protection patrimoniale ne crée aucune dispense : elle change les "
              "modalités du sondage, pas l'obligation de repérer. Le repérage amiante "
              "avant travaux et avant démolition relève du code du travail, articles R. "
              "4412-97 et suivants, et de l'arrêté du 16 juillet 2019 : il pèse sur le "
              "donneur d'ordre avant toute opération, sans condition d'âge du bâtiment "
              "et sans date d'exclusion. S'y ajoute, en amont, l'autorisation de "
              "travaux instruite avec l'architecte des Bâtiments de France, dont le "
              "calendrier commande celui du repérage : les deux instructions se mènent "
              "de front, l'une conditionnant l'étendue des investigations que l'autre "
              "exige.",
        points=[
            "Sur un ouvrage en béton armé, l’examen visuel n’écarte rien : ragréages, "
                "enduits de surfaçage et produits de réparation appliqués lors des "
                "campagnes d’entretien se sondent, et le point de prélèvement se choisit "
                "dans une zone destinée à la dépose.",
            "Les peintures anciennes se mesurent par fluorescence X, unité de "
                "diagnostic par unité de diagnostic, avant tout ponçage ou décapage : la "
                "mesure se fait sur site et sans prélèvement, ce qui la rend compatible "
                "avec la conservation des dispositions d’origine.",
            "En rénovation énergétique, le repérage porte sur tout ce que le "
                "programme va traverser — doublages, calfeutrements, joints, points de "
                "fixation — et non sur les seuls parements visibles ; la liste minimale "
                "des matériaux se lit au regard du programme communiqué.",
            "Tout ouvrage qu’il est impossible ou interdit de sonder se traduit par "
                "une réserve localisée au rapport : à défaut de levée, l’entreprise "
                "traite le matériau comme amianté, ce qui déplace vers le chantier le "
                "coût que le repérage n’a pas pu lever.",
            "L’état photographique de chaque point de sondage, avant et après remise "
                "en état, fait partie de la mission : sur un bâti protégé, c’est la pièce "
                "qui permet de justifier l’intervention auprès des services instructeurs.",
        ],
    ),

    "pessac/alouette": dict(
        methode="Le premier travail consiste à qualifier le donneur d'ordre, local par "
                "local. Un même secteur mêle syndicats de copropriétaires et résidences "
                "tenues par un gestionnaire : la commande d'un syndic ne couvre que ses "
                "parties communes, celle d'un bailleur que son propre patrimoine, et le "
                "repérage d'une partie privative suppose l'accord de son propriétaire. "
                "Sur les pavillons, ce sont les annexes et les extensions qui commandent "
                "le métré, et l'accès à ces volumes bas se prépare : échelle, éclairage, "
                "dégagement. Ce qui fait dériver un planning ici n'est pas la technique "
                "mais la dispersion — plusieurs bâtiments, plusieurs interlocuteurs, un "
                "rapport par immeuble, chacun avec son périmètre propre.",
        cadre="Deux obligations distinctes se répondent selon le statut du bien. Pour "
              "un syndicat de copropriétaires, le plan pluriannuel de travaux s'impose "
              "dès lors que le permis de construire a été délivré depuis plus de quinze "
              "ans ; l'échéance des syndicats d'au plus cinquante lots est passée "
              "depuis le 1er janvier 2025, celle du diagnostic de performance "
              "énergétique collectif depuis le 1er janvier 2026 — ce dernier reposant "
              "sur un autre critère, un permis de construire déposé avant le 1er "
              "janvier 2013, et ne visant que les bâtiments d'habitation collective. Le "
              "statut se vérifie donc à la commande, pas à la remise du rapport.",
        points=[
            "Sur une plaque ondulée en fibres-ciment d’annexe ou d’extension, le "
                "métré se relève avant la dépose et intègre les accessoires — faîtières, "
                "closoirs, fixations — que le devis de désamiantage oublie régulièrement.",
            "Les conduits en fibres-ciment de ventilation ou d’évacuation traversant "
                "une annexe se repèrent sur tout leur cheminement, y compris les tronçons "
                "encastrés ou enterrés, avant toute reprise de réseau.",
            "Les descentes d’eaux pluviales en amiante-ciment se contrôlent en même "
                "temps que la couverture qu’elles desservent : déposées séparément, elles "
                "échappent souvent au périmètre arrêté au marché.",
            "Dans un petit collectif, la chaufferie et les locaux techniques se "
                "visitent en début de mission : leur accès dépend d’un tiers — mainteneur "
                "ou gestionnaire — et son obtention conditionne la date de remise du "
                "rapport.",
            "En résidence, le repérage d’un logement témoin ne dispense pas "
                "d’examiner les circulations et les gaines qui le desservent : le "
                "programme de travaux d’un gestionnaire porte le plus souvent sur les "
                "deux à la fois.",
        ],
    ),

    "pessac/haut-leveque": dict(
        methode="Sur un bâtiment qui reste en activité, la mission se découpe en zones et "
                "se cale sur des fenêtres d’arrêt, non sur un planning continu. Le "
                "préalable est administratif : autorisation d’accès, plan de prévention "
                "établi avec le service technique, protocole d’intervention pour les "
                "locaux à accès restreint. Ces délais se traitent dès la commande, faute "
                "de quoi ils fixent seuls la date de remise du rapport. La visite "
                "commence par les locaux techniques et les cheminements de réseaux, qui "
                "livrent l’essentiel de l’information avant même l’entrée en zone occupée "
                ": c’est là que se trouvent les ouvrages calorifugés, et c’est le premier "
                "endroit où intervient une entreprise. Sur les collectifs et les "
                "résidences, l’ordre reste le même à une échelle réduite. Chaque zone "
                "libérée se traite ensuite comme un lot autonome, avec son périmètre, son "
                "rapport et sa date, ce qui permet d’engager les travaux par tranches "
                "sans attendre la fin de la campagne. Un maître d’ouvrage institutionnel "
                "impose enfin une forme d’annexe de marché — repérage localisé local par "
                "local, quantitatifs exploitables — arrêtée avant la visite, pas à la "
                "rédaction.",
        cadre="Deux corps de règles se croisent. Sur l’immeuble bâti, le repérage avant "
              "travaux et avant démolition relève du code du travail, articles R. "
              "4412-97 et suivants, de l’arrêté du 16 juillet 2019 et de la norme NF X "
              "46-020, sans date d’exclusion. Sur les installations, structures et "
              "équipements concourant à la réalisation d’une activité, ce sont la norme "
              "NF X 46-100 et l’arrêté du 22 juillet 2021 qui s’appliquent : domaine "
              "distinct, mission distincte. Le dossier technique amiante des parties "
              "communes procède, lui, du code de la santé publique, articles R. 1334-14 "
              "et suivants : document de gestion permanente tenu à jour par le "
              "propriétaire, limité aux listes A et B et sans investigation "
              "destructive, il ne vaut jamais repérage avant travaux. Enfin un repérage "
              "avant démolition conduit selon la NF X 46-020 couvre les besoins d’un "
              "repérage avant travaux ; l’inverse est faux.",
        points=[
            "Les calorifugeages de réseaux en local technique et en gaine se "
                "contrôlent avant toute intervention d’un mainteneur ; leur état de "
                "conservation se relève au même passage, un calorifugeage dégradé "
                "n’appelant pas la même suite qu’un calorifugeage intact.",
            "Aux traversées de parois coupe-feu, le rebouchage et ses joints se "
                "sondent avant tout percement ou repassage de réseau : c’est l’ouvrage le "
                "plus souvent repris et le moins souvent repéré.",
            "Les faux-plafonds de circulation s’ouvrent en début de visite : ils "
                "masquent les réseaux et leurs supports, et leur dépose conditionne "
                "l’accès à des ouvrages qu’aucun contrôle mené depuis le sol ne permet "
                "d’atteindre.",
            "La fiche récapitulative du dossier technique amiante des parties "
                "communes se remet à toute entreprise appelée à intervenir, mais elle ne "
                "couvre que les listes A et B : elle ne dispense d’aucun repérage avant "
                "travaux.",
            "Sur les équipements techniques concourant à l’activité, et non sur "
                "l’immeuble qui les abrite, le repérage relève d’un autre référentiel : "
                "une seule mission ne couvre pas les deux domaines, et le partage se "
                "tranche avant la commande.",
        ],
    ),

    "pessac/chataigneraie": dict(
        methode="Sans archive, la mission commence par une reconstitution : ce que le "
                "syndicat détient — procès-verbaux d'assemblée, contrats d'entretien, "
                "devis anciens — tient lieu d'historique de travaux et sert à dresser la "
                "liste des ouvrages à examiner. La visite se conduit ensuite d'un seul "
                "tenant, des volumes bas aux combles : locaux techniques, parties "
                "communes intérieures, enveloppe, couverture, dépendances. L'objectif "
                "n'est pas de tout mesurer mais de hiérarchiser, en distinguant ce qui "
                "touche à la sécurité et à l'étanchéité de ce qui touche au confort, pour "
                "que l'assemblée générale délibère sur un ordre de priorité et non sur "
                "une liasse de devis. Un point de méthode est décisif sur les rénovations "
                "énergétiques : le repérage avant travaux se commande avant le chiffrage, "
                "jamais après la signature du marché, un matériau découvert en cours "
                "d'exécution arrêtant l'opération et rouvrant la consultation.",
        cadre="Le diagnostic technique global procède du code de la construction et de "
              "l’habitation, articles L. 731-1 et suivants : obligatoire lors de la "
              "mise en copropriété d’un immeuble de plus de dix ans et sur injonction "
              "de l’autorité administrative, il est ailleurs soumis au vote de "
              "l’assemblée générale, et reste sur un immeuble sans archive le préalable "
              "réaliste à toute programmation. Le plan pluriannuel de travaux procède, "
              "lui, de l’article 14-2 de la loi du 10 juillet 1965 : il vise les "
              "immeubles à destination totale ou partielle d’habitation dont le permis "
              "de construire a été délivré depuis plus de quinze ans, et les trois "
              "échéances du calendrier — 2023, 2024, 2025 — sont aujourd’hui passées. "
              "La cotisation au fonds de travaux se calcule par référence au montant "
              "des travaux inscrits au plan.",
        points=[
            "L’état de conservation d’une couverture en fibres-ciment se relève au "
                "moment du repérage : plaque fissurée ou délitée, la dépose ne s’exécute "
                "plus dans les mêmes conditions que sur un matériau intact, et le devis "
                "de l’entreprise s’en trouve changé.",
            "Un conduit de fumée en amiante-ciment se contrôle sur toute sa hauteur, "
                "de la souche au raccordement de l’appareil : le tronçon traversant les "
                "combles et la souche en toiture ne relèvent pas du même mode opératoire "
                "de dépose.",
            "Avant une isolation de combles ou de façade, le support se sonde là où "
                "les fixations seront posées : c’est le percement, et non la pose, qui "
                "met le matériau en suspension.",
            "Sur une copropriété récente, aucune date ne dispense du repérage avant "
                "travaux : la date du permis de construire commande la présomption de "
                "présence des matériaux, pas l’obligation de les rechercher.",
        ],
    ),

    "talence/thouars": dict(
        methode="Sur un ensemble où logements sociaux et copropriétés se côtoient, la "
                "première question n’est pas technique mais contractuelle : qui commande. "
                "Le bailleur commande pour son patrimoine, le syndicat des "
                "copropriétaires pour le sien, et ce découpage s’arrête avant la visite, "
                "pas sur site. Vient ensuite le programme détaillé des travaux : c’est "
                "lui qui fixe la liste des matériaux à rechercher, et le périmètre du "
                "repérage se soumet pour avis au donneur d’ordre avant toute "
                "investigation. La reconnaissance commence par les locaux techniques et "
                "les circulations communes, accessibles sans occupant, puis se poursuit "
                "dans les logements. L’échantillonnage se construit sur plans : une liste "
                "arrêtée bâtiment par bâtiment, cage par cage, typologie par typologie, "
                "avec les clés et l’information des occupants organisées plusieurs "
                "semaines à l’avance. C’est cette logistique, plus que la technique, qui "
                "donne sa durée à l’intervention, chaque sondage destructif supposant un "
                "rebouchage immédiat. Réunir enfin les rapports antérieurs et les "
                "attestations de retrait des campagnes de réhabilitation déjà conduites : "
                "sans eux, la mission redécouvre ce qui a déjà été traité.",
        cadre="Le repérage avant travaux relève du code du travail, articles R. 4412-97 "
              "et suivants, et de l’arrêté du 16 juillet 2019, dont la méthode s’appuie "
              "sur la norme NF X 46-020. Il s’impose au donneur d’ordre préalablement à "
              "toute opération, sans aucune date d’exclusion tenant à l’âge du "
              "bâtiment, et le rapport se remet aux entreprises dès leur consultation ; "
              "l’opérateur doit être certifié avec mention et indépendant de "
              "l’entreprise de travaux. Côté copropriété, le plan pluriannuel de "
              "travaux vise les immeubles dont le permis de construire a été délivré "
              "depuis plus de quinze ans : exigible depuis le 1er janvier 2023 au-delà "
              "de deux cents lots, depuis le 1er janvier 2024 de cinquante et un à deux "
              "cents lots, depuis le 1er janvier 2025 pour les syndicats d’au plus "
              "cinquante lots. Le diagnostic de performance énergétique collectif obéit "
              "à un autre critère : un permis déposé avant le 1er janvier 2013.",
        points=[
            "Sur les menuiseries d’origine, ce sont les mastics de vitrage et les "
                "calfeutrements en périphérie de dormant qui portent le risque : ils se "
                "sondent avant dépose, celle du dormant emportant l’ouvrage support.",
            "Le revêtement de sol visible n’est presque jamais le seul en place : "
                "dans les logements comme dans les circulations communes, le sondage "
                "porte sur toute l’épaisseur du complexe, colle comprise, avant toute "
                "reprise.",
            "En chaufferie, l’habillage isolant des canalisations, les joints de "
                "brides et les garnitures de robinetterie se font repérer avant "
                "l’intervention d’un mainteneur : l’aspect ne conclut rien, seul le "
                "prélèvement analysé tranche.",
            "Sur l’enveloppe, ce sont les enduits et produits de rebouchage mis en "
                "œuvre lors des campagnes précédentes qui se sondent avant tout "
                "traitement mécanique de la surface, et non le béton lui-même.",
            "Les réhabilitations successives font coexister dans un même ensemble des "
                "ouvrages déjà traités et des ouvrages intacts : les conclusions se "
                "rendent cage par cage, jamais par extrapolation d’un bâtiment sur "
                "l’autre.",
        ],
    ),

    "talence/peixotto": dict(
        methode="La mission commence par la lecture des documents existants. Le dossier "
                "technique amiante des parties communes et sa fiche récapitulative disent "
                "ce qui a été trouvé, où, et à quelle date l’état de conservation a été "
                "apprécié pour la dernière fois. Ils orientent la visite sans la "
                "remplacer : un dossier technique ne couvre pas les matériaux que des "
                "travaux viendront atteindre, et un repérage reste dû avant intervention. "
                "La reconnaissance suit ensuite les réseaux — locaux techniques, gaines "
                "de distribution, trappes de visite, traversées de plancher —, "
                "c’est-à-dire des volumes fermés dont l’ouverture conditionne le reste de "
                "la visite et se demande dès la commande, avec les habilitations d’accès "
                "correspondantes. Sur les restructurations d’équipements, le bâtiment "
                "reste en service jusqu’à sa libération : créneaux d’intervention, "
                "autorisations pour les locaux fermés et présence d’un accompagnant "
                "connaissant les installations se fixent au même moment. C’est ce "
                "calendrier d’accès, davantage que le nombre de prélèvements, qui "
                "détermine la date de remise annoncée au maître d’ouvrage.",
        cadre="Deux régimes se superposent. Le dossier technique amiante des parties "
              "communes relève du code de la santé publique, articles R. 1334-14 et "
              "suivants : il vise les immeubles collectifs dont le permis de construire "
              "a été délivré avant le 1er juillet 1997, porte sur les listes A et B "
              "sans investigation destructive, et se tient à jour par le propriétaire "
              "ou le syndicat. Il ne couvre jamais la liste C et ne dispense donc "
              "d’aucun repérage avant travaux. Celui-ci procède du code du travail, "
              "articles R. 4412-97 et suivants, et de l’arrêté du 16 juillet 2019 : il "
              "pèse sur le donneur d’ordre, s’applique sans condition d’âge du bâtiment "
              "et suppose un opérateur certifié avec mention. Sur un marché de maîtrise "
              "d’ouvrage publique, le rapport devient pièce du dossier de consultation "
              "et se communique aux entreprises avant la remise des offres.",
        points=[
            "Le dossier technique amiante des parties communes se tient à jour : "
                "l’état de conservation des matériaux de la liste A se réévalue tous les "
                "trois ans, et la fiche récapitulative se remet à toute entreprise "
                "appelée à intervenir, avant qu’elle n’ouvre un ouvrage.",
            "Sur les réseaux en local technique, ce sont les points singuliers qui "
                "comptent — coudes, brides, vannes — là où l’habillage isolant a été "
                "rouvert puis refermé lors de maintenances antérieures : ils se "
                "contrôlent avant toute reprise de canalisation.",
            "Un habillage isolant en bon état apparent n’est pas un habillage écarté "
                ": c’est l’analyse du prélèvement qui conclut, et elle se conduit avant "
                "l’intervention, jamais pendant.",
            "Sur un bâtiment universitaire restructuré, les matériaux placés en "
                "hauteur — habillages de conduits, protections de structure — échappent à "
                "une reconnaissance menée depuis le sol : les moyens d’accès figurent au "
                "programme de la visite.",
        ],
    ),

    "talence/medoquine": dict(
        methode="Sur une copropriété née d’une division, la mission commence par une "
                "lecture de documents : le règlement de copropriété et l’état descriptif "
                "de division disent seuls ce qui est commun. Dans un immeuble divisé en "
                "deux ou trois lots, les parties communes se réduisent parfois à une "
                "entrée, un couloir, une couverture et des réseaux traversant des lots "
                "privatifs — un périmètre que les copropriétaires situent mal, et qu’il "
                "faut arrêter avant de chiffrer quoi que ce soit. Vient ensuite la "
                "question du donneur d’ordre : la commande suppose une décision "
                "d’assemblée et un interlocuteur désigné pour ouvrir les portes. La "
                "visite se conduit alors en une seule fois, en combinant ce que le "
                "programme appelle. Le constat de risque d’exposition au plomb des "
                "parties communes se mesure unité de diagnostic par unité de diagnostic, "
                "ce qui prend du temps dans une cage plusieurs fois repeinte ; les "
                "sondages destructifs, eux, supposent un accord préalable sur leur "
                "emplacement et leur nombre. Prévoir enfin l’accès aux volumes fermés et "
                "aux lots traversés par des ouvrages communs : c’est ce qui manque le "
                "plus souvent le jour de l’intervention.",
        cadre="Deux obligations se croisent sur ce bâti. Le constat de risque "
              "d’exposition au plomb des parties communes procède du code de la santé "
              "publique, articles L. 1334-5 et suivants, et vise les immeubles "
              "d’habitation construits avant le 1er janvier 1949 ; il se réalise selon "
              "la norme NF X 46-030, par mesure sur site, et impose au syndicat, en "
              "présence de revêtements dégradés, d’informer les occupants et de faire "
              "cesser l’exposition. Le repérage avant travaux relève lui du code du "
              "travail, articles R. 4412-97 et suivants, et de l’arrêté du 16 juillet "
              "2019 : il ne connaît aucune date d’exclusion et pèse sur le donneur "
              "d’ordre. S’y ajoute le plan pluriannuel de travaux, exigible depuis le "
              "1er janvier 2025 pour les syndicats d’au plus cinquante lots, dès lors "
              "que le permis de construire de l’immeuble a été délivré depuis plus de "
              "quinze ans.",
        points=[
            "Sur un immeuble d’habitation construit avant le 1er janvier 1949, le "
                "constat de risque d’exposition au plomb des parties communes porte sur "
                "l’ensemble des revêtements, y compris ceux posés bien après : c’est la "
                "date de construction qui ouvre l’obligation, pas celle de la peinture.",
            "Le remplacement d’une porte d’entrée ou d’un châssis de cage d’escalier "
                "met en jeu deux registres au même moment : les peintures anciennes du "
                "dormant, mesurées avant dépose, et les mastics et calfeutrements du "
                "châssis, sondés dans la même visite.",
            "Un conduit de fumée ou de ventilation ajouté lors d’une mise aux normes "
                "traverse plusieurs lots : son habillage et ses raccords se contrôlent "
                "avant tout percement, y compris à l’intérieur des lots concernés.",
            "Lorsqu’un hall a reçu un faux-plafond, le plénum s’ouvre pendant la "
                "visite : il abrite les réseaux ajoutés après coup, et il est refermé au "
                "moment où l’entreprise établit son prix.",
            "Un immeuble récemment divisé n’est pas un immeuble récent : la date de "
                "mise en copropriété ne renseigne en rien sur celle des travaux, et le "
                "repérage se cale sur l’historique du bâti, jamais sur celui du "
                "règlement.",
        ],
    ),

    "begles/terres-neuves": dict(
        methode="Sur un bâtiment libéré, le repérage est exhaustif, et sa conduite tient "
                "d’abord à la préparation. Les déposes partielles nécessaires pour "
                "atteindre ce qui est masqué se listent et se chiffrent avec le maître "
                "d’ouvrage avant la visite : décidées sur place, elles s’arrêtent à ce "
                "qui s’ouvre facilement et la mission se conclut par des réserves. Le "
                "site doit être vidé et sécurisé, les énergies coupées mais un éclairage "
                "disponible, les plans réunis, et un accompagnant connaissant les lieux "
                "présent — c’est lui qui signale les volumes qu’aucun plan ne montre. Les "
                "moyens d’accès en hauteur figurent au programme, jamais à "
                "l’improvisation. Sur le bâti d’habitation ancien conservé et occupé, "
                "tout s’inverse : périmètre limité au programme, information préalable "
                "des occupants, sondages rebouchés dans la journée, et mesures de plomb "
                "conduites unité par unité dans les parties communes. Dernier point à "
                "régler en amont : la surface de plancher cumulée, que seul le maître "
                "d’ouvrage peut fournir, et qui commande l’exigibilité du diagnostic "
                "portant sur les produits, équipements, matériaux et déchets.",
        cadre="Le repérage avant démolition procède du code du travail, articles R. "
              "4412-97 et suivants, et de l’arrêté du 16 juillet 2019, appliqués selon "
              "la norme NF X 46-020 : périmètre exhaustif, liste C comprise, sur "
              "bâtiment libéré, par un opérateur certifié avec mention. Conduit dans "
              "ces conditions, il vaut repérage avant travaux ; l’inverse n’est jamais "
              "vrai. S’y ajoute le diagnostic portant sur les produits, équipements, "
              "matériaux et déchets, issu du décret n° 2021-821 du 25 juin 2021 : dû en "
              "démolition comme en rénovation significative, dès que la surface de "
              "plancher cumulée dépasse mille mètres carrés ou que le bâtiment a "
              "accueilli une activité industrielle, agricole ou commerciale employant "
              "des substances dangereuses. Il se réalise avant le dépôt de la demande "
              "de permis de démolir ou, à défaut, avant l’acceptation des devis de "
              "travaux.",
        points=[
            "Les immeubles d’habitation conservés au sein d’une opération gardent "
                "leur régime propre : construits avant le 1er janvier 1949, ils relèvent "
                "du constat de risque d’exposition au plomb des parties communes, tandis "
                "que le repérage avant travaux porte sur les matériaux que le programme "
                "touche, quel que soit l’âge du bâtiment.",
            "Sur les bâtiments récents de l’opération, le repérage avant travaux "
                "reste dû : le code du travail ne prévoit aucune date d’exclusion, et le "
                "1er juillet 1997 ne borne que le champ du code de la santé publique.",
            "Dans un bâtiment libéré, ce qui est masqué commande le résultat : "
                "chapes, doublages, habillages et faux-plafonds s’ouvrent selon un "
                "programme de déposes arrêté avant la visite, et non selon ce qui s’ouvre "
                "sans effort.",
            "Le diagnostic portant sur les produits, équipements, matériaux et "
                "déchets se nourrit du repérage amiante sans s’y substituer : un matériau "
                "amianté quitte le site par une filière propre et sous bordereau de "
                "suivi, ce que le plan de gestion prévoit avant la consultation des "
                "entreprises.",
            "Sur une emprise laissée sans usage, l’état de conservation des matériaux "
                "évolue : un rapport ancien ne vaut pas constat du jour, et chaque "
                "matériau maintenu au programme se réexamine avant le curage.",
        ],
    ),

    "begles/centre": dict(
        methode="Sur une copropriété de taille modeste, la difficulté n'est pas la visite "
                "mais ce qui la précède. La commande suppose une décision d'assemblée "
                "générale et un interlocuteur désigné : les clés des parties communes et "
                "les pièces du dossier ne sont pas toujours réunies au même endroit. La "
                "liste demandée est courte et rarement complète — règlement de "
                "copropriété et état descriptif de division, procès-verbaux des dernières "
                "assemblées, contrats d'entretien en cours, factures des travaux déjà "
                "réalisés. Ce qui manque se reconstitue par le relevé sur place, et c'est "
                "ce report qui allonge l'intervention. La visite se conduit du haut vers "
                "le bas : couverture, façade, cage d'escalier, entrée, réseaux, puis les "
                "lots traversés par des ouvrages communs, dont l'accès s'organise à "
                "l'avance.",
        cadre="Le diagnostic technique global procède des articles L. 731-1 et suivants "
              "du code de la construction et de l’habitation : il réunit l’état "
              "apparent des parties communes et des équipements, la situation du "
              "syndicat au regard de ses obligations, les améliorations envisageables, "
              "un volet énergétique et l’évaluation sommaire du coût des travaux sur "
              "dix ans. Il est obligatoire pour tout immeuble de plus de dix ans "
              "faisant l’objet d’une mise en copropriété ; ailleurs, l’assemblée "
              "générale se prononce sur sa réalisation. Le plan pluriannuel de travaux, "
              "lui, s’impose depuis le 1er janvier 2025 aux syndicats d’au plus "
              "cinquante lots dont le permis de construire a été délivré depuis plus de "
              "quinze ans, et se projette sur dix ans. Le diagnostic de performance "
              "énergétique collectif suit un autre critère, un permis déposé avant le "
              "1er janvier 2013, avec une échéance atteinte au 1er janvier 2026 pour "
              "ces mêmes syndicats.",
        points=[
            "Le constat de risque d’exposition au plomb des parties communes ne se "
                "limite pas à un inventaire : un revêtement dégradé classé au niveau le "
                "plus élevé oblige le syndicat à informer les occupants et à faire cesser "
                "l’exposition, avant même le chantier envisagé.",
            "Avant une rénovation énergétique des parties communes, le repérage avant "
                "travaux précède la consultation : le rapport accompagne le dossier remis "
                "aux entreprises, faute de quoi les prix reçus ne couvrent pas le retrait "
                "et l’offre est reprise en cours de chantier.",
            "Dans un petit collectif sans local technique dédié, canalisations et "
                "habillages isolants courent en gaine ou en placard : ces volumes "
                "s’ouvrent pendant la visite, pas au moment de la reprise de colonne.",
            "Une couverture reprise après la construction porte des matériaux dont "
                "l’âge n’est pas celui des murs : l’ancienneté du bâti ne présume jamais "
                "l’absence de matériaux amiantés.",
            "L’évaluation sommaire du coût des travaux sur dix ans n’est pas un devis "
                ": elle se construit poste par poste à partir de l’état apparent relevé, "
                "et se présente à l’assemblée avec ses hypothèses.",
        ],
    ),

    "begles/rives-d-arcins": dict(
        methode="Ici, la mission produit une pièce de marché autant qu'un rapport : "
                "quantitatifs par local, plans de repérage cotés, localisation des "
                "matériaux sans ambiguïté. Ce livrable se définit à la commande, avec le "
                "maître d'ouvrage, car il conditionne le format du relevé sur site — un "
                "rapport rédigé pour un particulier ne s'annexe pas à une consultation "
                "d'entreprises. Le repérage commence par l'enveloppe : couverture et "
                "bardages se relèvent pan par pan et façade par façade, avec des moyens "
                "d'accès en hauteur prévus au programme et non improvisés le jour venu. "
                "C'est ce métré, et non le gros œuvre, qui porte le budget de "
                "déconstruction ; une surface estimée au ratio se paie à la facture "
                "finale. Prévoir enfin le délai d'analyse des prélèvements : sur de "
                "grandes surfaces, il pèse plus lourd sur la date de remise que la visite "
                "elle-même.",
        cadre="Le repérage avant démolition comme le repérage avant travaux relèvent du "
              "code du travail, articles R. 4412-97 et suivants, et de l’arrêté du 16 "
              "juillet 2019 ; sur les immeubles bâtis, la méthode est celle de la norme "
              "NF X 46-020, dont le tableau A1 fixe la liste minimale des matériaux à "
              "rechercher au vu du programme communiqué par le donneur d’ordre. Les "
              "installations, structures et équipements concourant à une activité "
              "relèvent d’un autre référentiel, la norme NF X 46-100 et l’arrêté du 22 "
              "juillet 2021 : une seule mission ne couvre pas les deux domaines, et le "
              "découpage se décide à la commande. S’y ajoute le diagnostic portant sur "
              "les produits, équipements, matériaux et déchets, dû dès mille mètres "
              "carrés de surface de plancher cumulée, avant le dépôt de la demande de "
              "permis de démolir. L’opérateur est certifié avec mention et indépendant "
              "de l’entreprise de travaux.",
        points=[
            "Les plaques de couverture en fibres-ciment ne résistent pas à la rupture "
                ": la reconnaissance suppose des moyens d’accès et une protection contre "
                "les chutes inscrits au programme de la visite, jamais décidés sur le "
                "toit.",
            "Les joints et mastics de calfeutrement en pied de bardage et en rive de "
                "couverture s’ajoutent au métré des plaques : ils sont déposés dans la "
                "même opération et relèvent du même bordereau de suivi.",
            "Un repérage avant travaux antérieur ne couvre pas une démolition : seul "
                "le périmètre exhaustif, liste C comprise et sur bâtiment libéré, y "
                "répond ; la réciproque, elle, est vraie.",
            "Les produits et équipements réemployables s’inventorient local par local "
                "avant le curage : mélangés en benne, ils sortent de toute filière de "
                "réemploi et l’inventaire devient inexploitable.",
        ],
    ),

    "le-bouscat/centre": dict(
        methode="Sur un immeuble de pierre à planchers mixtes, la mission commence par le "
                "dépouillement des pièces détenues par le syndic : procès-verbaux "
                "d’assemblée, factures d’entretien de la toiture et de la cage, contrats "
                "de l’ascenseur. Ces documents datent les campagnes de travaux "
                "successives et déterminent le nombre de sondages. La visite s’organise "
                "ensuite du haut vers le bas : combles et sous-face de couverture "
                "d’abord, où l’ardoise et le zinc imposent un moyen d’accès en hauteur et "
                "non une observation depuis la rue ; cage d’escalier et paliers ensuite, "
                "unité de diagnostic par unité de diagnostic pour le plomb ; caves et "
                "local des colonnes pour finir. La gaine d’ascenseur et sa machinerie se "
                "visitent appareil consigné, avec l’ascensoriste : c’est ce créneau qui "
                "fixe la date d’intervention, plus que la disponibilité de l’opérateur. "
                "Ce qui fait durer la mission n’est pas la surface mais le nombre de "
                "niveaux et l’étroitesse des accès. À réunir avant la venue : clés des "
                "combles et des caves, immobilisation programmée de l’ascenseur, et le "
                "programme détaillé des travaux envisagés, qui borne le périmètre du "
                "repérage avant travaux.",
        cadre="Deux régimes se superposent. Le constat de risque d’exposition au plomb "
              "des parties communes procède du code de la santé publique, articles L. "
              "1334-5 et suivants, et vise les immeubles d’habitation construits avant "
              "le 1er janvier 1949 ; la mesure se fait par fluorescence X sur site, "
              "unité de diagnostic par unité de diagnostic, selon la norme NF X 46-030 "
              "d’avril 2008. Le repérage amiante avant travaux relève, lui, du code du "
              "travail, articles R. 4412-97 et suivants, et de l’arrêté du 16 juillet "
              "2019 : il incombe au donneur d’ordre — ici le syndicat des "
              "copropriétaires —, ne connaît aucune date d’exclusion et se remet aux "
              "entreprises dès leur consultation. Le plan pluriannuel de travaux, "
              "enfin, vise les immeubles d’habitation dont le permis de construire a "
              "été délivré depuis plus de quinze ans ; la dernière échéance du "
              "calendrier, celle des syndicats d’au plus cinquante lots, est passée "
              "depuis le 1er janvier 2025.",
        points=[
            "En couverture ardoise ou zinc, solins, noues et souches reprises au fil "
                "des campagnes d’entretien peuvent comporter des éléments en "
                "amiante-ciment : ils se contrôlent avant toute reprise de toiture, "
                "depuis un moyen d’accès en hauteur et non depuis le sol.",
            "Les paliers à plancher métallique reçoivent un remplissage et une chape "
                "rapportés : le sondage traverse tout le complexe jusqu’au support, la "
                "couche visible ne préjugeant pas de celles qui subsistent dessous.",
            "La gaine et la machinerie d’ascenseur concentrent joints, tresses et "
                "calorifugeages : leur repérage précède toute modernisation de l’appareil "
                "et se conduit installation consignée.",
            "Dans une cage d’escalier d’immeuble d’habitation antérieur au 1er "
                "janvier 1949, tous les revêtements des parties communes — murs, "
                "plafonds, garde-corps, portes palières, menuiseries — relèvent du "
                "constat plomb, quelle que soit la date de pose de la peinture visible.",
            "Là où des conduits de fumée ont été chemisés ou condamnés lors d’une "
                "remise aux normes, leur contrôle précède tout percement de trémie ou "
                "passage de réseau vertical.",
        ],
    ),

    "le-bouscat/champ-de-courses": dict(
        methode="Une même commande recouvre ici deux natures d'intervention : de petits "
                "syndicats en immeuble collectif, et des maisons dont l'essentiel du "
                "risque se trouve en fond de parcelle. Sur les collectifs, le repérage "
                "part du hall, des paliers et de la cage, puis descend aux caves et au "
                "local technique. Sur les maisons, il commence à l'inverse par les "
                "annexes — garage, appentis, abri, auvent —, volumes les plus souvent "
                "absents de la commande initiale et les plus longs à atteindre. C'est ce "
                "point, et non la technique, qui fait revenir un opérateur une seconde "
                "fois. Trois éléments sont à réunir avant l'intervention : la liste "
                "exhaustive des annexes rattachées à l'opération, le programme détaillé "
                "des travaux envisagés, qui borne le périmètre du repérage, et l'identité "
                "du donneur d'ordre lorsque plusieurs propriétaires sont concernés par un "
                "même chantier.",
        cadre="Le repérage avant travaux et le repérage avant démolition relèvent l'un "
              "et l'autre du code du travail, articles R. 4412-97 et suivants, et de "
              "l'arrêté du 16 juillet 2019 pris pour les immeubles bâtis. La "
              "distinction est de périmètre : déposer la couverture d'une dépendance "
              "relève du repérage avant travaux ; abattre la dépendance entière appelle "
              "un repérage avant démolition, exhaustif, qui couvre également la liste "
              "C. Un repérage avant démolition conduit selon la norme NF X 46-020 "
              "d'août 2017 vaut repérage avant travaux ; l'inverse n'est jamais vrai. "
              "Côté copropriété, le plan pluriannuel de travaux s'impose depuis le 1er "
              "janvier 2025 aux syndicats d'au plus cinquante lots, dès lors que le "
              "permis de construire de l'immeuble a été délivré depuis plus de quinze "
              "ans.",
        points=[
            "Les plaques ondulées de couverture et les plaques planes de bardage des "
                "garages et abris se métrent au repérage : c’est ce métré, non le gros "
                "œuvre, qui commande le phasage de la dépose et son poste déchets.",
            "Les descentes d’eaux pluviales et les conduits de ventilation en "
                "amiante-ciment échappent régulièrement au métré : ils se relèvent au "
                "même passage que la couverture de l’annexe.",
            "Les remplissages d’allège et les sous-faces de balcon se contrôlent "
                "avant tout ravalement ou remplacement de menuiserie, ces éléments "
                "quittant rarement le bâtiment lors des campagnes précédentes.",
            "Lorsqu’un garage ou un local annexe appartient aux parties communes, le "
                "donneur d’ordre est le syndicat des copropriétaires et non l’occupant : "
                "cette qualité se tranche avant l’intervention, faute de quoi le rapport "
                "n’est opposable à personne.",
        ],
    ),

    "le-bouscat/sainte-germaine": dict(
        methode="Sur ce type de résidence, la mission ne se conçoit pas sans le programme "
                "détaillé des travaux : c'est lui qui détermine la liste des matériaux à "
                "rechercher, et non l'inverse. Le périmètre et le programme de repérage "
                "sont donc transmis au donneur d'ordre pour avis avant toute "
                "investigation sur site — étape formelle, souvent escamotée, et dont "
                "l'absence rend le rapport contestable. Dès que le programme touche les "
                "menuiseries ou les gaines traversant les logements, l'accès aux parties "
                "privatives s'organise en amont, par le syndic, avec un calendrier de "
                "visites nominatif et des relances : c'est ce poste qui décale les "
                "plannings, jamais la technique. À fournir avant la venue : plans de "
                "niveau, rapports de repérage antérieurs et attestations de retrait, "
                "faute de quoi l'opérateur rechiffre des matériaux déjà sortis du "
                "bâtiment.",
        cadre="Le dossier technique amiante des parties communes procède du code de la "
              "santé publique, articles R. 1334-14 et suivants : document de gestion "
              "permanente tenu à jour par le propriétaire, il porte sur les matériaux "
              "des listes A et B, sans investigation destructive, et sa fiche "
              "récapitulative se remet à toute entreprise appelée à intervenir. Il ne "
              "couvre jamais la liste C et ne dispense d’aucun repérage avant travaux. "
              "Ce dernier relève du code du travail, articles R. 4412-97 et suivants, "
              "et de l’arrêté du 16 juillet 2019 ; la norme NF X 46-020 d’août 2017 en "
              "fixe la méthode, et la liste minimale des matériaux à rechercher découle "
              "de son tableau A1, en fonction du programme détaillé communiqué par le "
              "donneur d’ordre. Le rapport accompagne le dossier de consultation des "
              "entreprises, non le marché signé.",
        points=[
            "Les tableaux, appuis et rejingots de baie sont entamés par la dépose des "
                "menuiseries : leurs mastics et calfeutrements entrent au périmètre du "
                "repérage avant travaux, même lorsque la commande ne mentionne que la "
                "fenêtre.",
            "En chaufferie et en sous-station, calorifugeages, joints de brides et "
                "garnitures de robinetterie se contrôlent avant toute intervention d’un "
                "mainteneur : seule l’analyse en laboratoire permet de conclure.",
            "Les trappes de visite des gaines techniques s’ouvrent au repérage : un "
                "habillage posé lors d’une campagne récente masque fréquemment un conduit "
                "conservé en place.",
            "Le dossier technique amiante des parties communes, limité aux listes A "
                "et B et conduit sans sondage destructif, ne vaut que comme point de "
                "départ documentaire : il ne dispense d’aucun repérage avant travaux.",
        ],
    ),

    "cenon/palmer": dict(
        methode="Sur une opération qui conserve une partie du bâti et fait disparaître "
                "l’autre, la première tâche n’est pas technique : elle consiste à "
                "arrêter, bâtiment par bâtiment et cage par cage, ce qui relève du "
                "repérage avant travaux et ce qui relève du repérage avant démolition. "
                "Les deux missions n’ont ni le même périmètre ni les mêmes moyens. La "
                "seconde se conduit sur bâtiment libéré, sondages destructifs autorisés, "
                "matériaux recherchés sous les chapes et derrière les habillages. La "
                "première s’exerce en site occupé, avec des investigations limitées par "
                "la présence des habitants et un fractionnement par cage. Le calage se "
                "fait sur le phasage réel du chantier et sur le calendrier de libération "
                "des logements, jamais sur le plan de masse. Sur le bâti conservé, la "
                "visite suit les logements rendus disponibles au fil des relogements "
                "temporaires : un créneau perdu se rattrape difficilement. À arrêter avec "
                "le maître d’ouvrage avant la commande : le phasage daté, la liste des "
                "logements libérés et les modalités d’information des occupants.",
        cadre="Les deux repérages procèdent du même socle : code du travail, articles "
              "R. 4412-97 et suivants, décret n° 2017-899 du 9 mai 2017 modifié, arrêté "
              "du 16 juillet 2019 et norme NF X 46-020 d’août 2017. Aucune date "
              "d’exclusion ne s’y attache : l’obligation pèse sur le donneur d’ordre "
              "avant toute opération, quel que soit l’âge du bâtiment. Le repérage "
              "avant démolition, de périmètre exhaustif, vaut repérage avant travaux ; "
              "la réciproque est exclue. L’opérateur est certifié avec mention au titre "
              "de l’arrêté du 25 juillet 2016, et indépendant du donneur d’ordre comme "
              "de l’entreprise de travaux. S’y ajoute, en démolition comme en "
              "rénovation significative, le diagnostic portant sur les produits, "
              "équipements, matériaux et déchets, dû dès que la surface de plancher "
              "cumulée dépasse mille mètres carrés : il se conduit avant le dépôt de la "
              "demande de permis de démolir ou, à défaut, avant l’acceptation des "
              "devis.",
        points=[
            "Un repérage avant travaux ne peut jamais tenir lieu de repérage avant "
                "démolition : sur un bâtiment voué à disparaître, le périmètre doit être "
                "exhaustif et couvrir la liste C.",
            "Sur la frontière entre zone conservée et zone démolie, les ouvrages "
                "partagés — planchers, murs de refend, réseaux traversants — se "
                "rattachent explicitement à l’une des deux missions, faute de quoi ils "
                "échappent aux deux.",
            "Un habillage posé lors d’une campagne de réhabilitation ne vaut pas "
                "dépose de ce qu’il recouvre : le contrôle porte sur l’ouvrage d’origine, "
                "atteint par sondage, et non sur le parement récent.",
            "En site occupé, les parties privatives touchées par le programme — "
                "menuiseries, gaines, sols — entrent au périmètre : leur accès se prépare "
                "avec le gestionnaire plusieurs semaines avant la visite.",
            "Dans un logement libéré, cloisons de doublage et coffrages techniques "
                "s’ouvrent au repérage : sur un bâtiment à démolir, aucun ouvrage ne se "
                "déclare exempt sans avoir été traversé.",
        ],
    ),

    "cenon/la-maregue": dict(
        methode="Un dossier ancien n'est pas un dossier faux, mais il ne vaut que "
                "réévalué — les matériaux des listes A et B se contrôlent périodiquement, "
                "et une dégradation change la conclusion sans changer le repérage. La "
                "visite reprend ensuite les locaux techniques dans l'ordre où les "
                "entreprises y interviennent : chaufferie et sous-station d'abord, local "
                "des colonnes et gaines ensuite, caves et circulations enfin. Les "
                "équipements communs d'origine sont le fil conducteur, puisque ce sont "
                "eux que le programme de travaux vient toucher et eux qui n'ont jamais "
                "été déposés. Un point d'organisation propre à la gestion mixte : la "
                "qualité du donneur d'ordre se tranche avant la commande, selon que "
                "l'ouvrage concerné relève du syndicat ou du bailleur. Un rapport adressé "
                "au mauvais destinataire n'est opposable à personne, et se refait.",
        cadre="Le dossier technique amiante des parties communes procède du code de la "
              "santé publique, articles R. 1334-14 et suivants. Il porte sur les "
              "matériaux des listes A et B, sans investigation destructive ; le "
              "propriétaire — ici le syndicat des copropriétaires — le tient à jour et "
              "le complète des évaluations périodiques de l’état de conservation. Il ne "
              "couvre jamais la liste C et ne dispense d’aucun repérage avant travaux, "
              "lequel relève du code du travail, articles R. 4412-97 et suivants, de "
              "l’arrêté du 16 juillet 2019 et de la norme NF X 46-020, sans condition "
              "d’âge du bâtiment. Sur le plan collectif, le plan pluriannuel de travaux "
              "vise les immeubles d’habitation dont le permis de construire a été "
              "délivré depuis plus de quinze ans ; l’assemblée générale se prononce sur "
              "son adoption, et la cotisation annuelle au fonds de travaux se calcule "
              "par référence au montant des travaux qui y sont inscrits.",
        points=[
            "La fiche récapitulative du dossier technique amiante se remet à toute "
                "entreprise appelée à intervenir dans les parties communes, y compris "
                "pour une opération de maintenance courante.",
            "Les calorifugeages de chaufferie sont le premier poste contrôlé, mais "
                "joints de brides, tresses de presse-étoupe et garnitures de robinetterie "
                "s’oublient plus souvent qu’eux : ils se relèvent au même passage.",
            "Un habillage de canalisation en bon état apparent ne conclut rien : "
                "seule l’analyse en laboratoire d’un prélèvement permet d’écarter "
                "l’amiante.",
            "Les dalles de sol et leur colle, dans les caves et les circulations "
                "basses, se sondent avant toute reprise de dallage ou tout passage de "
                "réseau, y compris sur une surface réduite.",
            "L’état de conservation des matériaux des listes A et B se réévalue "
                "périodiquement : c’est cette réévaluation, et non le repérage initial, "
                "qui déclenche les mesures à prendre en parties communes.",
        ],
    ),

    "cenon/le-loret": dict(
        methode="Sur un bâti mêlant maisons anciennes et petits collectifs en pente, la "
                "mission se conduit du bas vers le haut. Les points bas — cave, sous-sol, "
                "vide sanitaire lorsqu’il en existe un — et les pieds de mur se visitent "
                "en premier : c’est là que se lit l’humidité, et de là que se décide "
                "l’étendue du reste. L’examen des bois passe par le sondage mécanique des "
                "éléments accessibles — solives, abouts de poutre encastrés dans la "
                "maçonnerie, lambourdes, bas de poteaux — et par le soulèvement des "
                "isolants et habillages qui les masquent. Un plancher recouvert d’un "
                "revêtement récent ne se déclare pas sain : l’attaque se développe sous "
                "le doublage, à l’abri de la lumière. La visite se prolonge par les "
                "combles, puis par les parties communes des collectifs. Ce qui fait durer "
                "l’intervention, c’est l’accès : trappes condamnées, caves encombrées, "
                "point bas sans cheminement dégagé. À préparer avant la venue : ouverture "
                "des trappes, passage dégagé jusqu’aux niveaux inférieurs, et signalement "
                "des désordres d’eau déjà constatés par les occupants.",
        cadre="Un décalage subsiste : l'arrêté vise la norme NF P03-201 dans sa version "
              "de mars 2012, que l'AFNOR a remplacée par celle de février 2016 sans "
              "qu'aucun texte ne l'ait encore reconnue. La recherche de mérule et "
              "d'insectes à larves xylophages n'obéit pas au même cadre : elle se "
              "conduit à titre volontaire, en préalable à la programmation des travaux "
              "d'une copropriété. Le constat de risque d'exposition au plomb des "
              "parties communes, lui, procède du code de la santé publique et vise les "
              "immeubles d'habitation construits avant le 1er janvier 1949.",
        points=[
            "Les abouts de solive encastrés dans la maçonnerie sont le premier point "
                "de contrôle d’un plancher bois en pied de coteau : c’est à "
                "l’encastrement, humide et confiné, que l’attaque commence, non au milieu "
                "de la portée.",
            "Un revêtement de sol récemment posé sur un plancher bois masque autant "
                "qu’il protège : le contrôle se fait par la sous-face quand elle est "
                "accessible, avant toute reprise de sol.",
            "Là où un mur de parties communes est adossé à la pente, enduits et "
                "doublages se sondent avant toute reprise d’étanchéité intérieure : un "
                "drainage ou un cuvelage ajouté après coup constitue une couche de "
                "travaux à part entière.",
            "L’état parasitaire ne se substitue pas à l’état relatif à la présence de "
                "termites : le premier couvre la mérule et les insectes à larves "
                "xylophages, le second obéit au zonage préfectoral et à sa propre norme.",
        ],
    ),

    "lormont/genicart": dict(
        methode="Sur un bâtiment libéré destiné à disparaître, la mission se prépare sur "
                "plan avant de se conduire sur site. L’opérateur découpe le bâtiment en "
                "zones homogènes — typologies de logement, cages, locaux communs, "
                "sous-sols — et arrête un nombre de sondages par zone : c’est ce "
                "document, et non la visite, qui détermine la durée et le coût. La "
                "sécurisation conditionne l’intervention : fluides coupés et consignés, "
                "éclairage provisoire, cheminements dégagés, protection contre les "
                "intrusions. Un bâtiment libéré mais non sécurisé se sonde partiellement, "
                "ce qui produit une réserve au rapport et une incertitude dans le marché "
                "de travaux. La visite descend ensuite sous les revêtements successifs : "
                "dépose partielle des habillages, ouverture des coffrages, traversée des "
                "chapes, accès aux gaines. Le rendu se prépare dès la visite, le repérage "
                "devant être exploitable par une entreprise qui chiffre sans revenir sur "
                "site. À fournir en amont : plans de niveau exploitables, historique des "
                "interventions et calendrier de libération des logements.",
        cadre="Le repérage avant démolition procède du code du travail, articles R. "
              "4412-97 et suivants, du décret n° 2017-899 du 9 mai 2017 modifié et de "
              "l’arrêté du 16 juillet 2019, la méthode étant fixée par la norme NF X "
              "46-020 d’août 2017. Son périmètre est exhaustif et couvre la liste C ; "
              "conduit selon cette norme, il vaut repérage avant travaux, l’inverse "
              "restant exclu. L’opérateur doit être certifié avec mention par un "
              "organisme accrédité, au titre de l’arrêté du 25 juillet 2016, et "
              "indépendant du donneur d’ordre comme de l’entreprise de travaux : "
              "vérification que tout acheteur public peut opérer sur l’annuaire des "
              "diagnostiqueurs certifiés. Le diagnostic portant sur les produits, "
              "équipements, matériaux et déchets s’y ajoute, avant le dépôt de la "
              "demande de permis de démolir ou, à défaut, avant l’acceptation des devis "
              "de travaux.",
        points=[
            "Le nombre de sondages se fixe par zone homogène et se justifie dans le "
                "rapport : une conclusion étendue à un local qu’aucun sondage n’a "
                "traversé est une extrapolation, et l’entreprise de retrait est fondée à "
                "la refuser.",
            "Les locaux de service — local vide-ordures, local poubelles, gaines "
                "palières — se traitent comme des zones à part entière : leur faible "
                "surface ne réduit pas le nombre de matériaux à y rechercher.",
            "Le repérage avant démolition couvre la liste C : produits inaccessibles "
                "sans travaux destructifs, colles, mortiers, enduits de rebouchage et "
                "joints, à rechercher là où ils se trouvent et non là où ils se voient.",
            "Les rapports de repérage et les attestations de retrait des campagnes "
                "antérieures s’intègrent au dossier remis : ils bornent ce qui a déjà "
                "quitté le bâtiment et évitent de le chiffrer une seconde fois.",
        ],
    ),

    "lormont/carriet": dict(
        methode="Sur de grands linéaires occupés, la mission est d’abord un problème "
                "d’échantillonnage et d’accès. L’opérateur recense les typologies de "
                "logement présentes dans chaque bâtiment — surface, distribution, "
                "génération des équipements — et prévoit des sondages dans chacune : un "
                "logement visité ne vaut que pour les ouvrages qu’il a permis de "
                "traverser. Le découpage de la commande se décide en même temps, par "
                "cage, par bâtiment ou par lot de bâtiments, selon le phasage du "
                "programme ; arrêté à la commande, il permet de mutualiser les passages, "
                "décidé après coup il oblige à revenir. L’accès aux logements se prépare "
                "plusieurs semaines à l’avance, par le gestionnaire concerné, avec "
                "information écrite des occupants et créneaux nominatifs. Les parties "
                "communes et les équipements collectifs d’origine — cage, gaines, local "
                "des colonnes, chaufferie — se visitent le même jour que les logements de "
                "la cage, pour éviter un second déplacement. Le taux de logements "
                "inaccessibles se traite comme une donnée du chantier : un créneau de "
                "rattrapage figure au calendrier initial.",
        cadre="Le repérage avant travaux relève du code du travail, articles R. 4412-97 "
              "et suivants, et de l’arrêté du 16 juillet 2019 : l’obligation pèse sur "
              "le donneur d’ordre préalablement à toute opération, sans condition d’âge "
              "du bâtiment, et le rapport se remet aux entreprises dès leur "
              "consultation. La liste minimale des matériaux à rechercher découle du "
              "tableau A1 de la norme NF X 46-020, en fonction du programme détaillé de "
              "travaux communiqué par le donneur d’ordre, à qui le périmètre et le "
              "programme de repérage sont préalablement soumis pour avis. Côté "
              "copropriété, le plan pluriannuel de travaux vise les immeubles "
              "d’habitation dont le permis de construire a été délivré depuis plus de "
              "quinze ans ; il projette les travaux sur dix ans, et la cotisation "
              "annuelle au fonds de travaux se calcule par référence au montant de ceux "
              "qui y sont inscrits.",
        points=[
            "Deux logements de même surface ne sont pas deux logements de même "
                "typologie si leurs équipements ont été renouvelés à des dates "
                "différentes : c’est la génération des ouvrages, non le plan, qui "
                "commande l’échantillonnage.",
            "Les colonnes montantes et leurs gaines se contrôlent avant tout "
                "remplacement : conduits, joints de raccordement et calfeutrements de "
                "traversée de plancher se trouvent derrière l’habillage, non devant.",
            "Dans les équipements collectifs d’origine — chaufferie, local des "
                "colonnes, gaines palières —, l’absence de dégradation apparente ne "
                "conclut rien : seule l’analyse en laboratoire écarte l’amiante.",
            "Un logement resté inaccessible se signale comme tel dans le rapport, "
                "local par local : une zone non visitée qui n’apparaît pas en réserve "
                "devient une zone réputée repérée, et c’est l’entreprise qui en subit les "
                "conséquences.",
        ],
    ),

    "lormont/vieux-lormont": dict(
        methode="Elle commence donc par le dépouillement de ce qui subsiste — "
                "autorisations d'urbanisme, procès-verbaux d'assemblée, factures —, qui "
                "date les couches de travaux et borne le périmètre. Sur site, le constat "
                "plomb des parties communes se conduit unité de diagnostic par unité de "
                "diagnostic : chaque mur, plafond, garde-corps, porte, châssis et plinthe "
                "fait l'objet de mesures propres, et c'est le nombre d'unités, non la "
                "surface, qui détermine la durée de l'intervention. La cage d'escalier "
                "étant le plus souvent le seul espace commun, tout s'y concentre. La "
                "visite se prolonge par les caves et les combles, où passent les réseaux "
                "ajoutés après-guerre et où se lit l'état des bois. Deux préalables "
                "conditionnent l'intervention : la désignation d'un interlocuteur unique "
                "lorsque le syndicat est bénévole, et l'ouverture effective des caves et "
                "des combles le jour dit.",
        cadre="1334-5 et suivants, et de la norme NF X 46-030 d'avril 2008 ; deux "
              "normes complètent les analyses, NF X 46-031 pour l'analyse chimique des "
              "peintures et NF X 46-032 pour la mesure du plomb dans les poussières au "
              "sol. Dans un immeuble d'habitation construit avant le 1er janvier 1949, "
              "il porte sur tous les revêtements des parties communes, sans "
              "considération de leur date de pose. La mesure s'effectue par "
              "fluorescence X sur site, le prélèvement n'intervenant qu'en cas "
              "d'impossibilité de mesure directe. Le repérage amiante avant travaux, "
              "distinct, relève du code du travail : l'ancienneté des murs n'en "
              "dispense jamais, l'amiante-ciment ayant été employé bien avant guerre et "
              "n'ayant été interdit qu'au 1er janvier 1997.",
        points=[
            "Avant tout décapage ou ponçage de peinture en cage d’escalier, le "
                "constat plomb conditionne le mode opératoire de l’entreprise : c’est lui "
                "qui déclenche les mesures de protection des salariés au titre du code du "
                "travail.",
            "Les menuiseries des parties communes — porte d’entrée, châssis de cage, "
                "impostes — comptent parmi les unités de diagnostic les plus fréquemment "
                "classées : elles se mesurent au même passage que les murs et les "
                "plafonds.",
            "Dans les caves et les combles, les réseaux ajoutés après-guerre — "
                "conduits, habillages, calorifugeages — se contrôlent avant tout "
                "percement de plancher ou de mur, y compris pour un simple passage de "
                "câble.",
            "Un enduit ciment appliqué en pied de mur sur une maçonnerie de pierre "
                "retient l’humidité qu’il devait masquer : là où il existe, son ouverture "
                "précède l’examen des bois qu’il recouvre.",
            "Sur un syndicat dépourvu de document technique, le diagnostic technique "
                "global fournit l’état apparent des parties communes et des équipements, "
                "un volet énergétique et l’évaluation sommaire du coût des travaux sur "
                "dix ans : c’est le préalable réaliste à toute programmation.",
        ],
    ),

    "villenave-d-ornon/le-bourg": dict(
        methode="Sur une maison de ville tenue en micro-copropriété, l'essentiel du temps "
                "ne passe pas dans la visite mais dans la délimitation du périmètre. Le "
                "règlement de copropriété et l'état descriptif de division sont demandés "
                "avant l'intervention : eux seuls disent si le couloir d'entrée, la cage, "
                "les caves ou les combles sont communs, et donc ce que la mission couvre. "
                "Sans cette pièce, le rapport porte sur un périmètre supposé, ce "
                "qu'aucune entreprise n'acceptera. Deux registres s'y croisent : la "
                "mesure du plomb sur les revêtements des parties communes, unité de "
                "diagnostic par unité de diagnostic, et le sondage des couches de travaux "
                "ajoutées ensuite. À préparer : autorisations d'urbanisme, factures "
                "d'entreprises, procès-verbaux d'assemblée, et un interlocuteur désigné "
                "pour ouvrir les portes le jour dit.",
        cadre="Trois textes se superposent ici. Pour les immeubles d’habitation "
              "construits avant le 1er janvier 1949, le constat de risque d’exposition "
              "au plomb des parties communes relève des articles L. 1334-5 et suivants "
              "du code de la santé publique, selon la norme NF X 46-030 d’avril 2008 : "
              "il porte sur tous les revêtements des parties communes, quelle que soit "
              "leur date de pose. Le repérage amiante avant travaux relève, lui, du "
              "code du travail, articles R. 4412-97 et suivants, et de l’arrêté du 16 "
              "juillet 2019 : il s’impose au donneur d’ordre sans condition d’âge du "
              "bâtiment, y compris sur les programmes les plus récents. Enfin, le plan "
              "pluriannuel de travaux s’applique aux syndicats dont le permis de "
              "construire a été délivré depuis plus de quinze ans ; pour les "
              "copropriétés d’au plus cinquante lots, l’échéance du 1er janvier 2025 "
              "est passée, et le diagnostic technique global reste le préalable "
              "réaliste.",
        points=[
            "Dans un couloir et une cage d’escalier communs antérieurs à 1949, les "
                "peintures d’origine subsistent sous les repeints : la mesure se fait par "
                "fluorescence X sur site, unité de diagnostic par unité de diagnostic, "
                "avant tout ponçage ou décapage.",
            "Le revêtement de sol posé dans un couloir commun lors d’une remise en "
                "état se sonde sur toute l’épaisseur du complexe : c’est la dalle et sa "
                "colle, sous la couche visible, qui portent le risque.",
            "Sur un plancher bois séparant deux lots, le doublage ajouté sous parquet "
                "lors d’une rénovation est un point de sondage systématique avant toute "
                "reprise de sol.",
            "Sur les collectifs récents, l’âge du bâtiment ne dispense d’aucun "
                "repérage avant travaux : le code du travail ne connaît pas de date "
                "d’exclusion, et c’est le programme détaillé des travaux qui commande "
                "seul la liste des matériaux recherchés.",
        ],
    ),

    "villenave-d-ornon/sarcignan": dict(
        methode="La mission commence au bureau, pas sur site : le dossier technique "
                "amiante des parties communes, les rapports de repérage antérieurs et les "
                "attestations de retrait sont réclamés avant toute visite. Ils datent les "
                "campagnes déjà menées et évitent de rechercher, donc de chiffrer, un "
                "matériau déposé depuis dix ans. Ils ne remplacent rien pour autant : "
                "établi sans investigation destructive, ce dossier ignore la liste C et "
                "ne dispense d’aucun repérage avant travaux. Le repérage se construit "
                "ensuite autour du programme : c’est lui, et non la surface de "
                "l’immeuble, qui fixe la liste des matériaux à rechercher. Une campagne "
                "de menuiseries appelle un sondage par typologie de baie ; une reprise de "
                "colonne impose d’ouvrir gaines et trappes de visite. Ordre de visite : "
                "local technique, gaines, hall, circulations, puis dépendances. À "
                "préparer par le syndic : consignation des installations, clés des locaux "
                "communs, et l’accord d’accès aux logements si le programme touche les "
                "parties privatives — obtenu en assemblée générale, jamais pendant la "
                "mission.",
        cadre="Deux régimes distincts se croisent sur ces résidences. Le dossier "
              "technique amiante des parties communes relève du code de la santé "
              "publique, articles R. 1334-14 et suivants : établi selon la NF X 46-020 "
              "sur les listes A et B, sans investigation destructive, il est tenu à "
              "jour par le propriétaire et sa fiche récapitulative se remet à toute "
              "entreprise appelée à intervenir. Il ne couvre jamais la liste C. Le "
              "repérage avant travaux relève du code du travail, articles R. 4412-97 à "
              "R. 4412-97-6, du décret n° 2017-899 modifié et de l’arrêté du 16 juillet "
              "2019, la NF X 46-020 d’août 2017 fixant la méthode et son tableau A1 la "
              "liste minimale des matériaux, en fonction du programme détaillé "
              "communiqué par le donneur d’ordre. Il exige un opérateur certifié avec "
              "mention, au sens de l’arrêté du 25 juillet 2016, indépendant du donneur "
              "d’ordre et de l’entreprise de travaux.",
        points=[
            "Le mastic de vitrage et le calfeutrement périphérique des menuiseries "
                "d’origine se prélèvent par typologie de baie, avant lancement d’une "
                "campagne de remplacement : un sondage ne vaut que pour l’ouvrage qu’il "
                "traverse.",
            "Lorsqu’une gaine palière est habillée en fibres-ciment, sa trappe de "
                "visite s’ouvre avant toute reprise de colonne montante, seule l’analyse "
                "en laboratoire permettant de conclure.",
            "Sous le revêtement rapporté d’un hall ou d’une circulation, la dalle "
                "semi-rigide et sa colle bitumineuse subsistent : le sondage porte sur "
                "toute l’épaisseur du complexe, pas sur la couche visible.",
            "Lorsque la résidence dispose d’un local technique de chauffage, "
                "calorifugeages, joints de brides et tresses de robinetterie s’y "
                "contrôlent avant l’intervention d’un mainteneur : le donneur d’ordre est "
                "alors le syndicat des copropriétaires.",
        ],
    ),

    "villenave-d-ornon/pont-de-la-maye": dict(
        methode="Deux missions cohabitent sur ce secteur, et la première question à "
                "trancher est celle du donneur d'ordre. Sur un immeuble accueillant à la "
                "fois des logements et des locaux commerciaux, le syndicat commande le "
                "repérage des parties communes, mais les aménagements intérieurs d'un "
                "local relèvent de son exploitant : sans arbitrage écrit avant la visite, "
                "des volumes restent hors périmètre et ressortent en cours de chantier. "
                "Sur une emprise d'activité vouée à disparaître, la mission change de "
                "nature. Elle se conduit sur bâtiment libéré, fluides coupés et "
                "consignés, avec dépose d'habillages et découpes : c'est ce qui distingue "
                "un repérage avant démolition d'une simple visite. Le livrable, enfin, se "
                "prépare dès l'étude : quantitatifs par local et plans cotés, faute de "
                "quoi les entreprises consultées ne peuvent pas chiffrer. Le diagnostic "
                "portant sur les produits, équipements, matériaux et déchets se conduit "
                "dans le même passage, mais il répond à une autre question : non pas ce "
                "qu'il faut retirer, mais où chaque matériau déposé sera dirigé.",
        cadre="Sur ce secteur, l’obligation change de titulaire selon le local. Pour "
              "les parties communes d’un immeuble d’habitation, le donneur d’ordre est "
              "le syndicat des copropriétaires : il doit le dossier technique amiante "
              "au titre des articles R. 1334-14 et suivants du code de la santé "
              "publique, et le plan pluriannuel de travaux dès lors que le permis de "
              "construire a été délivré depuis plus de quinze ans. Pour les "
              "aménagements d’un local d’activité, l’obligation pèse sur l’exploitant "
              "en qualité de donneur d’ordre, au titre du code du travail. Le repérage "
              "avant travaux comme le repérage avant démolition relèvent des articles "
              "R. 4412-97 et suivants et de l’arrêté du 16 juillet 2019, sans condition "
              "d’âge du bâtiment. Le diagnostic portant sur les produits, équipements, "
              "matériaux et déchets s’ajoute dès mille mètres carrés de surface de "
              "plancher cumulée, ou dès qu’une activité y a mis en œuvre des substances "
              "dangereuses.",
        points=[
            "Sur les bâtiments d’activité, bardages et plaques ondulées de couverture "
                "en fibres-ciment se métrent local par local : leur dépose en zone "
                "commande le phasage et pèse plus lourd sur le budget que le gros œuvre.",
            "Le plénum d’un faux-plafond démontable s’ouvre avant dépose des cloisons "
                ": dalles, suspentes, conduits et calfeutrements de traversée y sont "
                "regroupés hors de vue.",
        ],
    ),

    "gradignan/centre": dict(
        methode="L’erreur la plus coûteuse ici est l’ordre des missions. Un repérage "
                "avant travaux ne se commande pas avant qu’un programme existe : la liste "
                "des matériaux recherchés se déduit du programme détaillé communiqué par "
                "le donneur d’ordre, et un repérage lancé sur une simple intention "
                "produit un rapport que l’entreprise devra faire compléter. "
                "L’enchaînement utile est donc : diagnostic technique global pour "
                "connaître l’état réel, plan pluriannuel pour hiérarchiser et étaler, "
                "programme détaillé une fois le poste voté, puis repérage sur ce "
                "périmètre. Sur le terrain, deux bâtis se partagent la même assemblée. "
                "Dans une échoppe ou une maison en pierre tenue en micro-copropriété, la "
                "visite est brève mais la mesure du plomb prend le temps : chaque "
                "revêtement commun constitue une unité de diagnostic distincte. Dans un "
                "petit collectif des décennies 1960 à 1990, l’essentiel se joue derrière "
                "les habillages — gaines, sous-faces, plénums —, et rien ne s’ouvre sans "
                "autorisation préalable. À réunir avant l’intervention : règlement de "
                "copropriété, procès-verbaux d’assemblée, factures des entreprises "
                "passées, accès aux caves et aux combles.",
        cadre="Trois échéances sont derrière nous. Le plan pluriannuel de travaux, "
              "prévu par l’article 14-2 de la loi du 10 juillet 1965, vise les "
              "syndicats dont le permis de construire a été délivré depuis plus de "
              "quinze ans : la dernière vague, celle des copropriétés d’au plus "
              "cinquante lots, court depuis le 1er janvier 2025. Le diagnostic de "
              "performance énergétique collectif obéit à un autre critère — un permis "
              "déposé avant le 1er janvier 2013, un bâtiment d’habitation collective — "
              "et sa dernière échéance, le 1er janvier 2026, est également passée. Le "
              "diagnostic technique global, régi par l’article L. 731-1 du code de la "
              "construction et de l’habitation, reste le document qui alimente les "
              "deux. Le constat de risque d’exposition au plomb des parties communes, "
              "lui, ne dépend d’aucun calendrier : il tient à la date de construction, "
              "antérieure au 1er janvier 1949.",
        points=[
            "Les menuiseries communes — porte palière, imposte, fenêtre de cage — "
                "constituent des unités de diagnostic distinctes du mur qui les porte : "
                "la mesure du plomb les traite séparément, avant tout décapage.",
            "Sur les petits collectifs, le mastic d’étanchéité en périphérie des "
                "menuiseries se prélève avant campagne de remplacement, indépendamment de "
                "l’état apparent du dormant.",
            "Sur les paliers, le ragréage ou le doublage ajouté sous le revêtement "
                "lors d’une remise en état est un point de sondage systématique avant "
                "reprise de sol.",
        ],
    ),

    "gradignan/malartic": dict(
        methode="Sur ce secteur, la mission commence toujours par les mêmes volumes : "
                "locaux techniques, gaines et cheminements de réseaux. C’est là que se "
                "concentrent les calorifugeages, et c’est là qu’un mainteneur "
                "interviendra en premier ; un repérage qui les traite en fin de visite "
                "laisse le poste le plus dimensionnant au chiffrage approximatif. Ces "
                "volumes ne s’ouvrent pas seuls : consignation des installations, arrêt "
                "de la distribution, moyens d’accès en hauteur et équipements de "
                "protection se calent à la commande. Deux donneurs d’ordre se partagent "
                "ensuite le secteur, et n’imposent pas le même rythme. Pour une "
                "résidence, le syndicat commande, et la contrainte est l’accès : "
                "l’échantillonnage se construit par typologie de logement et non par "
                "bâtiment, et les rendez-vous se prennent plusieurs semaines à l’avance. "
                "Pour un maître d’ouvrage institutionnel, la contrainte est le calendrier "
                "d’exploitation : les sondages destructifs se placent en période de "
                "fermeture, et le rapport rejoint le dossier de consultation des "
                "entreprises, pas le marché signé.",
        cadre="Deux référentiels de repérage se rencontrent ici. Sur l’immeuble bâti, "
              "le repérage avant travaux relève du code du travail, articles R. 4412-97 "
              "à R. 4412-97-6, et de l’arrêté du 16 juillet 2019, conduit selon la NF X "
              "46-020 d’août 2017 ; il ne connaît aucune date d’exclusion, y compris "
              "sur les constructions les plus récentes du secteur. Sur les "
              "installations, structures et équipements concourant à une activité, le "
              "référentiel est la NF X 46-100, rendue opposable par l’arrêté du 22 "
              "juillet 2021 : c’est un domaine distinct, qu’une mission portant sur le "
              "bâti ne couvre pas. En parties communes de résidence, le dossier "
              "technique amiante, prévu aux articles R. 1334-14 et suivants du code de "
              "la santé publique, se tient à jour et fait l’objet d’une évaluation "
              "périodique de l’état de conservation ; sa fiche récapitulative se remet "
              "à toute entreprise intervenant sur l’immeuble.",
        points=[
            "Les plaques et panneaux de protection thermique posés derrière les "
                "générateurs et le long des parois de local technique sont fréquemment "
                "omis, parce qu’ils passent pour un simple doublage.",
            "Les joints des portes coupe-feu de circulation et de local technique se "
                "prélèvent avant remplacement d’huisserie, indépendamment de l’état du "
                "vantail.",
            "Sur les équipements techniques et les installations d’un bâtiment "
                "d’enseignement, le référentiel n’est pas celui de l’immeuble bâti : la "
                "mission se scinde dès la commande, sous peine de laisser une partie du "
                "périmètre sans repérage.",
        ],
    ),

    "gradignan/cayac": dict(
        methode="Sur ce bâti, la visite se conduit de bas en haut et commence par les "
                "bois en contact avec la maçonnerie humide : pieds de mur, abouts de "
                "solive, lambourdes, plinthes et seuils. C’est le seul ordre qui permette "
                "d’arbitrer, avant de repartir, l’extension des sondages. L’examen "
                "parasitaire et le repérage amiante se conduisent dans le même passage, "
                "parce qu’ils réclament exactement les mêmes ouvertures : dépose de "
                "plinthe, découpe de doublage, ouverture de trappe. Les mener séparément "
                "revient à payer deux fois la remise en état. Ce qui fait durer une "
                "intervention ici tient à deux choses : le vide sanitaire, quand il en "
                "existe un, dont la trappe est souvent condamnée et le cheminement "
                "encombré, et les dépendances, dont les clés sont rarement disponibles le "
                "jour dit. À préparer : trappes ouvertes, abords de murs dégagés sur une "
                "largeur utile, accès aux annexes. Une limite à poser dès la commande : "
                "le constat parasitaire décrit un état, il ne conclut pas sur l’origine "
                "de l’humidité, qui relève d’un examen distinct.",
        cadre="126-4 et suivants du code de la construction et de l'habitation et de "
              "l'arrêté du 29 mars 2007, modifié le 7 mars 2012 : il n'est exigible que "
              "dans les zones délimitées par arrêté préfectoral, la Gironde étant "
              "couverte de longue date. Un décalage subsiste : l'arrêté vise la NF "
              "P03-201 de mars 2012, tandis que l'AFNOR publie la version de février "
              "2016, jamais reprise par un texte. Le repérage amiante avant travaux, "
              "lui, relève du code du travail et ne connaît aucune date d'exclusion ; "
              "le plan pluriannuel de travaux, enfin, vise les syndicats dont le permis "
              "de construire a été délivré depuis plus de quinze ans.",
        points=[
            "L’about de solive, au droit de son entrée dans la maçonnerie, se sonde "
                "au poinçon avant toute reprise de sol : c’est le point où l’attaque "
                "commence, et le seul qui ne se voie pas depuis la pièce.",
            "En sous-face de plancher bas, doublage et isolant rapportés se traitent "
                "d’un même geste : sondage amiante et examen de l’état des bois porteurs.",
            "En charpente, galeries de sortie et vermoulure se cherchent d’abord au "
                "droit des pénétrations de couverture et des abouts de panne, là où l’eau "
                "a transité.",
            "Sur un bâti ancien, le risque plomb des peintures conditionne la "
                "protection de l’entreprise appelée à décaper, au titre du code du "
                "travail ; en immeuble collectif d’habitation antérieur à 1949, le "
                "constat porte sur les parties communes.",
        ],
    ),

    "floirac/dravemont": dict(
        methode="Un repérage en site occupé se prépare comme une opération, pas comme une "
                "visite. Le plan de sondage s’arrête sur plan avant le premier "
                "déplacement : une liste de logements par cage et par typologie, un "
                "nombre de sondages par ouvrage, et un protocole de remise en état après "
                "percement — humidification, colmatage, nettoyage — sans lequel aucun "
                "conseil syndical ne donnera son accord. Vient ensuite une étape que les "
                "campagnes de réhabilitation successives rendent indispensable : le "
                "dépouillement des rapports antérieurs et des attestations de retrait. "
                "Sans lui, on sonde à nouveau ce qui a été traité, on le chiffre une "
                "seconde fois, et l’on perd le crédit du reste du rapport. L’information "
                "des occupants et la prise de rendez-vous absorbent l’essentiel du délai, "
                "bien avant la technique. Enfin, sur une même opération, deux périmètres "
                "coexistent souvent : le bâti conservé, où le repérage se limite au "
                "programme de travaux, et le bâti voué à disparaître, où il devient "
                "exhaustif et se conduit sur bâtiment libéré. Ils ne se mènent ni au même "
                "moment, ni avec le même niveau de destruction.",
        cadre="Le repérage avant travaux est une obligation du donneur d’ordre au titre "
              "du code du travail, articles R. 4412-97 à R. 4412-97-6, précisée par le "
              "décret n° 2017-899 du 9 mai 2017 modifié et par l’arrêté du 16 juillet "
              "2019. La NF X 46-020 d’août 2017 en fixe la méthode, son tableau A1 la "
              "liste minimale des matériaux à rechercher, en fonction du programme "
              "détaillé des travaux. Un point de procédure est souvent négligé : "
              "l’opérateur soumet au donneur d’ordre, pour avis, le périmètre et le "
              "programme de repérage avant toute investigation sur site — un rapport "
              "établi sans cette étape est contestable. La mission exige une "
              "certification avec mention, au sens de l’arrêté du 25 juillet 2016, et "
              "un opérateur indépendant du donneur d’ordre comme de l’entreprise de "
              "travaux. Le rapport se remet aux entreprises dès la consultation, non à "
              "la signature du marché.",
        points=[
            "Lorsque la façade est constituée de panneaux préfabriqués, le mastic des "
                "joints entre panneaux et le calfeutrement des appuis de baie se "
                "prélèvent avant toute intervention d’enveloppe, tableaux compris.",
            "Une gaine technique verticale et sa trappe palière s’ouvrent avant "
                "reprise de colonne : conduits, habillages et joints restent en place "
                "derrière un coffrage refait.",
            "Sous le revêtement de sol des paliers et des logements, ce sont le "
                "ragréage et la colle qui portent le risque, parfois deux couches sous la "
                "surface visible : le sondage traverse tout le complexe.",
            "Les locaux communs en pied de bâtiment, de faible surface, sortent "
                "souvent des programmes de travaux ; ils ne sortent jamais du périmètre "
                "de repérage dès lors que le programme les touche.",
        ],
    ),

    "floirac/les-coteaux": dict(
        methode="La pente commande l’ordre de la visite. On commence par le niveau le "
                "plus bas — caves et rez-de-chaussée —, là où se cumulent remontées "
                "d’humidité, réseaux et attaque des bois, puis on remonte cage par cage. "
                "Le constat plomb des parties communes se conduit dans le même passage, "
                "la mesure se faisant par fluorescence X sur site, unité de diagnostic "
                "par unité de diagnostic ; le prélèvement n’intervient qu’en cas "
                "d’impossibilité de mesure directe. Les ouvertures nécessaires se listent "
                "avant l’intervention : dépose de plinthe, découpe de doublage, ouverture "
                "de trappe. Sur un bâti ancien tenu par une copropriété de quelques lots, "
                "elles se négocient une par une, et c’est ce qui allonge la mission bien "
                "plus que le nombre de sondages. Le relief pèse aussi sur la logistique : "
                "stationnement, matériel monté à la main, évacuation des déchets. À "
                "préparer : caves dégagées, clés des annexes, plans s’il en existe, et un "
                "point d’arrêt convenu pour arbitrer une extension de sondages en cours "
                "de visite.",
        cadre="Le constat de risque d’exposition au plomb des parties communes relève "
              "des articles L. 1334-5 et suivants du code de la santé publique et de la "
              "norme NF X 46-030 d’avril 2008, complétée par la NF X 46-031 pour "
              "l’analyse chimique des peintures et la NF X 46-032 pour le plomb dans "
              "les poussières au sol. Il vise les immeubles d’habitation construits "
              "avant le 1er janvier 1949 et porte alors sur l’ensemble des revêtements "
              "des parties communes. Le repérage amiante avant travaux relève d’un tout "
              "autre texte : le code du travail, articles R. 4412-97 et suivants, et "
              "l’arrêté du 16 juillet 2019, qui ne fixent aucune date d’exclusion — la "
              "date du 1er juillet 1997 borne le champ du code de la santé publique, "
              "pas celui-là. Le plan pluriannuel de travaux, enfin, s’impose depuis le "
              "1er janvier 2025 aux copropriétés d’au plus cinquante lots.",
        points=[
            "En pied de mur et au droit des abouts de solive engagés dans la "
                "maçonnerie, le sondage des bois précède tout doublage ou toute reprise "
                "de sol.",
            "Dans un immeuble collectif d’habitation antérieur à 1949, le constat "
                "porte sur tous les revêtements des parties communes, quelle que soit la "
                "date de pose du repeint qui les recouvre.",
            "Le revêtement de sol posé après-guerre sur le plancher bois d’origine "
                "des paliers se sonde sur toute l’épaisseur : le risque tient à la colle "
                "autant qu’à la dalle.",
            "Le conduit de fumée et sa souche, habillés lors d’une réfection, se "
                "repèrent avant montage de l’échafaudage : une fois celui-ci en place, "
                "l’accès ne se rejoue pas.",
        ],
    ),

    "floirac/garonne-eiffel": dict(
        methode="Tout commence par un désaccord de vocabulaire à lever : un aménageur "
                "raisonne par emprise, un opérateur de repérage par bâtiment et par "
                "ouvrage. La première étape est donc contradictoire, plans à l’appui — ce "
                "qui tombe, ce qui reste, ce qui est déjà démoli, et à quelle date chaque "
                "partie a été autorisée. De ce calage dépend le périmètre du rapport, "
                "donc sa recevabilité en pièce annexe. Vient la reconnaissance des accès "
                ": bâtiment libéré, fluides coupés et consignés, moyens d’accès en "
                "hauteur pour les charpentes et les sous-faces de couverture, ouverture "
                "des galeries, caniveaux et vides sanitaires. Le repérage avant "
                "démolition autorise la dépose d’habillages et la découpe — c’est ce qui "
                "le distingue d’une visite, et ce qui fixe sa durée. Le rendu se conçoit "
                "enfin dès l’étude : quantitatifs par local, plans de repérage cotés, "
                "localisation sans ambiguïté, exutoire identifié. Deux limites se posent "
                "à la commande : les équipements de process ne relèvent pas du "
                "référentiel du bâti, et la pollution des sols n’entre dans aucune de ces "
                "missions.",
        cadre="Le repérage avant démolition relève du code du travail, articles R. "
              "4412-97 à R. 4412-97-6, du décret n° 2017-899 du 9 mai 2017 modifié par "
              "le décret n° 2019-251 et de l’arrêté du 16 juillet 2019. Conduit selon "
              "la NF X 46-020 d’août 2017 sur un périmètre exhaustif incluant la liste "
              "C, il vaut repérage avant travaux ; un repérage avant travaux ne peut "
              "jamais tenir lieu de repérage avant démolition. Les installations, "
              "structures et équipements concourant à une activité relèvent de la NF X "
              "46-100 et de l’arrêté du 22 juillet 2021 : sur une friche, bâti et "
              "process forment deux missions. Le diagnostic portant sur les produits, "
              "équipements, matériaux et déchets se conduit avant le dépôt de la "
              "demande de permis de démolir ou, à défaut, avant l’acceptation des devis "
              "de travaux. La mission suppose un opérateur certifié avec mention.",
        points=[
            "Lorsqu’une emprise comporte galeries techniques et caniveaux enterrés, "
                "ils concentrent conduits et calorifugeages : ils s’ouvrent et se "
                "repèrent avant curage, jamais pendant.",
            "Les mortiers-colle et les enduits des locaux humides sont des matériaux "
                "de liste C : invisibles tant que le carrelage tient, ils ne se repèrent "
                "que sur bâtiment libéré.",
            "Les joints, tresses et plaques d’isolation des portes coupe-feu et des "
                "cloisons techniques se relèvent porte par porte, l’habillage ne "
                "renseignant jamais sur le contenu.",
            "Sur un bâtiment industriel ou ferroviaire, l’ancienneté n’ouvre pas le "
                "constat plomb, réservé aux immeubles d’habitation : le risque plomb des "
                "peintures de charpente et de menuiserie métallique se traite au titre du "
                "code du travail, dans le mode opératoire de l’entreprise.",
        ],
    ),

}
