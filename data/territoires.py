# -*- coding: utf-8 -*-
"""
TERRITOIRES NON OCCUPÉS PAR LE SITE A.

Le site existant ne publie de pages communales que sur une poignée de communes
de la métropole (Bordeaux, Eysines, Le Haillan, Lormont, Blanquefort,
Saint-Médard-en-Jalles, Mérignac, Le Taillan-Médoc). Tout le reste est vide :
bassin d'Arcachon, Libournais, Sud-Gironde, Médoc, et l'intégralité des Landes.

C'est là que le second site prend du terrain sans jamais croiser le premier.
"""

GIRONDE_ELARGIE = [
    dict(
        nom="Arcachon", slug="arcachon", cp="33120", insee="33009", dept="33",
        quartiers=["Ville d'Hiver", "Ville d'Été", "Le Moulleau", "Pereire", "L'Aiguillon"],
        parc="Arcachon est dominée par les villas de la Ville d'Hiver, bâties entre 1860 et "
             "1900, et par un parc de résidences collectives balnéaires construites entre "
             "1960 et 1985 en front de mer.",
        enjeu="Les copropriétés balnéaires cumulent exposition saline, occupation "
              "saisonnière et charges élevées : le plan pluriannuel de travaux y est "
              "structurellement chargé sur les façades et les menuiseries. Les villas "
              "protégées imposent un arbitrage préalable sur les sondages destructifs.",
        voisins=["la-teste-de-buch", "gujan-mestras", "lege-cap-ferret"],
    ),
    dict(
        nom="La Teste-de-Buch", slug="la-teste-de-buch", cp="33260", insee="33529", dept="33",
        quartiers=["Cazaux", "Pyla-sur-Mer", "Centre", "Le Courbey"],
        parc="Commune la plus étendue du bassin, La Teste-de-Buch associe un centre ancien, "
             "les résidences du Pyla, le village de Cazaux et de vastes zones "
             "pavillonnaires et d'activité.",
        enjeu="Le parc collectif du Pyla, largement antérieur à 1997, concentre dalles de "
              "sol et conduits amiantés. Sur les zones d'activité, les opérations de "
              "reconstruction après sinistre relèvent du repérage avant démolition.",
        voisins=["arcachon", "gujan-mestras", "biganos"],
    ),
    dict(
        nom="Gujan-Mestras", slug="gujan-mestras", cp="33470", insee="33199", dept="33",
        quartiers=["La Hume", "Meyran", "Le Teich-Ouest", "Les Ports ostréicoles"],
        parc="Gujan-Mestras s'organise autour de ses sept ports ostréicoles, avec un bâti "
             "de cabanes, un pavillonnaire des années 1970-1990 et des résidences de "
             "tourisme récentes.",
        enjeu="Bâti technique portuaire ancien et hangars ostréicoles : couvertures en "
              "fibres-ciment très fréquentes, souvent démolies sans repérage préalable.",
        voisins=["la-teste-de-buch", "biganos", "arcachon"],
    ),
    dict(
        nom="Andernos-les-Bains", slug="andernos-les-bains", cp="33510", insee="33005", dept="33",
        quartiers=["Le Bétey", "Mauret", "Centre", "Le Coulin"],
        parc="Station balnéaire du bassin nord, Andernos-les-Bains présente un parc de "
             "villas de villégiature et de petites copropriétés construites entre 1960 et "
             "1990, complété par des programmes neufs.",
        enjeu="Forte proportion de résidences secondaires en copropriété de moins de "
              "50 lots : toutes dans le champ du plan pluriannuel de travaux, avec des "
              "conseils syndicaux souvent peu disponibles et un besoin d'accompagnement "
              "en assemblée.",
        voisins=["lege-cap-ferret", "biganos"],
    ),
    dict(
        nom="Lège-Cap-Ferret", slug="lege-cap-ferret", cp="33950", insee="33236", dept="33",
        quartiers=["Le Cap-Ferret", "Claouey", "Piraillan", "Petit Piquey", "Lège"],
        parc="Étirée sur toute la presqu'île, la commune associe cabanes ostréicoles, "
             "villas de villégiature et petits collectifs de villages, avec très peu de "
             "grands ensembles.",
        enjeu="Bâti dispersé et accès contraints : la logistique d'intervention pèse autant "
              "que la mission elle-même. Les constructions balnéaires des années 1960-1990 "
              "recèlent fréquemment des plaques de couverture et des cloisons amiantées.",
        voisins=["andernos-les-bains", "arcachon"],
    ),
    dict(
        nom="Biganos", slug="biganos", cp="33380", insee="33051", dept="33",
        quartiers=["Facture", "Le Bourg", "Lamothe"],
        parc="Biganos combine le bourg ancien, le quartier industriel et ferroviaire de "
             "Facture avec sa cité ouvrière, et une urbanisation pavillonnaire récente.",
        enjeu="La cité ouvrière et le patrimoine industriel de Facture constituent un "
              "gisement classique de matériaux amiantés en couverture et en calorifugeage, "
              "sur des bâtiments régulièrement restructurés.",
        voisins=["gujan-mestras", "la-teste-de-buch", "andernos-les-bains"],
    ),
    dict(
        nom="Libourne", slug="libourne", cp="33500", insee="33243", dept="33",
        quartiers=["Centre bastide", "Les Dagueys", "Peyanne", "La Vieille Église"],
        parc="Bastide médiévale au bâti de pierre très ancien, Libourne comprend aussi des "
             "ensembles collectifs des années 1960-1970 et un patrimoine militaire "
             "reconverti.",
        enjeu="Le centre bastide antérieur à 1949 cumule risque plomb et amiante des "
              "travaux ultérieurs. Les opérations de renouvellement urbain sur les "
              "quartiers collectifs génèrent des missions de repérage avant démolition "
              "de volume significatif.",
        voisins=["saint-andre-de-cubzac"],
    ),
    dict(
        nom="Saint-André-de-Cubzac", slug="saint-andre-de-cubzac", cp="33240", insee="33366", dept="33",
        quartiers=["Centre", "Le Pas de Rauzet", "Cubzac-les-Ponts"],
        parc="Ville-carrefour du nord Gironde, au bâti de bourg ancien complété par des "
             "lotissements des années 1970-2000 et des zones d'activité en croissance.",
        enjeu="Copropriétés de taille moyenne construites entre 1975 et 1995, arrivant "
              "toutes au premier cycle de gros entretien sans historique technique.",
        voisins=["libourne", "blaye"],
    ),
    dict(
        nom="Langon", slug="langon", cp="33210", insee="33227", dept="33",
        quartiers=["Centre", "Les Allées", "Toucaut"],
        parc="Sous-préfecture du Sud-Gironde, Langon présente un centre ancien dense, des "
             "immeubles de rapport du XIXe siècle et des ensembles collectifs des années "
             "1960-1980.",
        enjeu="Les immeubles de rapport anciens en copropriété, souvent en division "
              "successive, cumulent plomb, amiante des travaux d'après-guerre et absence "
              "totale de programmation de travaux.",
        voisins=["podensac"],
    ),
    dict(
        nom="Cestas", slug="cestas", cp="33610", insee="33122", dept="33",
        quartiers=["Gazinet", "Le Bourg", "Toctoucau", "Réjouit"],
        parc="Très étendue sur la lande, Cestas est majoritairement pavillonnaire, avec "
             "d'importantes zones logistiques et industrielles le long de l'A63.",
        enjeu="Le parc logistique et industriel antérieur à 1997 est le principal enjeu : "
              "bardages, couvertures et dalles amiantées sur des bâtiments régulièrement "
              "démolis ou reconvertis.",
        voisins=["leognan", "canejan"],
    ),
    dict(
        nom="Léognan", slug="leognan", cp="33850", insee="33238", dept="33",
        quartiers=["Le Bourg", "Gaillardin", "Lacanau-de-Mios"],
        parc="Commune viticole des Graves, Léognan associe châteaux et chais, un bourg "
             "ancien et un pavillonnaire résidentiel développé depuis les années 1970.",
        enjeu="Le patrimoine viticole — chais, cuveries, dépendances — concentre des "
              "couvertures en fibres-ciment rarement repérées avant démolition ou "
              "réfection.",
        voisins=["cestas", "canejan"],
    ),
    dict(
        nom="Canéjan", slug="canejan", cp="33610", insee="33090", dept="33",
        quartiers=["Le Bourg", "Cantelaude", "Migelane"],
        parc="Canéjan mêle un bourg ancien, un pavillonnaire des années 1970-1990 et une "
             "zone d'activité tournée vers l'artisanat.",
        enjeu="Petites copropriétés et locaux d'activité antérieurs à 1997 : le repérage "
              "avant travaux y est systématiquement omis lors des rénovations "
              "énergétiques financées.",
        voisins=["cestas", "leognan"],
    ),
    dict(
        nom="Blaye", slug="blaye", cp="33390", insee="33058", dept="33",
        quartiers=["La Citadelle", "Centre", "Le Port"],
        parc="Blaye est structurée par sa citadelle classée au patrimoine mondial, un "
             "centre ancien de pierre et un habitat de bourg largement antérieur à 1949.",
        enjeu="Bâti protégé et très ancien : le plomb est structurel, l'amiante se loge "
              "dans les interventions d'après-guerre. Toute mission suppose un arbitrage "
              "préalable avec l'architecte des Bâtiments de France.",
        voisins=["saint-andre-de-cubzac"],
    ),
    dict(
        nom="Podensac", slug="podensac", cp="33720", insee="33328", dept="33",
        quartiers=["Le Bourg", "Les Quais"],
        parc="Bourg viticole des Graves, au bâti ancien de centre et aux dépendances "
             "agricoles nombreuses, complété par des lotissements récents.",
        enjeu="Dépendances viticoles et bâtiments agricoles en fin de vie : démolitions "
              "fréquentes, repérage préalable presque jamais réalisé.",
        voisins=["langon"],
    ),
]

