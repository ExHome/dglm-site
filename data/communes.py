# -*- coding: utf-8 -*-
"""
Données locales — Bordeaux Métropole (28 communes).

Chaque commune porte un contenu RÉELLEMENT différenciant :
- `parc`      : typologie dominante du bâti (déterminante pour l'amiante / le plomb)
- `enjeu`     : pourquoi RAAT/RAAD/DTG/PPPT s'y posent différemment d'ailleurs
- `quartiers` : ancrage micro-local (requêtes longue traîne)
- `voisins`   : maillage interne géographique

Aucun chiffre inventé : uniquement des typologies vérifiables.
"""

COMMUNES = [
    dict(
        nom="Bordeaux", slug="bordeaux", cp="33000", insee="33063",
        quartiers=["Chartrons", "Saint-Michel", "Nansouty", "Bacalan",
                   "Caudéran", "Saint-Augustin", "Bassins à flot", "Belcier"],
        parc="Bordeaux concentre trois parcs très différents : l'immeuble de pierre "
             "des XVIIIe et XIXe siècles du secteur UNESCO, l'échoppe bordelaise en "
             "R+0 ou R+1 des faubourgs, et les opérations de reconstruction des "
             "années 1950 à 1980 sur Belcier, Bacalan ou la Bastide.",
        enjeu="Le bâti antérieur à 1949 impose de traiter conjointement le plomb et "
              "l'amiante des interventions ultérieures : dans une échoppe restructurée "
              "dans les années 1970, les colles de carrelage, les enduits de rebouchage "
              "et les conduits sont les points durs. En secteur sauvegardé, le repérage "
              "doit composer avec les contraintes ABF, ce qui interdit les sondages "
              "destructifs improvisés.",
        voisins=["le-bouscat", "talence", "begles", "bruges", "cenon", "floirac"],
    ),
    dict(
        nom="Mérignac", slug="merignac", cp="33700", insee="33281",
        quartiers=["Capeyron", "Arlac", "Beaudésert", "Beutre", "Chemin Long", "Le Burck"],
        parc="Deuxième commune de la métropole, Mérignac associe un très large "
             "pavillonnaire des années 1960-1980, les grands ensembles du Burck et de "
             "Beaudésert, et l'un des plus vastes tissus d'activité de Gironde autour "
             "de l'aéroport et de la zone aéronautique.",
        enjeu="Sur les grands ensembles du Burck et de Beaudésert, les réhabilitations "
              "lourdes déclenchent RAAT et RAAD sur des volumes qui exigent une "
              "organisation de chantier réelle. Le très large pavillonnaire des années "
              "1960-1980 alimente un flux continu de repérages avant travaux : dalles de "
              "sol, colles et joints de menuiserie d'avant juillet 1997.",
        voisins=["pessac", "le-haillan", "eysines", "martignas-sur-jalle", "bordeaux"],
    ),
    dict(
        nom="Pessac", slug="pessac", cp="33600", insee="33318",
        quartiers=["Saige", "Alouette", "Cité Frugès", "Toctoucau", "Compostelle"],
        parc="Pessac superpose la Cité Frugès de Le Corbusier, classée au patrimoine "
             "mondial, les résidences universitaires du campus, les tours et barres de "
             "Saige-Formanoir, et un pavillonnaire diffus très étendu vers Toctoucau.",
        enjeu="Le parc étudiant et social des années 1960-1970 est le cœur du sujet : "
              "réhabilitations énergétiques en site occupé, donc repérage avant travaux "
              "systématique et phasage strict. Sur le patrimoine protégé, tout sondage "
              "destructif doit être arbitré en amont avec la maîtrise d'ouvrage.",
        voisins=["merignac", "talence", "gradignan", "canejan-hors-metropole", "bordeaux"],
    ),
    dict(
        nom="Talence", slug="talence", cp="33400", insee="33522",
        quartiers=["Thouars", "Le Domaine Universitaire", "Centre", "Raba"],
        parc="Talence est marquée par le domaine universitaire, un parc de résidences "
             "collectives des années 1960-1970 très dense, le grand ensemble de Thouars "
             "et un tissu d'échoppes et de maisons de ville en limite de Bordeaux.",
        enjeu="Fort volume de copropriétés de plus de 15 ans, souvent avec chauffage "
              "collectif d'origine : le PPPT y arrive avec des enjeux de calorifugeage "
              "et de réseaux qui appellent un repérage amiante avant toute intervention "
              "sur les gaines techniques.",
        voisins=["bordeaux", "pessac", "gradignan", "begles", "villenave-d-ornon"],
    ),
    dict(
        nom="Villenave-d'Ornon", slug="villenave-d-ornon", cp="33140", insee="33550",
        quartiers=["Chambéry", "Sarcignan", "Courréjean", "Le Bocage"],
        parc="Commune en croissance rapide, Villenave-d'Ornon mêle un pavillonnaire "
             "des années 1970-1980, des copropriétés de taille moyenne le long de la "
             "route de Toulouse, et un front de constructions neuves autour du tramway.",
        enjeu="Les copropriétés livrées entre 1975 et 1995 arrivent aujourd'hui à "
              "l'échéance du PPPT alors que leurs premiers gros travaux n'ont jamais "
              "été programmés : toitures, menuiseries et réseaux constituent le triptyque "
              "récurrent, avec présence probable d'amiante sur les conduits et les colles.",
        voisins=["begles", "talence", "gradignan", "bordeaux", "bouliac"],
    ),
    dict(
        nom="Bègles", slug="begles", cp="33130", insee="33039",
        quartiers=["Terres Neuves", "Le Dorat", "Yves Farge", "Centre"],
        parc="Ancienne commune industrielle, Bègles conserve des friches et des halles "
             "reconverties, un tissu d'échoppes ouvrières et le secteur rénové des "
             "Terres Neuves.",
        enjeu="La reconversion de bâti industriel place le RAAD au premier plan : "
              "couvertures et bardages en fibres-ciment, dalles semi-rigides, flocages "
              "résiduels. Sur les échoppes, le couple plomb-amiante conditionne le "
              "budget réel des opérations de rénovation. Sur une maison d'avant 1949, "
              "un constat plomb avant travaux se couple au repérage amiante en une "
              "seule visite : mentionnez-le dans votre demande.",
        voisins=["bordeaux", "talence", "villenave-d-ornon", "floirac"],
    ),
    dict(
        nom="Gradignan", slug="gradignan", cp="33170", insee="33192",
        quartiers=["Malartic", "Cayac", "Le Solarium", "Laurenzane"],
        parc="Gradignan est très majoritairement pavillonnaire, avec quelques "
             "résidences collectives des années 1970 et un patrimoine communal ancien "
             "autour du prieuré de Cayac.",
        enjeu="Le sujet dominant est la maison individuelle antérieure à 1997 en phase "
              "d'extension ou de surélévation : le RAAT y est souvent oublié alors "
              "qu'il conditionne la responsabilité du maître d'ouvrage privé.",
        voisins=["talence", "pessac", "villenave-d-ornon"],
    ),
    dict(
        nom="Le Bouscat", slug="le-bouscat", cp="33110", insee="33069",
        quartiers=["Barrière du Médoc", "Champ de Courses", "Ermitage", "La Vache"],
        parc="Le Bouscat présente une forte densité d'échoppes et de maisons "
             "bourgeoises de la fin du XIXe siècle, complétée par des petites "
             "copropriétés des années 1960-1980.",
        enjeu="Bâti massivement antérieur à 1949 : le risque plomb est structurel et "
              "l'amiante se concentre dans les couches de travaux postérieures. Les "
              "petites copropriétés de moins de 50 lots y sont nombreuses et toutes "
              "concernées par le PPPT.",
        voisins=["bordeaux", "bruges", "eysines", "caudéran-bordeaux"],
    ),
    dict(
        nom="Bruges", slug="bruges", cp="33520", insee="33075",
        quartiers=["Tanaïs", "Le Tasta", "Ausone", "Les Places"],
        parc="Bruges a connu une urbanisation très rapide : ZAC récentes du Tasta et "
             "d'Ausone, zone d'activités de Tanaïs, et un noyau ancien plus limité.",
        enjeu="Deux régimes cohabitent : un parc neuf hors champ amiante, et une zone "
              "d'activités des années 1970-1990 où les opérations de démolition-"
              "reconstruction imposent un RAAD exhaustif avant tout dépôt de permis "
              "de démolir.",
        voisins=["bordeaux", "le-bouscat", "eysines", "blanquefort", "parempuyre"],
    ),
    dict(
        nom="Eysines", slug="eysines", cp="33320", insee="33162",
        quartiers=["Migron", "Le Vigean", "Grand Caillou", "Carès"],
        parc="Eysines conserve son identité maraîchère avec un bâti agricole ancien, "
             "auquel s'ajoutent un pavillonnaire dense des années 1970-1990 et des "
             "opérations collectives récentes.",
        enjeu="Les bâtiments agricoles et hangars antérieurs à 1997 sont un point "
              "aveugle classique : plaques ondulées en fibres-ciment, conduits, "
              "cloisons. Leur démolition ou reconversion relève du RAAD, avec analyse "
              "en laboratoire accrédité.",
        voisins=["le-bouscat", "bruges", "le-haillan", "le-taillan-medoc", "merignac"],
    ),
    dict(
        nom="Le Haillan", slug="le-haillan", cp="33185", insee="33200",
        quartiers=["Centre", "Bel Air", "Meycat"],
        parc="Le Haillan associe un pavillonnaire des années 1970-1990, quelques "
             "résidences collectives et une zone d'activités tournée vers "
             "l'aéronautique.",
        enjeu="Les locaux d'activité en cours de restructuration constituent le "
              "principal gisement de RAAT : faux-plafonds, dalles de sol et réseaux "
              "enterrés doivent être repérés avant toute intervention d'entreprise.",
        voisins=["merignac", "eysines", "saint-medard-en-jalles", "le-taillan-medoc"],
    ),
    dict(
        nom="Saint-Médard-en-Jalles", slug="saint-medard-en-jalles", cp="33160", insee="33449",
        quartiers=["Hastignan", "Corbiac", "Issac", "Cérillan", "Magudas"],
        parc="Très étendue, Saint-Médard-en-Jalles combine des bourgs anciens "
             "(Hastignan, Corbiac, Issac), un pavillonnaire diffus considérable et un "
             "site industriel historique.",
        enjeu="L'étalement du bâti impose une logistique de repérage adaptée. Sur les "
              "équipements publics et industriels antérieurs à 1997, le RAAT relève du "
              "code du travail et engage directement la responsabilité du donneur "
              "d'ordre avant toute intervention.",
        voisins=["le-haillan", "saint-aubin-de-medoc", "martignas-sur-jalle", "le-taillan-medoc"],
    ),
    dict(
        nom="Blanquefort", slug="blanquefort", cp="33290", insee="33056",
        quartiers=["Caychac", "Tanaïs", "Centre", "Grand Louis"],
        parc="Blanquefort est marquée par un vaste héritage industriel et logistique, "
             "un centre ancien autour du château, et des lotissements des années "
             "1970-1990.",
        enjeu="Les friches et bâtiments logistiques en reconversion appellent des "
              "missions RAAD lourdes, avec sondages destructifs et repérage des "
              "matériaux enfouis. C'est le type d'opération où un repérage incomplet "
              "arrête un chantier.",
        voisins=["bruges", "parempuyre", "le-taillan-medoc", "saint-aubin-de-medoc"],
    ),
    dict(
        nom="Parempuyre", slug="parempuyre", cp="33290", insee="33312",
        quartiers=["Centre", "Landegrand", "Le Bourg"],
        parc="Commune de palus et de vignoble en limite nord de la métropole, "
             "Parempuyre présente un bâti ancien de bourg, des dépendances viticoles "
             "et des lotissements récents.",
        enjeu="Le patrimoine agricole et viticole ancien concentre les matériaux "
              "amiantés en couverture. Les copropriétés y étant peu nombreuses, "
              "l'essentiel de la demande porte sur le RAAT en maison et sur le RAAD "
              "de dépendances.",
        voisins=["blanquefort", "bruges", "saint-louis-de-montferrand"],
    ),
    dict(
        nom="Ambarès-et-Lagrave", slug="ambares-et-lagrave", cp="33440", insee="33003",
        quartiers=["La Gorp", "Sabarèges", "Bassens-Nord", "Centre"],
        parc="Ambarès-et-Lagrave associe un bâti ouvrier ancien lié au chemin de fer "
             "et à la Dordogne, des lotissements des années 1970-1990 et des "
             "opérations neuves autour de la gare.",
        enjeu="Le parc social et les copropriétés modestes des années 1970 y sont "
              "surreprésentés : le PPPT y sert directement à mobiliser le fonds de "
              "travaux et à séquencer des rénovations qui n'ont jamais été planifiées.",
        voisins=["saint-louis-de-montferrand", "saint-vincent-de-paul", "bassens", "carbon-blanc"],
    ),
    dict(
        nom="Ambès", slug="ambes", cp="33810", insee="33004",
        quartiers=["Le Bourg", "La Presqu'île"],
        parc="Située à la confluence, Ambès est dominée par les installations "
             "industrielles et énergétiques de la presqu'île, avec un bourg ancien de "
             "taille limitée.",
        enjeu="Territoire à forte composante industrielle : les opérations de "
              "maintenance et de démantèlement relèvent du repérage avant travaux au "
              "sens du code du travail, avec des exigences de coordination renforcées "
              "sur sites classés.",
        voisins=["saint-louis-de-montferrand", "ambares-et-lagrave"],
    ),
    dict(
        nom="Artigues-près-Bordeaux", slug="artigues-pres-bordeaux", cp="33370", insee="33013",
        quartiers=["Feydeau", "Bourbon", "Centre"],
        parc="Artigues-près-Bordeaux présente un pavillonnaire majoritaire des années "
             "1970-1990, quelques résidences collectives et un parc d'activités.",
        enjeu="Les copropriétés de taille moyenne construites entre 1975 et 1990 y "
              "abordent leur premier cycle de gros entretien : le DTG est l'outil "
              "adapté quand l'état réel du bâti n'a jamais été objectivé.",
        voisins=["cenon", "carbon-blanc", "bassens", "floirac"],
    ),
    dict(
        nom="Bassens", slug="bassens", cp="33530", insee="33032",
        quartiers=["Le Bousquet", "Meignan", "Beauval", "Centre"],
        parc="Bassens est structurée par le port et ses installations industrielles, "
             "avec un habitat ouvrier ancien et des ensembles collectifs des années "
             "1960-1970 sur le plateau.",
        enjeu="Combinaison rare de bâti industriel portuaire et de logement collectif "
              "ancien : les deux régimes de repérage, RAAT industriel et RAAD de "
              "bâtiment, coexistent sur un territoire restreint.",
        voisins=["carbon-blanc", "ambares-et-lagrave", "lormont", "artigues-pres-bordeaux"],
    ),
    dict(
        nom="Bouliac", slug="bouliac", cp="33270", insee="33065",
        quartiers=["Le Bourg", "Bellevue", "Bardanac"],
        parc="Perchée sur le coteau, Bouliac est essentiellement pavillonnaire, avec "
             "un bourg ancien et des maisons individuelles de standing des années "
             "1970-2000.",
        enjeu="La demande porte majoritairement sur la maison individuelle antérieure "
              "à 1997 en rénovation lourde ou extension, où le repérage avant travaux "
              "reste largement sous-prescrit.",
        voisins=["floirac", "villenave-d-ornon", "begles"],
    ),
    dict(
        nom="Carbon-Blanc", slug="carbon-blanc", cp="33560", insee="33096",
        quartiers=["Centre", "Le Faisan", "Les Griffons"],
        parc="Petite commune dense, Carbon-Blanc mêle bâti de bourg ancien, "
             "lotissements des années 1970-1980 et résidences collectives de taille "
             "modeste.",
        enjeu="Le tissu de petites copropriétés de moins de 50 lots y est dominant : "
              "toutes sont désormais dans le champ du plan pluriannuel de travaux, "
              "souvent sans historique technique exploitable.",
        voisins=["bassens", "ambares-et-lagrave", "cenon", "artigues-pres-bordeaux"],
    ),
    dict(
        nom="Cenon", slug="cenon", cp="33150", insee="33119",
        quartiers=["Palmer", "La Morlette", "Le Loret", "Bas-Cenon", "Plaisance"],
        parc="Cenon est marquée par les grands ensembles des années 1960-1970 sur le "
             "plateau (Palmer, La Morlette) et un tissu d'échoppes et de maisons de "
             "coteau en partie basse.",
        enjeu="Territoire de renouvellement urbain : les réhabilitations et "
              "démolitions programmées imposent des repérages amiante exhaustifs sur "
              "des bâtiments massivement construits avant 1997, avec des matériaux de "
              "liste A et B fréquents.",
        voisins=["lormont", "floirac", "bordeaux", "carbon-blanc", "artigues-pres-bordeaux"],
    ),
    dict(
        nom="Floirac", slug="floirac", cp="33270", insee="33167",
        quartiers=["Dravemont", "Jean Jaurès", "Les Étauliers", "La Burthe"],
        parc="Floirac combine le grand ensemble de Dravemont, un bâti de coteau "
             "ancien, et le secteur en mutation des Quais autour de l'Arena.",
        enjeu="Les opérations de renouvellement urbain y génèrent des missions de "
              "repérage avant démolition sur des volumes importants. En parallèle, les "
              "copropriétés des années 1960-1970 entrent dans le champ du PPPT avec des "
              "besoins de rénovation énergétique lourds.",
        voisins=["cenon", "bouliac", "begles", "bordeaux"],
    ),
    dict(
        nom="Lormont", slug="lormont", cp="33310", insee="33249",
        quartiers=["Génicart", "Carriet", "Le Bas-Lormont", "Bois Fleuri"],
        parc="Lormont est l'une des communes les plus marquées par les grands "
             "ensembles des années 1960-1970 (Génicart, Carriet), aux côtés d'un "
             "bourg ancien en bord de Garonne.",
        enjeu="Le parc social et copropriétaire de cette période est le terrain "
              "typique du repérage avant travaux en site occupé : dalles vinyle-"
              "amiante, colles, conduits de vide-ordures et calorifugeages sont à "
              "traiter avant toute réhabilitation.",
        voisins=["cenon", "bassens", "carbon-blanc", "bordeaux"],
    ),
    dict(
        nom="Martignas-sur-Jalle", slug="martignas-sur-jalle", cp="33127", insee="33273",
        quartiers=["Centre", "Le Barp-Nord", "Camp de Souge"],
        parc="Commune de lande en frange ouest, Martignas-sur-Jalle est "
             "majoritairement pavillonnaire, avec des équipements publics et un site "
             "aéronautique.",
        enjeu="Bâti public et industriel antérieur à 1997 en cours de rénovation : "
              "le repérage avant travaux relève ici du code du travail, avec obligation "
              "pour le donneur d'ordre de le transmettre aux entreprises consultées.",
        voisins=["merignac", "saint-medard-en-jalles", "pessac"],
    ),
    dict(
        nom="Saint-Aubin-de-Médoc", slug="saint-aubin-de-medoc", cp="33160", insee="33376",
        quartiers=["Centre", "Le Fongravey", "Picot"],
        parc="Saint-Aubin-de-Médoc est une commune résidentielle de faible densité, "
             "essentiellement composée de maisons individuelles construites depuis "
             "les années 1970.",
        enjeu="Peu de collectif, donc peu de DTG et de PPPT : la demande porte quasi "
              "exclusivement sur le repérage avant travaux en maison individuelle, "
              "notamment lors des rénovations énergétiques financées.",
        voisins=["saint-medard-en-jalles", "le-taillan-medoc", "blanquefort"],
    ),
    dict(
        nom="Saint-Louis-de-Montferrand", slug="saint-louis-de-montferrand", cp="33440", insee="33433",
        quartiers=["Le Bourg", "Les Palus"],
        parc="Commune de palus en bord de Garonne, au bâti ancien de bourg complété "
             "par des constructions individuelles récentes.",
        enjeu="Bâti ancien et dépendances agricoles concentrent les couvertures en "
              "fibres-ciment. Les opérations de démolition, même modestes, relèvent "
              "du repérage avant démolition.",
        voisins=["ambares-et-lagrave", "ambes", "parempuyre"],
    ),
    dict(
        nom="Saint-Vincent-de-Paul", slug="saint-vincent-de-paul", cp="33440", insee="33487",
        quartiers=["Le Bourg", "Beauvallon"],
        parc="Petite commune de la rive droite, à dominante pavillonnaire avec un "
             "noyau ancien limité.",
        enjeu="Demande principalement orientée maison individuelle et bâti agricole : "
              "repérage avant travaux lors des extensions et rénovations, repérage "
              "avant démolition pour les dépendances.",
        voisins=["ambares-et-lagrave", "saint-louis-de-montferrand"],
    ),
    dict(
        nom="Le Taillan-Médoc", slug="le-taillan-medoc", cp="33320", insee="33519",
        quartiers=["Centre", "Germignan", "Le Chêne Vert"],
        parc="Le Taillan-Médoc mêle un bourg ancien, un domaine viticole, et un "
             "pavillonnaire étendu développé à partir des années 1970.",
        enjeu="Le patrimoine viticole et les dépendances anciennes appellent des "
              "repérages avant démolition spécifiques. Le collectif reste minoritaire, "
              "avec quelques copropriétés récentes hors champ amiante.",
        voisins=["eysines", "blanquefort", "le-haillan", "saint-aubin-de-medoc", "saint-medard-en-jalles"],
    ),
]

