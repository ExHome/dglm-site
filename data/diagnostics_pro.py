# -*- coding: utf-8 -*-
"""
LES DIAGNOSTICS, VERSION COLLECTIVE ET PROFESSIONNELLE.

Le site A occupe les diagnostics de vente et de location : « diagnostic
amiante », « DPE », « diagnostic plomb », « diagnostic termites »…
Il n'occupe RIEN de leur version collective, qui est un marché distinct,
avec d'autres commanditaires, d'autres textes et d'autres volumes.

Règle absolue : chaque titre porte un qualificatif (collectif, parties
communes, parties privatives, copropriété, avant travaux, avant démolition).
C'est ce qui sépare les deux sites aux yeux de Google — et c'est vérifié
automatiquement par audit_seo.py.

⚠ Références à revalider avant mise en ligne (voir LISEZ-MOI).
"""

DIAGS_PRO = [
    dict(
        slug="dossier-technique-amiante",
        sigle="DTA",
        nom="Dossier technique amiante des parties communes",
        h1="Dossier technique amiante (DTA) des parties communes",
        accroche="Le document que tout syndic doit pouvoir présenter, et tenir à jour.",
        meta="Dossier technique amiante (DTA) des parties communes à {lieu} : repérage "
             "listes A et B, état de conservation, fiche récapitulative.",
        intro="Le dossier technique amiante recense les matériaux amiantés des parties "
              "communes d'un immeuble collectif d'habitation, ainsi que de tout bâtiment "
              "autre qu'une maison individuelle. Il doit être constitué, tenu à jour, et "
              "sa fiche récapitulative communiquée aux occupants comme aux entreprises "
              "qui interviennent.",
        cadre=[
            ("Code de la santé publique, art. R.1334-29-5",
             "Impose la constitution d'un dossier technique amiante pour les parties "
             "communes des immeubles collectifs d'habitation et pour les autres bâtiments, "
             "dont le permis est antérieur au 1er juillet 1997."),
            ("Périmètre du repérage",
             "Matériaux des listes A et B, avec évaluation de leur état de conservation et, "
             "le cas échéant, mesures d'empoussièrement ou travaux de confinement."),
            ("Obligation de mise à jour",
             "Le dossier doit être actualisé à chaque travaux modifiant l'état des "
             "matériaux. Un DTA de 2005 jamais révisé n'est plus opposable."),
        ],
        faq=[
            ("Quelle différence entre DTA et repérage avant travaux ?",
             "Le DTA est un document de gestion permanente du bâtiment. Le repérage avant "
             "travaux est établi pour une opération précise, avec sondages destructifs dans "
             "le périmètre du chantier. Le DTA ne dispense jamais du repérage avant travaux."),
            ("Qui doit constituer le DTA d'une copropriété ?",
             "Le syndic, pour le compte du syndicat des copropriétaires. Il doit tenir la "
             "fiche récapitulative à disposition des occupants et la remettre à toute "
             "entreprise intervenant dans l'immeuble."),
            ("Mon DTA date de plus de quinze ans : est-il valable ?",
             "Il reste formellement en vigueur, mais l'évaluation de l'état de conservation "
             "des matériaux y est périmée. Une réévaluation périodique est attendue, et "
             "indispensable dès qu'un doute existe."),
        ],
        fiche=[
            ("Pour qui", "Le syndic, pour le compte du syndicat des copropriétaires."),
            ("Quel bâtiment", "Parties communes des immeubles collectifs dont le permis "
                              "est antérieur au 1er juillet 1997."),
            ("Périmètre", "Matériaux des listes A et B, avec état de conservation."),
            ("À tenir à jour", "À chaque travaux modifiant l'état des matériaux."),
            ("À remettre", "Fiche récapitulative aux occupants et aux entreprises."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="amiante-parties-privatives",
        sigle="DAPP",
        nom="Amiante des parties privatives (DAPP)",
        h1="Amiante des parties privatives (DAPP) en immeuble collectif",
        accroche="L'obligation du propriétaire bailleur, distincte de celle du syndic.",
        meta="Diagnostic amiante des parties privatives (DAPP) à {lieu} : repérage liste A "
             "en immeuble collectif d'habitation. Devis sous 2 h.",
        intro="Le diagnostic amiante des parties privatives porte sur les logements d'un "
              "immeuble collectif d'habitation. Il incombe au propriétaire de chaque lot, "
              "et non au syndicat des copropriétaires. Les bailleurs sociaux et privés en "
              "sont les premiers concernés.",
        cadre=[
            ("Code de la santé publique, art. R.1334-29-4",
             "Impose au propriétaire de rechercher les matériaux de la liste A dans les "
             "parties privatives des immeubles collectifs d'habitation dont le permis est "
             "antérieur au 1er juillet 1997."),
            ("Périmètre : liste A uniquement",
             "Flocages, calorifugeages et faux-plafonds. Le repérage est donc plus étroit "
             "que celui d'un dossier technique amiante."),
            ("Campagnes de patrimoine",
             "Sur un parc locatif, la mission se conduit en campagne : information des "
             "locataires, taux de pénétration, gestion des absences et des refus."),
        ],
        faq=[
            ("Le DAPP suffit-il avant des travaux dans un logement ?",
             "Non. Il ne couvre que la liste A et ne comporte pas de sondages destructifs. "
             "Toute intervention exposant des travailleurs impose un repérage avant travaux."),
            ("Qui paie le DAPP en copropriété ?",
             "Le propriétaire du lot concerné. Le syndicat des copropriétaires prend en "
             "charge le dossier technique amiante des parties communes, pas les parties "
             "privatives."),
            ("Le DAPP est-il à remettre au locataire ?",
             "Le constat doit être tenu à disposition des occupants et des personnes "
             "appelées à intervenir dans le logement."),
        ],
        fiche=[
            ("Pour qui", "Chaque propriétaire de lot — bailleurs sociaux et privés en tête."),
            ("Quel bâtiment", "Logements en immeuble collectif d'avant juillet 1997."),
            ("Périmètre", "Liste A seule : flocages, calorifugeages, faux-plafonds."),
            ("À savoir", "Ne remplace jamais un repérage avant travaux."),
            ("Parc locatif", "Mission conduite en campagne organisée, logement par logement."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="diagnostic-pemd",
        sigle="PEMD",
        nom="Diagnostic produits, équipements, matériaux et déchets",
        h1="Diagnostic PEMD avant démolition ou rénovation significative",
        accroche="L'obligation que presque personne n'anticipe, et qui bloque les marchés.",
        meta="Diagnostic PEMD à {lieu} : inventaire des produits, équipements, matériaux "
             "et déchets avant démolition ou rénovation significative. Devis sous 2 h.",
        intro="Le diagnostic portant sur la gestion des produits, équipements, matériaux "
              "et déchets est obligatoire avant la démolition ou la rénovation "
              "significative de certains bâtiments. Il inventorie ce qui sort du chantier, "
              "estime les quantités et oriente vers les filières de réemploi et de "
              "valorisation. Un formulaire de récolement doit être transmis après travaux.",
        cadre=[
            ("Code de la construction et de l'habitation, art. L.126-34 et R.126-8",
             "Fixent l'obligation de diagnostic préalable à la démolition ou à la "
             "rénovation significative, issue de la loi anti-gaspillage."),
            ("Seuils d'application",
             "Bâtiments de plus de 1 000 m² de surface cumulée, et bâtiments ayant accueilli "
             "une activité agricole, industrielle ou commerciale ayant employé ou stocké "
             "des substances dangereuses."),
            ("Récolement après travaux",
             "Un formulaire de récolement décrivant la nature et les quantités réellement "
             "évacuées doit être transmis à l'issue de l'opération."),
        ],
        faq=[
            ("Le PEMD remplace-t-il le repérage amiante avant démolition ?",
             "Non. Ce sont deux missions distinctes, avec deux fondements juridiques "
             "différents. Elles se conduisent le plus souvent lors de la même visite, ce "
             "qui réduit le coût global."),
            ("Qu'est-ce qu'une rénovation significative ?",
             "Une opération portant sur au moins deux des principaux éléments de second "
             "œuvre, dans un bâtiment dépassant les seuils de surface. Nous qualifions "
             "l'opération avant de vous établir un devis."),
            ("Qui est responsable du diagnostic PEMD ?",
             "Le maître d'ouvrage. Il doit le faire réaliser avant le dépôt de la demande "
             "d'autorisation ou, à défaut, avant l'acceptation des devis de travaux."),
        ],
        fiche=[
            ("Pour qui", "Le maître d'ouvrage de l'opération."),
            ("Quand", "Avant démolition ou rénovation significative."),
            ("Seuils", "Plus de 1 000 m², ou activité ayant employé ou stocké des "
                       "substances dangereuses."),
            ("Livrable", "Inventaire, quantités estimées, filières de réemploi."),
            ("Après travaux", "Formulaire de récolement à transmettre."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="dpe-collectif-copropriete",
        sigle="DPE collectif",
        nom="DPE collectif de copropriété",
        h1="DPE collectif de copropriété : obligation et calendrier",
        accroche="L'étiquette énergétique de l'immeuble entier, désormais obligatoire partout.",
        meta="DPE collectif de copropriété à {lieu} : obligation, calendrier par nombre de "
             "lots, articulation avec le plan pluriannuel de travaux.",
        intro="Le diagnostic de performance énergétique collectif porte sur l'immeuble "
              "entier et non sur un lot. Il est obligatoire dans les copropriétés "
              "d'habitation dont le permis de construire est antérieur à 2013, selon un "
              "calendrier échelonné par nombre de lots aujourd'hui intégralement déployé.",
        cadre=[
            ("Loi Climat et Résilience du 22 août 2021",
             "Généralise le diagnostic de performance énergétique collectif aux "
             "copropriétés d'habitation."),
            ("Calendrier par nombre de lots",
             "Plus de 200 lots depuis le 1er janvier 2024, de 51 à 200 lots depuis le "
             "1er janvier 2025, 50 lots et moins depuis le 1er janvier 2026."),
            ("Articulation avec le plan pluriannuel",
             "Le volet énergétique nourrit directement le plan pluriannuel de travaux. "
             "Faire réaliser les deux séparément coûte sensiblement plus cher."),
        ],
        faq=[
            ("Le DPE collectif remplace-t-il le DPE de chaque lot ?",
             "Non pour la vente ou la location, où le diagnostic individuel reste requis. "
             "Le DPE collectif décrit la performance de l'immeuble et sert la décision "
             "collective."),
            ("Quelle est sa durée de validité ?",
             "Dix ans, sous réserve de travaux modifiant substantiellement la performance "
             "de l'immeuble."),
            ("Faut-il un vote en assemblée générale ?",
             "L'obligation s'impose ; l'assemblée se prononce sur les modalités de "
             "réalisation et le prestataire retenu."),
        ],
        fiche=[
            ("Pour qui", "Copropriétés d'habitation dont le permis est antérieur à 2013."),
            ("Calendrier", "Toutes les tailles de copropriétés concernées depuis le "
                           "1er janvier 2026."),
            ("Porte sur", "L'immeuble entier, pas les lots individuels."),
            ("Validité", "Dix ans, sauf travaux modifiant la performance."),
            ("À savoir", "Nourrit directement le plan pluriannuel de travaux."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="audit-energetique-copropriete",
        sigle="Audit énergétique",
        nom="Audit énergétique de copropriété",
        h1="Audit énergétique de copropriété : au-delà de l'étiquette",
        accroche="Des scénarios de travaux chiffrés, pas seulement une lettre de A à G.",
        meta="Audit énergétique de copropriété à {lieu} : scénarios de rénovation chiffrés, "
             "gains attendus, articulation avec le plan pluriannuel de travaux.",
        intro="L'audit énergétique va plus loin que le diagnostic de performance "
              "énergétique collectif : il propose des scénarios de travaux hiérarchisés, "
              "chiffrés, avec les gains énergétiques attendus. C'est le document qui "
              "permet à une assemblée générale de choisir entre plusieurs stratégies de "
              "rénovation plutôt que de subir un constat.",
        cadre=[
            ("Une obligation devenue démarche volontaire",
             "L'audit énergétique de copropriété a été obligatoire pour les immeubles d'au "
             "moins cinquante lots dotés d'une installation collective de chauffage ou de "
             "refroidissement et dont le permis de construire a été déposé avant le 1er juin "
             "2001, avec une mise en conformité attendue au 1er janvier 2017. Depuis la loi "
             "Climat et Résilience, c'est le DPE collectif qui s'impose ; l'audit énergétique "
             "reste une démarche volontaire, mais déterminante pour décider des travaux et "
             "accéder aux aides à la rénovation."),
            ("Contenu attendu",
             "État des lieux technique, analyse des consommations réelles, scénarios de "
             "travaux avec estimation des coûts et des gains, préconisations d'usage."),
            ("Financement",
             "L'audit conditionne l'accès à plusieurs dispositifs d'aide à la rénovation "
             "des copropriétés. Le faire réaliser avant de voter les travaux, et non "
             "après, change le plan de financement."),
        ],
        faq=[
            ("Quelle différence avec le DPE collectif ?",
             "Le DPE collectif classe l'immeuble. L'audit énergétique propose des chemins "
             "de sortie chiffrés. Le premier constate, le second décide."),
            ("L'audit peut-il alimenter le plan pluriannuel de travaux ?",
             "Oui, et c'est l'usage recommandé : les scénarios de rénovation énergétique "
             "s'intègrent directement à l'échéancier décennal."),
            ("Faut-il l'un ou l'autre ?",
             "Le DPE collectif est l'obligation : son échéance dépend du nombre de lots et "
             "de l'année du permis. L'audit énergétique, lui, n'est plus obligatoire mais "
             "reste le meilleur outil pour décider des travaux et monter un plan de "
             "financement. Notre simulateur d'obligations vous donne une première réponse."),
        ],
        fiche=[
            ("Statut", "Démarche volontaire — l'obligation, c'est le DPE collectif."),
            ("Pour qui", "Copropriétés qui préparent une rénovation."),
            ("Livrable", "Scénarios de travaux hiérarchisés et chiffrés, gains attendus."),
            ("Financement", "Conditionne l'accès à plusieurs aides à la rénovation."),
            ("À savoir", "S'intègre directement à l'échéancier du plan pluriannuel."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="crep-parties-communes",
        sigle="CREP communes",
        nom="Constat plomb des parties communes",
        h1="Constat de risque d'exposition au plomb des parties communes",
        accroche="Une obligation ancienne, rarement satisfaite, systématiquement réveillée par les travaux.",
        meta="Constat plomb des parties communes à {lieu} : immeubles d'habitation "
             "antérieurs à 1949, mesures par fluorescence X. Devis sous 2 h.",
        intro="Les parties communes des immeubles d'habitation construits avant le "
              "1er janvier 1949 doivent faire l'objet d'un constat de risque d'exposition "
              "au plomb. L'échéance légale est ancienne, mais une part importante du parc "
              "bordelais et landais n'y a jamais satisfait — jusqu'au jour où des travaux "
              "sont engagés.",
        cadre=[
            ("Code de la santé publique, art. L.1334-8",
             "Impose un constat de risque d'exposition au plomb dans les parties communes "
             "des immeubles d'habitation construits avant le 1er janvier 1949."),
            ("Méthode",
             "Mesures par appareil à fluorescence X, unité de diagnostic par unité de "
             "diagnostic, avec classement de l'état de conservation des revêtements."),
            ("Conséquence sur les travaux",
             "Un revêtement dégradé contenant du plomb impose des mesures de protection "
             "des travailleurs et des occupants avant toute intervention."),
        ],
        faq=[
            ("Notre immeuble date de 1930 et n'a jamais eu de CREP : que risque-t-on ?",
             "La responsabilité du syndicat des copropriétaires peut être recherchée en cas "
             "d'intoxication, en particulier chez un enfant. C'est le risque le plus lourd "
             "de tout le champ des diagnostics."),
            ("Le CREP des parties communes a-t-il une durée de validité ?",
             "Un constat concluant à l'absence de plomb ou à des revêtements non dégradés "
             "n'a pas à être renouvelé. Un constat révélant des dégradations appelle des "
             "travaux et un nouveau contrôle."),
            ("Faut-il un CREP avant une réfection de cage d'escalier ?",
             "Sur un immeuble antérieur à 1949, oui : c'est la condition d'une "
             "organisation de chantier conforme."),
        ],
        fiche=[
            ("Pour qui", "Le syndicat des copropriétaires."),
            ("Quel bâtiment", "Immeubles d'habitation construits avant le 1er janvier 1949."),
            ("Méthode", "Mesures par appareil à fluorescence X, unité par unité."),
            ("Validité", "Définitive si absence de plomb ou revêtements non dégradés."),
            ("Enjeu", "Responsabilité lourde du syndicat en cas d'intoxication."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="etat-parasitaire-avant-travaux",
        sigle="État parasitaire",
        nom="État parasitaire et termites avant travaux",
        h1="État parasitaire et termites avant travaux ou acquisition",
        accroche="Au-delà des termites : mérule, capricornes, vrillettes et bois de structure.",
        meta="État parasitaire avant travaux à {lieu} : termites, mérule, insectes "
             "xylophages, bois de structure. Gironde et Landes en zone déclarée.",
        intro="L'état parasitaire dépasse le seul contrôle des termites exigé lors d'une "
              "vente : il couvre l'ensemble des agents de dégradation biologique du bois — "
              "termites, capricornes, vrillettes, mérule et autres champignons "
              "lignivores. Sur un immeuble ancien, il conditionne le diagnostic de "
              "structure et le budget de travaux.",
        cadre=[
            ("Gironde et Landes en zone délimitée",
             "Les deux départements font l'objet d'arrêtés préfectoraux délimitant des "
             "zones contaminées par les termites. Le risque n'est pas théorique."),
            ("Une mission contractuelle, pas seulement réglementaire",
             "L'état parasitaire n'est pas un diagnostic obligatoire de vente : c'est une "
             "mission d'expertise commandée avant travaux, avant acquisition d'un immeuble "
             "de rapport, ou en cas de désordre constaté."),
            ("Portée sur les bois de structure",
             "Planchers, charpentes, solives et pans de bois sont examinés en tant "
             "qu'éléments porteurs, et pas seulement comme supports."),
        ],
        faq=[
            ("Différence avec le diagnostic termites de vente ?",
             "Le diagnostic de vente répond à une obligation ponctuelle et se limite aux "
             "termites. L'état parasitaire est une expertise plus large, destinée à "
             "préparer des travaux ou une acquisition."),
            ("La mérule est-elle fréquente en Gironde ?",
             "Le climat océanique et l'humidité des bâtis anciens de bord de Garonne et du "
             "littoral landais y créent des conditions favorables. Un désordre d'humidité "
             "persistant justifie une investigation."),
            ("Quand le commander ?",
             "Avant la signature d'une acquisition d'immeuble, ou avant l'établissement "
             "d'un plan pluriannuel de travaux sur un bâti ancien."),
        ],
        fiche=[
            ("Nature", "Mission d'expertise contractuelle — pas un diagnostic de "
                       "transaction."),
            ("Quand", "Avant travaux, avant acquisition, ou sur désordre constaté."),
            ("Couvre", "Termites, mérule, capricornes, vrillettes — et les bois de "
                       "structure."),
            ("Territoire", "Gironde et Landes, en zone termites délimitée par arrêté."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
    dict(
        slug="installations-collectives-gaz-electricite",
        sigle="Installations collectives",
        nom="Contrôle des installations collectives de gaz et d'électricité",
        h1="Contrôle des installations collectives de gaz et d'électricité",
        accroche="Un contrôle qui relève d'organismes agréés — voici lequel, et quand.",
        meta="Installations collectives de gaz et d'électricité à {lieu} : un contrôle "
             "d'organisme agréé. À qui s'adresser, comment l'intégrer au DTG.",
        intro="Les installations collectives de gaz et d'électricité des parties communes "
              "— colonnes montantes, locaux techniques, éclairage de sécurité, tableaux "
              "généraux — ne relèvent pas du diagnostic immobilier : leur vérification "
              "appartient aux bureaux et organismes de contrôle agréés. Nous ne réalisons "
              "pas ce contrôle. Notre rôle est de vous orienter vers qui de droit, puis "
              "d'intégrer ses conclusions à l'état des équipements communs du diagnostic "
              "technique global et au plan pluriannuel de travaux.",
        cadre=[
            ("À qui s'adresser",
             "Aux bureaux et organismes de contrôle agréés pour les installations de gaz "
             "et d'électricité. Votre syndic ou votre assureur peut en recommander ; nous "
             "pouvons vous orienter."),
            ("Obligation d'entretien de l'immeuble",
             "Le syndicat des copropriétaires répond de la conservation et de l'entretien "
             "des parties communes et des équipements communs. La vérification de ces "
             "installations est régulièrement demandée par les assureurs."),
            ("Notre rôle",
             "Intégrer les conclusions de ces contrôles au diagnostic technique global et "
             "au plan pluriannuel de travaux — pas les réaliser."),
        ],
        faq=[
            ("Est-ce un diagnostic immobilier ?",
             "Non. Ce contrôle relève des organismes de contrôle agréés, pas du "
             "diagnostiqueur immobilier. C'est pourquoi nous ne le proposons pas, et vous "
             "renvoyons vers qui de droit."),
            ("Est-ce obligatoire ?",
             "Il n'existe pas de diagnostic réglementaire équivalent à celui de la vente "
             "pour les parties communes. La vérification relève de l'obligation générale "
             "d'entretien, et devient déterminante en cas de sinistre."),
            ("Peut-on l'intégrer au diagnostic technique global ?",
             "L'état apparent des équipements communs fait partie du périmètre du DTG. "
             "Les rapports des organismes de contrôle viennent le documenter : "
             "transmettez-les nous en début de mission."),
            ("Qui commande ce contrôle ?",
             "Le syndic, auprès d'un organisme de contrôle agréé, sur décision du conseil "
             "syndical ou de l'assemblée générale."),
        ],
        fiche=[
            ("Qui le réalise", "Un organisme de contrôle agréé — pas un diagnostiqueur "
                               "immobilier."),
            ("Notre rôle", "Vous orienter vers qui de droit, puis intégrer les "
                           "conclusions au DTG et au plan pluriannuel."),
            ("Qui le commande", "Le syndic, sur décision du conseil syndical ou de "
                                "l'assemblée générale."),
            ("Enjeu", "Obligation d'entretien de l'immeuble, dossier assureur."),
        ],
    ),
    dict(
        slug="conformite-assainissement-copropriete",
        sigle="Assainissement",
        nom="Conformité assainissement en copropriété",
        h1="Conformité de l'assainissement en copropriété et en immeuble",
        accroche="Le raccordement collectif, contrôlé avant que la collectivité ne le fasse.",
        meta="Contrôle de conformité de l'assainissement en copropriété à {lieu} : "
             "raccordement au réseau public, branchements, mise en conformité.",
        intro="Le contrôle de conformité du raccordement au réseau public d'assainissement "
              "porte sur la séparation des eaux usées et pluviales, l'absence de rejets "
              "non conformes et l'état des branchements. Les collectivités le réclament de "
              "plus en plus, et les mises en demeure arrivent avec des délais courts.",
        cadre=[
            ("Contrôle par la collectivité",
             "Le service public d'assainissement peut contrôler la conformité des "
             "branchements et exiger leur mise en conformité dans un délai déterminé."),
            ("Immeubles anciens",
             "Sur les immeubles antérieurs aux années 1970, les réseaux unitaires et les "
             "branchements successifs non déclarés sont la règle plutôt que l'exception."),
            ("Anticipation",
             "Faire réaliser le contrôle avant la mise en demeure permet d'inscrire les "
             "travaux au plan pluriannuel plutôt que de les subir en urgence."),
        ],
        faq=[
            ("Qui doit faire ce contrôle en copropriété ?",
             "Le syndicat des copropriétaires pour les parties communes et le branchement "
             "de l'immeuble, chaque copropriétaire pour ses installations privatives."),
            ("Que se passe-t-il en cas de non-conformité ?",
             "La collectivité fixe un délai de mise en conformité, au-delà duquel une "
             "majoration de la redevance peut s'appliquer."),
            ("Peut-on l'intégrer au plan pluriannuel de travaux ?",
             "Oui, et c'est recommandé : les reprises de réseau sont coûteuses et se "
             "programment mal en urgence."),
        ],
        fiche=[
            ("Pour qui", "Le syndicat pour les parties communes, chaque copropriétaire "
                         "pour ses installations privatives."),
            ("Porte sur", "Raccordement au réseau public, séparation eaux usées et "
                          "pluviales, état des branchements."),
            ("Enjeu", "Mise en demeure à délai court, majoration possible de la "
                      "redevance."),
            ("À savoir", "À inscrire au plan pluriannuel plutôt qu'à subir en urgence."),
            ("Devis", "Chiffré, sous 2 heures ouvrées."),
        ],
    ),
]