LANDES = [
    dict(
        nom="Mont-de-Marsan", slug="mont-de-marsan", cp="40000", insee="40192", dept="40",
        quartiers=["Le Peyrouat", "Saint-Médard", "Centre", "Nonères", "La Moustey"],
        parc="Préfecture des Landes, Mont-de-Marsan associe un centre ancien de pierre "
             "coquillière, le grand ensemble du Peyrouat construit dans les années 1960, "
             "et un important patrimoine militaire.",
        enjeu="Le renouvellement urbain du Peyrouat et la reconversion de patrimoine "
              "militaire génèrent des missions de repérage avant démolition sur des "
              "volumes importants. Le parc collectif des années 1960-1970 entre "
              "simultanément dans le champ du plan pluriannuel de travaux.",
        voisins=["saint-pierre-du-mont", "morcenx"],
    ),
    dict(
        nom="Dax", slug="dax", cp="40100", insee="40088", dept="40",
        quartiers=["Le Sablar", "Cuyès", "Le Gond", "Centre thermal"],
        parc="Première ville thermale de France, Dax présente une densité exceptionnelle "
             "d'établissements thermaux et de résidences de cure construits entre 1950 et "
             "1985, aux côtés d'un centre ancien.",
        enjeu="Le parc thermal et les résidences de cure sont le sujet dominant : "
              "bâtiments techniques, réseaux de fluides calorifugés et dalles de sol "
              "amiantées, sur des immeubles rénovés en continu et en site occupé. "
              "Rares sont les diagnostiqueurs positionnés sur ce segment.",
        voisins=["saint-paul-les-dax", "narrosse"],
    ),
    dict(
        nom="Saint-Paul-lès-Dax", slug="saint-paul-les-dax", cp="40990", insee="40279", dept="40",
        quartiers=["Le Lac", "Christus", "Centre", "Lesbazeilles"],
        parc="Commune thermale jumelle de Dax, Saint-Paul-lès-Dax concentre des résidences "
             "de cure et des copropriétés de tourisme autour du lac de Christus, bâties "
             "principalement entre 1970 et 1990.",
        enjeu="Copropriétés de tourisme à forte rotation et à gouvernance dispersée : "
              "le plan pluriannuel de travaux y est difficile à faire voter, ce qui "
              "suppose une présentation en assemblée générale et un chiffrage lisible.",
        voisins=["dax", "narrosse"],
    ),
    dict(
        nom="Biscarrosse", slug="biscarrosse", cp="40600", insee="40046", dept="40",
        quartiers=["Biscarrosse-Plage", "Navarrosse", "Le Bourg", "Ispe"],
        parc="Biscarrosse se partage entre un bourg landais, la station balnéaire de "
             "Biscarrosse-Plage et les rives des lacs, avec un parc de résidences de "
             "tourisme construites entre 1965 et 1995.",
        enjeu="Résidences secondaires en copropriété, exposition saline et occupation "
              "saisonnière : les travaux ne peuvent être planifiés qu'hors saison, ce qui "
              "impose une programmation décennale précise plutôt que des urgences.",
        voisins=["parentis-en-born", "mimizan"],
    ),
    dict(
        nom="Capbreton", slug="capbreton", cp="40130", insee="40065", dept="40",
        quartiers=["Le Port", "La Pointe", "Centre", "Les Deux Pins"],
        parc="Station portuaire dense, Capbreton présente un parc de copropriétés "
             "balnéaires très serré, construit pour l'essentiel entre 1965 et 1990 en "
             "front de mer et autour du port.",
        enjeu="Densité de copropriétés parmi les plus fortes des Landes, avec des façades "
              "exposées et des menuiseries en fin de cycle. Le triptyque façade-menuiserie-"
              "étanchéité domine les plans pluriannuels.",
        voisins=["soorts-hossegor", "labenne"],
    ),
    dict(
        nom="Soorts-Hossegor", slug="soorts-hossegor", cp="40150", insee="40304", dept="40",
        quartiers=["Le Lac", "La Plage", "Soorts", "Le Golf"],
        parc="Hossegor est marquée par ses villas basco-landaises des années 1920-1930, "
             "classées pour partie, et par des résidences collectives balnéaires plus "
             "récentes autour du lac et du golf.",
        enjeu="Villas patrimoniales antérieures à 1949 : plomb systématique, et amiante "
              "issue des rénovations d'après-guerre. Les contraintes patrimoniales "
              "conditionnent l'étendue des sondages destructifs.",
        voisins=["capbreton", "seignosse"],
    ),
    dict(
        nom="Seignosse", slug="seignosse", cp="40510", insee="40296", dept="40",
        quartiers=["Le Penon", "Les Bourdaines", "Le Bourg", "Estagnots"],
        parc="Seignosse-Océan est une station créée dans les années 1960-1970 par la "
             "Mission d'aménagement de la côte aquitaine, avec un parc collectif homogène "
             "de cette période.",
        enjeu="Station intégralement construite dans la période de plus forte utilisation "
              "de l'amiante : dalles, colles, conduits et bardages sont présumés présents "
              "sur l'ensemble du parc collectif tant qu'un repérage ne l'a pas infirmé.",
        voisins=["soorts-hossegor", "soustons"],
    ),
    dict(
        nom="Soustons", slug="soustons", cp="40140", insee="40306", dept="40",
        quartiers=["Le Bourg", "Soustons-Plage", "Le Lac", "Port d'Albret"],
        parc="Soustons associe un bourg landais traditionnel, un secteur lacustre "
             "résidentiel et la station de Soustons-Plage développée à partir des "
             "années 1970.",
        enjeu="Mélange de bâti traditionnel landais à colombages et de collectif "
              "balnéaire des années 1970 : deux logiques de repérage très différentes "
              "sur une même commune.",
        voisins=["seignosse", "vieux-boucau"],
    ),
    dict(
        nom="Tarnos", slug="tarnos", cp="40220", insee="40312", dept="40",
        quartiers=["Le Bourg", "La Zone industrielle", "Tarnos-Plage"],
        parc="Commune la plus industrielle des Landes, Tarnos accueille une vaste zone "
             "d'activité métallurgique et aéronautique, avec des cités ouvrières et un "
             "habitat collectif des années 1950-1970.",
        enjeu="Territoire à dominante industrielle : les opérations de maintenance, de "
              "restructuration et de démantèlement relèvent du repérage avant travaux au "
              "sens du code du travail, avec des exigences de coordination renforcées.",
        voisins=["labenne", "ondres"],
    ),
    dict(
        nom="Labenne", slug="labenne", cp="40530", insee="40142", dept="40",
        quartiers=["Le Bourg", "Labenne-Océan"],
        parc="Labenne combine un bourg en forte croissance démographique et la station de "
             "Labenne-Océan, avec un parc résidentiel majoritairement postérieur à 1975.",
        enjeu="Croissance rapide et copropriétés récentes en majorité : la demande porte "
              "surtout sur le plan pluriannuel de travaux des programmes des années "
              "1985-2005, désormais tous concernés.",
        voisins=["capbreton", "tarnos", "ondres"],
    ),
    dict(
        nom="Mimizan", slug="mimizan", cp="40200", insee="40177", dept="40",
        quartiers=["Mimizan-Plage", "Le Bourg", "La Papeterie", "Aureilhan"],
        parc="Mimizan est structurée par son usine papetière historique, un bourg landais "
             "et la station de Mimizan-Plage développée entre 1960 et 1990.",
        enjeu="Coexistence rare d'un site industriel majeur et d'un parc balnéaire "
              "collectif : les deux régimes de repérage, industriel et bâtiment, se "
              "rencontrent sur un même territoire.",
        voisins=["parentis-en-born", "biscarrosse"],
    ),
    dict(
        nom="Parentis-en-Born", slug="parentis-en-born", cp="40160", insee="40219", dept="40",
        quartiers=["Le Bourg", "Le Lac", "Les Sables"],
        parc="Parentis-en-Born associe un bourg landais, un site pétrolier historique et "
             "un secteur résidentiel et touristique autour de l'étang.",
        enjeu="Installations techniques du site pétrolier et bâti agricole ancien : "
              "couvertures en fibres-ciment et calorifugeages sont les matériaux "
              "récurrents avant toute intervention.",
        voisins=["biscarrosse", "mimizan"],
    ),
    dict(
        nom="Saint-Vincent-de-Tyrosse", slug="saint-vincent-de-tyrosse", cp="40230", insee="40282", dept="40",
        quartiers=["Le Bourg", "La Gare", "Cabanes"],
        parc="Ville-carrefour du sud des Landes, Saint-Vincent-de-Tyrosse mêle bâti de "
             "bourg ancien, lotissements des années 1970-1990 et zones d'activité.",
        enjeu="Petites copropriétés de moins de 50 lots et locaux d'activité antérieurs "
              "à 1997 : deux segments largement sous-équipés en programmation de travaux.",
        voisins=["soustons", "capbreton"],
    ),
    dict(
        nom="Saint-Pierre-du-Mont", slug="saint-pierre-du-mont", cp="40280", insee="40281", dept="40",
        quartiers=["Le Bourg", "Bosquet", "Les Arènes"],
        parc="Commune limitrophe de Mont-de-Marsan, à dominante pavillonnaire avec "
             "quelques ensembles collectifs des années 1970 et des zones commerciales.",
        enjeu="Le collectif des années 1970 y arrive en fin de premier cycle : "
              "menuiseries, réseaux et toitures constituent l'essentiel des plans "
              "pluriannuels à établir.",
        voisins=["mont-de-marsan"],
    ),
]

TOUS_TERRITOIRES = GIRONDE_ELARGIE + LANDES
