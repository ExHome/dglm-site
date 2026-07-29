# -*- coding: utf-8 -*-
"""
BORDEAUX AU QUARTIER.

Le site A s'arrête à « diagnostic immobilier Bordeaux ». Une seule page pour
une ville dont le bâti n'a rien d'homogène : une échoppe de Nansouty, un chai
des Chartrons et une barre du Grand Parc n'appellent ni les mêmes sondages, ni
le même plan de repérage, ni le même budget de travaux.

C'est le niveau de granularité où l'on ne peut pas être suivi sans faire le
travail : il faut connaître le bâti. Personne ne publie ça sur Bordeaux.
"""

QUARTIERS_BORDEAUX = [
    dict(
        nom="Chartrons", slug="chartrons",
        intro="Quartier des négociants en vin, les Chartrons alignent hôtels particuliers "
              "du XVIIIe siècle, immeubles de pierre et anciens chais reconvertis en "
              "logements à partir des années 1980.",
        bati="Pierre de taille et planchers bois pour le bâti d'origine ; les chais "
             "transformés en lofts l'ont été en pleine période d'usage de l'amiante en "
             "second œuvre.",
        enjeu="Double risque : plomb structurel sur tout ce qui est antérieur à 1949, et "
              "amiante dans les reconversions des années 1980-1990 — dalles de sol, colles, "
              "cloisons, conduits. Les copropriétés issues de division de chais ont des "
              "règlements récents mais un bâti très ancien : le diagnostic technique global "
              "y révèle presque toujours des désordres de structure sous-estimés.",
        vigilance="Secteur sauvegardé sur une partie du quartier : l'étendue des sondages "
                  "destructifs se cale avec l'architecte des Bâtiments de France avant "
                  "l'intervention.",
        voisins=["bacalan", "grand-parc", "saint-seurin"],
    ),
    dict(
        nom="Saint-Michel et Capucins", slug="saint-michel-capucins",
        intro="Le cœur populaire et le plus ancien de Bordeaux : parcellaire médiéval, "
              "immeubles étroits sur plusieurs niveaux, forte densité de petites "
              "copropriétés.",
        bati="Bâti majoritairement antérieur à 1900, souvent divisé et redivisé, avec des "
             "travaux successifs jamais documentés.",
        enjeu="C'est le secteur où l'on trouve le plus de copropriétés de moins de dix lots "
              "sans syndic professionnel, sans carnet d'entretien et sans aucun diagnostic. "
              "Le constat plomb des parties communes y est obligatoire depuis longtemps et "
              "presque jamais réalisé. Les procédures de péril et les arrêtés d'insalubrité "
              "y sont plus fréquents qu'ailleurs dans la métropole.",
        vigilance="Sur un immeuble sous arrêté, le diagnostic technique global est le "
                  "document qui permet de sortir de la procédure. Nous intervenons dans ce "
                  "cadre avec des délais courts.",
        voisins=["nansouty-saint-genes", "la-bastide", "belcier-euratlantique"],
    ),
    dict(
        nom="Bacalan et Bassins à flot", slug="bacalan-bassins-a-flot",
        intro="Ancien quartier portuaire et industriel, Bacalan est le territoire de "
              "Bordeaux qui s'est le plus transformé en quinze ans : hangars, bases "
              "sous-marines et ateliers côtoient des programmes neufs livrés depuis 2012.",
        bati="Patrimoine industriel de la première moitié du XXe siècle — charpentes "
             "métalliques, bardages et couvertures en fibres-ciment — et immeubles "
             "récents en béton.",
        enjeu="Le quartier concentre l'essentiel des missions de repérage avant démolition "
              "de la ville : friches, hangars et ateliers cédés à des promoteurs. Le "
              "diagnostic sur les produits, équipements, matériaux et déchets y est "
              "systématiquement requis, les surfaces dépassant très largement les seuils.",
        vigilance="Sur les opérations mixtes démolition-conservation, le périmètre du "
                  "repérage doit être calé sur le phasage réel du chantier, faute de quoi "
                  "les entreprises se retrouvent hors périmètre en cours de travaux.",
        voisins=["chartrons", "le-lac-aubiers", "grand-parc"],
    ),
    dict(
        nom="Caudéran", slug="cauderan",
        intro="Quartier résidentiel de l'ouest bordelais, Caudéran est dominé par les "
              "maisons bourgeoises, les échoppes doubles et un pavillonnaire des années "
              "1930 à 1970.",
        bati="Maisons individuelles majoritaires, avec des petits collectifs de standing "
             "construits entre 1965 et 1990 sur les axes principaux.",
        enjeu="Peu de grandes copropriétés, mais une forte densité de petits immeubles de "
              "10 à 40 lots aujourd'hui tous concernés par le plan pluriannuel de travaux. "
              "Ce sont des copropriétés bien gérées financièrement mais sans historique "
              "technique : le diagnostic technique global y remplit un vide.",
        vigilance="Les extensions et vérandas ajoutées dans les années 1970-1980 sur ces "
                  "maisons contiennent fréquemment des plaques de couverture amiantées, "
                  "que les propriétaires découvrent au moment de les déposer.",
        voisins=["saint-augustin", "saint-seurin"],
    ),
    dict(
        nom="Nansouty et Saint-Genès", slug="nansouty-saint-genes",
        intro="Le royaume de l'échoppe bordelaise : rues entières de maisons basses en "
              "pierre, mitoyennes, construites entre 1860 et 1930, entrecoupées de petits "
              "immeubles de rapport.",
        bati="Pierre calcaire, planchers bois, couvertures tuiles canal. Beaucoup de "
             "surélévations et de divisions réalisées après 1950.",
        enjeu="Les divisions d'échoppes et d'immeubles de rapport en deux ou trois lots ont "
              "créé une multitude de micro-copropriétés qui ignorent leurs obligations. "
              "Antérieures à 1949 pour la plupart, elles relèvent du constat plomb des "
              "parties communes, et désormais toutes du plan pluriannuel de travaux.",
        vigilance="Sur ce bâti, la mérule et les insectes xylophages attaquent les planchers "
                  "bois en pied de mur. L'état parasitaire précède utilement toute "
                  "programmation de travaux.",
        voisins=["saint-michel-capucins", "belcier-euratlantique", "saint-augustin"],
    ),
    dict(
        nom="La Bastide", slug="la-bastide",
        intro="Rive droite, la Bastide associe un faubourg ouvrier ancien, d'anciennes "
              "emprises ferroviaires et industrielles, et le vaste secteur neuf de Brazza "
              "livré depuis 2018.",
        bati="Maisons ouvrières basses, ateliers et entrepôts du XIXe et XXe siècle, "
             "immeubles contemporains.",
        enjeu="Le tissu industriel résiduel alimente les missions de repérage avant "
              "démolition et de diagnostic PEMD, tandis que le faubourg ancien relève du "
              "plomb et du repérage avant travaux sur des opérations de rénovation "
              "énergétique subventionnées.",
        vigilance="Sols potentiellement pollués sur les anciennes emprises : le repérage "
                  "amiante ne couvre pas ce risque, il doit être articulé avec une étude "
                  "de sols menée par un bureau spécialisé.",
        voisins=["saint-michel-capucins", "belcier-euratlantique"],
    ),
    dict(
        nom="Saint-Augustin", slug="saint-augustin",
        intro="Entre le centre et Mérignac, Saint-Augustin mêle échoppes, résidences "
              "collectives des années 1960-1980 et équipements hospitaliers et "
              "universitaires.",
        bati="Collectif en béton de la période 1960-1980, très majoritaire sur les axes, "
             "et échoppes dans les rues intérieures.",
        enjeu="Le collectif de cette période est celui qui concentre le plus de matériaux "
              "amiantés en parties communes : conduits, gaines techniques, dalles de sol "
              "des halls et des caves, calorifugeages de chaufferie. Le dossier technique "
              "amiante y est obligatoire, souvent ancien et jamais réévalué.",
        vigilance="Les chaufferies collectives de ces résidences sont le premier point de "
                  "contrôle : c'est là que se trouvent les calorifugeages dégradés, et "
                  "c'est là qu'interviennent les entreprises de maintenance.",
        voisins=["cauderan", "nansouty-saint-genes"],
    ),
    dict(
        nom="Grand Parc", slug="grand-parc",
        intro="Grand ensemble construit à partir de 1959 au nord du centre-ville, le Grand "
              "Parc a fait l'objet d'une réhabilitation de grande ampleur saluée "
              "internationalement, et poursuit sa transformation.",
        bati="Barres et tours en béton des années 1959-1975, avec des interventions lourdes "
             "de réhabilitation depuis 2014.",
        enjeu="Bâti intégralement construit dans la période de plus forte utilisation de "
              "l'amiante. Toute intervention sur ce parc — réhabilitation, remplacement de "
              "menuiseries, reprise de réseaux — impose un repérage avant travaux avec "
              "sondages destructifs, sur des immeubles occupés.",
        vigilance="En site occupé, le plan de repérage se conçoit avec le calendrier de "
                  "relogement temporaire. C'est le point qui fait dériver les plannings "
                  "quand il est traité trop tard.",
        voisins=["chartrons", "bacalan-bassins-a-flot", "le-lac-aubiers"],
    ),
    dict(
        nom="Le Lac et Aubiers", slug="le-lac-aubiers",
        intro="Au nord, le secteur du Lac associe le grand ensemble des Aubiers, le parc "
              "des expositions, des zones d'activité et un secteur en renouvellement "
              "urbain actif.",
        bati="Grand ensemble des années 1970, halls d'exposition et bâtiments techniques "
             "de la même période.",
        enjeu="Renouvellement urbain en cours : démolitions programmées, restructurations "
              "d'équipements. Le repérage avant démolition et le diagnostic PEMD y sont "
              "commandés par des maîtres d'ouvrage publics et des bailleurs, avec des "
              "exigences de forme strictes pour l'annexion aux marchés.",
        vigilance="Sur marché public, le rapport doit être exploitable en pièce annexe : "
                  "quantitatifs par local, plans de repérage cotés, et localisation "
                  "sans ambiguïté des matériaux.",
        voisins=["bacalan-bassins-a-flot", "grand-parc"],
    ),
    dict(
        nom="Belcier et Euratlantique", slug="belcier-euratlantique",
        intro="Autour de la gare Saint-Jean, Belcier est le secteur qui connaît la mutation "
              "la plus rapide de la métropole, sous l'effet de l'opération d'intérêt "
              "national Bordeaux Euratlantique.",
        bati="Faubourg ouvrier ancien de maisons basses, emprises ferroviaires, entrepôts, "
             "et tours de bureaux et de logements livrées depuis 2016.",
        enjeu="Densité de démolitions et de restructurations sans équivalent en Gironde. "
              "Le diagnostic PEMD y est requis sur presque toutes les opérations, et le "
              "repérage avant démolition conditionne le calendrier d'un chantier dont le "
              "moindre décalage coûte cher.",
        vigilance="Les maisons de faubourg conservées au milieu des opérations neuves "
                  "restent antérieures à 1949 : plomb obligatoire, et amiante des travaux "
                  "d'après-guerre presque systématique.",
        voisins=["saint-michel-capucins", "la-bastide", "nansouty-saint-genes"],
    ),
    dict(
        nom="Saint-Seurin et Fondaudège", slug="saint-seurin",
        intro="Quartier bourgeois du centre-ouest, Saint-Seurin aligne immeubles de pierre "
              "du XIXe siècle, hôtels particuliers et copropriétés de standing.",
        bati="Pierre de taille, planchers bois et métalliques, toitures ardoise et zinc. "
             "Quelques collectifs des années 1960-1980 en insertion.",
        enjeu="Copropriétés anciennes bien tenues mais coûteuses à entretenir : façades en "
              "pierre, toitures complexes, ascenseurs anciens. Le plan pluriannuel de "
              "travaux y a une vraie utilité budgétaire, les postes étant lourds et "
              "difficiles à absorber en appel de fonds exceptionnel.",
        vigilance="Les cages d'escalier antérieures à 1949 relèvent du constat plomb des "
                  "parties communes avant toute réfection de peinture — un chantier très "
                  "fréquent dans ce quartier.",
        voisins=["chartrons", "cauderan"],
    ),
]

