/* SIMULATEUR — QUELS DIAGNOSTICS POUR MON LOGEMENT ?

   Ce site est dédié à la copropriété et aux travaux. Les particuliers qui
   arrivaient ici par une question de vente ou de location étaient redirigés
   ailleurs au bout de quatre secondes : nous perdions le visiteur avant même
   de lui avoir répondu.

   Ce simulateur répond à sa question, explique chaque réponse, puis donne le
   moyen de nous joindre. Il ne vise aucune requête — la page reste non
   indexée — il retient ceux qui sont déjà là.

   SOURCE DES RÈGLES : les deux fiches publiées du site,
   /questions/diagnostics-obligatoires-vente/ et
   /questions/diagnostics-obligatoires-location/, elles-mêmes sourcées sur
   Service Public et le code de la construction et de l'habitation. Aucune
   règle n'est écrite ici qui n'y figure déjà.

   TOUTE MODIFICATION D'UNE RÈGLE DOIT ÊTRE RÉPERCUTÉE DANS CES DEUX FICHES,
   et inversement : deux sources qui divergent valent moins qu'une seule. */
(function () {
  "use strict";
  var racine = document.getElementById("simu-part");
  if (!racine) return;

  var CFG = window.DGLM_PART || {};
  var etat = {};

  /* Chaque question porte son aide courte, visible d'emblée, et son aide
     longue, dépliable — le lecteur qui sait avance, celui qui doute
     comprend. */
  var QUESTIONS = [
    {
      cle: "operation",
      titre: "Que souhaitez-vous faire ?",
      aide: "Onze documents peuvent composer un dossier de vente, six un dossier de location.",
      pourquoi: "La vente engage le vendeur sur la garantie des vices cachés : "
        + "le dossier y est plus étendu, et il s'annexe à la promesse ou à l'acte. "
        + "La location, elle, protège le locataire pendant toute la durée du bail : "
        + "le dossier s'y annexe à la signature et à chaque renouvellement.",
      choix: [
        { v: "vente", t: "Vendre ce logement", s: "Maison ou appartement" },
        { v: "location", t: "Le mettre en location", s: "Bail d'habitation" },
      ],
    },
    {
      cle: "bien",
      titre: "De quel bien s'agit-il ?",
      aide: "Un lot en copropriété et une maison individuelle n'appellent pas la même liste.",
      pourquoi: "Pour un appartement, la performance énergétique est due sans condition "
        + "de surface, l'audit énergétique ne s'applique pas, et la surface privative — "
        + "dite loi Carrez — doit figurer dans l'acte. Pour une maison, l'audit "
        + "énergétique entre en jeu selon l'étiquette, et l'assainissement autonome "
        + "appelle son propre contrôle.",
      choix: [
        { v: "appartement", t: "Un appartement", s: "En copropriété" },
        { v: "maison", t: "Une maison", s: "Individuelle" },
      ],
    },
    {
      cle: "epoque",
      titre: "De quand date le permis de construire ?",
      aide: "Deux dates commandent presque tout : 1949 pour le plomb, juillet 1997 pour l'amiante.",
      pourquoi: "Les peintures au plomb ont été interdites dans l'habitation en 1949 : "
        + "un logement antérieur appelle un constat de risque d'exposition. L'amiante a "
        + "été interdite au 1ᵉʳ janvier 1997, et le critère retenu par les textes est la "
        + "date de délivrance du permis de construire, antérieure au 1ᵉʳ juillet 1997. "
        + "Si vous ne savez pas, l'acte de propriété ou la mairie vous le diront.",
      choix: [
        { v: "avant1949", t: "Avant 1949", s: "Plomb et amiante possibles" },
        { v: "1949a1997", t: "De 1949 à juillet 1997", s: "Amiante possible" },
        { v: "apres1997", t: "Après juillet 1997", s: "Ni plomb ni amiante" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      cle: "gaz",
      titre: "L'installation de gaz a-t-elle plus de quinze ans ?",
      aide: "S'il n'y a pas de gaz dans le logement, la question ne se pose pas.",
      pourquoi: "L'état de l'installation intérieure de gaz est dû dès lors que "
        + "l'installation a plus de quinze ans, en vente comme en location. L'âge se "
        + "compte depuis la mise en service, ou depuis la dernière réfection complète. "
        + "Un certificat de conformité de moins de quinze ans peut en tenir lieu.",
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
      aide: "L'âge se compte depuis la dernière réfection complète de l'installation.",
      pourquoi: "Même règle que pour le gaz : au-delà de quinze ans, l'état de "
        + "l'installation intérieure d'électricité est dû, en vente comme en location. "
        + "Le tableau électrique en dit souvent long : disjoncteur différentiel, prises "
        + "de terre et fusibles à cartouche ne datent pas de la même époque.",
      choix: [
        { v: "oui", t: "Plus de quinze ans", s: "" },
        { v: "non", t: "Moins de quinze ans", s: "" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
    {
      cle: "assain",
      titre: "Comment le logement évacue-t-il ses eaux usées ?",
      aide: "Une installation autonome appelle un contrôle propre.",
      pourquoi: "En vente d'une maison, le diagnostic de l'assainissement est dû lorsque "
        + "l'installation est autonome — fosse toutes eaux, micro-station, filtre à "
        + "sable. Sur certains territoires, ou en présence d'un arrêté municipal, un "
        + "contrôle est également demandé en assainissement collectif.",
      quand: function (e) { return e.bien === "maison" && e.operation === "vente"; },
      choix: [
        { v: "autonome", t: "Installation autonome", s: "Fosse, micro-station" },
        { v: "collectif", t: "Tout-à-l'égout", s: "Réseau collectif" },
        { v: "inconnu", t: "Je ne sais pas", s: "Nous le vérifierons" },
      ],
    },
  ];

  /* Chaque document du résultat porte sa condition ET son explication : ce
     qu'il est, et à quoi il sert. */
  function calculer(e) {
    var dus = [], selon = [], hors = [];
    var vente = e.operation === "vente";

    if (vente) {
      if (e.bien === "maison") {
        dus.push(["Diagnostic de performance énergétique", "dû dès 50 m² de surface de plancher",
          "Il classe le logement de A à G selon sa consommation et ses émissions. "
          + "Sa durée de validité est de dix ans."]);
        dus.push(["Audit énergétique", "si l'étiquette du diagnostic de performance est E, F ou G",
          "Il propose des scénarios de travaux chiffrés pour atteindre une meilleure "
          + "classe. Il s'ajoute au diagnostic de performance, il ne le remplace pas."]);
      } else {
        dus.push(["Diagnostic de performance énergétique",
          "dû sans condition de surface pour un lot en copropriété",
          "Il classe le logement de A à G. Pour un appartement, il peut s'appuyer sur "
          + "le diagnostic collectif de l'immeuble lorsqu'il existe."]);
      }
    } else {
      dus.push(["Diagnostic de performance énergétique",
        "sauf occupation de moins de quatre mois par an, monument historique, ou maison "
        + "individuelle indépendante de moins de 50 m²",
        "Depuis 2025, un logement classé G ne peut plus être proposé à la location "
        + "comme logement décent. Le calendrier se poursuit pour les classes F et E."]);
    }

    if (e.epoque === "avant1949") {
      dus.push(["Constat de risque d'exposition au plomb",
        "la construction est antérieure au 1ᵉʳ janvier 1949",
        "Il mesure le plomb des peintures, revêtement par revêtement. En vente, il vaut "
        + "un an s'il est positif, et sans limite s'il est négatif ; en location, six ans "
        + "et sans limite respectivement."]);
    } else if (e.epoque === "inconnu") {
      selon.push(["Constat de risque d'exposition au plomb",
        "dû si la construction est antérieure au 1ᵉʳ janvier 1949",
        "La date de construction figure sur l'acte de propriété, ou s'obtient en mairie."]);
    } else {
      hors.push(["Constat de risque d'exposition au plomb",
        "réservé aux constructions antérieures à 1949", ""]);
    }

    var appLoc = (e.bien === "appartement" && !vente);
    var lib = appLoc ? "Diagnostic amiante des parties privatives" : "État d'amiante";
    var cond = appLoc
      ? "tenu à la disposition du locataire, et non annexé au bail"
      : "le permis de construire est antérieur au 1ᵉʳ juillet 1997";
    var expl = appLoc
      ? "C'est le point le plus mal compris : l'obligation existe bien, mais le document "
        + "se tient à disposition sur demande plutôt que de s'annexer au bail."
      : "Il recherche les matériaux amiantés accessibles sans travaux destructifs. "
        + "Un état négatif établi après 2013 n'a pas de limite de validité.";
    if (e.epoque === "avant1949" || e.epoque === "1949a1997") {
      dus.push([lib, cond, expl]);
    } else if (e.epoque === "inconnu") {
      selon.push([lib, "dû si le permis de construire est antérieur au 1ᵉʳ juillet 1997", expl]);
    } else {
      hors.push([lib, "réservé aux permis antérieurs à juillet 1997", ""]);
    }

    if (e.gaz === "oui") {
      dus.push(["État de l'installation intérieure de gaz", "l'installation a plus de quinze ans",
        "Il porte sur la tuyauterie fixe, les raccordements, la ventilation et la "
        + "combustion. Il vaut trois ans en vente, six ans en location."]);
    } else if (e.gaz === "inconnu") {
      selon.push(["État de l'installation intérieure de gaz",
        "dû si l'installation a plus de quinze ans",
        "L'âge se compte depuis la mise en service ou la dernière réfection complète."]);
    } else if (e.gaz === "non") {
      hors.push(["État de l'installation intérieure de gaz",
        "l'installation a moins de quinze ans", ""]);
    }

    if (e.elec === "oui") {
      dus.push(["État de l'installation intérieure d'électricité",
        "l'installation a plus de quinze ans",
        "Il vérifie l'appareil général de commande, la protection différentielle, la "
        + "prise de terre et les matériels vétustes. Trois ans en vente, six en location."]);
    } else if (e.elec === "inconnu") {
      selon.push(["État de l'installation intérieure d'électricité",
        "dû si l'installation a plus de quinze ans",
        "Le tableau électrique donne souvent la réponse au premier coup d'œil."]);
    } else {
      hors.push(["État de l'installation intérieure d'électricité",
        "l'installation a moins de quinze ans", ""]);
    }

    if (vente && e.bien === "appartement") {
      dus.push(["Surface privative — loi Carrez", "à indiquer dans la promesse ou dans l'acte",
        "Elle exclut les surfaces sous 1,80 m de hauteur, les caves, garages et "
        + "terrasses. Une erreur de plus de 5 % ouvre droit à une réduction du prix."]);
    }

    if (vente && e.bien === "maison") {
      if (e.assain === "autonome") {
        dus.push(["Diagnostic de l'assainissement des eaux usées", "l'installation est autonome",
          "Il est réalisé par le service public d'assainissement non collectif de votre "
          + "commune, et vaut trois ans."]);
      } else if (e.assain === "inconnu") {
        selon.push(["Diagnostic de l'assainissement des eaux usées",
          "dû en installation autonome, et sur certains territoires en collectif",
          "Votre facture d'eau indique si vous êtes raccordé au réseau collectif."]);
      } else {
        selon.push(["Diagnostic de l'assainissement des eaux usées",
          "sur certains territoires, ou en présence d'un arrêté municipal",
          "À vérifier auprès de votre commune."]);
      }
    }

    selon.push(["État des risques",
      "en zone ou périmètre à risques : naturels, miniers, technologiques, sismiques, radon",
      "Il dépend entièrement de l'adresse du bien. Le bailleur ou le vendeur peut "
      + "l'établir lui-même, et il doit dater de moins de six mois."]);
    selon.push(["Diagnostic bruit",
      "en zone d'exposition au bruit des aéroports",
      "Il dépend de l'adresse. Comme l'état des risques, il peut être établi sans "
      + "diagnostiqueur."]);
    if (vente) {
      selon.push(["État relatif à la présence de termites",
        "en zone déclarée par arrêté préfectoral",
        "La Gironde est concernée sur une large part de son territoire. L'état vaut "
        + "six mois : une infestation évolue vite."]);
      selon.push(["Carnet d'information du logement",
        "si un permis ou une déclaration préalable a été déposé depuis le 1ᵉʳ janvier 2023, "
        + "ou en cas de travaux de rénovation depuis cette date",
        "Il rassemble les documents utiles à la performance énergétique du logement, et "
        + "se transmet à l'acquéreur."]);
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

  function rendreResultat() {
    var r = calculer(etat);
    var quoi = etat.operation === "vente" ? "vendre" : "mettre en location";
    var bien = etat.bien === "maison" ? "cette maison" : "cet appartement";

    var h = barre()
      + '<p class="simu__etape">Votre situation</p>'
      + '<h3 class="simu__titre">Pour ' + quoi + " " + bien + "</h3>"
      + '<p class="simu__aide">Cette liste découle de vos réponses. Elle vous donne une '
      + "base solide : seule une vérification sur pièces et sur place l'arrête "
      + "définitivement.</p>";

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
       simulateurs du site : deux implémentations du même formulaire finiraient
       par diverger, et c'est toujours celle qu'on oublie qui casse.

       Elle s'ajoute APRÈS le résultat : le visiteur a sa réponse complète
       sans rien avoir donné, puis il choisit. */
    if (window.DGLM_RAPPEL) {
      window.DGLM_RAPPEL(racine.querySelector(".simu__place"), {
        objet: "Demande de devis — "
          + (etat.operation === "vente" ? "vente" : "location") + " — particulier",
        titre: "Nous établissons ce dossier.",
        phrase: "Il nous manque trois choses pour vous répondre avec un prix ferme : "
          + "où se trouve le bien, sa surface, et comment vous joindre. Le reste, "
          + "vous venez de nous le dire.",
        recap: recap(r),
      });
    }
  }

  /* Le récapitulatif envoyé avec la demande : les six réponses, puis la liste
     des documents. Un devis se chiffre là-dessus, sans un appel de plus. */
  function recap(r) {
    var L = {
      operation: { vente: "vente", location: "mise en location" },
      bien: { appartement: "appartement en copropriété", maison: "maison individuelle" },
      epoque: {
        avant1949: "permis antérieur à 1949", "1949a1997": "permis de 1949 à juillet 1997",
        apres1997: "permis postérieur à juillet 1997", inconnu: "époque du permis inconnue",
      },
      gaz: {
        oui: "gaz de plus de 15 ans", non: "gaz de moins de 15 ans",
        aucun: "pas de gaz", inconnu: "âge du gaz inconnu",
      },
      elec: {
        oui: "électricité de plus de 15 ans", non: "électricité de moins de 15 ans",
        inconnu: "âge de l'électricité inconnu",
      },
      assain: {
        autonome: "assainissement autonome", collectif: "tout-à-l'égout",
        inconnu: "assainissement inconnu",
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


  rendreQuestion();
})();
