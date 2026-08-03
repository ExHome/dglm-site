# -*- coding: utf-8 -*-
"""
TEXTES DE FOND DES COMMUNES.

Les pages de ville n'affichaient qu'un titre et une grille de vignettes :
160 mots, et rien à apprendre. Ces textes leur donnent un contenu réel —
le parc bâti, ce qu'il implique pour les missions collectives, la forme que
prend la copropriété sur place, et les repères de terrain.

Ils ont été rédigés puis passés à deux contrôles successifs : le premier a
relevé 142 défauts, le second 127, dont dix fautes professionnelles graves
— des formules laissant croire qu'un bâtiment récent échapperait au repérage
amiante. Toutes ont été corrigées ou supprimées.

RÈGLE DE MODIFICATION : aucune phrase ne doit laisser entendre qu'un bâtiment
est exempt d'amiante ou de plomb du fait de son âge. Le code du travail ne
connaît aucune date d'exclusion pour le repérage avant travaux ; seule la
présomption de présence est datée.
"""

TEXTES = {
    "bordeaux": dict(
        parc="Bordeaux superpose trois strates. La pierre d’abord : immeubles de rapport "
             "des XVIIIe et XIXe siècles en calcaire régional, planchers bois, escaliers "
             "de pierre, tuile canal, dans un centre inscrit au patrimoine mondial au "
             "titre du Port de la Lune. Les faubourgs ensuite, où l’échoppe mitoyenne et "
             "basse tient des rues entières à Nansouty, Saint-Genès ou Saint-Augustin. "
             "Le collectif d’après-guerre enfin : le Grand Parc, les Aubiers, Bacalan. "
             "S’y ajoutent chais des Chartrons et entrepôts de Bacalan, reconvertis en "
             "logements au fil des dernières décennies : structure ancienne, "
             "aménagements récents, deux histoires de matériaux dans un même bâtiment.",
        enjeu="Le point dur bordelais n’est pas l’âge du bâti, c’est son empilement. Dans "
              "un immeuble d’habitation construit avant le 1er janvier 1949, le plomb se "
              "tient dans les peintures des cages d’escalier et des menuiseries : les "
              "parties communes relèvent du constat de risque d’exposition au plomb. "
              "L’amiante appartient aux couches de travaux postérieures, jusqu’à "
              "l’interdiction entrée en vigueur le 1er janvier 1997 : dalles de hall, "
              "colles, conduits, enduits de rebouchage, faux-plafonds. Le seuil qui "
              "commande le repérage reste le permis de construire délivré avant le 1er "
              "juillet 1997, jamais la date des murs. Deuxième particularité : la "
              "contrainte vient du site patrimonial remarquable et des abords de "
              "monuments historiques, non de l’inscription au patrimoine mondial. "
              "L’étendue des sondages destructifs s’arbitre avec l’architecte des "
              "Bâtiments de France, en amont de l’autorisation de travaux. Enfin, pour "
              "les copropriétés de cinquante lots au plus, nombreuses dans le centre "
              "ancien, le plan pluriannuel de travaux court depuis le 1er janvier 2025 et "
              "le DPE collectif depuis le 1er janvier 2026.",
        copro="La copropriété bordelaise est d’abord une affaire de petite taille. "
              "Échoppes divisées en deux ou trois lots, immeubles de rapport découpés "
              "étage par étage, chais transformés en une poignée de logements : le "
              "conseil syndical y gère un immeuble sans ascenseur, sans chauffage "
              "collectif ni document technique. Le règlement peut remonter à une division "
              "très ancienne comme dater des années 1980, sans rapport avec l’âge des "
              "murs ; ses clauses contraires à la loi du 10 juillet 1965 sont réputées "
              "non écrites. À l’opposé, les ensembles d’après-guerre concentrent le "
              "risque amiante dans leurs équipements communs : chaufferie, vide-ordures, "
              "gaines. Un même syndic gère les deux profils, à obligations comparables et "
              "budgets sans commune mesure.",
        reperes=[
            "Dans une cage d’escalier d’immeuble collectif d’habitation antérieur à "
                "1949, la réfection des peintures s’appuie sur le constat de risque "
                "d’exposition au plomb des parties communes : l’un des chantiers les plus "
                "souvent engagés sans ce document.",
            "Un chai des Chartrons reconverti en logements est un bâtiment du XIXe "
                "siècle porteur d’une couche de travaux récente.",
            "En site patrimonial remarquable, aucun sondage destructif de façade ou de "
                "cage d’escalier ne s’improvise : le plan de sondage se valide en amont "
                "avec l’architecte des Bâtiments de France.",
            "Les caves voûtées, humides et encombrées, abritent les réseaux ajoutés "
                "après-guerre : un local qu’aucun repérage ne devrait écarter malgré sa "
                "faible surface.",
        ],
    ),

    "merignac": dict(
        parc="Mérignac s’est constituée autour de ses bourgs — Arlac, Capeyron, Beutre — "
             "avant que l’aéroport et l’industrie aéronautique n’y fixent une population "
             "ouvrière et technicienne. Il en reste un pavillonnaire très étendu, des "
             "cités et des résidences bâties pour ces emplois, et les grands ensembles "
             "du Burck et de Beaudésert. Sur les grandes voies et autour du secteur "
             "commercial de Mérignac-Soleil se sont ajoutés, jusqu’aux années 1990, des "
             "immeubles de trois à cinq niveaux couverts en terrasse. Le tramway et la "
             "requalification commerciale insèrent depuis des programmes neufs dans un "
             "tissu resté horizontal.",
        enjeu="Deux sujets structurent les missions collectives. Le premier est la "
              "toiture-terrasse. Le complexe d’étanchéité bitumineux figure en liste B au "
              "titre du dossier technique amiante des parties communes, mais le repérage "
              "avant travaux ne s’y limite pas : il couvre tous les matériaux que le "
              "programme va toucher, avant reprise d’acrotère, réfection de relevé ou "
              "pose d’équipement. C’est un poste que les plans pluriannuels chiffrent "
              "souvent sans l’avoir fait contrôler. Le second tient à la nature "
              "horizontale du bâti : maisons groupées, copropriétés horizontales, "
              "lotissements dotés d’une association syndicale libre. Or une association "
              "syndicale de propriétaires relève de l’ordonnance du 1er juillet 2004, non "
              "du statut de la copropriété : le plan pluriannuel de travaux ne lui est "
              "pas exigible, ni le DPE collectif, réservé aux bâtiments d’habitation "
              "collective. Qualifier le statut de l’ensemble avant de commander la "
              "mission évite un rapport sans destinataire.",
        copro="La copropriété mérignacaise est éclatée. Beaucoup de syndicats de dix à "
              "cinquante lots, dispersés sur un territoire vaste, aux équipements communs "
              "modestes : une chaufferie ou des chaudières individuelles, un local "
              "technique, un sous-sol partiel. À côté, le Burck et Beaudésert mêlent "
              "patrimoine de bailleurs sociaux et lots de copropriétaires, sur des "
              "calendriers de réhabilitation qui débordent le mandat d’un conseil "
              "syndical. Le mur est partout le même : aucune archive depuis la livraison, "
              "un carnet d’entretien vierge, des devis d’étanchéité chiffrés en supposant "
              "le repérage de terrasse déjà fait. Les copropriétés issues des programmes "
              "neufs entreront dans le champ du plan pluriannuel à mesure qu’elles "
              "franchiront quinze ans ; le DPE collectif, lui, obéit à un autre critère : "
              "un permis de construire déposé avant le 1er janvier 2013.",
        reperes=[
            "Sur les immeubles couverts en terrasse, l’étanchéité bitumineuse "
                "multicouche se repère avant toute reprise de relevé, d’acrotère ou "
                "d’évacuation d’eaux pluviales, même pour une réparation ponctuelle.",
            "Dans le pavillonnaire dont le permis de construire est antérieur au 1er "
                "juillet 1997 — y compris les maisons intégrées à une copropriété "
                "horizontale —, les plaques ondulées en fibres-ciment des garages, abris et "
                "auvents figurent parmi les matériaux les plus souvent mis au jour par un "
                "repérage avant travaux ou avant démolition.",
            "Avant toute programmation, réclamer les statuts : une association "
                "syndicale gère des ouvrages communs sans relever du régime de la "
                "copropriété, et le plan pluriannuel de travaux ne lui est pas opposable.",
            "Dans les chaufferies gaz collectives d’avant 1997, calorifugeages, joints "
                "de brides et tresses se contrôlent avant toute intervention d’un "
                "mainteneur : seule l’analyse en laboratoire écarte l’amiante.",
        ],
    ),

    "pessac": dict(
        parc="Pessac réunit des objets bâtis sans rapport les uns avec les autres. Les "
             "Quartiers modernes Frugès, maisons en béton armé conçues par Le Corbusier "
             "et Pierre Jeanneret dans les années 1920, inscrites au patrimoine mondial "
             "avec l’œuvre architecturale de leur auteur. Le vignoble de Pessac-Léognan, "
             "dont chartreuses, chais et dépendances agricoles restent enclavés dans le "
             "tissu urbain. Le grand ensemble de Saige, tours et barres des décennies "
             "1960 et 1970. Le domaine universitaire et le site hospitalier du "
             "Haut-Lévêque, avec résidences et bâtiments techniques. Vers Toctoucau "
             "enfin, un pavillonnaire diffus sur la lande : d’un chantier à l’autre, la "
             "méthode change du tout au tout.",
        enjeu="Le calendrier réglementaire a rattrapé Pessac par le haut, la commune "
              "comptant de très grandes copropriétés : au-delà de deux cents lots, le "
              "plan pluriannuel de travaux était dû au 1er janvier 2023 et le DPE "
              "collectif au 1er janvier 2024 ; les petites copropriétés du centre ne sont "
              "entrées dans le premier qu’au 1er janvier 2025, dans le second qu’au 1er "
              "janvier 2026. Sur les grands ensembles, la difficulté est ailleurs : un "
              "repérage avant travaux ne s’arrête pas aux parties communes, et dès que le "
              "programme touche menuiseries, gaines ou sols des logements, l’accès aux "
              "parties privatives s’organise — assemblée générale, calendrier de visites, "
              "relances. C’est ce point, non la technique, qui fait glisser les "
              "plannings. L’échantillonnage couvre chaque typologie de logement d’un même "
              "bâtiment, un sondage ne valant que pour l’ouvrage qu’il traverse. À "
              "l’autre extrémité, le bâti protégé au titre des monuments historiques et "
              "le patrimoine viticole imposent d’arbitrer les sondages destructifs avant "
              "la visite.",
        copro="Trois familles de copropriétés cohabitent. Les grands ensembles de Saige, "
              "où chaque décision se chiffre à une échelle étrangère à celle d’un "
              "immeuble ordinaire et où le fonds de travaux se constitue sur une "
              "décennie. Les résidences des avenues et des abords du campus, avec "
              "sous-sol, espaces verts communs et chaufferie : charges lourdes, "
              "équipements en fin de vie au même moment. Les petites copropriétés du "
              "centre-ville et des rues d’échoppes, issues de divisions, sans carnet "
              "d’entretien exploitable. S’y ajoute un cas particulier : les maisons "
              "Frugès, propriétés privées individuelles dont plusieurs sont protégées au "
              "titre des monuments historiques. Chaque propriétaire décide pour sa "
              "parcelle, mais toute autorisation de travaux s’instruit au regard de la "
              "cohérence de l’ensemble bâti.",
        reperes=[
            "Sur les maisons Frugès, l’ancienneté ne dispense de rien : "
                "l’amiante-ciment est employé industriellement bien avant guerre, et la "
                "borne réglementaire reste le 1er juillet 1997, date de délivrance du "
                "permis. Le risque se loge dans les couches d’entretien postérieures — "
                "sols, étanchéités, réseaux — et le plomb dans les peintures anciennes.",
            "Sur une barre de Saige, un rapport bâti sur deux appartements expose le "
                "chantier à un arrêt dès la découverte d’un matériau non repéré, et "
                "l’entreprise de retrait est fondée à en refuser l’exécution.",
            "Les réhabilitations successives ont déjà retiré une partie des matériaux : "
                "le repérage intègre rapports antérieurs et attestations de retrait, sous "
                "peine de redécouvrir ce qui a été traité.",
            "L’accès aux parties privatives se prépare en assemblée générale avant le "
                "lancement de la mission, jamais pendant.",
        ],
    ),

    "talence": dict(
        parc="Talence n’a plus ni friche industrielle ni réserve foncière : hors les "
             "hectares de vigne classés en Pessac-Léognan qui subsistent à l’ouest — "
             "Château La Mission Haut-Brion y est implanté, le vignoble de Château "
             "Haut-Brion étant à cheval sur Pessac et Talence —, elle est bâtie d’un "
             "bout à l’autre. Son histoire tient en deux temps. D’abord un tissu "
             "d’échoppes et d’immeubles de rapport en pierre, prolongement des faubourgs "
             "bordelais le long des voies parties des anciennes barrières. Puis, à "
             "partir des années 1960, le domaine universitaire et Thouars font basculer "
             "la commune dans le collectif : immeubles de trois à dix niveaux, studios "
             "en nombre, chaufferies desservant plusieurs bâtiments. Depuis, elle se "
             "renouvelle sur elle-même : surélévations, pavillon remplacé par un petit "
             "collectif, densification autour du tramway et de la Médoquine.",
        enjeu="Faute de foncier, Talence se densifie sur son propre bâti : surélévations, "
              "extensions, cession du droit de surélever par des copropriétés qui y "
              "voient un financement de travaux. Une surélévation sur un immeuble d’avant "
              "le 1er juillet 1997 déclenche un repérage avant travaux visant "
              "toiture-terrasse, acrotères, souches et gaines mises à nu ; il incombe au "
              "donneur d’ordre au titre du code du travail, suit les modalités de "
              "l’arrêté du 16 juillet 2019 et se remet aux entreprises dès la "
              "consultation. Elle suppose aussi que la copropriété connaisse l’état réel "
              "de ses parties communes : le diagnostic technique global lui permet de "
              "délibérer sur un état des lieux, non sur une promesse d’opérateur. Second "
              "point, propre aux ensembles conçus d’un seul tenant : chaufferies "
              "desservant plusieurs bâtiments et réseaux enterrés en caniveau technique "
              "sortent du périmètre habituel des visites, et aucune entreprise ne devrait "
              "en ouvrir un sans repérage préalable.",
        copro="Le parc collectif talençais s’est constitué autour de l’université : "
              "beaucoup de studios et de deux-pièces, donc beaucoup de propriétaires "
              "bailleurs non résidents. Les assemblées s’en ressentent : participation "
              "faible, majorités difficiles à réunir sur des travaux dont un bailleur ne "
              "perçoit pas le bénéfice direct. À l’autre bout, les syndicats nés du tissu "
              "d’échoppes comptent souvent moins de dix lots et fonctionnent sans syndic "
              "professionnel. Entre les deux, les résidences des décennies 1960 à 1980, "
              "chauffage collectif et parties communes étendues, portent l’essentiel des "
              "charges et des obligations : plan pluriannuel de travaux, fonds de travaux "
              "alimenté par une cotisation annuelle dont la loi fixe le minimum, DPE "
              "collectif si le permis de construire a été demandé avant le 1er janvier "
              "2013.",
        reperes=[
            "Les gaines palières et leurs trappes de visite, dans les résidences "
                "d’avant 1997, sont souvent habillées de plaques en fibres-ciment : à "
                "contrôler avant tout remplacement de colonne, seule l’analyse permettant "
                "de conclure.",
            "Avant de céder un droit de surélévation, une copropriété a intérêt à "
                "disposer d’un diagnostic technique global : il objective l’état apparent "
                "des parties communes et des équipements sollicités.",
            "Un caniveau technique reliant deux bâtiments n’est pas une partie commune "
                "visible : son ouverture suppose un repérage dédié, commandé par le donneur "
                "d’ordre.",
            "Dans les copropriétés à majorité de bailleurs, planifier le repérage sur "
                "les périodes de rotation des locataires reste le moyen le plus simple "
                "d’obtenir l’accès aux logements.",
        ],
    ),

    "begles": dict(
        parc="Bègles s’étend sur les palus de la rive gauche, terres basses et humides "
             "où le sous-sol est rare et le plancher bas posé sur vide sanitaire. Le "
             "bâti garde la trace du passé morutier et industriel de la commune : "
             "sécheries, entrepôts, ateliers et halles alignés entre la voie ferrée et "
             "le fleuve, dont une partie est aujourd’hui reconvertie en logements ou en "
             "bureaux. Autour s’étend un tissu dense d’échoppes et de maisons ouvrières "
             "mitoyennes, avec courées et dépendances de fond de parcelle. Le secteur "
             "des Terres Neuves porte le collectif d’après-guerre et les opérations de "
             "renouvellement urbain qui l’ont remplacé ; le sud associe emprises "
             "commerciales et programmes résidentiels récents.",
        enjeu="La reconversion du bâti industriel domine les missions bèglaises, et se "
              "joue rarement en une seule intervention. Une ancienne sécherie transformée "
              "en logements fait presque toujours l’objet d’une démolition partielle avec "
              "conservation de l’enveloppe : repérage avant démolition et repérage avant "
              "travaux portent alors sur des périmètres distincts, calés sur le phasage "
              "réel du chantier, faute de quoi des zones se découvrent en cours "
              "d’exécution. Le second obéit à l’arrêté du 16 juillet 2019 : il incombe au "
              "donneur d’ordre et se remet aux entreprises dès leur consultation. S’y "
              "ajoute, en démolition comme en rénovation significative, le diagnostic "
              "portant sur les produits, équipements, matériaux et déchets, dû dès que le "
              "bâtiment dépasse mille mètres carrés de surface de plancher ou qu’il a "
              "accueilli une activité industrielle, agricole ou commerciale mettant en "
              "œuvre des substances dangereuses — pièce désormais couramment réclamée à "
              "la consultation. Sur les échoppes divisées en lots, les peintures "
              "antérieures à 1949 imposent le constat plomb des parties communes, conduit "
              "dans la même visite que le repérage des matériaux amiantés apportés "
              "après-guerre.",
        copro="Trois familles se côtoient. Les copropriétés nées de la reconversion d’un "
              "bâtiment industriel ont un règlement récent posé sur une structure "
              "ancienne : charpente métallique, planchers rapportés, verrières, volumes "
              "atypiques dont l’historique de travaux n’a jamais été reconstitué. Les "
              "micro-copropriétés issues de la division d’échoppes ouvrières fonctionnent "
              "souvent sans syndic professionnel, sans carnet d’entretien et sans "
              "document technique. Les immeubles collectifs des axes abordent leur "
              "premier cycle de gros entretien avec des équipements d’origine. L’obstacle "
              "tient donc moins à l’âge du bâti qu’à l’absence de mémoire technique. Sur "
              "un immeuble reconverti, le repérage commence par le dépouillement des "
              "autorisations d’urbanisme successives : elles datent les couches de "
              "travaux et bornent le périmètre de la mission.",
        reperes=[
            "Sur les anciennes sécheries et les entrepôts, la couverture en plaques "
                "ondulées et les bardages en fibres-ciment sont les premiers postes à "
                "métrer : leur dépose en zone amiantée commande le phasage et pèse lourd "
                "sur le budget de déconstruction.",
            "Dans les logements aménagés au sein de ces volumes sous un permis de "
                "construire antérieur au 1er juillet 1997, la dalle semi-rigide et surtout "
                "sa colle bitumineuse subsistent sous le revêtement posé depuis.",
            "Sur les palus, l’humidité en pied de mur attaque les planchers bois : un "
                "diagnostic parasitaire avant réhabilitation éclaire l’arbitrage du "
                "programme de travaux de la copropriété.",
            "Le repérage amiante ne dit rien de la pollution des sols d’une ancienne "
                "emprise industrielle : il s’articule avec une étude de sols confiée à un "
                "bureau spécialisé.",
        ],
    ),

    "villenave-d-ornon": dict(
        parc="Villenave-d’Ornon n’a pas un centre mais plusieurs noyaux, longtemps "
             "séparés par des terres agricoles : le bourg ancien autour de l’église, et "
             "le Pont-de-la-Maye au contact de Bègles. Entre eux, la route de Toulouse a "
             "fixé un chapelet d’immeubles de rapport, de commerces en pied d’immeuble "
             "et de petites résidences construits des années 1960 aux années 1990. La "
             "commune conserve des domaines viticoles en appellation, des terres "
             "maraîchères et des emprises de recherche agronomique. Depuis le "
             "prolongement du tramway, zones d’aménagement concerté et programmes neufs "
             "se sont posés au contact du pavillonnaire des années 1970-1980, sans "
             "transition d’échelle.",
        enjeu="La densification a créé un effet de seuil rarement anticipé. Les "
              "résidences livrées au tournant des années 2000, le long de la route de "
              "Toulouse, ont dépassé depuis longtemps les quinze ans à partir desquels le "
              "plan pluriannuel de travaux s’impose, et les programmes des années 2010 "
              "les rejoignent. Le diagnostic de performance énergétique collectif suit un "
              "autre critère : le permis déposé avant le 1er janvier 2013, avec une "
              "échéance déjà passée pour les syndicats d’au plus cinquante lots. "
              "L’exercice ne consiste pas à repérer un matériau dangereux, mais à étaler "
              "sur dix ans un renouvellement d’équipements simultané — ce qu’objective le "
              "diagnostic technique global. Sur les collectifs des années 1970-1980, le "
              "repérage avant travaux reste à l’inverse la porte d’entrée obligatoire.",
        copro="Deux régimes se répondent. Sur la route de Toulouse, les immeubles de "
              "rapport des années 1960-1990 mêlent logements et commerces en "
              "rez-de-chaussée : la répartition des charges entre lots d’habitation et "
              "lots commerciaux y nourrit des contestations, et l’exposition à la "
              "circulation dégrade façades et menuiseries. Dans les opérations récentes, "
              "la copropriété n’est qu’un étage de la gestion : elle cohabite avec une "
              "association foncière urbaine ou une association syndicale qui porte "
              "voiries, espaces communs et bassins de rétention. Un conseil syndical y "
              "constate souvent tardivement qu’une partie des ouvrages à entretenir "
              "n’appartient pas au syndicat, et que le plan pluriannuel de travaux, "
              "limité à ses parties communes et à ses équipements, ne les couvre pas.",
        reperes=[
            "Sur les immeubles de la route de Toulouse dont le permis de construire est "
                "antérieur au 1er juillet 1997, faux-plafonds de hall et gaines techniques "
                "de cage d’escalier sont les volumes à ouvrir en premier.",
            "Les toitures-terrasses des résidences du tournant des années 2000 sont "
                "sorties de garantie décennale : l’examen de l’étanchéité, des acrotères et "
                "des évacuations commande l’ordre des postes du plan pluriannuel.",
            "Les dépendances agricoles et viticoles conservées dans le tissu "
                "pavillonnaire portent des couvertures en plaques ondulées de fibres-ciment "
                ": leur dépose relève du repérage avant travaux, le repérage avant "
                "démolition ne s’imposant que si la dépendance est abattue.",
            "Dans les parties basses du Pont-de-la-Maye, les locaux techniques enterrés "
                "subissent des remontées d’eau : les calorifugeages y sont plus dégradés "
                "que dans le reste de l’immeuble.",
        ],
    ),

    "gradignan": dict(
        parc="Gradignan s’est développée le long de l’Eau Bourde, dans une vallée humide "
             "jalonnée d’anciens moulins et du prieuré de Cayac, où les parcs des "
             "anciens domaines ont fixé le centre. Autour de ce noyau, la commune s’est "
             "bâtie par lotissements successifs, des années 1950 aux années 1990, en "
             "maisons individuelles posées sous un couvert de pins et de chênes "
             "largement conservé. Le collectif reste minoritaire et prend la forme de "
             "petites résidences insérées le long des grands axes et aux abords du "
             "domaine universitaire, dont une partie s’étend sur le territoire communal. "
             "S’y ajoutent des équipements publics d’envergure et un patrimoine communal "
             "ancien, entretenu bâtiment par bâtiment.",
        enjeu="La particularité gradignanaise est juridique avant d’être technique. Le "
              "bâti groupé y relève fréquemment de lotissements administrés par des "
              "associations syndicales libres, et non de syndicats de copropriétaires : "
              "ces ensembles échappent au plan pluriannuel de travaux, réservé aux "
              "immeubles régis par la loi du 10 juillet 1965 dont la réception des "
              "travaux date de plus de quinze ans. Leurs voiries, réseaux et ouvrages "
              "communs vieillissent pourtant au même rythme, sans obligation de provision "
              "ni fonds de travaux. Rien n’interdit en revanche de conduire à titre "
              "volontaire une évaluation d’ensemble bâtie sur le modèle du diagnostic "
              "technique global : c’est le moyen le plus sûr d’objectiver l’état de ces "
              "ouvrages et d’échelonner la dépense avant l’appel de fonds exceptionnel. "
              "Sur les copropriétés véritables des années 1970-1990, le sujet redevient "
              "classique — parties communes autorisées avant le 1er juillet 1997, "
              "chaufferies, sols de halls et de caves — avec en plus l’humidité de la "
              "vallée, qui pèse sur les planchers bas et les structures bois.",
        copro="Le tissu de copropriétés est étroit et fragmenté : petites résidences le "
              "long des axes, quelques ensembles des années 1970 près du campus, et de "
              "nombreux ensembles pavillonnaires groupés dont le statut, copropriété "
              "horizontale ou association syndicale, n’est pas toujours clair pour les "
              "résidents. La gestion bénévole y est fréquente et la rotation des conseils "
              "syndicaux rapide. L’essentiel du budget part aux extérieurs : voirie "
              "interne, réseaux enterrés, éclairage, et surtout arbres de haute tige, "
              "dont l’élagage et le risque de chute pèsent lourd. Les parties communes "
              "bâties sont modestes, souvent sans ascenseur ni chaufferie collective, ce "
              "qui déplace le plan pluriannuel de travaux vers l’enveloppe et les abords "
              "plutôt que vers les équipements.",
        reperes=[
            "Sous couvert d’arbres, les toitures des résidences des années 1970-1980 "
                "retiennent l’humidité ; les conduits de fumée et de ventilation en "
                "fibres-ciment traversant les combles se repèrent avant toute reprise de "
                "couverture.",
            "Le diagnostic technique global n’est pas un simple état des lieux : il "
                "réunit l’état apparent des parties communes et des équipements, la "
                "situation du syndicat au regard de ses obligations, les améliorations "
                "envisageables, un volet énergétique et l’évaluation sommaire du coût des "
                "travaux sur dix ans.",
            "Les ensembles gérés en association syndicale n’ont pas d’obligation de "
                "fonds de travaux : leurs voiries et leurs réseaux se financent en appel "
                "exceptionnel, ce qui rend l’échelonnement d’autant plus utile.",
            "Sur les bâtiments publics et scolaires autorisés avant le 1er juillet "
                "1997, le repérage avant travaux relève du code du travail : il se remet "
                "aux entreprises consultées avant la signature des marchés.",
        ],
    ),

    "le-bouscat": dict(
        parc="Le Bouscat est une commune de faible étendue, entièrement construite : "
             "tout s’y fait en remplacement, en division ou en surélévation. Le bâti est "
             "celui d’un faubourg bourgeois de la fin du XIXe et du début du XXe siècle "
             "— échoppes simples et doubles, maisons de maître avec jardin clos, "
             "immeubles de rapport en pierre le long de l’avenue de la Libération, "
             "quelques ensembles des années 1930. Le champ de courses et les grands "
             "jardins privés découpent ce tissu. Les décennies 1960 à 1990 y ont inséré "
             "de petits collectifs en dents creuses, et la mise en service du tramway a "
             "densifié les abords de l’axe qui traverse la commune.",
        enjeu="Un immeuble de rapport en pierre a traversé plusieurs campagnes de travaux "
              ": chaufferie et conduits refaits, salles d’eau créées, sols de hall "
              "recouverts, cages d’escalier repeintes. Le repérage avant travaux consiste "
              "donc à lire des couches successives plutôt qu’à inspecter une structure "
              "homogène ; l’ancienneté des murs ne présume jamais l’absence de matériaux "
              "amiantés, l’amiante-ciment ayant été employé industriellement bien "
              "avant-guerre et n’ayant été interdit qu’au 1er janvier 1997. Le bâti "
              "d’habitation construit avant le 1er janvier 1949 impose en parallèle le "
              "constat de risque d’exposition au plomb des parties communes : les "
              "peintures d’origine subsistent sous les repeints, et l’entreprise qui "
              "vient les décaper doit protéger ses salariés au titre du code du travail. "
              "Depuis le 1er janvier 2025, les copropriétés d’au plus cinquante lots à "
              "usage de logements, de bureaux ou de commerces relèvent à leur tour du "
              "plan pluriannuel de travaux, dès lors que la réception de l’immeuble "
              "remonte à plus de quinze ans : l’échéance atteint ici des syndicats "
              "jusqu’alors sans obligation de programmation.",
        copro="La copropriété bouscataise est petite et ancienne. Beaucoup de syndicats "
              "sont nés de la division d’une maison de maître ou d’un immeuble de "
              "rapport, avec un règlement rédigé il y a plusieurs décennies, des lots de "
              "cave et de comble mal identifiés, parfois un ascenseur ajouté après coup "
              "dans le vide de la cage. Les postes de dépense sont ceux du bâti bourgeois "
              ": façade en pierre, toiture en ardoise ou en zinc, souches de cheminée, "
              "menuiseries bois d’origine. Les montants restent élevés au regard du "
              "nombre de lots, et la parcelle ne laisse aucune emprise de chantier : "
              "échafaudage sur voirie, autorisation d’occupation du domaine public, "
              "travaux en site pleinement occupé.",
        reperes=[
            "Dans les cages d’escalier repeintes, c’est la sous-couche d’origine qui "
                "compte : la mesure par fluorescence X porte sur chaque unité de "
                "diagnostic, jamais sur un échantillon global.",
            "Sous le carrelage ou le stratifié des halls et paliers, les reprises de "
                "sol menées avant le 1er juillet 1997 ont rarement été déposées : le "
                "sondage porte sur toute l’épaisseur du complexe, pas sur la couche "
                "visible.",
            "Les petits collectifs en dents creuses ont conservé conduits de "
                "vide-ordures et gaines verticales : ce sont les premiers volumes à ouvrir "
                "avant une reprise de colonnes.",
            "Sur ces parcelles sans cour ni recul, les sondages destructifs se "
                "programment avec la même autorisation de voirie que l’échafaudage, sous "
                "peine de repasser deux fois.",
        ],
    ),

    "cenon": dict(
        parc="Cenon se lit en deux étages. En contrebas, le long de la voie ferrée et de "
             "la Garonne, le Bas-Cenon aligne échoppes, maisons de faubourg et anciens "
             "ateliers, dans un tissu ouvrier fixé par le chemin de fer. Au-dessus, le "
             "plateau porte les grands ensembles des années 1960 et 1970 — Palmer, La "
             "Morlette, Le Loret — barres et tours organisées autour du parc Palmer. "
             "Entre les deux, le coteau conserve propriétés anciennes et jardins en "
             "terrasse, sur une pente qui contraint les accès de chantier. Le pôle "
             "d’échanges de la Buttinière a fixé, depuis l’arrivée du tramway, des "
             "programmes collectifs plus récents.",
        enjeu="Le plateau se renouvelle en site occupé : le repérage amiante avant "
              "travaux couvre les parties communes et les logements touchés par les "
              "interventions d’enveloppe, tableaux et appuis de baie compris. L’arrêté du "
              "16 juillet 2019 en fixe le cadre et impose au donneur d’ordre de "
              "communiquer le rapport aux entreprises consultées : il accompagne le "
              "dossier de consultation, pas le marché signé. Sur les immeubles collectifs "
              "de cette période, les points durs sont constants : mastics de joints entre "
              "panneaux, remplissages de loggia en amiante-ciment, conduits de "
              "vide-ordures, gaines techniques, colles de dalles de sol. En contrebas, la "
              "logique s’inverse. Sur un immeuble d’habitation construit avant le 1er "
              "janvier 1949, c’est le risque plomb des peintures de cage d’escalier qui "
              "commande l’organisation du chantier. L’amiante n’y disparaît pas pour "
              "autant : l’amiante-ciment est employé industriellement bien avant-guerre, "
              "et les travaux successifs en ont ajouté jusqu’à ce que l’amiante soit "
              "interdit, au 1er janvier 1997. Une même commune, deux protocoles "
              "d’intervention.",
        copro="La copropriété cenonnaise se répartit entre les ensembles du plateau — "
              "souvent plus de cinquante lots, chauffage collectif, ascenseurs, sous-sols "
              "— et de petits syndicats de faubourg de quelques lots en partie basse. Les "
              "premiers sont arrivés au plan pluriannuel de travaux avec des archives "
              "partielles : plans de réseaux perdus, historique reconstitué de mémoire. "
              "Les seconds, longtemps hors radar, sont concernés depuis le 1er janvier "
              "2025 : c’est la dernière échéance du calendrier, celle des copropriétés "
              "d’au plus cinquante lots, après les plus de deux cents lots au 1er janvier "
              "2023 et les cinquante et un à deux cents lots au 1er janvier 2024. Le plan "
              "ne s’impose qu’aux immeubles de plus de quinze ans, et l’assemblée "
              "générale se prononce sur son adoption.",
        reperes=[
            "Sur les immeubles du plateau dont le permis est antérieur au 1er juillet "
                "1997, les remplissages de garde-corps de loggia sont fréquemment en "
                "amiante-ciment : leur dépose lors d’un ravalement relève du repérage avant "
                "travaux.",
            "Une colonne de vide-ordures condamnée n’est pas une colonne déposée : "
                "conduit, trappes et joints restent en place derrière l’habillage et "
                "ressortent au premier percement.",
            "Avant qu’un mainteneur n’ouvre une chaufferie ou une sous-station, le "
                "donneur d’ordre est le syndicat des copropriétaires : habillage isolant "
                "des canalisations et garnitures de robinetterie sont à faire repérer.",
            "En Bas-Cenon, les échoppes divisées en petites copropriétés cumulent deux "
                "registres: le constat plomb porte sur l’ensemble des revêtements des "
                "parties communes, l’immeuble étant antérieur à 1949, le repérage amiante "
                "sur tous les matériaux touchés.",
        ],
    ),

    "lormont": dict(
        parc="Lormont juxtapose trois âges de construction sans transition. Au bord de "
             "la Garonne, le vieux bourg garde ses ruelles en pente et un bâti "
             "majoritairement antérieur à 1949. À flanc de coteau, Carriet aligne un "
             "logement ouvrier organisé en cité, hérité de l’industrialisation de la "
             "rive droite. Sur le plateau, Génicart déploie une opération d’urbanisme "
             "des années 1960 : barres et tours, dalles de circulation, garages en "
             "sous-sol. Le parc de l’Ermitage, ancienne carrière reconquise, sépare ces "
             "ensembles du fleuve. Les programmes plus récents se sont greffés le long "
             "du tramway et autour de Bois Fleuri, en couture des ensembles existants.",
        enjeu="Ici, la démolition est une composante du projet urbain, et elle impose un "
              "repérage exhaustif : le repérage avant démolition porte sur la liste C et "
              "se conduit sur bâtiment libéré, sondages destructifs autorisés, matériaux "
              "recherchés sous les chapes et derrière les habillages, déposes partielles "
              "pour atteindre colles et calorifugeages en gaine. L’enchaînement repérage, "
              "curage, désamiantage, démolition ne supporte pas l’approximation : un "
              "matériau découvert en phase travaux arrête le chantier et rouvre le "
              "marché. Le diagnostic PEMD s’y articule directement, puisque le tri et les "
              "filières de valorisation se décident avant le premier coup de pelle, "
              "jamais au pied de la benne. Sur le patrimoine conservé, la logique change. "
              "Lorsqu’un immeuble est raccordé à un réseau de chaleur, le gisement "
              "d’économies se déplace vers l’enveloppe et la distribution intérieure, ce "
              "que le DPE collectif doit traduire.",
        copro="Le syndicat lormontais type n’est pas né d’une promotion privée : des "
              "copropriétés issues d’ensembles construits pour l’accession dans les "
              "années 1960-1970, ou de logements vendus par leur bailleur, s’y "
              "rencontrent régulièrement. Conséquence pratique : des immeubles de grande "
              "taille, des équipements communs coûteux — ascenseurs, sous-stations, "
              "parkings, dalles piétonnes — et des budgets de travaux calibrés au plus "
              "juste. Le fonds de travaux, dont la cotisation annuelle se calcule "
              "désormais par référence au montant des travaux inscrits au plan, part de "
              "bas ; le plan pluriannuel y sert donc moins à programmer qu’à hiérarchiser "
              ": ce qui touche la sécurité et l’étanchéité avant ce qui touche le "
              "confort. Dans le bas-bourg, à l’inverse, quelques lots par immeuble, sans "
              "ascenseur, dans un bâti ancien où chaque intervention croise plomb et "
              "amiante.",
        reperes=[
            "Sur les immeubles de Génicart, le repérage avant démolition descend sous "
                "les revêtements successifs : c’est la colle qui porte l’amiante plus "
                "souvent que le sol visible, et elle se trouve parfois deux couches plus "
                "bas.",
            "Les dalles piétonnes et passerelles du plateau abritent réseaux et "
                "étanchéités anciennes, rarement documentés dans les archives du syndicat : "
                "leur périmètre se fixe avec le maître d’ouvrage avant l’émission du devis.",
            "À Carriet, les annexes et dépendances des cités concentrent les éléments "
                "en fibres-ciment : ils quittent le chantier sous bordereau de suivi des "
                "déchets d’amiante, exutoire identifié dès l’étude.",
            "Dans le bas-bourg, l’étroitesse des ruelles en pente pèse autant que le "
                "bâti : accès des engins, stockage et évacuation des déchets plombés se "
                "calent avant l’intervention, pas le jour même.",
        ],
    ),

    "floirac": dict(
        parc="Floirac se compose de trois morceaux qui ne se ressemblent pas. La plaine, "
             "entre les quais et la rocade, garde un tissu d’entrepôts, d’ateliers et de "
             "terrains d’activité en cours de mutation, où l’Arena et l’aménagement des "
             "bords de Garonne ont remplacé une partie des emprises anciennes. Le coteau "
             "porte le bourg historique, ses échoppes autour de l’avenue Jean Jaurès, "
             "des maisons de maître et le domaine de la Burthe, sur une pente qui "
             "commande les accès de chantier. Sur le plateau, Dravemont concentre le "
             "collectif des années 1960-1970, tours et barres desservies par une voirie "
             "en boucle. Les livraisons neuves les plus visibles se concentrent en "
             "partie basse.",
        enjeu="La plaine est le terrain des missions de démolition et de reconversion. "
              "Sur un entrepôt ou un atelier autorisé avant le 1er juillet 1997, le "
              "repérage porte sur les plaques ondulées et les bardages en fibres-ciment, "
              "sur les dalles semi-rigides et sur les protections coupe-feu projetées des "
              "charpentes métalliques, souvent oubliées parce que hautes et masquées par "
              "un bac acier. Le diagnostic PEMD s’ajoute dès que la surface cumulée de "
              "plancher dépasse mille mètres carrés, ou que le bâtiment a abrité une "
              "activité mettant en œuvre des substances dangereuses. Deuxième "
              "particularité : en zone basse, les bâtiments sont souvent construits sans "
              "sous-sol, réseaux et calorifugeages passant en vide sanitaire ; l’accès "
              "conditionne le repérage et se prépare avant la visite. Sur le plateau, "
              "Dravemont impose à l’inverse d’intervenir sur des bâtiments habités : le "
              "repérage se fractionne par cage et par typologie, l’information des "
              "occupants précédant chaque phase.",
        copro="Floirac cumule deux copropriétés opposées. Celle des quais et de la "
              "plaine, livrée à partir des années 2000, équipée d’ascenseurs, de "
              "ventilation mécanique et de stationnements enterrés, dont les premières "
              "résidences ont franchi les quinze ans qui déclenchent le plan pluriannuel "
              "de travaux. L’âge apparent n’y règle rien : le repérage amiante se "
              "détermine sur la date du permis, non sur celle de la remise des clés ; une "
              "résidence occupée depuis les années 2000 peut avoir été autorisée avant le "
              "1er juillet 1997. Celle du plateau et du bourg, plus ancienne, où le sujet "
              "est l’enveloppe : menuiseries d’origine, toitures-terrasses, façades. Un "
              "conseil syndical de résidence récente aborde le plan sans historique de "
              "travaux ; à Dravemont, avec un bâti dont chaque intervention suppose un "
              "repérage préalable. Les deux ont besoin d’un état technique, pour des "
              "raisons inverses.",
        reperes=[
            "Dans les entrepôts de la plaine, la protection coupe-feu projetée sur "
                "charpente métallique échappe à tout repérage conduit depuis le sol : la "
                "reconnaissance en hauteur figure au programme de la visite.",
            "Sur le coteau, les petits immeubles adossés à la pente présentent des "
                "désordres de structure qu’un examen construit distingue d’un défaut "
                "d’entretien : en copropriété, le diagnostic technique global en est le "
                "cadre.",
            "En partie basse, l’absence de sous-sol renvoie les réseaux sous le "
                "plancher bas : sans trappe accessible ni cheminement dégagé, le repérage "
                "se conclut par une réserve.",
            "À Dravemont, les conduits en amiante-ciment sont restés derrière les "
                "habillages : une reprise de gaine suffit à les atteindre, ce qui étend le "
                "repérage aux parties privatives concernées.",
        ],
    ),

    "bassens": dict(
        parc="Bassens tourne le dos au fleuve et la coupure est nette. En bas, le long "
             "de la Garonne, les emprises portuaires et industrielles occupent presque "
             "tout le linéaire : terminal, silos, dépôts, installations classées, sur un "
             "site dont l’aménagement moderne remonte au port construit pendant la "
             "Première Guerre mondiale. En haut, le plateau porte une commune "
             "résidentielle de taille modeste : bourg ancien autour de l’église, cités "
             "et ensembles collectifs des années 1950 à 1970 répartis autour du bourg, "
             "lotissements pavillonnaires plus récents. Entre les deux, un coteau boisé "
             "et des voies en pente qui rendent l’accès des engins et des bennes moins "
             "simple qu’il n’y paraît sur un plan.",
        enjeu="Deux régimes de repérage coexistent sur quelques kilomètres. Côté port et "
              "industrie, l’intervention relève du code du travail : le donneur d’ordre "
              "est l’exploitant, le repérage précède toute opération de maintenance ou de "
              "démantèlement, il alimente le plan de prévention établi avec l’entreprise "
              "extérieure et se cale sur les arrêts techniques ; l’accès au site suppose "
              "autorisations et protocoles obtenus en amont. Côté plateau, le sujet est "
              "le patrimoine résidentiel des années 1950-1970, où une part notable du "
              "parc est gérée par des bailleurs : les missions y sont commandées par lot "
              "de bâtiments, ce qui permet de mutualiser repérages et rapports, mais "
              "suppose d’arrêter le découpage dès la commande. Les friches en "
              "reconversion relèvent, elles, du repérage avant démolition ; le diagnostic "
              "PEMD s’y conduit avant le dépôt de la demande de permis de démolir ou, à "
              "défaut, avant l’acceptation des devis de travaux.",
        copro="Les copropriétés rencontrées à Bassens sont le plus souvent de petite "
              "taille : immeubles de trois ou quatre niveaux sans ascenseur, chauffage "
              "fréquemment individuel, syndicats de quelques dizaines de lots, gérés par "
              "des conseils syndicaux bénévoles. Petites, elles relèvent de la dernière "
              "vague du calendrier : plan pluriannuel de travaux depuis le 1er janvier "
              "2025, DPE collectif depuis le 1er janvier 2026. Les deux textes ne se "
              "déclenchent pourtant pas sur le même critère : l’un raisonne sur l’âge de "
              "l’immeuble, l’autre sur la date de dépôt du permis de construire. Sur ces "
              "petits syndicats, la question est toujours la même : par quoi commencer "
              "quand le budget annuel est faible ? La réponse tient rarement dans un "
              "devis : elle tient dans un ordre de priorités que le conseil syndical "
              "puisse défendre en assemblée générale.",
        reperes=[
            "Sur les installations mises en service avant 1997, calorifugeages, joints "
                "de brides et tresses restent courants : leur repérage relève du code du "
                "travail et précède le mode opératoire de l’entreprise extérieure.",
            "Les hangars, garages et abris annexes du patrimoine communal et des cités "
                "du plateau sont souvent couverts de plaques en fibres-ciment : posées "
                "avant 1997, elles relèvent du repérage avant travaux — du repérage avant "
                "démolition si le bâtiment entier tombe.",
            "Dans les cités des années 1950-1960, chaque campagne de rénovation a "
                "ajouté une couche : le nombre de sondages se décide sur plan, avant la "
                "visite.",
            "Pour toute intervention en zone portuaire ou industrielle, le délai "
                "d’obtention des autorisations d’accès conditionne la date de remise du "
                "rapport : il se traite dès la commande.",
        ],
    ),

    "eysines": dict(
        parc="Eysines s’est construite sur les terres basses de la jalle, et son bâti en "
             "garde la trace : fermes maraîchères basses en moellon, hangars et cabanes "
             "de bord de parcelle, souvent remaniés en logement ou en atelier. Autour "
             "des noyaux du Vigean, de Migron et du bourg, l’échoppe côtoie un "
             "pavillonnaire dense étalé sur trois décennies, de 1960 à 1990. Le "
             "collectif n’est apparu qu’ensuite : petites résidences le long des grands "
             "axes, puis opérations plus denses aux abords du terminus du tramway. Les "
             "caves y sont rares, le plancher bas reposant le plus souvent sur vide "
             "sanitaire — volume vers lequel se déplacent réseaux et calorifugeages.",
        enjeu="La reconversion des hangars et des serres maraîchères est le sujet propre "
              "à Eysines. Un bâtiment ayant abrité une activité agricole et stocké des "
              "substances classées dangereuses — produits phytosanitaires au premier chef "
              "— déclenche le diagnostic PEMD dès lors qu’il est démoli ou fait l’objet "
              "d’une rénovation significative, sans condition de surface: c’est "
              "l’activité passée qui commande, pas le mètre carré. Le repérage avant "
              "travaux, lui, procède du code du travail et ne connaît aucune date butoir. "
              "Côté logement, le plan pluriannuel de travaux a rattrapé les petites "
              "copropriétés au 1er janvier 2025, à deux conditions cumulatives: cinquante "
              "lots au plus, et un permis de construire délivré depuis plus de quinze "
              "ans. Beaucoup l’abordent sans état des lieux technique; le diagnostic "
              "technique global en est alors le préalable réaliste.",
        copro="La copropriété eysinaise est de petit format : résidences de deux à quatre "
              "niveaux édifiées entre 1970 et 1995 le long des axes, immeubles de bourg "
              "divisés au fil des successions. Beaucoup sont administrées bénévolement, "
              "ou par un cabinet qui les gère parmi des dizaines d’autres ; les pièces "
              "techniques disponibles se limitent aux procès-verbaux d’assemblée. Le "
              "déclencheur y est presque toujours l’eau : remontées en pied de mur et "
              "désordres de dallage amènent le conseil syndical à la question technique "
              "bien avant le calendrier réglementaire. Ce calendrier commande pourtant la "
              "trésorerie : le fonds de travaux devient obligatoire dix ans après la "
              "réception de l’immeuble, soit cinq ans avant que le plan pluriannuel "
              "lui-même ne soit exigible.",
        reperes=[
            "Sur les hangars maraîchers, plaques ondulées de couverture et plaques "
                "planes de bardage en fibres-ciment se repèrent en priorité ; les descentes "
                "d’eaux pluviales en amiante-ciment, elles, sont souvent omises du métré.",
            "Dans les petites résidences des axes, conduits de ventilation et gaines "
                "techniques en amiante-ciment traversent les logements : le repérage "
                "suppose un accès aux parties privatives, à organiser avec le syndic "
                "plusieurs semaines à l’avance.",
            "Le vide sanitaire y tient lieu de sous-sol : atteindre les canalisations "
                "et leurs calorifugeages exige une trappe ouverte et un cheminement dégagé, "
                "à préparer avant l’intervention.",
            "Sur le bâti de bourg antérieur au 1er janvier 1949, le risque plomb des "
                "peintures s’évalue avant tout ponçage ou décapage ; en immeuble collectif, "
                "le constat porte sur les parties communes.",
        ],
    ),

    "le-haillan": dict(
        parc="Détaché d’Eysines et érigé en commune au XIXe siècle, Le Haillan est resté "
             "rural jusqu’à l’après-guerre. Son bâti actuel s’est constitué en deux "
             "temps : des lotissements pavillonnaires réguliers des années 1970 à 1990 "
             "autour du centre et de Bel Air, puis une densification récente aux abords "
             "du terminus de la ligne A du tramway, sous forme de petits collectifs de "
             "trois à cinq niveaux. La commune porte aussi un tissu d’activité "
             "industrielle et tertiaire important au regard de sa superficie : halls "
             "d’assemblage, laboratoires, ateliers et bâtiments de bureaux édifiés pour "
             "l’essentiel entre 1960 et 1990.",
        enjeu="Le Haillan fait tenir deux régimes sur un territoire restreint. Sur les "
              "halls et les bureaux, le repérage amiante avant travaux relève du code du "
              "travail : l’obligation pèse sur le donneur d’ordre, préalablement à toute "
              "opération et sans condition d’âge du bâtiment, l’arrêté du 16 juillet 2019 "
              "en fixant les modalités pour les immeubles bâtis. Le rapport se remet aux "
              "entreprises dès la consultation, mais le site reste en production, et les "
              "sondages destructifs se calent sur les arrêts techniques. Ces mêmes "
              "bâtiments dépassent les mille mètres carrés de surface de plancher cumulée "
              "qui déclenchent le diagnostic dit PEMD — produits, équipements, matériaux "
              "et déchets — en démolition, mais aussi en rénovation significative, "
              "c’est-à-dire dès que l’opération détruit ou remplace au moins deux "
              "éléments de second œuvre : huisseries extérieures, cloisons, plomberie, "
              "électricité, chauffage. Sur le versant résidentiel, les petits collectifs "
              "abordent leur plan pluriannuel avec façades en panneaux préfabriqués et "
              "menuiseries d’origine : deux postes lourds, deux repérages à conduire "
              "avant le chiffrage.",
        copro="Le collectif haillanais est jeune, de petite taille, et se range en deux "
              "familles. D’abord des résidences de trois à cinq niveaux livrées dans les "
              "décennies 1970 à 1990, aux parties communes réduites, dont le fonds de "
              "travaux a souvent été constitué tard au regard de l’âge du bâti : le "
              "premier renouvellement d’enveloppe se présente alors sans provision "
              "correspondante. Ensuite les programmes issus de la densification, qui "
              "associent logements, locaux commerciaux et stationnement en sous-sol, "
              "parfois organisés en volumes distincts. Cette seconde catégorie produit un "
              "conseil syndical peu banal ici, appelé à arbitrer la répartition des "
              "charges entre bâtiments ou entre volumes avant de disposer d’un historique "
              "d’entretien. Les deux profils n’appellent pas la même mission.",
        reperes=[
            "Dans les locaux d’activité, les points durs sont les joints de portes "
                "coupe-feu, les tresses d’étanchéité des étuves et des fours et les "
                "calorifugeages de réseaux en gaine technique, tous invisibles depuis le "
                "sol.",
            "Sur une façade en panneaux préfabriqués, les points de repérage sont les "
                "mastics de vitrage et les joints de dilatation entre panneaux, rarement "
                "décrits dans les pièces d’un marché de ravalement.",
            "Sur les programmes organisés en volumes, réclamer l’état descriptif de "
                "division avant toute mission collective : il détermine qui commande et qui "
                "supporte la dépense.",
            "Dans les bâtiments dont le permis de construire est antérieur au 1er "
                "juillet 1997, les faux-plafonds de bureaux imposent une dépose partielle "
                "pour repérage : la prévoir au marché, pas en cours de chantier.",
        ],
    ),

    "saint-medard-en-jalles": dict(
        parc="Saint-Médard-en-Jalles n’a pas un centre mais une série de bourgs reliés "
             "par des lotissements successifs, dont Hastignan. Le long des jalles "
             "subsiste un bâti d’eau ancien : moulins et dépendances agricoles en "
             "moellon et en brique, dont beaucoup ont changé d’usage sans laisser "
             "d’archives de travaux. À l’ouest, la lande boisée porte des constructions "
             "dispersées et des bâtiments d’exploitation. La commune abrite aussi une "
             "vaste emprise industrielle héritée d’une ancienne poudrerie et tournée "
             "depuis vers la propulsion ; son patrimoine bâti est lui-même étalé : "
             "magasins et bâtiments techniques édifiés par strates jusqu’aux années "
             "1980. Le logement collectif, lui, est resté minoritaire.",
        enjeu="L’étendue de la commune change la nature de la mission : un patrimoine "
              "dispersé sur des sites distants ne se repère pas comme un immeuble, il se "
              "planifie par campagnes, dans un ordre de priorité fondé sur l’année de "
              "construction et le programme voté. Sur ces emprises comme sur les "
              "bâtiments communaux, la collectivité ou l’exploitant agit en qualité de "
              "donneur d’ordre : le code du travail lui impose de faire rechercher "
              "l’amiante préalablement à l’opération, et le rapport accompagne le dossier "
              "de consultation ; à défaut, les offres reposent sur un aléa. Les groupes "
              "scolaires et les gymnases forment un gisement continu, calé sur les "
              "vacances : ces missions se commandent plusieurs mois à l’avance, faute de "
              "quoi le chantier d’été saute. Les autorisations d’accès aux sites protégés "
              "se règlent, elles, avant le devis.",
        copro="Saint-Médard compte peu de grandes copropriétés verticales, mais beaucoup "
              "de structures collectives d’un autre type : ensembles pavillonnaires "
              "administrés tantôt en association syndicale libre, tantôt en copropriété, "
              "et la distinction est lourde de conséquences. L’association syndicale "
              "libre relève de l’ordonnance du 1er juillet 2004 : ni plan pluriannuel, ni "
              "fonds de travaux obligatoire, quand ses voiries et ses réseaux "
              "vieillissent au même rythme. La copropriété, même horizontale, est régie "
              "par la loi du 10 juillet 1965 et y reste soumise. Les copropriétés "
              "verticales se répartissent entre le centre et Hastignan ; sous le même "
              "syndic, elles n’ont pas les mêmes échéances, car c’est le nombre de lots "
              "qui commande le calendrier : plan pluriannuel exigible depuis le 1er "
              "janvier 2023 au-delà de deux cents lots, depuis le 1er janvier 2024 de "
              "cinquante et un à deux cents, depuis le 1er janvier 2025 en deçà, le DPE "
              "collectif suivant la même progression jusqu’au 1er janvier 2026 pour les "
              "plus petites. La première vérification porte donc sur l’état descriptif de "
              "division.",
        reperes=[
            "Les bâtiments industriels anciens portent des matériaux absents du "
                "logement : calorifugeages de conduites vapeur, tresses et bourrages de "
                "vannes, joints de brides sur réseaux techniques.",
            "Dans les groupes scolaires des décennies 1960 et 1970, les dalles de sol "
                "semi-rigides et les faux-plafonds de couloir sont les deux repérages qui "
                "conditionnent la faisabilité d’un chantier d’été.",
            "Sur un ensemble pavillonnaire, établir d’abord le statut juridique : de "
                "lui dépend l’assujettissement au plan pluriannuel, et donc l’ordre du "
                "jour.",
            "Les dépendances de bord de jalle portent souvent une couverture en "
                "fibres-ciment posée en remplacement de la tuile : le repérage est dû avant "
                "démolition si la dépendance disparaît, avant travaux si elle est "
                "conservée.",
        ],
    ),

    "martignas-sur-jalle": dict(
        parc="À la frange ouest du périmètre métropolitain, Martignas-sur-Jalle marque "
             "le passage de l’urbanisation à la lande. Le bourg ancien — maisons basses "
             "en moellon enduit groupées autour de l’église — est cerné par des "
             "lotissements pavillonnaires édifiés en nappes successives des années 1970 "
             "aux années 2000, sur les sols sableux où l’usage constructif a écarté le "
             "niveau enterré au profit du dallage sur terre-plein. La commune accueille "
             "aussi des emprises non résidentielles — activités aéronautiques et "
             "emprises de défense — dont le bâti relève de maîtres d’ouvrage propres, "
             "avec leurs règles d’accès et de passation. S’y ajoutent les équipements "
             "publics — groupe scolaire, salle omnisports, ateliers municipaux — "
             "construits pour l’essentiel entre 1970 et 1990.",
        enjeu="Ici, une part importante de la commande collective vient d’une "
              "collectivité, d’un bailleur ou d’un exploitant plutôt que d’un syndic. Sur "
              "les hangars et les ateliers, couvertures et bardages en fibres-ciment "
              "forment le matériau structurant : leur dépose suppose un repérage "
              "préalable, et l’opération relève du diagnostic PEMD dès qu’elle en remplit "
              "les conditions. Ce diagnostic se réalise avant le dépôt de la demande de "
              "permis de démolir ou, lorsqu’aucun permis n’est requis — cas courant sur "
              "un bâtiment agricole ou d’activité —, avant l’acceptation des devis et la "
              "passation des marchés ; il identifie les filières de réemploi et de "
              "valorisation, et donne lieu à un récolement après travaux. Les équipements "
              "communaux posent une autre question, la rénovation énergétique : isoler "
              "des combles ou reprendre une chaufferie appelle un repérage avant travaux, "
              "faute de quoi l’entreprise refuse d’intervenir ou chiffre un aléa.",
        copro="La copropriété martignaise se compte en dizaines de lots, pas en "
              "centaines, sous deux formes : quelques petits immeubles de deux ou trois "
              "niveaux au bourg, livrés entre 1980 et 2005, et des ensembles de maisons "
              "groupées issus de lotissements, dont les réseaux d’eaux pluviales "
              "dimensionnés pour un sol sableux forment le principal poste commun — et le "
              "premier sujet d’expertise, faute de plan de récolement. La gestion "
              "bénévole y est courante : le conseil syndical cumule la fonction de maître "
              "d’ouvrage sans interlocuteur technique de référence. La question à poser "
              "en premier est le nombre de lots : il fixe la date d’entrée en vigueur de "
              "l’obligation, au 1er janvier 2025 pour les syndicats qui ne dépassent pas "
              "cinquante lots. Le DPE collectif obéit à un second filtre, celui du permis "
              "déposé avant le 1er janvier 2013.",
        reperes=[
            "Les hangars de la lande associent charpente métallique et couverture en "
                "plaques ondulées de fibres-ciment ; les plaques translucides "
                "d’éclairement, fragiles, imposent une reconnaissance à distance avant "
                "toute circulation en toiture.",
            "Les canalisations enterrées en amiante-ciment échappent au repérage de "
                "l’immeuble bâti : leur recherche s’inscrit dans la préparation du "
                "terrassement, non le jour où l’engin les rencontre.",
            "Dans les équipements communaux, les plaques de protection thermique "
                "placées derrière les appareils de chauffage et les joints de portes "
                "techniques comptent parmi les éléments les plus souvent omis.",
            "Avant d’inscrire un plan pluriannuel de travaux à l’ordre du jour, relever "
                "deux données : la date de réception, qui commande le seuil de quinze ans, "
                "et le nombre de lots, dont dépend la date d’exigibilité.",
        ],
    ),

    "bruges": dict(
        parc="Bruges s’est construite en deux temps. Le noyau ancien, groupé autour de "
             "l’église, aligne des maisons de bourg et des échoppes basses héritées du "
             "passé maraîcher des palus, complétées de petits collectifs des années "
             "1960-1980. À l’ouest, la réserve naturelle des marais a fixé la limite de "
             "l’urbanisation et reporté la croissance sur la frange est : la ZAC du "
             "Tasta et les opérations d’aménagement voisines y ont livré, à partir du "
             "milieu des années 2000, des ensembles collectifs de plusieurs bâtiments, "
             "en béton, avec parkings enterrés et toitures-terrasses. Au nord, la zone "
             "d’activités de Tanaïs aligne halls et ateliers, dont beaucoup sont "
             "antérieurs au 1er juillet 1997.",
        enjeu="Bruges oblige à distinguer deux régimes dans une même commune. Deux "
              "critères distincts commandent en revanche les obligations collectives. Le "
              "plan pluriannuel de travaux s’impose dès quinze ans après la réception des "
              "travaux, échéance opposable à toutes les tailles de copropriété depuis le "
              "1er janvier 2025. Le DPE collectif, lui, ne vise que les copropriétés à "
              "usage principal d’habitation dont la demande de permis de construire a été "
              "déposée avant le 1er janvier 2013. Le sujet technique est ailleurs : "
              "garanties décennales éteintes, isolation par l’extérieur, ventilation "
              "mécanique — et une enveloppe dont aucun document ne décrit l’état. Le "
              "bourg ancien et Tanaïs restent le terrain du repérage avant travaux et du "
              "repérage avant démolition.",
        copro="La copropriété brugeaise est jeune et d’un format particulier : des "
              "résidences de plusieurs bâtiments, livrées en tranches successives, avec "
              "parkings en sous-sol, ascenseurs, locaux vélos, larges espaces verts "
              "communs et, selon les programmes, chaufferie gaz collective ou production "
              "individuelle. Un conseil syndical y rencontre trois choses en même temps : "
              "l’extinction des garanties constructeur, des charges d’entretien qui "
              "montent avec les équipements, et l’absence de tout document technique en "
              "dehors du dossier des ouvrages exécutés. Subsistent à l’écart de petites "
              "copropriétés du bourg, issues de divisions de maisons anciennes, sans "
              "syndic professionnel et sans historique.",
        reperes=[
            "Sur les résidences livrées dans les années 2000-2010, l’étanchéité des "
                "toitures-terrasses et des relevés de balcon est le premier poste à "
                "objectiver : la garantie décennale est éteinte, et seul un état technique "
                "documenté — diagnostic technique global, ou l’analyse du bâti qui ouvre le "
                "plan pluriannuel de travaux — décrit l’état réel avant le vote.",
            "C’est la date de dépôt du permis, et non celle de la livraison, qui "
                "détermine l’assujettissement au DPE collectif : sur une opération étalée "
                "en tranches, deux bâtiments voisins peuvent relever de régimes différents.",
            "Sur sols de marais, les fissures relevées en pied d’immeuble se lisent "
                "avec l’implantation des joints de dilatation : c’est ce qui distingue un "
                "tassement stabilisé d’un désordre évolutif.",
            "Dans la zone d’activités de Tanaïs, les ateliers autorisés avant le 1er "
                "juillet 1997 associent couvertures en plaques ondulées de fibres-ciment et "
                "bandeaux translucides en polyester : les deux se déposent ensemble, mais "
                "ne partent pas dans la même filière de déchets.",
        ],
    ),

    "blanquefort": dict(
        parc="Blanquefort tient sur trois assises distinctes. Un centre ancien organisé "
             "autour de la forteresse médiévale et du domaine de Dillon, avec un bâti de "
             "bourg en pierre et les anciens villages de Caychac et de Dulamon. Un vaste "
             "appareil industriel et logistique à l’est, le long de la ligne du Médoc : "
             "halls de grande portée, entrepôts, ateliers, et l’emprise de l’ancienne "
             "usine automobile. Enfin des lotissements et des résidences construits "
             "entre les années 1970 et 1990, greffés sur le bourg, auxquels s’ajoutent "
             "les programmes apparus avec le prolongement du tramway. Des domaines "
             "viticoles classés en appellation Haut-Médoc subsistent à l’écart des zones "
             "bâties, avec leurs chais et leurs dépendances.",
        enjeu="Ici, l’échelle change tout. Sur un hall logistique ou un atelier dont le "
              "permis de construire a été délivré avant le 1er juillet 1997, l’amiante ne "
              "se limite pas à la couverture : mastics de vitrage, joints de bardage, "
              "calorifugeage des réseaux d’air chaud et dalles semi-rigides des locaux "
              "sociaux entrent dans le périmètre. Ces bâtiments dépassant sans peine 1 "
              "000 m² de surface de plancher cumulée, le diagnostic des produits, "
              "équipements, matériaux et déchets s’ajoute au repérage avant démolition : "
              "une même visite, deux fondements juridiques, deux rapports, et un "
              "formulaire de récolement à produire une fois les travaux achevés. Côté "
              "habitation, les copropriétés du centre et de Caychac construites entre "
              "1970 et 1990 relèvent du repérage avant travaux dès qu’on ouvre une gaine "
              "palière ou une chaufferie. L’obligation pèse sur le donneur d’ordre, et le "
              "rapport se joint au dossier de consultation des entreprises, avant la "
              "remise des offres et non une fois le marché signé.",
        copro="Le collectif blanquefortais s’est constitué par strates. Autour du centre "
              "et de Caychac, des résidences des années 1970-1990, de taille moyenne, "
              "souvent conçues avec chauffage collectif, colonnes techniques encastrées "
              "et vide-ordures aujourd’hui condamnés : c’est le parc qui affronte le "
              "premier renouvellement complet de ses équipements, ascenseur, menuiseries, "
              "colonnes et production de chaleur. S’y ajoutent les copropriétés apparues "
              "avec le prolongement du tramway, encore sous garanties, et un parc social "
              "qui relève de la commande de bailleur. Enfin, quelques ensembles mixtes "
              "réunissent logements et locaux professionnels sous un même règlement : la "
              "répartition des charges de gros entretien y est le premier point à "
              "clarifier avant toute programmation.",
        reperes=[
            "Les canalisations enterrées en amiante-ciment posées avant 1997 ne "
                "relèvent pas du repérage de l’immeuble bâti : elles ressortent au "
                "terrassement, et arrêtent le chantier si personne ne les a anticipées.",
            "Dans les halls de grande hauteur, le moyen d’accès à la couverture, "
                "nacelle ou cordiste, se cale au moment du devis : ce poste fait varier le "
                "prix d’un repérage avant démolition davantage que le nombre de "
                "prélèvements.",
            "Sur l’emprise de l’ancienne usine automobile comme sur les entrepôts de la "
                "ligne du Médoc, le bâti et les équipements de production relèvent de deux "
                "référentiels distincts : une seule mission ne couvre pas les deux, et "
                "l’oubli se découvre au démontage.",
            "Dans les résidences des années 1970-1980, les trémies de vide-ordures "
                "condamnées gardent conduits, trappes et calorifugeages derrière "
                "l’habillage : ce sont les premiers volumes ouverts lors d’une reprise de "
                "colonnes.",
        ],
    ),

    "parempuyre": dict(
        parc="Parempuyre est une commune de palus et de vignoble, établie sur la rive "
             "gauche de la Garonne, à la frange nord de la métropole. Le bourg ancien, "
             "resserré autour de l’église, garde des maisons basses en pierre et en "
             "moellon, sans sous-sol, portées sur vide sanitaire. Autour, les propriétés "
             "viticoles du Haut-Médoc alignent chais, cuviers et dépendances, dont les "
             "charpentes et couvertures ont été reprises au fil du XXe siècle. Vers le "
             "fleuve, les terres basses restent occupées par les prairies, les esteys et "
             "les digues. Le reste de la commune s’est urbanisé tardivement, en "
             "lotissements pavillonnaires et en opérations groupées, largement "
             "postérieurs aux années 1980.",
        enjeu="Le collectif y est peu nombreux et rarement vertical : l’essentiel prend "
              "la forme d’opérations groupées de maisons, souvent organisées en "
              "copropriété horizontale. Un tel syndicat relève pourtant de la loi du 10 "
              "juillet 1965 : passé quinze ans, le plan pluriannuel de travaux lui est "
              "opposable. Ce que l’on sous-estime, c’est son objet : le sol, la voirie, "
              "les réseaux enterrés, l’éclairage, les clôtures — non des façades. Un "
              "programme crédible commence par l’état des réseaux et du poste de "
              "relevage. Le DPE collectif s’adresse aux seuls bâtiments d’habitation "
              "collectifs : une opération composée exclusivement de maisons individuelles "
              "reste hors de son champ. Second point, propre au vignoble : dès qu’un chai "
              "ou un cuvier ayant stocké des produits phytosanitaires fait l’objet d’une "
              "démolition ou d’une rénovation significative, le diagnostic portant sur "
              "les produits, équipements, matériaux et déchets est dû au titre de "
              "l’activité agricole, sans qu’il soit besoin d’atteindre les 1 000 m² de "
              "plancher cumulés.",
        copro="Peu de résidences, et beaucoup de structures collectives qui n’en portent "
              "pas le nom. Les opérations groupées récentes ont créé des copropriétés "
              "horizontales de petite taille, dont la gestion est souvent bénévole et le "
              "fonctionnement assimilé, à tort, à celui d’un simple lotissement. Le "
              "conseil syndical y découvre tardivement que l’immeuble n’est pas le sujet "
              ": ce sont les réseaux d’assainissement des parties communes, la voirie "
              "interne, l’éclairage et le poste de relevage qui pèsent, et qu’aucun "
              "carnet d’entretien ne documente. Dans le bourg, quelques divisions de "
              "maisons anciennes forment des micro-copropriétés construites avant le 1er "
              "janvier 1949, où la cage d’escalier et les menuiseries relèvent du constat "
              "de risque d’exposition au plomb des parties communes.",
        reperes=[
            "Dans une copropriété horizontale, le règlement se lit avant le programme : "
                "selon les cas, voirie, réseaux et poste de relevage sont communs, "
                "rétrocédés à la commune, ou laissés à chaque propriétaire. C’est ce "
                "partage qui fixe le périmètre du plan pluriannuel de travaux.",
            "L’absence de sous-sol reporte les réseaux en vide sanitaire : c’est là que "
                "se trouvent les évacuations en amiante-ciment, et c’est l’accès à ménager "
                "avant la visite de repérage.",
            "Sur les propriétés viticoles, le périmètre du repérage avant travaux doit "
                "englober chais, cuviers et hangars agricoles : laissés hors mission, ce "
                "sont eux qui concentrent plaques ondulées, conduits et couvertures en "
                "amiante-ciment.",
            "Les parcelles couvertes par un plan de prévention du risque inondation "
                "supportent des prescriptions applicables au bâti existant : elles se "
                "chiffrent avec le programme de travaux, et non après son vote.",
        ],
    ),

    "le-taillan-medoc": dict(
        parc="Le Taillan-Médoc s’étire le long de la route du Médoc, entre les zones "
             "humides de la jalle et le bois du Taillan. Le bourg ancien et le hameau de "
             "Germignan conservent un bâti de pierre et de moellon d’avant-guerre, "
             "autour du domaine viticole du château du Taillan et de ses chais. "
             "L’essentiel de la commune s’est construit à partir des années 1970 en "
             "lotissements pavillonnaires : maisons de plain-pied ou à combles aménagés, "
             "garages et appentis accolés, dépendances de jardin. Le collectif est venu "
             "plus tard, concentré sur l’axe et le centre : petites résidences des "
             "années 1980-1990, puis programmes récents de densification.",
        enjeu="Le collectif communal est dominé par de petites copropriétés, le plus "
              "souvent d’au plus cinquante lots : les dernières entrées dans le "
              "calendrier réglementaire, et celles qui n’ont jamais fait établir de "
              "document technique. Elles y sont entrées ensemble, et découvrent leurs "
              "obligations de programmation en même temps que le chiffrage de leur "
              "enveloppe. La difficulté est ailleurs : ces immeubles n’ont pas "
              "d’installation de chauffage commune, de sorte qu’aucun poste unique ne "
              "porte le gain énergétique et que le programme se construit ligne par ligne "
              "— menuiseries, combles perdus, planchers bas sur vide sanitaire. Chacune "
              "de ces lignes suppose son préalable : un repérage avant travaux sur tout "
              "bâtiment autorisé avant le 1er juillet 1997, une reconnaissance de "
              "charpente en comble, un accès de vide sanitaire ménagé avant la visite. "
              "L’autre moitié du sujet échappe à la loi du 10 juillet 1965 : les "
              "lotissements des années 1970-1980 relèvent d’une association syndicale "
              "libre, non d’un syndicat de copropriétaires.",
        copro="Le parc collectif taillanais est petit et récent en gestion : des "
              "résidences de quelques dizaines de lots au plus, en R+2, à cage d’escalier "
              "unique, parfois avec ascenseur, rarement avec chaufferie collective. Sur "
              "ce format d’immeuble, la gestion est fréquemment bénévole, ou confiée à un "
              "cabinet pour lequel le mandat reste de petite taille. Le fonds de travaux, "
              "quand il est réellement alimenté, y est le seul amortisseur d’un programme "
              "d’enveloppe étalé sur plusieurs exercices, et le premier vote arrive le "
              "plus souvent sans budget constitué ni état des lieux.",
        reperes=[
            "Sur les résidences des années 1980-1990, le repérage avant travaux se joue "
                "là où l’on ne regarde pas : conduits de ventilation en toiture, plaques de "
                "couverture des auvents d’entrée et des abris à conteneurs, évacuations en "
                "vide sanitaire.",
            "Dans une association syndicale libre, l’assemblée n’a ni fonds de travaux "
                "ni plan pluriannuel à voter : le financement passe par un appel "
                "exceptionnel, d’où l’intérêt d’établir l’état technique de la voirie et "
                "des réseaux avant que leur dégradation n’impose la dépense.",
            "Les copropriétés d’au plus cinquante lots, majoritaires ici, sont entrées "
                "dans le plan pluriannuel de travaux au 1er janvier 2025 si l’immeuble a "
                "plus de quinze ans, et dans le DPE collectif au 1er janvier 2026 si le "
                "permis a été demandé avant le 1er janvier 2013.",
            "Sur les chais et les dépendances anciennes du bourg et de Germignan, les "
                "charpentes de grande portée exposées à l’humidité de la jalle appellent un "
                "diagnostic parasitaire avant réhabilitation, préalable à tout chiffrage.",
        ],
    ),

    "ambares-et-lagrave": dict(
        parc="Ambarès-et-Lagrave n'a pas un centre mais plusieurs : le bourg d'Ambarès, "
             "celui de Lagrave, et des noyaux hérités du maraîchage et de la vigne. Le "
             "chemin de fer a fixé la commune ; ses emprises y ont laissé un habitat "
             "ouvrier en bandes, brique et enduit, largement remanié depuis. Autour, les "
             "lotissements des années 1970 à 1990 ont occupé les terres basses drainées, "
             "puis des résidences collectives de trois à cinq niveaux se sont posées le "
             "long des axes.",
        enjeu="Le parc collectif y est assez développé pour que les échéances de la "
              "copropriété constituent un calendrier réel, immeuble par immeuble. Les "
              "résidences bâties entre 1960 et 1990 relèvent, dès lors qu'elles comptent "
              "au plus cinquante lots, du plan pluriannuel de travaux depuis le 1er "
              "janvier 2025 et du diagnostic de performance énergétique collectif depuis "
              "le 1er janvier 2026 ; le décompte des lots se vérifie sur l'état "
              "descriptif de division. Deux conditions s'y ajoutent : quinze ans révolus "
              "depuis la réception des travaux pour le plan pluriannuel, et un permis de "
              "construire déposé avant le 1er janvier 2013 pour le diagnostic collectif. "
              "Sur ces immeubles, le repérage amiante avant travaux porte d'abord sur les "
              "parties communes, mais son périmètre reste celui de la zone de travaux : "
              "une gaine ou une colonne qui traverse un logement impose d'y accéder. Au "
              "centre, les opérations de renouvellement appellent un repérage avant "
              "démolition, complété du diagnostic PEMD au-delà de mille mètres carrés de "
              "surface cumulée de plancher — seuil valable en démolition comme en "
              "rénovation significative.",
        copro="Le paysage local est composite. Une première famille rassemble les petits "
              "collectifs des années 1960-1980, souvent acquis par des propriétaires "
              "bailleurs : la forte proportion de lots non occupés par leur propriétaire "
              "rend les assemblées difficiles à réunir et les majorités incertaines. Une "
              "deuxième tient aux divisions d'anciennes maisons de bourg et de "
              "dépendances maraîchères : le nombre de lots y est faible, mais les "
              "servitudes de passage héritées du parcellaire agricole compliquent le "
              "partage des charges bien plus que l'état du bâti. Une troisième, récente, "
              "regroupe les programmes du centre, encore sous garanties. Trois situations "
              "sans rapport pour un même conseil syndical : alimenter un fonds de travaux "
              "parti de zéro, reconstituer des plans perdus, faire jouer une décennale "
              "avant extinction.",
        reperes=[
            "Sur les résidences des années 1970, le revêtement de sol semi-rigide et la "
                "colle qui le fixe se rencontrent d'abord dans les paliers, les caves et "
                "les locaux techniques.",
            "Les réfections de couverture des années 1970-1980 ont fréquemment posé des "
                "ardoises en fibres-ciment sur charpente ancienne : sous-face, closoirs et "
                "rives sont à sonder avant toute intervention.",
            "Les chaufferies collectives d'origine conservent des calorifugeages aux "
                "coudes, aux tés et aux vannes, même lorsque la chaudière a déjà été "
                "remplacée.",
            "Dans le bâti de bourg antérieur au 1er janvier 1949, les peintures des "
                "menuiseries et des ferronneries des parties communes peuvent contenir du "
                "plomb : le relever pendant le repérage amiante avant travaux évite une "
                "seconde visite.",
        ],
    ),

    "ambes": dict(
        parc="Ambès occupe la pointe de la presqu'île, là où la Garonne et la Dordogne "
             "se rejoignent. Le sol est celui des palus : alluvions, nappe haute, "
             "remblais, digues. Le bâti se lit en trois ensembles. Le bourg ancien, "
             "resserré, en moellons enduits et tuiles canal, avec ses dépendances et ses "
             "chais. Un tissu de logements alignés et standardisés, édifié au milieu du "
             "XXe siècle et largement remanié depuis. Et le bâti d'activité lui-même — "
             "ateliers, entrepôts, cuves et réseaux de tuyauteries — qui donne à la "
             "commune sa physionomie. La construction individuelle récente y est "
             "contenue par les servitudes liées aux risques technologique et "
             "d'inondation.",
        enjeu="La logique dominante n'est pas celle de la copropriété mais celle du code "
              "du travail. Sur les bâtiments de ces sites, le repérage amiante avant "
              "travaux obéit à l'arrêté du 16 juillet 2019 : il incombe au donneur "
              "d'ordre et doit être joint au dossier de consultation, avant remise des "
              "offres et non après. Sur les installations, structures et équipements "
              "industriels eux-mêmes, l'arrêté propre à ce domaine n'est pas publié ; "
              "l'obligation d'évaluation du risque prévue à l'article R. 4412-97 du code "
              "du travail demeure, et le repérage se conduit alors sur un cahier des "
              "charges contractuel. Le diagnostic PEMD, lui, ne tient pas au seul "
              "franchissement des mille mètres carrés de plancher cumulé : un bâtiment "
              "ayant accueilli une activité industrielle et abrité des substances "
              "classées dangereuses y est soumis quelle que soit son emprise, et la "
              "rénovation significative ouvre la même obligation que la démolition. Sur "
              "l'habitat, ce sont les travaux prescrits au titre du risque technologique "
              "qui déclenchent les repérages.",
        copro="La copropriété y est marginale, et c'est ce qui la rend délicate. Les "
              "rares immeubles collectifs du bourg comptent peu de lots : beaucoup "
              "relèvent du régime des petites copropriétés — au plus cinq lots "
              "principaux, ou un budget prévisionnel moyen inférieur à quinze mille euros "
              "— qui les dispense de conseil syndical et les autorise à tenir une "
              "comptabilité de trésorerie ; le syndic y est le plus souvent bénévole. Les "
              "logements bâtis en série puis cédés par lots ont laissé des mitoyennetés "
              "et des servitudes mal établies dont personne ne détient les plans. Quand "
              "une décision de travaux s'impose, le syndic constate l'absence de carnet "
              "d'entretien, d'un état descriptif exploitable et de tout repérage amiante "
              "des parties communes.",
        reperes=[
            "Sur les réseaux industriels antérieurs à 1997, le calorifugeage amianté se "
                "double de joints de brides, de tresses et de plaques de protection "
                "thermique : de faible volume, ils échappent au métré mais relèvent du même "
                "régime de retrait que les tuyauteries.",
            "Les bâtiments d'exploitation de la presqu'île sont couverts en plaques "
                "ondulées de fibres-ciment sur pannes métalliques ; rives et closoirs de "
                "faîtage sont du même matériau.",
            "Les cuves et rétentions désaffectées doivent être vidées et attestées "
                "avant le repérage avant démolition : sans cela l'accès aux parois et aux "
                "calorifuges reste impossible.",
        ],
    ),

    "saint-louis-de-montferrand": dict(
        parc="Saint-Louis-de-Montferrand s'étire le long de la Garonne, derrière les "
             "digues qui tiennent les palus. Le bourg est linéaire, aligné sur la route "
             "qui suit le fleuve : maisons basses en moellons enduits, tuiles canal à "
             "faible pente, planchers surélevés de quelques marches, sans cave, car la "
             "nappe l'interdit. En arrière, le territoire est un marais drainé, "
             "quadrillé de jalles et de fossés, avec ses chais, ses hangars maraîchers "
             "et ses serres. La partie récente tient en lotissements pavillonnaires "
             "implantés sur remblai depuis les années 1980 et en quelques collectifs de "
             "deux ou trois niveaux. Le bâti reste bas et étalé, sans équipement commun "
             "lourd : ni ascenseur, ni sous-sol, ni chaufferie desservant plusieurs "
             "bâtiments.",
        enjeu="Le risque d'inondation structure les missions davantage que l'âge du bâti. "
              "Après une submersion, la remise en état des rez-de-chaussée touche "
              "précisément les matériaux qu'on ne peut pas déposer sans repérage : "
              "revêtements de sol collés, plinthes, doublages, enduits de ragréage. Le "
              "repérage amiante avant travaux incombe au donneur d'ordre, non à "
              "l'entreprise qui intervient ; le faire réaliser avant le premier "
              "arrachage, et non après, sépare un chantier tenu d'un chantier arrêté. Sur "
              "le bâti agricole, le diagnostic PEMD ne dépend pas de la seule surface : "
              "un hangar ayant abrité le stockage de produits phytosanitaires y est "
              "soumis au titre de son activité passée, sans condition d'emprise. Enfin, "
              "l'absence de sous-sol et les planchers sur terre-plein ferment les "
              "scénarios d'isolation par le bas : sur les rares immeubles collectifs "
              "concernés par le diagnostic de performance énergétique collectif, les "
              "gains se jouent en toiture, en menuiseries et en ventilation.",
        copro="La copropriété au sens de la loi du 10 juillet 1965 est rare ici : la "
              "confusion la plus fréquente porte sur les lotissements. Les ensembles "
              "pavillonnaires livrés depuis les années 1980 relèvent le plus souvent "
              "d'une association syndicale libre, quand la voirie et les réseaux n'ont "
              "pas été rétrocédés à la commune. Ces structures entretiennent chaussées, "
              "réseaux et ouvrages de gestion des eaux pluviales sans être des syndicats "
              "de copropriétaires : elles échappent donc au plan pluriannuel de travaux "
              "comme au diagnostic de performance énergétique collectif. Les véritables "
              "copropriétés se comptent dans le bourg : quelques lots issus de divisions, "
              "parfois avec un commerce en rez-de-chaussée, dans un bâti ancien "
              "administré sans syndic professionnel. Les ouvrages hydrauliques du marais "
              "dépendent, eux, de structures syndicales encore différentes.",
        reperes=[
            "Les toitures à faible pente du bourg supportent mal la surcharge : les "
                "réfections y ont privilégié des plaques de fibres-ciment posées sur "
                "liteaunage léger, dont la dépose se prépare depuis l'extérieur, sans "
                "circulation en sous-face.",
            "Sur un rez-de-chaussée qui a pris l'eau, la colle noire bitumineuse "
                "subsiste sous l'ancien revêtement, y compris lorsqu'un carrelage a été "
                "reposé par-dessus sans dépose.",
            "Un hangar maraîcher cumule couverture en fibres-ciment, bardages et "
                "stockages résiduels : le repérage avant démolition et l'inventaire des "
                "déchets se préparent sur la même visite.",
            "L'implantation sur remblai et l'absence de cave réduisent les points "
                "d'accès aux réseaux : les sondages destructifs s'arbitrent au chiffrage, "
                "pas en cours de chantier.",
        ],
    ),

    "saint-vincent-de-paul": dict(
        parc="Saint-Vincent-de-Paul forme la porte nord-est de la métropole, là où la "
             "Dordogne se franchit vers Cubzac-les-Ponts, par le rail comme par la "
             "route. Le territoire repose sur deux sols, le palus au bord de la rivière "
             "et les premières pentes en arrière : d'où un bourg groupé en moellons "
             "enduits et un habitat dispersé sur les hauts. Le logement individuel "
             "domine, porté par les lotissements ouverts à partir des années 1970 ; le "
             "collectif y reste rare et récent. Le corridor d'infrastructures a en "
             "revanche fixé des entrepôts et des ateliers, dont une partie est "
             "antérieure à 1997 : c'est sur ce bâti d'activité que se rencontrent les "
             "grandes surfaces couvertes.",
        enjeu="Deux régimes se croisent sur un territoire pourtant modeste. Le premier "
              "concerne les locaux d'activité : dès lors que leur permis de construire a "
              "été délivré avant le 1er juillet 1997, une restructuration, un percement "
              "de bardage ou une reprise d'éclairage zénithal impose au donneur d'ordre "
              "un repérage amiante avant travaux, remis aux entreprises avant chiffrage. "
              "Faux-plafonds, revêtements de sol collés, bardages et couvertures en "
              "fibres-ciment en sont les postes habituels. Le second tient aux immeubles "
              "anciens du bourg que l'on divise : la mise en copropriété d'un bâtiment "
              "construit depuis plus de dix ans rend le diagnostic technique global "
              "obligatoire, avec l'état apparent des parties communes et des équipements, "
              "et l'évaluation des travaux nécessaires sur dix ans. Enfin, les petits "
              "collectifs du début des années 2010 atteignent quinze ans : c'est la date "
              "de réception des travaux, non celle de l'entrée dans les lieux, qui les "
              "fait basculer dans le champ du plan pluriannuel de travaux.",
        copro="Le stock de copropriétés y est récent, constitué pour l'essentiel au cours "
              "des vingt dernières années. Deux familles s'y distinguent. D'un côté, les "
              "petits programmes collectifs en R+2, à faible nombre de lots, où le syndic "
              "gère surtout des équipements — portail, pompe de relevage, ventilation "
              "mécanique — plutôt qu'un clos et couvert vieillissant. De l'autre, les "
              "divisions de maisons anciennes et de leurs annexes, qui créent des "
              "copropriétés de trois ou quatre lots dont les tantièmes n'ont jamais été "
              "recalculés ; la première dépense utile y est un modificatif de l'état "
              "descriptif, avant tout devis. Dans les deux cas, le conseil syndical part "
              "sans mémoire technique : le diagnostic technique global y remet une base "
              "commune.",
        reperes=[
            "Sur un entrepôt dont le permis est antérieur à juillet 1997, la couverture "
                "en fibres-ciment relève du même repérage que les descentes d'eaux "
                "pluviales et les conduits de ventilation.",
            "Les faux-plafonds des bureaux aménagés dans les années 1980 relèvent de la "
                "liste A, comme les flocages et les calorifugeages : leur état de "
                "conservation doit être évalué, et cette évaluation commande la suite.",
            "Dans les maisons de bourg divisées, l'escalier devient une partie commune "
                "sans avoir jamais été traité comme tel : marches, contremarches et paliers "
                "entrent dans le périmètre du repérage dès qu'une reprise de la cage est "
                "votée.",
            "Le bourg tient du palus et du coteau : sur les bâtiments en pied de pente, "
                "les fissurations relevées au diagnostic technique global appellent une "
                "reconnaissance de sols avant d'être imputées au bâti.",
        ],
    ),

    "artigues-pres-bordeaux": dict(
        parc="Artigues-près-Bordeaux occupe un plateau calcaire qui domine la rive "
             "droite de la Garonne. La commune est restée agricole et viticole jusqu’aux "
             "années 1960 : il en subsiste des maisons de maître, des chais et des "
             "dépendances de pierre dispersés autour du bourg ancien. L’urbanisation "
             "s’est faite ensuite par vagues de lotissements pavillonnaires, puis par "
             "des résidences collectives de taille moyenne — quelques niveaux, espaces "
             "verts communs, stationnement souvent en sous-sol — édifiées pour "
             "l’essentiel entre les années 1970 et 1990. S’y ajoute un tissu de bureaux "
             "et de locaux d’activité né des mêmes décennies, dont les plateaux ont été "
             "recloisonnés plusieurs fois depuis leur livraison.",
        enjeu="Ce parc place la commune dans une configuration mixte : résidences "
              "collectives des décennies 1970-1990, bâti ancien de pierre et surfaces "
              "tertiaires sur un même territoire. Les résidences relèvent aujourd’hui du "
              "plan pluriannuel de travaux et du DPE collectif, souvent sans qu’un "
              "document technique d’ensemble ait jamais été produit ; le diagnostic "
              "technique global est l’étape qui rend le reste exploitable, parce qu’il "
              "objective l’état des façades, des couvertures et des réseaux avant que "
              "l’assemblée générale ne vote un budget. Dès lors que le permis de "
              "construire est antérieur au 1er juillet 1997, toute opération susceptible "
              "de libérer des fibres — percement, dépose de revêtement, reprise de gaine "
              "— suppose un repérage amiante avant travaux conforme à l’arrêté du 16 "
              "juillet 2019, étendu aux locaux techniques et aux caves. Sur les surfaces "
              "tertiaires, la dépose de faux-plafonds et de cloisons démontables relève "
              "du code du travail : le donneur d’ordre y est l’exploitant qui engage les "
              "travaux, pas nécessairement le propriétaire des murs.",
        copro="La copropriété artiguaise est faite de résidences de taille moyenne, "
              "réparties en plusieurs bâtiments autour d’espaces verts communs, souvent "
              "avec chauffage individuel. Ce format produit des charges contenues, donc "
              "des conseils syndicaux peu habitués aux opérations lourdes, et un fonds de "
              "travaux fréquemment alimenté au minimum légal. Les sujets sont ceux d’un "
              "parc livré en une vingtaine d’années : menuiseries et garde-corps "
              "d’origine, étanchéité de toiture-terrasse en fin de second cycle, "
              "ventilation mécanique jamais reprise depuis la livraison. S’y ajoutent des "
              "copropriétés horizontales issues des lotissements : leur budget ne porte "
              "pas sur du bâti mais sur des équipements de desserte, ce qui déplace "
              "l’objet même du plan pluriannuel.",
        reperes=[
            "Dans les résidences dont le permis est antérieur au 1er juillet 1997, les "
                "dalles de sol semi-rigides et leur colle bitumineuse subsistent surtout "
                "dans les halls, les circulations et les caves.",
            "Conduits de ventilation et descentes d’eaux pluviales en fibres-ciment "
                "traversent les gaines techniques : les trappes de palier en donnent "
                "souvent une lecture suffisante pour cadrer les sondages destructifs.",
            "Les plafonds de cages d’escalier ont fréquemment reçu un enduit projeté : "
                "à faire repérer avant tout percement, pose de gaine ou création de trémie.",
            "Sur le bâti antérieur au 1er janvier 1949, le constat de risque "
                "d’exposition au plomb des parties communes s’impose au syndicat : il "
                "conditionne l’organisation d’un chantier de peinture avant même son "
                "chiffrage.",
        ],
    ),

    "carbon-blanc": dict(
        parc="Carbon-Blanc s’inscrit sur un territoire restreint et déjà occupé, ce qui "
             "explique la forme de son bâti. Le noyau ancien s’étire en village-rue le "
             "long de l’ancienne route qui traverse la commune : maisons de bourg "
             "mitoyennes en moellon, souvent en rez-de-chaussée surélevé, quelques "
             "immeubles de deux ou trois niveaux avec un commerce en pied. Autour, les "
             "lotissements des années 1960 à 1980 ont occupé les anciennes parcelles "
             "maraîchères et viticoles du plateau. Le collectif reste modeste : petites "
             "résidences, un patrimoine de logement social ancien, et des programmes "
             "contemporains insérés en dents creuses, à la place d’un pavillon, d’un "
             "hangar ou d’un atelier démoli.",
        enjeu="Un territoire déjà bâti impose une règle simple : on construit en "
              "démolissant. Chaque opération neuve prend la place d’une construction des "
              "décennies 1950-1980, ce qui déclenche un repérage amiante avant démolition "
              "— mission de liste C, conduite sur bâtiment libéré, sondages destructifs "
              "autorisés. S’y ajoute, dès que le seuil de surface fixé par le code de la "
              "construction et de l’habitation est franchi, ou que le bâtiment a hébergé "
              "une activité ayant pu mettre en œuvre des substances dangereuses, le "
              "diagnostic portant sur les produits, équipements, matériaux et déchets : "
              "il se réalise avant le dépôt de la demande de permis de démolir ou, à "
              "défaut, avant la passation des marchés. Sur le parc résidentiel, "
              "l’échéance est d’un autre ordre. Les copropriétés d’au plus cinquante lots "
              "relèvent du plan pluriannuel de travaux depuis le 1er janvier 2025, dès "
              "lors que l’immeuble a plus de quinze ans, et du DPE collectif depuis le "
              "1er janvier 2026 lorsque le permis a été déposé avant le 1er janvier 2013.",
        copro="Le conseil syndical, à Carbon-Blanc, gère rarement plus d’un bâtiment. La "
              "forme dominante est le petit immeuble de bourg — une cage d’escalier, peu "
              "de lots, parfois un local commercial en pied — et la résidence de deux ou "
              "trois plots héritée des lotissements. Beaucoup fonctionnent avec un syndic "
              "non professionnel : carnet d’entretien non tenu, archives limitées au "
              "dernier ravalement, plans de réseaux absents. La conséquence se répète au "
              "moment d’établir le plan pluriannuel de travaux : personne ne sait ce qui "
              "a été repris, à quelle date, ni avec quels matériaux. Le diagnostic "
              "technique global comble ce vide, et il vaut d’être voté avant l’engagement "
              "de la première dépense plutôt qu’après.",
        reperes=[
            "Dans le village-rue, les maisons de bourg mitoyennes antérieures à 1949 "
                "partagent souvent une cage d’escalier ajoutée après coup : c’est là, sur "
                "les portes palières et les huisseries repeintes couche sur couche, que le "
                "plomb se concentre.",
            "Dans les résidences des années 1970, chaufferie et sous-sols restent les "
                "zones les plus productives d’un repérage : calorifugeage des réseaux, "
                "joints de brides, rebouchages coupe-feu au passage des gaines.",
            "Avant une démolition en dent creuse, l’usage passé du bâtiment compte "
                "autant que sa date de construction : un ancien atelier impose des "
                "recherches que la seule surface ne déclenche pas.",
            "Sur ces parcelles étroites, le phasage démolition-construction s’arrête "
                "avant le repérage, faute de quoi le périmètre repéré ne couvre pas ce qui "
                "sera réellement déposé.",
        ],
    ),

    "bouliac": dict(
        parc="Bouliac occupe un point haut du coteau calcaire qui borde la Garonne en "
             "rive droite, et cette pente ordonne tout le bâti. Le bourg ancien, "
             "resserré autour de son église, conserve des maisons de pierre et des "
             "dépendances liées au vignoble qui couvrait le versant. Sur les flancs et "
             "en contrebas, les décennies 1970 à 2000 ont installé un pavillonnaire bâti "
             "en gradins, avec sous-sols semi-enterrés et murs de soutènement. Le "
             "collectif y est rare et de faible hauteur : petites résidences à "
             "toiture-terrasse ou à faible pente, souvent adossées au terrain naturel "
             "plutôt que posées dessus, desservies par des voiries privées en rampe.",
        enjeu="Ce qui commande les missions collectives à Bouliac n’est pas d’abord "
              "l’amiante, mais le sol et la structure. Le bâti repose sur des terrains "
              "argilo-calcaires exposés au retrait-gonflement des argiles, dont l’aléa se "
              "vérifie parcelle par parcelle sur la cartographie nationale : fissures de "
              "façade, désordres de dallage, murs de soutènement et drainage deviennent "
              "des postes lourds, que le fonds de travaux n’anticipe pas. Le diagnostic "
              "technique global sert ici à recenser ces désordres et à déclencher, quand "
              "ils le justifient, le suivi instrumenté qui dira s’ils sont stabilisés ou "
              "évolutifs ; il ne tranche pas seul cette question. L’amiante se loge, "
              "elle, dans les étanchéités de toiture-terrasse et les conduits des "
              "constructions autorisées avant le 1er juillet 1997. L’ancienneté ne "
              "protège de rien : l’amiante-ciment est fabriqué industriellement depuis le "
              "début du XXe siècle, et une couverture posée sur une dépendance de pierre "
              "peut être bien plus récente que ses murs.",
        copro="La copropriété bouliacaise est atypique : peu de grands immeubles, "
              "beaucoup de petites résidences basses, et un nombre notable de "
              "copropriétés horizontales et d’associations syndicales libres issues des "
              "lotissements de coteau. Dans ces dernières, l’objet de la gestion n’est ni "
              "un escalier ni une façade : une chaussée en rampe, un réseau d’eaux "
              "pluviales dimensionné pour un ruissellement rapide, un éclairage, parfois "
              "un ouvrage de rétention — des équipements mal identifiés dans les "
              "règlements anciens et rarement provisionnés. Les résidences collectives, "
              "elles, cumulent toiture-terrasse, garages semi-enterrés et soutènements : "
              "trois postes dont la reprise engage des montants sans rapport avec le "
              "nombre de lots entre lesquels les répartir.",
        reperes=[
            "Sur les bâtiments dont le permis de construire a été délivré avant le 1er "
                "juillet 1997, l’étanchéité de toiture-terrasse se sonde en premier : une "
                "réfection récente recouvre souvent le complexe d’origine sans l’avoir "
                "déposé. Ces revêtements bitumineux figurent en liste B et doivent "
                "apparaître au dossier technique amiante des parties communes.",
            "Dans le vieux bourg et les anciennes dépendances viticoles, le plomb avant "
                "travaux se cherche sur les volets et les ferronneries extérieures, "
                "repeints couche sur couche sans décapage.",
            "Une fissure sur mur de soutènement ne se traite pas comme une fissure de "
                "façade : témoins posés et relevés datés conditionnent le rang que le plan "
                "pluriannuel donnera à ce poste.",
            "Sur les parcelles en pente, l’accès des engins et les zones de stockage se "
                "calent en amont : cette contrainte pèse souvent davantage sur le coût que "
                "la nature des matériaux repérés.",
        ],
    ),

    "saint-aubin-de-medoc": dict(
        parc="Saint-Aubin-de-Médoc est une commune de lande et de pins, à la frange "
             "nord-ouest de la métropole. Le bourg ancien se réduit à quelques rues "
             "autour de l’église et de la mairie ; l’essentiel du reste s’est construit "
             "à partir des années 1970, sous couvert boisé, par lotissements "
             "pavillonnaires, sur des sols sableux où le vide sanitaire a remplacé le "
             "sous-sol. Les maisons sont individuelles, presque toujours accompagnées "
             "d’annexes ajoutées au fil du temps : garages, abris, préaux. Le collectif "
             "se limite à quelques petits programmes récents et à un patrimoine communal "
             "— écoles, salles, équipements sportifs — édifié dans les décennies 1970 et "
             "1980.",
        enjeu="La commune comptant très peu de copropriétés verticales, l’obligation qui "
              "structure les missions collectives n’est ici ni le plan pluriannuel de "
              "travaux ni le DPE collectif, mais le repérage amiante avant travaux au "
              "titre du code du travail, sur le patrimoine public et associatif. Une "
              "école, un gymnase ou une salle des fêtes des années 1970-1990 mise en "
              "rénovation énergétique réunit exactement les matériaux recherchés : dalles "
              "de sol collées, faux-plafonds, plaques de sous-toiture, calorifugeages de "
              "chaufferie. L’arrêté du 16 juillet 2019 fixe le contenu de cette mission ; "
              "le donneur d’ordre, commune ou association gestionnaire, doit la faire "
              "réaliser puis en remettre le rapport aux entreprises consultées, avant "
              "leur remise de prix et non au moment de l’ordre de service. Un repérage "
              "produit trop tard n’a plus d’effet utile : l’entreprise a chiffré sans "
              "lui, et l’avenant suit. Le second gisement tient aux annexes et aux "
              "équipements de lotissement, où la démolition d’un simple préau relève du "
              "repérage avant démolition.",
        copro="Ce qui tient lieu de copropriété à Saint-Aubin-de-Médoc, ce sont les "
              "lotissements : associations syndicales libres et copropriétés "
              "horizontales. La distinction n’est pas formelle. Le plan pluriannuel de "
              "travaux s’impose aux syndicats de copropriétaires régis par la loi du 10 "
              "juillet 1965, non aux associations syndicales libres, qui relèvent de "
              "l’ordonnance du 1er juillet 2004 et de leurs propres statuts : vérifier le "
              "régime avant de commander évite un rapport sans destinataire. Les "
              "instances y sont bénévoles et les budgets faibles.",
        reperes=[
            "Sur le patrimoine communal des années 1970-1990, les points productifs "
                "sont les colles de dalles de sol, les plaques de sous-toiture des préaux "
                "et les conduits de chaufferie.",
            "Les annexes des maisons — garages, abris, préaux — sont le principal "
                "gisement de plaques ondulées en fibres-ciment, et leur dépose est "
                "fréquemment engagée sans repérage préalable.",
            "Dans un lotissement géré en association syndicale libre, la frontière "
                "entre partie commune et partie privative se lit dans le cahier des charges "
                "et les statuts ; dans une copropriété horizontale, elle se lit dans le "
                "règlement de copropriété. C’est ce document qui détermine qui commande et "
                "qui paie.",
            "Le couvert forestier gêne l’identification des réseaux enterrés : un "
                "repérage avant travaux sur voirie de lotissement se prépare avec les plans "
                "de récolement, quand ils existent.",
        ],
    ),

}