# --------------------------------------------------------------------------- Mérignac
QUARTIERS_MERIGNAC = [
    dict(
        nom="Arlac", slug="arlac",
        intro="Ancien bourg de l'est mérignacais devenu quartier résidentiel prisé, Arlac "
              "mêle échoppes, maisons de ville du début du XXe siècle et petits collectifs "
              "insérés le long de l'axe du tram A.",
        bati="Échoppes et maisons en pierre d'avant-guerre, complétées par des immeubles "
             "de rapport des années 1950-1980 et quelques programmes récents en béton.",
        enjeu="Beaucoup de petites copropriétés issues de divisions, aujourd'hui toutes "
              "concernées par le plan pluriannuel de travaux mais dépourvues d'historique "
              "technique. Le bâti antérieur à 1949 relève du constat plomb des parties "
              "communes, et l'amiante des travaux d'après-guerre se rencontre dès qu'on "
              "touche aux sols, aux conduits ou aux menuiseries.",
        vigilance="Les copropriétés de moins de dix lots sans syndic professionnel y sont "
                  "nombreuses : le diagnostic technique global est souvent le premier "
                  "document technique jamais établi sur l'immeuble.",
        voisins=["centre", "capeyron"],
    ),
    dict(
        nom="Capeyron", slug="capeyron",
        intro="Quartier pavillonnaire du nord de Mérignac, Capeyron s'est construit entre "
              "les années 1930 et 1970 autour de sa place et de ses commerces, avec une "
              "insertion progressive de petits collectifs.",
        bati="Pavillonnaire majoritaire, maisons individuelles et échoppes, ponctué de "
             "petits immeubles collectifs de 10 à 40 lots construits entre 1960 et 1990.",
        enjeu="Les petits collectifs de cette période concentrent les matériaux amiantés "
              "de second œuvre en parties communes — dalles de sol, colles, conduits, "
              "calorifugeages de chaufferie. Le dossier technique amiante y est obligatoire, "
              "souvent ancien et jamais réévalué. Toute rénovation énergétique déclenche un "
              "repérage avant travaux.",
        vigilance="Les dépendances et garages des pavillons portent fréquemment des plaques "
                  "de couverture en fibres-ciment amianté, découvertes au moment de la "
                  "dépose.",
        voisins=["arlac", "le-burck", "centre"],
    ),
    dict(
        nom="Le Burck", slug="le-burck",
        intro="Grand ensemble construit dans les années 1960-1970 au sud-est de Mérignac, "
              "le Burck associe barres et tours de logements, copropriétés et parc social, "
              "et fait l'objet d'un renouvellement urbain de longue haleine.",
        bati="Immeubles en béton de la période 1960-1975, souvent en copropriété ou en "
             "gestion mixte, avec des campagnes de réhabilitation successives.",
        enjeu="Bâti intégralement construit à la période de plus forte utilisation de "
              "l'amiante. Toute intervention — réhabilitation, remplacement de menuiseries, "
              "reprise de réseaux ou de chaufferie — impose un repérage avant travaux avec "
              "sondages destructifs, sur des immeubles occupés. Le plan pluriannuel de "
              "travaux y structure des programmes lourds et étalés.",
        vigilance="En site occupé, le plan de repérage se cale sur le calendrier de "
                  "relogement temporaire : traité trop tard, c'est le premier poste qui "
                  "fait déraper le planning.",
        voisins=["capeyron", "centre"],
    ),
    dict(
        nom="Centre et Mérignac-Soleil", slug="centre",
        intro="Le centre de Mérignac et le secteur commercial de Mérignac-Soleil connaissent "
              "une densification rapide : anciennes copropriétés, maisons et vastes emprises "
              "commerciales cèdent la place à des programmes neufs.",
        bati="Copropriétés des années 1960-1990 et pavillonnaire, au contact d'emprises "
             "commerciales et tertiaires en cours de restructuration.",
        enjeu="Double marché : d'un côté des copropriétés existantes relevant du DTG, du "
              "PPPT et de l'amiante en parties communes ; de l'autre, des opérations de "
              "démolition-reconstruction sur les emprises commerciales, qui appellent le "
              "repérage avant démolition et le diagnostic PEMD dès que les surfaces "
              "dépassent les seuils.",
        vigilance="Sur les opérations mixtes conservation-démolition, le périmètre du "
                  "repérage doit suivre le phasage réel, faute de quoi des zones "
                  "apparaissent hors périmètre en cours de chantier.",
        voisins=["arlac", "capeyron", "le-burck", "chemin-long"],
    ),
    dict(
        nom="Beutre", slug="beutre",
        intro="Au sud de Mérignac, aux abords de l'aéroport, Beutre garde un caractère "
              "pavillonnaire et semi-rural, mêlé à des zones d'activité et à des emprises "
              "aéroportuaires.",
        bati="Pavillonnaire des années 1950-1980, hangars, ateliers et bâtiments d'activité "
             "de la même période.",
        enjeu="Le tissu d'activité alimente des missions de repérage avant démolition et de "
              "diagnostic PEMD sur des ateliers et entrepôts anciens, tandis que le "
              "pavillonnaire relève du plomb et de l'amiante des dépendances lors des "
              "rénovations.",
        vigilance="Les bâtiments d'activité de cette période cumulent bardages et "
                  "couvertures en fibres-ciment : le métré d'amiante conditionne le budget "
                  "de déconstruction bien plus que le gros œuvre.",
        voisins=["chemin-long", "centre"],
    ),
    dict(
        nom="Chemin Long et l'aéroport", slug="chemin-long",
        intro="Secteur d'entreprises, de tertiaire et d'équipements autour de l'aéroport de "
              "Bordeaux-Mérignac et de la zone aéronautique, Chemin Long est un territoire "
              "de bâtiments d'activité en renouvellement.",
        bati="Bâtiments d'activité, entrepôts, bureaux et halls techniques allant des "
             "années 1960 à aujourd'hui.",
        enjeu="Territoire dominé par les opérations professionnelles : restructurations "
              "et démolitions de bâtiments tertiaires et industriels, où le repérage avant "
              "démolition et le diagnostic PEMD sont commandés par des maîtres d'ouvrage "
              "et des entreprises, avec des exigences de forme strictes pour l'annexion aux "
              "marchés.",
        vigilance="Sur marché privé comme public, le rapport doit être exploitable en pièce "
                  "annexe : quantitatifs par local, plans de repérage cotés et localisation "
                  "sans ambiguïté des matériaux.",
        voisins=["beutre", "centre"],
    ),
]