# Communes limitrophes couvertes sans page dédiée (évite les pages satellites vides)
ZONE_ELARGIE = [
    "Cestas", "Canéjan", "Léognan", "Cadaujac", "Saint-Jean-d'Illac",
    "Le Pian-Médoc", "Ludon-Médoc", "Macau", "Latresne", "Carignan-de-Bordeaux",
    "Tresses", "Beychac-et-Caillau", "Izon", "Libourne", "Saint-André-de-Cubzac",
    "Arcachon", "La Teste-de-Buch", "Gujan-Mestras", "Andernos-les-Bains",
    "Lège-Cap-Ferret", "Langon", "Créon", "Podensac", "Blaye",
]

# Les textes de fond (parc, enjeu, copropriété locale, repères de terrain)
# vivent dans un module séparé : ils ont été rédigés et vérifiés à part, et les
# garder ici rendrait ce fichier illisible. La fusion écrase parc et enjeu,
# et ajoute copro et reperes.
from data.communes_textes import TEXTES as _TEXTES
for _c in COMMUNES:
    _c.update(_TEXTES.get(_c["slug"], {}))

SLUG_TO_NOM = {c["slug"]: c["nom"] for c in COMMUNES}
# Acces direct a la fiche complete depuis un slug : les pages de ville
# affichent le parc, les enjeux et la copropriete locale.
PAR_SLUG = {c["slug"]: c for c in COMMUNES}
