/* SIMULATEUR — QUELS DIAGNOSTICS POUR MON LOGEMENT ?

   Ce site est dédié à la copropriété et aux travaux. Les particuliers qui
   arrivaient ici par une question de vente ou de location étaient redirigés
   ailleurs au bout de quatre secondes : nous perdions le visiteur avant même
   de lui avoir répondu.

   ────────────────────────────────────────────────────────────────────────
   SOURCE DES RÈGLES — cette section engage qui la modifie.

   Une première version annonçait tirer toutes ses règles des deux fiches
   publiées du site. C'était faux : les durées venaient d'une troisième fiche,
   et plusieurs conditions ne venaient d'aucune. Un contrôle mené sur les
   textes officiels a relevé 39 défauts, dont sept fautes professionnelles —
   notamment une maison mitoyenne de moins de 50 m² dispensée à tort de
   diagnostic de performance, et une amiante réclamée à tort pour la location
   d'une maison.

   Chaque règle porte désormais sa source en commentaire. Les trois fiches du
   site restent la référence éditoriale :
     · /questions/diagnostics-obligatoires-vente/     (documents, vente)
     · /questions/diagnostics-obligatoires-location/  (documents, location)
     · /questions/duree-validite-diagnostics/         (durées)

   TOUTE MODIFICATION D'UNE RÈGLE DOIT ÊTRE RÉPERCUTÉE DANS LA FICHE
   CORRESPONDANTE, et inversement. Deux sources qui divergent valent moins
   qu'une seule.
   ──────────────────────────────────────────────────────────────────────── */