# --------------------------------------------------------------------------- Pessac
QUARTIERS_PESSAC = [
    dict(
        nom="Pessac Centre", slug="centre",
        intro="Le centre historique de Pessac associe échoppes, maisons de ville et "
              "copropriétés récentes, dans un secteur densifié par l'arrivée du tram B et "
              "les opérations du cœur de ville.",
        bati="Échoppes et pavillonnaire d'avant-guerre, immeubles de rapport des années "
             "1960-1990 et programmes neufs en béton le long des axes.",
        enjeu="Copropriétés de toutes générations : le bâti ancien relève du constat plomb "
              "des parties communes et de l'amiante des travaux d'après-guerre, tandis que "
              "les collectifs des années 1970-1990 concentrent l'amiante de second œuvre. "
              "Toutes les copropriétés d'habitation de plus de quinze ans sont désormais "
              "concernées par le plan pluriannuel de travaux.",
        vigilance="Les divisions d'échoppes en deux ou trois lots créent des "
                  "micro-copropriétés qui ignorent le plus souvent leurs obligations "
                  "techniques.",
        voisins=["alouette", "chataigneraie", "saige"],
    ),
    dict(
        nom="Saige", slug="saige",
        intro="Grand ensemble édifié dans les années 1960-1970, Saige-Formanoir aligne "
              "tours et barres de logements en copropriété et en parc social, et fait "
              "l'objet d'un renouvellement urbain engagé.",
        bati="Immeubles de grande hauteur en béton de la période 1965-1975, avec des "
             "campagnes de réhabilitation successives.",
        enjeu="Bâti construit au sommet de l'utilisation de l'amiante. Réhabilitation, "
              "remplacement de menuiseries, reprise de colonnes ou de chaufferie : chaque "
              "intervention impose un repérage avant travaux avec sondages destructifs, sur "
              "des immeubles occupés. Les copropriétés y mènent des plans pluriannuels de "
              "travaux lourds, à étaler sur dix ans.",
        vigilance="En site occupé et sur de grands linéaires, l'échantillonnage du repérage "
                  "doit être représentatif de chaque typologie de logement, sous peine d'un "
                  "rapport que les entreprises refuseront d'exploiter.",
        voisins=["centre", "haut-leveque"],
    ),
    dict(
        nom="Cité Frugès–Le Corbusier", slug="cite-fruges",
        intro="Les Quartiers Modernes Frugès, conçus par Le Corbusier et Pierre Jeanneret et "
              "édifiés vers 1924-1926, forment un ensemble de maisons en béton inscrit au "
              "patrimoine mondial de l'UNESCO.",
        bati="Maisons en béton armé de l'entre-deux-guerres, à l'architecture protégée, "
             "au sein d'un périmètre patrimonial strict.",
        enjeu="Un bâti d'avant-guerre au statut patrimonial exceptionnel : toute "
              "intervention se conçoit avec l'architecte des Bâtiments de France, et le "
              "repérage amiante comme le constat plomb doivent composer avec l'interdiction "
              "d'altérer les dispositions d'origine. La rénovation énergétique y est un "
              "exercice d'équilibre entre performance et conservation.",
        vigilance="L'étendue des sondages destructifs se négocie en amont avec les services "
                  "du patrimoine : sur ce type de bien, aucun prélèvement ne s'improvise.",
        voisins=["alouette", "centre"],
    ),
    dict(
        nom="Alouette", slug="alouette",
        intro="Au sud de Pessac, l'Alouette s'organise autour de sa gare et de la proximité "
              "du campus et de l'hôpital : pavillonnaire, résidences et petits collectifs.",
        bati="Pavillonnaire des années 1930-1980 et petits collectifs, avec des résidences "
             "étudiantes et des programmes récents près des équipements.",
        enjeu="Marché mixte de petites copropriétés et de résidences : le plan pluriannuel "
              "de travaux s'applique aux immeubles d'habitation de plus de quinze ans, et "
              "l'amiante de second œuvre se rencontre dans les collectifs des années "
              "1960-1990 dès qu'on intervient sur les parties communes.",
        vigilance="Les extensions et annexes des pavillons d'après-guerre portent "
                  "fréquemment des plaques et conduits en fibres-ciment amianté.",
        voisins=["centre", "cite-fruges", "haut-leveque"],
    ),
    dict(
        nom="Haut-Lévêque et Magonty", slug="haut-leveque",
        intro="Autour du site hospitalier du Haut-Lévêque et du campus, ce secteur de "
              "l'ouest pessacais mêle résidences, logements étudiants, pavillonnaire et "
              "équipements en renouvellement.",
        bati="Collectifs et résidences des années 1970-1990, pavillonnaire, et bâtiments "
             "hospitaliers et universitaires de la même période.",
        enjeu="Les collectifs et résidences de cette période relèvent du dossier technique "
              "amiante en parties communes et du plan pluriannuel de travaux. Les "
              "restructurations d'équipements hospitaliers et universitaires génèrent des "
              "missions de repérage avant travaux et avant démolition pour des maîtres "
              "d'ouvrage institutionnels.",
        vigilance="Sur les bâtiments techniques et de santé, les réseaux et locaux "
                  "techniques concentrent les calorifugeages : ce sont les premiers points "
                  "de contrôle avant toute intervention.",
        voisins=["saige", "alouette", "chataigneraie"],
    ),
    dict(
        nom="Châtaigneraie et Arago", slug="chataigneraie",
        intro="Quartiers résidentiels de l'est de Pessac, la Châtaigneraie et Arago "
              "alignent pavillonnaire, échoppes et petits collectifs dans un tissu calme "
              "proche de Talence.",
        bati="Pavillonnaire des années 1930-1980 et petits immeubles collectifs, avec "
             "quelques copropriétés de standing plus récentes.",
        enjeu="Copropriétés de taille modeste, souvent sans historique technique : le "
              "diagnostic technique global y comble un vide, et le plan pluriannuel de "
              "travaux s'impose désormais à tous les immeubles de plus de quinze ans. "
              "L'amiante de second œuvre apparaît lors des rénovations énergétiques.",
        vigilance="Les couvertures et conduits en fibres-ciment des dépendances sont le "
                  "point de vigilance récurrent du pavillonnaire de cette période.",
        voisins=["centre", "haut-leveque"],
    ),
]

# --------------------------------------------------------------------------- Talence
QUARTIERS_TALENCE = [
    dict(
        nom="Thouars", slug="thouars",
        intro="Au sud de Talence, Thouars est un grand ensemble des années 1960-1970, "
              "associant logements sociaux et copropriétés, engagé dans un renouvellement "
              "urbain de longue haleine.",
        bati="Barres et tours en béton de la période 1960-1975, avec des campagnes de "
             "réhabilitation successives et quelques résidentialisations récentes.",
        enjeu="Bâti construit au sommet de l'utilisation de l'amiante : chaque intervention "
              "— réhabilitation, menuiseries, colonnes, chaufferie — impose un repérage avant "
              "travaux avec sondages destructifs, sur des immeubles occupés. Les copropriétés "
              "y mènent des plans pluriannuels de travaux lourds, à étaler sur dix ans.",
        vigilance="En site occupé et sur de grands linéaires, l'échantillonnage du repérage "
                  "doit couvrir chaque typologie de logement, faute de quoi le rapport est "
                  "refusé par les entreprises.",
        voisins=["peixotto", "medoquine"],
    ),
    dict(
        nom="Peixotto et l'Université", slug="peixotto",
        intro="Autour du campus, Peixotto mêle résidences étudiantes, logements collectifs et "
              "échoppes, dans un secteur marqué par les équipements universitaires et "
              "hospitaliers.",
        bati="Résidences et collectifs en béton des années 1960-1985, échoppes en pierre, et "
             "bâtiments universitaires de la même période.",
        enjeu="Les résidences de cette période relèvent du dossier technique amiante en "
              "parties communes, souvent ancien et jamais réévalué. Les restructurations "
              "d'équipements universitaires génèrent des missions de repérage avant travaux et "
              "avant démolition pour des maîtres d'ouvrage institutionnels.",
        vigilance="Réseaux et locaux techniques des résidences concentrent les calorifugeages "
                  "amiantés : ce sont les premiers points de contrôle avant toute intervention.",
        voisins=["medoquine", "thouars"],
    ),
    dict(
        nom="La Médoquine et le centre", slug="medoquine",
        intro="Le centre de Talence et le secteur de la Médoquine alignent échoppes, maisons "
              "de ville et petits collectifs, densifiés par le tram et la proximité de "
              "Bordeaux.",
        bati="Échoppes et pavillonnaire d'avant-guerre, complétés d'immeubles de rapport des "
             "années 1960-1990 le long des axes.",
        enjeu="Beaucoup de micro-copropriétés issues de divisions d'échoppes, aujourd'hui "
              "toutes concernées par le plan pluriannuel de travaux. Le bâti antérieur à 1949 "
              "relève du constat plomb des parties communes, et l'amiante de second œuvre "
              "apparaît dès qu'on touche aux sols, conduits ou menuiseries.",
        vigilance="Les divisions d'échoppes en deux ou trois lots créent des copropriétés qui "
                  "ignorent le plus souvent leurs obligations techniques.",
        voisins=["peixotto", "thouars"],
    ),
]