(function () {
  "use strict";
  var racine = document.getElementById("simu-part");
  if (!racine) return;

  var CFG = window.DGLM_PART || {};
  var etat = {};

  /* Le plomb et l'amiante ne se déclenchent PAS sur le même fait : le constat
     de risque d'exposition au plomb vise les immeubles d'habitation CONSTRUITS
     avant le 1ᵉʳ janvier 1949 (CSP, art. L1334-5 et L1334-6) ; l'amiante
     retient la date de DÉLIVRANCE DU PERMIS DE CONSTRUIRE, antérieure au
     1ᵉʳ juillet 1997 (CSP, art. R1334-29-4 et suivants). Une question unique
     appliquait un critère unique à deux règles distinctes : elles sont
     désormais séparées. */
  var QUESTIONS = [
    {
      cle: "operation",
      titre: "Que souhaitez-vous faire ?",
      aide: "Onze documents peuvent composer un dossier de vente, sept un dossier de location.",
      pourquoi: "La vente engage le vendeur sur la garantie des vices cachés : le dossier y "
        + "est plus étendu, et il s'annexe à la promesse ou à l'acte. La location protège le "
        + "locataire pendant toute la durée du bail : le dossier s'y annexe à la signature et "
        + "à chaque renouvellement.",
      choix: [
        { v: "vente", t: "Vendre ce logement", s: "Maison ou appartement" },
        { v: "location", t: "Le mettre en location", s: "Bail d'habitation" },
      ],
    },
    {
      cle: "bien",
      titre: "De quel bien s'agit-il ?",
      aide: "Un lot en copropriété et une maison individuelle n'appellent pas la même liste.",
      pourquoi: "Pour un appartement, la performance énergétique est due sans condition de "
        + "surface et l'audit énergétique ne s'applique pas. Pour une maison, l'audit entre "
        + "en jeu selon l'étiquette, et l'assainissement autonome appelle son propre contrôle.",
      choix: [
        { v: "appartement", t: "Un appartement", s: "En copropriété" },
        { v: "maison", t: "Une maison", s: "Individuelle" },
      ],
    },
    {
      /* Le mot « indépendant » est le pivot de l'exemption de performance
         énergétique : l'article R126-15 du CCH ne dispense que les BÂTIMENTS
         INDÉPENDANTS de moins de 50 m². Une maison mitoyenne de 45 m² y est
         soumise. La version précédente l'en dispensait — faute la plus grave
         relevée par le contrôle. */
      cle: "mitoyen",
      titre: "Votre maison est-elle isolée ou accolée ?",
      aide: "Ce détail commande une exemption que beaucoup s'appliquent à tort.",
      pourquoi: "Le seuil de 50 m² qui dispense du diagnostic de performance énergétique ne "
        + "vise que les bâtiments INDÉPENDANTS, c'est-à-dire isolés de toute autre "
        + "construction. Une maison de ville, une maison de bourg en bande ou une maison "
        + "mitoyenne n'est pas un bâtiment indépendant : le diagnostic y est dû quelle que "
        + "soit sa surface.",
      quand: function (e) { return e.bien === "maison"; },
      choix: [
        { v: "isolee", t: "Isolée", s: "Aucune construction accolée" },
        { v: "mitoyenne", t: "Mitoyenne ou accolée", s: "Maison de ville, en bande…" },
      ],
    },
    {
      /* Une maison peut appartenir à une copropriété horizontale — un
         lotissement placé sous le statut de la copropriété, fréquent en
         périphérie bordelaise. La loi Carrez vise « tout lot de copropriété »
         (loi du 10 juillet 1965, art. 46), pas « tout appartement ». */
      cle: "copro",
      titre: "Votre maison fait-elle partie d'une copropriété ?",
      aide: "Lotissement en copropriété, règlement de copropriété, syndic, charges communes.",
      pourquoi: "La surface privative dite loi Carrez est due pour tout lot de copropriété, "
        + "et non pour les seuls appartements. Une maison intégrée à un lotissement placé "
        + "sous le statut de la copropriété — configuration courante autour de Bordeaux — est "
        + "un lot de copropriété : sa superficie doit figurer dans la promesse et dans l'acte.",
      quand: function (e) { return e.bien === "maison" && e.operation === "vente"; },
      choix: [
        { v: "oui", t: "Oui", s: "Il y a un syndic ou un règlement" },
        { v: "non", t: "Non", s: "Propriété isolée" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      cle: "construction",
      titre: "Le logement a-t-il été construit avant 1949 ?",
      aide: "C'est la date de construction qui commande le constat plomb, pas celle du permis.",
      pourquoi: "Les peintures au plomb ont été interdites dans l'habitation en 1949. Le "
        + "constat de risque d'exposition au plomb vise les immeubles d'habitation construits "
        + "avant le 1ᵉʳ janvier 1949 — c'est bien la date de construction, et non celle du "
        + "permis, qui déclenche cette obligation. L'acte de propriété ou la mairie vous "
        + "renseigneront.",
      choix: [
        { v: "oui", t: "Oui, avant 1949", s: "Constat plomb dû" },
        { v: "non", t: "Non, après 1949", s: "" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      cle: "permis",
      titre: "Le permis de construire est-il antérieur à juillet 1997 ?",
      aide: "Pour l'amiante, c'est la date de délivrance du permis qui compte.",
      pourquoi: "L'amiante a été interdite en France au 1ᵉʳ janvier 1997. Le critère retenu "
        + "par les textes n'est pas la date de construction mais celle de DÉLIVRANCE DU "
        + "PERMIS DE CONSTRUIRE, antérieure au 1ᵉʳ juillet 1997. Un bâtiment achevé en 1999 "
        + "sous un permis de 1996 reste dans le champ.",
      choix: [
        { v: "oui", t: "Oui, avant juillet 1997", s: "Amiante à rechercher" },
        { v: "non", t: "Non, après juillet 1997", s: "" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      cle: "gaz",
      titre: "L'installation de gaz a-t-elle plus de quinze ans ?",
      aide: "S'il n'y a pas de gaz dans le logement, la question ne se pose pas.",
      /* Le point de départ est la RÉALISATION de l'installation (CCH,
         art. R134-6), et seul un certificat de conformité visé par un
         organisme agréé et établi depuis MOINS DE TROIS ANS tient lieu de
         l'état. La version précédente écrivait « moins de quinze ans » : elle
         exonérait à tort. */
      pourquoi: "L'état de l'installation intérieure de gaz est dû dès lors que "
        + "l'installation a été réalisée depuis plus de quinze ans, ou que son dernier "
        + "certificat de conformité date de plus de quinze ans. Seul un certificat de "
        + "conformité visé par un organisme agréé et établi depuis moins de trois ans peut "
        + "tenir lieu de cet état.",
      choix: [
        { v: "oui", t: "Plus de quinze ans", s: "" },
        { v: "non", t: "Moins de quinze ans", s: "" },
        { v: "aucun", t: "Il n'y a pas de gaz", s: "" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      cle: "elec",
      titre: "L'installation électrique a-t-elle plus de quinze ans ?",
      aide: "Les quinze ans se comptent depuis la réalisation de l'installation.",
      pourquoi: "Même règle que pour le gaz : au-delà de quinze ans depuis la réalisation de "
        + "l'installation, l'état de l'installation intérieure d'électricité est dû, en vente "
        + "comme en location. Une installation entièrement refaite et attestée par un "
        + "certificat de conformité repart à zéro ; des travaux partiels non attestés, non.",
      choix: [
        { v: "oui", t: "Plus de quinze ans", s: "" },
        { v: "non", t: "Moins de quinze ans", s: "" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      /* L'obligation tient au fait que l'immeuble n'est pas raccordé au réseau
         public (CSP, art. L1331-11-1), et non au type de bien : la question se
         pose donc pour toute vente. */
      cle: "assain",
      titre: "Comment le logement évacue-t-il ses eaux usées ?",
      aide: "En appartement, la réponse est presque toujours le réseau collectif.",
      pourquoi: "En vente, le diagnostic de l'assainissement est dû lorsque l'immeuble n'est "
        + "pas raccordé au réseau public — fosse toutes eaux, micro-station, filtre à sable. "
        + "L'obligation tient au mode d'évacuation, non au type de bien : un lot en "
        + "copropriété desservi par une installation autonome est concerné.",
      quand: function (e) { return e.operation === "vente"; },
      choix: [
        { v: "autonome", t: "Installation autonome", s: "Fosse, micro-station" },
        { v: "collectif", t: "Tout-à-l'égout", s: "Réseau collectif" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      /* Ajouté au dossier de vente par la loi n°2024-322 du 9 avril 2024
         (CCH, art. L271-4 I, 11°). L'agglomération bordelaise est couverte par
         un plan de protection de l'atmosphère : le cas est courant ici. */
      cle: "bois",
      titre: "Le logement est-il chauffé au bois ?",
      aide: "Poêle, insert, cheminée à foyer fermé, chaudière à bois ou à granulés.",
      pourquoi: "Depuis avril 2024, lorsqu'un logement situé dans le périmètre d'un plan de "
        + "protection de l'atmosphère comporte un appareil de chauffage au bois, un "
        + "certificat attestant sa conformité rejoint le dossier de vente. L'agglomération "
        + "bordelaise est couverte par un tel plan.",
      quand: function (e) { return e.operation === "vente"; },
      choix: [
        { v: "oui", t: "Oui", s: "Poêle, insert, chaudière" },
        { v: "non", t: "Non", s: "" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
  ];

  /* ------------------------------------------------------------------ règles
     Chaque ligne : [document, condition de déclenchement, explication].
     La condition est TOUJOURS ce qui rend le document exigible — jamais une
     modalité de remise, qui appartient à l'explication. */
  function calculer(e) {
    var dus = [], selon = [], hors = [];
    var vente = e.operation === "vente";
    var maison = e.bien === "maison";

    /* ---- Performance énergétique ----
       CCH art. R126-15 : le diagnostic est dû pour tout logement, SAUF sept
       catégories, dont les bâtiments INDÉPENDANTS de moins de 50 m². Ces
       exemptions valent en vente comme en location. */
    var dpeDuree = "Sa validité est de dix ans — avec une réserve qui touche encore beaucoup "
      + "de logements : les diagnostics réalisés entre le 1ᵉʳ janvier 2018 et le 30 juin 2021 "
      + "sont caducs depuis le 1ᵉʳ janvier 2025 et doivent être refaits, même s'ils ont moins "
      + "de dix ans.";
    var dpeExempt = "Il n'est pas exigé pour un bâtiment indépendant de moins de 50 m² de "
      + "surface de plancher, un monument historique classé ou inscrit, un logement occupé "
      + "moins de quatre mois par an, ou un logement dépourvu de système fixe de chauffage et "
      + "de climatisation.";
    var dpeLoc = vente ? "" : " Depuis le 1ᵉʳ janvier 2025, un logement classé G ne peut plus "
      + "faire l'objet d'un nouveau bail, d'un renouvellement ni d'une reconduction tacite ; "
      + "viendra la classe F au 1ᵉʳ janvier 2028, puis la classe E au 1ᵉʳ janvier 2034. Depuis "
      + "le 1ᵉʳ janvier 2026, le coefficient de conversion de l'électricité est passé de 2,3 à "
      + "1,9 : si votre logement est chauffé à l'électricité et que son diagnostic est "
      + "antérieur, l'étiquette peut s'améliorer sans un seul travail.";

    if (maison && e.mitoyen === "isolee") {
      selon.push(["Diagnostic de performance énergétique",
        "dû, sauf si votre maison isolée fait moins de 50 m² de surface de plancher",
        dpeExempt + " " + dpeDuree + dpeLoc]);
    } else {
      dus.push(["Diagnostic de performance énergétique",
        maison ? "dû : une maison accolée n'est pas un bâtiment indépendant"
               : "dû sans condition de surface pour un lot en copropriété",
        dpeExempt + " " + dpeDuree + dpeLoc]);
    }

    /* ---- Audit énergétique ----
       CCH art. L126-28-1. Maison individuelle ou immeuble en monopropriété
       seulement, jamais un lot de copropriété. Sa condition — l'étiquette —
       n'est pas connue du simulateur : il va donc en « à vérifier ». */
    if (vente && maison) {
      selon.push(["Audit énergétique",
        "si l'étiquette du diagnostic de performance est E, F ou G",
        "Il propose des scénarios de travaux chiffrés pour atteindre une meilleure classe. Il "
        + "s'ajoute au diagnostic de performance, il ne le remplace pas, et il vaut cinq ans — "
        + "la moitié du diagnostic. Depuis le 1ᵉʳ janvier 2026, le coefficient de conversion "
        + "de l'électricité est passé de 2,3 à 1,9 : si le logement est chauffé à "
        + "l'électricité et que son diagnostic est antérieur, demandez d'abord la réédition "
        + "gratuite de l'attestation auprès de l'ADEME — l'étiquette peut s'améliorer sans un "
        + "seul travail."]);
    }

    /* ---- Plomb ---- CSP art. L1334-5 à L1334-7 : date de CONSTRUCTION. */
    if (e.construction === "oui") {
      dus.push(["Constat de risque d'exposition au plomb",
        "le logement a été construit avant le 1ᵉʳ janvier 1949",
        "Il mesure le plomb des peintures, revêtement par revêtement. En vente, il vaut un an "
        + "s'il est positif et sans limite s'il est négatif ; en location, six ans et sans "
        + "limite respectivement."]);
    } else if (e.construction === "inconnu") {
      selon.push(["Constat de risque d'exposition au plomb",
        "dû si le logement a été construit avant le 1ᵉʳ janvier 1949",
        "La date de construction figure sur l'acte de propriété, ou s'obtient en mairie."]);
    } else {
      hors.push(["Constat de risque d'exposition au plomb",
        "réservé aux logements construits avant 1949", ""]);
    }

    /* ---- Amiante ----
       En VENTE : état d'amiante, permis antérieur au 1ᵉʳ juillet 1997.
       En LOCATION : le 3° de l'article 3-3 de la loi du 6 juillet 1989 attend
       toujours son décret d'application. L'obligation qui existe est le
       dossier amiante des parties privatives (CSP art. R1334-29-4), qui ne
       vise QUE les parties privatives d'immeubles collectifs d'habitation :
       une maison individuelle mise en location en est exclue. */
    var amianteExpl = "Il recherche les matériaux amiantés accessibles sans travaux "
      + "destructifs. Un état négatif établi à compter du 1ᵉʳ avril 2013 n'a pas de limite de "
      + "validité ; établi avant cette date, il doit être refait, même négatif.";

    if (!vente && maison) {
      hors.push(["État d'amiante",
        "non exigé pour la mise en location d'une maison individuelle",
        "Le dossier amiante des parties privatives ne concerne que les appartements en "
        + "immeuble collectif. Pour une maison mise en location, aucun document amiante n'est "
        + "aujourd'hui exigible : le texte qui le prévoit attend son décret d'application."]);
    } else {
      var lib = vente ? "État d'amiante" : "Dossier amiante des parties privatives";
      var explFinale = vente ? amianteExpl
        : amianteExpl + " Il est tenu à la disposition du locataire et se communique sur "
          + "simple demande : il ne s'annexe pas au bail.";
      if (e.permis === "oui") {
        dus.push([lib, "le permis de construire est antérieur au 1ᵉʳ juillet 1997", explFinale]);
      } else if (e.permis === "inconnu") {
        selon.push([lib, "dû si le permis de construire est antérieur au 1ᵉʳ juillet 1997",
          explFinale]);
      } else {
        hors.push([lib, "réservé aux permis antérieurs à juillet 1997", ""]);
      }
    }

    /* ---- Gaz ---- CCH art. R134-6 : réalisation depuis plus de quinze ans. */
    if (e.gaz === "oui") {
      dus.push(["État de l'installation intérieure de gaz",
        "l'installation a été réalisée depuis plus de quinze ans",
        "Il porte sur la tuyauterie fixe, les raccordements, la ventilation et la combustion. "
        + "Il vaut trois ans en vente, six ans en location. Un certificat de conformité visé "
        + "par un organisme agréé et établi depuis moins de trois ans peut en tenir lieu."]);
    } else if (e.gaz === "inconnu") {
      selon.push(["État de l'installation intérieure de gaz",
        "dû si l'installation a été réalisée depuis plus de quinze ans",
        "Les quinze ans se comptent depuis la réalisation de l'installation."]);
    } else if (e.gaz === "non") {
      hors.push(["État de l'installation intérieure de gaz",
        "l'installation a moins de quinze ans", ""]);
    }

    /* ---- Électricité ---- CCH art. R134-10, même logique. */
    if (e.elec === "oui") {
      dus.push(["État de l'installation intérieure d'électricité",
        "l'installation a été réalisée depuis plus de quinze ans",
        "Il vérifie l'appareil général de commande, la protection différentielle, la prise de "
        + "terre et les matériels vétustes. Trois ans en vente, six en location."]);
    } else if (e.elec === "inconnu") {
      selon.push(["État de l'installation intérieure d'électricité",
        "dû si l'installation a été réalisée depuis plus de quinze ans",
        "Le tableau électrique donne souvent la réponse au premier coup d'œil."]);
    } else {
      hors.push(["État de l'installation intérieure d'électricité",
        "l'installation a moins de quinze ans", ""]);
    }

    /* ---- Surface ----
       Loi du 10 juillet 1965, art. 46 : tout LOT DE COPROPRIÉTÉ, et non le
       seul appartement. En location, la surface habitable dite loi Boutin
       relève de l'article 3 de la loi du 6 juillet 1989. */
    if (vente) {
      var enCopro = !maison || e.copro === "oui";
      var carrezExpl = "Elle exclut les surfaces sous 1,80 m de hauteur, les caves, garages "
        + "et terrasses, et ne s'applique pas aux lots de moins de 8 m². Une erreur de plus de "
        + "5 % ouvre droit à une réduction du prix. Sa validité est illimitée, sauf travaux "
        + "modifiant la surface.";
      if (enCopro) {
        dus.push(["Surface privative — loi Carrez",
          "le bien est un lot de copropriété", carrezExpl]);
      } else if (maison && e.copro === "inconnu") {
        selon.push(["Surface privative — loi Carrez",
          "due si votre maison est un lot de copropriété", carrezExpl]);
      }
    } else {
      selon.push(["Surface habitable — loi Boutin",
        "à indiquer dans le contrat de location",
        "Ce n'est pas un diagnostic et aucune certification n'est exigée, mais une surface "
        + "surévaluée de plus d'un vingtième ouvre au locataire une action en diminution du "
        + "loyer."]);
    }

    /* ---- Assainissement ---- CSP art. L1331-11-1. */
    if (vente) {
      if (e.assain === "autonome") {
        dus.push(["Diagnostic de l'assainissement des eaux usées",
          "le logement n'est pas raccordé au réseau public",
          "Il est réalisé par le service public d'assainissement non collectif de votre "
          + "commune, et doit dater de moins de trois ans à la date de l'acte."]);
      } else if (e.assain === "inconnu") {
        selon.push(["Diagnostic de l'assainissement des eaux usées",
          "dû si le logement n'est pas raccordé au réseau public",
          "Votre facture d'eau indique si vous êtes raccordé au réseau collectif."]);
      } else {
        selon.push(["Contrôle de raccordement au réseau public",
          "sur certains territoires seulement, ou en présence d'un règlement de service",
          "Il n'est pas dû partout : à vérifier auprès de votre commune."]);
      }
    }

    /* ---- Chauffage au bois ----
       CCH art. L271-4 I, 11°, ajouté par la loi n°2024-322 du 9 avril 2024. */
    if (vente && e.bois === "oui") {
      selon.push(["Certificat de conformité de l'appareil de chauffage au bois",
        "si le logement se trouve dans le périmètre d'un plan de protection de l'atmosphère",
        "L'agglomération bordelaise est couverte par un tel plan. Le certificat atteste que "
        + "l'appareil respecte les performances exigées ; il rejoint le dossier de vente "
        + "depuis avril 2024."]);
    }

    /* ---- Ce qui dépend de l'adresse ---- */
    selon.push(["État des risques",
      "en zone ou périmètre à risques : naturels, miniers, technologiques, sismiques, radon, "
      + "recul du trait de côte, sols pollués, retrait-gonflement des argiles, ou zone soumise "
      + "à obligation de débroussaillement",
      "Il dépend entièrement de l'adresse. Le vendeur ou le bailleur peut l'établir lui-même, "
      + "il se remet dès la première visite, et l'annonce doit renvoyer à georisques.gouv.fr. "
      + "Il doit dater de moins de six mois à la signature — et être refait, même dans ce "
      + "délai, si le zonage a changé entre-temps."]);
    selon.push(["Diagnostic bruit",
      "en zone d'exposition au bruit des aéroports",
      "Il dépend de l'adresse. Comme l'état des risques, il peut être établi sans "
      + "diagnostiqueur."]);

    if (vente) {
      selon.push(["État relatif à la présence de termites",
        "en zone déclarée par arrêté préfectoral",
        "La Gironde est concernée sur une large part de son territoire. L'état vaut six "
        + "mois : une infestation évolue vite."]);
      /* CCH art. L271-4 I, 9° : ce n'est pas un diagnostic mais une
         information jointe au dossier. La fiche du site la mentionne déjà. */
      selon.push(["Information sur la présence d'un risque de mérule",
        "en zone délimitée par arrêté préfectoral",
        "Ce n'est pas un diagnostic : c'est une information à porter dans la promesse ou dans "
        + "l'acte, qui se vérifie auprès de la préfecture."]);
      /* CCH art. L126-35-2 : travaux ayant une INCIDENCE SIGNIFICATIVE sur la
         performance énergétique, liste limitative du décret n°2022-1674. */
      selon.push(["Carnet d'information du logement",
        "si un permis ou une déclaration préalable a été déposé depuis le 1ᵉʳ janvier 2023, ou "
        + "en cas de travaux ayant une incidence significative sur la performance énergétique "
        + "depuis cette date",
        "Les travaux visés sont limitativement énumérés : isolation des murs, des toitures ou "
        + "des planchers bas, remplacement des menuiseries extérieures, installation ou "
        + "remplacement d'un système de chauffage, d'eau chaude sanitaire ou de ventilation."]);
      /* CCH art. L271-4 I, 12°, loi n°2024-322 du 9 avril 2024. */
      selon.push(["Arrêtés de police de la sécurité et de la salubrité",
        "s'il en existe sur le logement ou sur l'immeuble",
        "Arrêté de mise en sécurité, de traitement de l'insalubrité : ils se joignent au "
        + "dossier depuis avril 2024. Ils ne se commandent pas, ils se produisent."]);
    }

    return { dus: dus, selon: selon, hors: hors };
  }

  /* ---------------------------------------------------------------- rendu */
  var idx = 0, visibles = [];

  function majVisibles() {
    visibles = QUESTIONS.filter(function (q) { return !q.quand || q.quand(etat); });
  }

  function barre() {
    majVisibles();
    var n = visibles.length || 1;
    var pct = Math.round((Math.min(idx, n) / n) * 100);
    return '<div class="simu__barre"><i style="width:' + pct + '%"></i></div>';
  }

  function rendreQuestion() {
    majVisibles();
    if (idx >= visibles.length) return rendreResultat();
    var q = visibles[idx];
    var h = barre()
      + '<p class="simu__etape">Question ' + (idx + 1) + " sur " + visibles.length + "</p>"
      + '<h3 class="simu__titre">' + q.titre + "</h3>"
      + '<p class="simu__aide">' + q.aide + "</p>"
      + '<div class="simu__choix">';
    q.choix.forEach(function (c) {
      h += '<button type="button" class="simu__opt" data-v="' + c.v + '">'
        + '<span class="simu__opt-t">' + c.t + "</span>"
        + (c.s ? '<span class="simu__opt-s">' + c.s + "</span>" : "")
        + '<span class="simu__opt-fl" aria-hidden="true">→</span></button>';
    });
    h += "</div>"
      + '<details class="simu__pourquoi"><summary>Pourquoi cette question ?</summary>'
      + "<p>" + q.pourquoi + "</p></details>";
    if (idx > 0) h += '<button type="button" class="simu__retour">← Question précédente</button>';
    racine.innerHTML = h;
    racine.classList.remove("simu--entre");
    void racine.offsetWidth;
    racine.classList.add("simu--entre");

    Array.prototype.forEach.call(racine.querySelectorAll(".simu__opt"), function (b) {
      b.addEventListener("click", function () {
        etat[q.cle] = b.getAttribute("data-v");
        idx++;
        rendreQuestion();
      });
    });
    var r = racine.querySelector(".simu__retour");
    if (r) r.addEventListener("click", function () { idx--; rendreQuestion(); });
  }

  function ligne(x, cls) {
    return '<li class="simu__item ' + cls + '">'
      + '<span class="simu__item-t">' + x[0] + "</span>"
      + '<span class="simu__item-c">' + x[1] + "</span>"
      + (x[2] ? '<span class="simu__item-e">' + x[2] + "</span>" : "")
      + "</li>";
  }

  /* Le récapitulatif envoyé avec la demande : les réponses, puis les
     documents. Un devis se chiffre là-dessus, sans un appel de plus. */
  function recap(r) {
    var L = {
      operation: { vente: "vente", location: "mise en location" },
      bien: { appartement: "appartement en copropriété", maison: "maison individuelle" },
      mitoyen: { isolee: "maison isolée", mitoyenne: "maison mitoyenne ou accolée" },
      copro: { oui: "en copropriété", non: "hors copropriété", inconnu: "régime à vérifier" },
      construction: {
        oui: "construit avant 1949", non: "construit après 1949",
        inconnu: "date de construction inconnue",
      },
      permis: {
        oui: "permis antérieur à juillet 1997", non: "permis postérieur à juillet 1997",
        inconnu: "date du permis inconnue",
      },
      gaz: {
        oui: "gaz réalisé depuis plus de 15 ans", non: "gaz de moins de 15 ans",
        aucun: "pas de gaz", inconnu: "âge du gaz inconnu",
      },
      elec: {
        oui: "électricité réalisée depuis plus de 15 ans",
        non: "électricité de moins de 15 ans", inconnu: "âge de l'électricité inconnu",
      },
      assain: {
        autonome: "assainissement autonome", collectif: "tout-à-l'égout",
        inconnu: "assainissement inconnu",
      },
      bois: {
        oui: "chauffage au bois", non: "pas de chauffage au bois",
        inconnu: "chauffage au bois à vérifier",
      },
    };
    var lignes = ["SITUATION DÉCLARÉE PAR LE VISITEUR", ""];
    Object.keys(L).forEach(function (k) {
      if (etat[k] && L[k][etat[k]]) lignes.push("· " + L[k][etat[k]]);
    });
    lignes.push("", "DOCUMENTS DUS D'APRÈS SES RÉPONSES", "");
    (r.dus || []).forEach(function (x) { lignes.push("· " + x[0] + " — " + x[1]); });
    if ((r.selon || []).length) {
      lignes.push("", "À VÉRIFIER SELON L'ADRESSE", "");
      (r.selon || []).forEach(function (x) { lignes.push("· " + x[0]); });
    }
    return lignes.join("\n");
  }

  function rendreResultat() {
    var r = calculer(etat);
    var quoi = etat.operation === "vente" ? "vendre" : "mettre en location";
    var bien = etat.bien === "maison" ? "cette maison" : "cet appartement";

    var h = barre()
      + '<p class="simu__etape">Votre situation</p>'
      + '<h3 class="simu__titre">Pour ' + quoi + " " + bien + "</h3>"
      + '<p class="simu__aide">Cette liste découle de vos réponses. Elle vous donne une base '
      + "solide : seule une vérification sur pièces et sur place l'arrête définitivement.</p>";

    if (r.dus.length) {
      h += '<h4 class="simu__sous">Ce qui est dû dans votre cas</h4>'
        + '<ul class="simu__liste">'
        + r.dus.map(function (x) { return ligne(x, "simu--du"); }).join("") + "</ul>";
    }
    if (r.selon.length) {
      h += '<h4 class="simu__sous">Ce qui dépend de l\'adresse ou d\'un point à vérifier</h4>'
        + '<ul class="simu__liste">'
        + r.selon.map(function (x) { return ligne(x, "simu--selon"); }).join("") + "</ul>";
    }
    if (r.hors.length) {
      h += '<h4 class="simu__sous">Ce qui ne vous concerne pas</h4>'
        + '<ul class="simu__liste">'
        + r.hors.map(function (x) { return ligne(x, "simu--hors"); }).join("") + "</ul>";
    }

    h += '<div class="simu__place"></div>'
      + '<button type="button" class="simu__retour">← Reprendre le questionnaire</button>';

    racine.innerHTML = h;
    racine.classList.remove("simu--entre");
    void racine.offsetWidth;
    racine.classList.add("simu--entre");
    racine.querySelector(".simu__retour").addEventListener("click", function () {
      idx = 0;
      rendreQuestion();
    });

    /* La demande de devis vient d'un module partagé avec les autres
       simulateurs : deux implémentations du même formulaire finiraient par
       diverger, et c'est celle qu'on oublie qui casse. Elle s'ajoute APRÈS le
       résultat : le visiteur a sa réponse complète sans rien avoir donné. */
    if (window.DGLM_RAPPEL) {
      window.DGLM_RAPPEL(racine.querySelector(".simu__place"), {
        objet: "Demande de devis — "
          + (etat.operation === "vente" ? "vente" : "location") + " — particulier",
        titre: "Nous établissons ce dossier.",
        phrase: "Il nous manque trois choses pour vous répondre avec un prix ferme : où se "
          + "trouve le bien, sa surface, et comment vous joindre. Le reste, vous venez de "
          + "nous le dire.",
        recap: recap(r),
      });
    }
  }

  rendreQuestion();
})();