# --------------------------------------------------------------------------- Bègles
QUARTIERS_BEGLES = [
    dict(
        nom="Terres Neuves", slug="terres-neuves",
        intro="Ancien quartier ouvrier et industriel au contact de Bordeaux, Terres Neuves "
              "s'est transformé autour d'une ZAC et de programmes neufs, tout en conservant "
              "des friches et des emprises en mutation.",
        bati="Entrepôts et ateliers des XIXe et XXe siècles, immeubles ouvriers, et "
             "programmes contemporains en béton livrés depuis les années 2000.",
        enjeu="Le tissu industriel résiduel alimente les missions de repérage avant démolition "
              "et de diagnostic PEMD, les surfaces dépassant largement les seuils, tandis que "
              "le faubourg ancien relève du plomb et du repérage avant travaux sur les "
              "opérations de rénovation.",
        vigilance="Sols potentiellement pollués sur les anciennes emprises : le repérage "
                  "amiante ne couvre pas ce risque et doit être articulé avec une étude de "
                  "sols menée par un bureau spécialisé.",
        voisins=["centre", "rives-d-arcins"],
    ),
    dict(
        nom="Centre et Mairie", slug="centre",
        intro="Le centre de Bègles, autour de la mairie et de l'église, aligne échoppes, "
              "maisons de ville et petites copropriétés dans un tissu ancien densifié.",
        bati="Échoppes et maisons en pierre d'avant-guerre, ponctuées de petits collectifs "
             "des années 1960-1990.",
        enjeu="Les copropriétés de taille modeste, souvent sans historique technique, sont "
              "toutes concernées par le plan pluriannuel de travaux. Le bâti antérieur à 1949 "
              "relève du constat plomb des parties communes, et l'amiante de second œuvre "
              "ressort lors des rénovations énergétiques.",
        vigilance="Les micro-copropriétés issues de divisions n'ont ni carnet d'entretien ni "
                  "diagnostic : le diagnostic technique global y est souvent le premier document "
                  "technique établi.",
        voisins=["terres-neuves", "rives-d-arcins"],
    ),
    dict(
        nom="Rives d'Arcins et la Garonne", slug="rives-d-arcins",
        intro="En bord de Garonne, Rives d'Arcins associe une vaste zone commerciale et des "
              "programmes de logements récents, dans un secteur en densification continue.",
        bati="Grandes surfaces commerciales et bâtiments d'activité, au contact de programmes "
             "résidentiels récents en béton.",
        enjeu="Territoire d'opérations professionnelles : démolitions et reconstructions "
              "d'emprises commerciales, où le repérage avant démolition et le diagnostic PEMD "
              "sont commandés par des maîtres d'ouvrage et des enseignes, avec des exigences de "
              "forme strictes pour l'annexion aux marchés.",
        vigilance="Sur ces bâtiments, le métré des bardages et couvertures en fibres-ciment "
                  "conditionne le budget de déconstruction bien plus que le gros œuvre.",
        voisins=["terres-neuves", "centre"],
    ),
]

# --------------------------------------------------------------------------- Le Bouscat
QUARTIERS_BOUSCAT = [
    dict(
        nom="Centre et Hôtel de Ville", slug="centre",
        intro="Le centre du Bouscat, autour de l'hôtel de ville et de l'avenue de la "
              "Libération, aligne immeubles bourgeois de pierre et copropriétés de standing.",
        bati="Pierre de taille, planchers bois et métalliques, toitures ardoise et zinc, avec "
             "quelques collectifs des années 1960-1980 en insertion.",
        enjeu="Copropriétés anciennes bien tenues mais coûteuses à entretenir — façades en "
              "pierre, toitures complexes, ascenseurs anciens. Le plan pluriannuel de travaux "
              "y a une vraie utilité budgétaire, les postes étant lourds et difficiles à "
              "absorber en appel de fonds exceptionnel.",
        vigilance="Les cages d'escalier antérieures à 1949 relèvent du constat plomb des "
                  "parties communes avant toute réfection de peinture, chantier très fréquent "
                  "dans ce quartier.",
        voisins=["champ-de-courses", "sainte-germaine"],
    ),
    dict(
        nom="Champ de Courses", slug="champ-de-courses",
        intro="Autour de l'hippodrome et de la barrière du Médoc, ce secteur résidentiel du "
              "Bouscat mêle échoppes doubles, pavillonnaire et petits collectifs.",
        bati="Échoppes et pavillonnaire des années 1930-1970, complétés de petits immeubles "
             "collectifs construits entre 1960 et 1990.",
        enjeu="Les petites copropriétés sont toutes concernées par le plan pluriannuel de "
              "travaux, et l'amiante de second œuvre se rencontre dans les collectifs des "
              "années 1960-1990 dès qu'on intervient sur les parties communes.",
        vigilance="Les dépendances et garages des maisons portent fréquemment des plaques de "
                  "couverture en fibres-ciment amianté, découvertes au moment de la dépose.",
        voisins=["centre", "sainte-germaine"],
    ),
    dict(
        nom="Sainte-Germaine et Ravezies", slug="sainte-germaine",
        intro="Au contact de Bordeaux et du pôle de Ravezies, Sainte-Germaine se densifie sous "
              "l'effet du tram, mêlant petits collectifs et programmes récents.",
        bati="Petits collectifs des années 1970-1990 et programmes contemporains en béton près "
             "de Ravezies, au contact du pavillonnaire.",
        enjeu="Les collectifs de cette période relèvent du dossier technique amiante en parties "
              "communes et du plan pluriannuel de travaux. Les rénovations énergétiques y "
              "déclenchent des repérages avant travaux sur les sols, conduits et menuiseries.",
        vigilance="Dalles et colles de sol des halls et caves, et calorifugeages des "
                  "chaufferies collectives, sont les premiers points de contrôle.",
        voisins=["centre", "champ-de-courses"],
    ),
]

# --------------------------------------------------------------------------- Cenon
QUARTIERS_CENON = [
    dict(
        nom="Palmer et les Hauts de Cenon", slug="palmer",
        intro="Sur les hauts de Cenon, le secteur Palmer est un grand ensemble engagé dans "
              "le renouvellement de la plaine rive droite, entre réhabilitations lourdes et "
              "opérations ponctuelles de démolition-reconstruction.",
        bati="Tours et barres en béton de la période 1960-1975, remaniées par des campagnes "
             "de réhabilitation successives.",
        enjeu="Double marché : sur le bâti conservé, chaque réhabilitation impose un repérage "
              "avant travaux avec sondages destructifs, sur des immeubles occupés ; sur les "
              "immeubles voués à disparaître, le repérage avant démolition et le diagnostic "
              "PEMD sont commandés par des bailleurs et des maîtres d'ouvrage publics.",
        vigilance="En site occupé, le plan de repérage se cale sur le calendrier de relogement "
                  "temporaire, sous peine de faire déraper le planning d'opération.",
        voisins=["la-maregue", "le-loret"],
    ),
    dict(
        nom="La Marègue", slug="la-maregue",
        intro="Quartier résidentiel de Cenon, la Marègue associe copropriétés des années "
              "1960-1980 et parc social, dans un tissu de collectifs desservi par le tram A.",
        bati="Collectifs en béton de la période 1960-1980, en copropriété ou en gestion "
             "mixte, avec des équipements communs d'origine.",
        enjeu="Les copropriétés de cette période concentrent les matériaux amiantés de second "
              "œuvre en parties communes — dalles de sol, colles, conduits, calorifugeages de "
              "chaufferie. Le dossier technique amiante y est obligatoire, souvent ancien et "
              "jamais réévalué, et toute rénovation énergétique déclenche un repérage avant "
              "travaux.",
        vigilance="Les chaufferies collectives sont le premier point de contrôle : c'est là "
                  "que se trouvent les calorifugeages dégradés et qu'interviennent les "
                  "entreprises de maintenance.",
        voisins=["palmer", "le-loret"],
    ),
    dict(
        nom="Le Loret et Beausite", slug="le-loret",
        intro="Sur les coteaux de Cenon, le Loret et Beausite gardent un caractère "
              "pavillonnaire, mêlé de petits collectifs, dans un relief marqué par la "
              "proximité du parc et de la Garonne.",
        bati="Pavillonnaire des années 1930-1980 et petits immeubles collectifs, sur un "
             "coteau exposé à l'humidité.",
        enjeu="Petites copropriétés désormais soumises au plan pluriannuel de travaux, "
              "pavillons anciens relevant du plomb, et amiante des dépendances lors des "
              "rénovations. Le relief et l'humidité des coteaux appellent souvent un état "
              "parasitaire.",
        vigilance="La mérule et les insectes xylophages attaquent les planchers bois du bâti "
                  "ancien sur ces coteaux humides : l'état parasitaire précède utilement "
                  "toute programmation de travaux.",
        voisins=["palmer", "la-maregue"],
    ),
]

# --------------------------------------------------------------------------- Lormont
QUARTIERS_LORMONT = [
    dict(
        nom="Génicart", slug="genicart",
        intro="Génicart est l'un des plus vastes grands ensembles de la métropole, au cœur "
              "d'un projet de renouvellement urbain d'ampleur, marqué par des démolitions et "
              "des reconstructions programmées.",
        bati="Barres et tours en béton de la période 1960-1975, en cours de transformation "
             "profonde depuis le milieu des années 2000.",
        enjeu="Le renouvellement urbain y concentre les missions de repérage avant démolition "
              "et de diagnostic PEMD, commandées par des bailleurs sociaux et des maîtres "
              "d'ouvrage publics, tandis que le bâti conservé relève du repérage avant travaux "
              "sur des réhabilitations occupées.",
        vigilance="Sur marché public, le rapport doit être exploitable en pièce annexe : "
                  "quantitatifs par local, plans de repérage cotés et localisation sans "
                  "ambiguïté des matériaux.",
        voisins=["carriet", "vieux-lormont"],
    ),
    dict(
        nom="Carriet", slug="carriet",
        intro="En bord de Garonne, Carriet est un grand ensemble des années 1960-1970 "
              "associant parc social et copropriétés, engagé dans des campagnes de "
              "réhabilitation.",
        bati="Immeubles en béton de la période 1960-1970, en gestion mixte, avec des "
             "équipements collectifs d'origine.",
        enjeu="Bâti construit au sommet de l'utilisation de l'amiante : réhabilitation, "
              "remplacement de menuiseries, reprise de colonnes ou de chaufferie imposent un "
              "repérage avant travaux avec sondages destructifs, sur des immeubles occupés. "
              "Les copropriétés y mènent des plans pluriannuels de travaux étalés sur dix ans.",
        vigilance="Sur de grands linéaires occupés, l'échantillonnage du repérage doit couvrir "
                  "chaque typologie de logement, faute de quoi le rapport est refusé par les "
                  "entreprises.",
        voisins=["genicart", "vieux-lormont"],
    ),
    dict(
        nom="Bas-Lormont et les coteaux", slug="vieux-lormont",
        intro="Le vieux bourg de Lormont et ses coteaux dominant la Garonne alignent maisons "
              "de pierre anciennes, échoppes et petits immeubles, dans un relief patrimonial "
              "et humide.",
        bati="Bâti en pierre majoritairement antérieur à 1949, planchers bois, sur des "
             "coteaux exposés aux remontées d'humidité.",
        enjeu="Le bâti ancien relève du constat plomb des parties communes et de l'amiante des "
              "travaux d'après-guerre, tandis que l'humidité des coteaux favorise la mérule. "
              "Les petites copropriétés du bourg sont désormais toutes soumises au plan "
              "pluriannuel de travaux.",
        vigilance="Sur ce bâti ancien et humide, l'état parasitaire — mérule et insectes "
                  "xylophages en pied de mur — précède toute programmation de travaux.",
        voisins=["genicart", "carriet"],
    ),
]

# --------------------------------------------------------------------------- Villenave-d'Ornon
QUARTIERS_VILLENAVE = [
    dict(
        nom="Le Bourg", slug="le-bourg",
        intro="Le bourg ancien de Villenave-d'Ornon, autour de la mairie et de l'église, "
              "se densifie : échoppes et maisons de ville côtoient des programmes collectifs "
              "récents le long des axes.",
        bati="Échoppes et maisons en pierre d'avant-guerre, complétées d'immeubles récents "
             "en béton livrés ces quinze dernières années.",
        enjeu="Petites copropriétés anciennes désormais soumises au plan pluriannuel de "
              "travaux, bâti antérieur à 1949 relevant du constat plomb des parties communes, "
              "et amiante de second œuvre lors des rénovations. Les collectifs neufs, eux, "
              "entrent progressivement dans le champ des obligations.",
        vigilance="Les micro-copropriétés issues de divisions manquent de carnet d'entretien "
                  "et de diagnostic : le diagnostic technique global y comble un vide.",
        voisins=["sarcignan", "pont-de-la-maye"],
    ),
    dict(
        nom="Sarcignan", slug="sarcignan",
        intro="Au sud de la commune, Sarcignan est un secteur résidentiel de pavillons et de "
              "résidences, dans un tissu calme en développement continu.",
        bati="Pavillonnaire des années 1960-1990 et petites résidences collectives, avec des "
             "programmes récents près des équipements.",
        enjeu="Les résidences et petites copropriétés des années 1970-1990 relèvent du dossier "
              "technique amiante en parties communes et du plan pluriannuel de travaux. "
              "L'amiante de second œuvre ressort dès qu'on intervient sur les sols, conduits "
              "ou menuiseries.",
        vigilance="Les dépendances et garages des pavillons portent fréquemment des plaques "
                  "de couverture en fibres-ciment amianté, découvertes à la dépose.",
        voisins=["le-bourg", "pont-de-la-maye"],
    ),
    dict(
        nom="Le Pont-de-la-Maye", slug="pont-de-la-maye",
        intro="Le long de la route de Toulouse, le Pont-de-la-Maye est un secteur commerçant "
              "et d'activité, ponctué de collectifs et d'emprises en restructuration.",
        bati="Commerces, petits collectifs et bâtiments d'activité des années 1960-1990, au "
             "contact de programmes résidentiels récents.",
        enjeu="Double marché : des copropriétés relevant du DTG, du PPPT et de l'amiante en "
              "parties communes ; et des restructurations d'emprises commerciales et "
              "d'activité, qui appellent le repérage avant démolition et le diagnostic PEMD "
              "dès que les surfaces dépassent les seuils.",
        vigilance="Sur les bâtiments d'activité, le métré des bardages et couvertures en "
                  "fibres-ciment conditionne le budget de déconstruction plus que le gros œuvre.",
        voisins=["le-bourg", "sarcignan"],
    ),
]

# --------------------------------------------------------------------------- Gradignan
QUARTIERS_GRADIGNAN = [
    dict(
        nom="Centre et Barthez", slug="centre",
        intro="Le centre de Gradignan, autour de la mairie et du parc de Mandavit, aligne "
              "échoppes, maisons de ville et petites copropriétés dans un cadre verdoyant.",
        bati="Échoppes et maisons en pierre d'avant-guerre, complétées de petits collectifs "
             "des années 1960-1990.",
        enjeu="Copropriétés de taille modeste, souvent sans historique technique, toutes "
              "concernées par le plan pluriannuel de travaux. Le bâti antérieur à 1949 relève "
              "du constat plomb des parties communes, et l'amiante de second œuvre apparaît "
              "lors des rénovations énergétiques.",
        vigilance="Sur ces micro-copropriétés, le diagnostic technique global est souvent le "
                  "premier document technique jamais établi sur l'immeuble.",
        voisins=["malartic", "cayac"],
    ),
    dict(
        nom="Malartic", slug="malartic",
        intro="Proche du campus et des équipements, Malartic mêle résidences, logements "
              "étudiants et pavillonnaire, dans un secteur en renouvellement.",
        bati="Résidences et collectifs des années 1970-1990, pavillonnaire, et bâtiments "
             "d'enseignement de la même période.",
        enjeu="Les résidences de cette période relèvent du dossier technique amiante en "
              "parties communes et du plan pluriannuel de travaux. Les restructurations "
              "d'équipements génèrent des missions de repérage avant travaux pour des maîtres "
              "d'ouvrage institutionnels.",
        vigilance="Réseaux et locaux techniques des résidences concentrent les calorifugeages "
                  "amiantés : ce sont les premiers points de contrôle.",
        voisins=["centre", "cayac"],
    ),
    dict(
        nom="Cayac et Monjous", slug="cayac",
        intro="Au sud de Gradignan, le long de l'Eau Bourde, Cayac et Monjous gardent un "
              "caractère pavillonnaire et boisé, en lisière de forêt.",
        bati="Pavillonnaire des années 1950-1980, sur un secteur humide traversé par l'Eau "
             "Bourde.",
        enjeu="Pavillons anciens relevant du plomb, amiante des dépendances lors des "
              "rénovations, et petites copropriétés soumises au plan pluriannuel de travaux. "
              "La proximité de la rivière et l'humidité appellent souvent un état parasitaire.",
        vigilance="La mérule et les insectes xylophages attaquent les planchers bois du bâti "
                  "ancien en secteur humide : l'état parasitaire précède toute programmation.",
        voisins=["centre", "malartic"],
    ),
]

# --------------------------------------------------------------------------- Floirac
QUARTIERS_FLOIRAC = [
    dict(
        nom="Dravemont", slug="dravemont",
        intro="Sur les hauts de Floirac, Dravemont est un grand ensemble des années 1960-1970 "
              "engagé dans un renouvellement urbain de longue haleine, mêlant parc social et "
              "copropriétés.",
        bati="Barres et tours en béton de la période 1960-1975, remaniées par des campagnes "
             "de réhabilitation successives.",
        enjeu="Bâti construit au sommet de l'utilisation de l'amiante : chaque réhabilitation "
              "impose un repérage avant travaux avec sondages destructifs, sur des immeubles "
              "occupés, tandis que les immeubles voués à disparaître appellent le repérage "
              "avant démolition et le diagnostic PEMD.",
        vigilance="En site occupé, le plan de repérage se cale sur le calendrier de relogement "
                  "temporaire, faute de quoi le planning d'opération dérive.",
        voisins=["les-coteaux", "garonne-eiffel"],
    ),
    dict(
        nom="Les Coteaux et le Bourg", slug="les-coteaux",
        intro="Le vieux bourg de Floirac et ses coteaux dominant la Garonne alignent maisons "
              "de pierre anciennes et échoppes, dans un relief patrimonial et humide.",
        bati="Bâti en pierre majoritairement antérieur à 1949, planchers bois, sur des coteaux "
             "exposés aux remontées d'humidité.",
        enjeu="Le bâti ancien relève du constat plomb des parties communes et de l'amiante des "
              "travaux d'après-guerre, tandis que l'humidité des coteaux favorise la mérule. "
              "Les petites copropriétés du bourg sont désormais soumises au plan pluriannuel "
              "de travaux.",
        vigilance="Sur ce bâti ancien et humide, l'état parasitaire — mérule et insectes "
                  "xylophages en pied de mur — précède toute programmation de travaux.",
        voisins=["dravemont", "garonne-eiffel"],
    ),
    dict(
        nom="Garonne-Eiffel", slug="garonne-eiffel",
        intro="En bord de fleuve, le secteur Garonne-Eiffel est une vaste opération "
              "d'aménagement sur d'anciennes emprises ferroviaires et industrielles, mêlant "
              "friches et programmes neufs.",
        bati="Friches industrielles et ferroviaires du XXe siècle, et immeubles contemporains "
             "en béton livrés depuis le milieu des années 2010.",
        enjeu="Densité de démolitions et de restructurations : le repérage avant démolition et "
              "le diagnostic PEMD y sont requis sur presque toutes les opérations, commandés "
              "par des aménageurs et des promoteurs, avec des exigences de forme strictes pour "
              "l'annexion aux marchés.",
        vigilance="Sols potentiellement pollués sur les anciennes emprises : le repérage "
                  "amiante ne couvre pas ce risque et doit être articulé avec une étude de "
                  "sols menée par un bureau spécialisé.",
        voisins=["dravemont", "les-coteaux"],
    ),
]

# Villes hors Bordeaux disposant d'un découpage par quartier (mêmes gabarits).
QUARTIERS_PAR_VILLE = [
    dict(nom="Mérignac", slug="merignac", quartiers=QUARTIERS_MERIGNAC),
    dict(nom="Pessac", slug="pessac", quartiers=QUARTIERS_PESSAC),
    dict(nom="Talence", slug="talence", quartiers=QUARTIERS_TALENCE),
    dict(nom="Bègles", slug="begles", quartiers=QUARTIERS_BEGLES),
    dict(nom="Le Bouscat", slug="le-bouscat", quartiers=QUARTIERS_BOUSCAT),
    dict(nom="Cenon", slug="cenon", quartiers=QUARTIERS_CENON),
    dict(nom="Lormont", slug="lormont", quartiers=QUARTIERS_LORMONT),
    dict(nom="Villenave-d'Ornon", slug="villenave-d-ornon", quartiers=QUARTIERS_VILLENAVE),
    dict(nom="Gradignan", slug="gradignan", quartiers=QUARTIERS_GRADIGNAN),
    dict(nom="Floirac", slug="floirac", quartiers=QUARTIERS_FLOIRAC),
]
