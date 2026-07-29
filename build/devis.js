/* Demande de devis — DGLM Expertises
   Formulaire adaptatif : les questions posées dépendent de la mission choisie.
   Objectif : que le devis puisse être établi sans rappel préalable.

   Aucun framework. Aucune donnée conservée côté navigateur. */
(function () {
  "use strict";

  var CFG = window.DEVIS_CFG || {};

  /* ---------- questions communes ---------- */
  var CONTACT = [
    { id: "qualite", label: "Vous êtes", type: "select", requis: true, options: [
      "Syndic professionnel", "Conseil syndical ou syndic bénévole",
      "Bailleur ou administrateur de biens", "Maître d'ouvrage",
      "Entreprise de travaux", "Architecte ou maître d'œuvre",
      "Collectivité ou bailleur social", "Particulier" ] },
    { id: "societe", label: "Société ou copropriété", type: "text", requis: true,
      aide: "Nom du cabinet, du syndicat ou de la structure" },
    { id: "nom", label: "Nom et prénom", type: "text", requis: true },
    { id: "email", label: "Courriel", type: "email", requis: true },
    { id: "tel", label: "Téléphone", type: "tel", requis: true }
  ];

  var BIEN = [
    { id: "adresse", label: "Adresse du bien", type: "text", requis: true,
      aide: "Numéro, rue, code postal et commune" },
    { id: "typologie", label: "Type de bâtiment", type: "select", requis: true, options: [
      "Immeuble collectif d'habitation", "Maison ou immeuble en division",
      "Bureaux ou commerce", "Bâtiment industriel ou entrepôt",
      "Équipement public", "Bâtiment agricole ou viticole" ] },
    { id: "annee", label: "Année de construction", type: "select", requis: true, options: [
      "Avant 1949", "De 1949 à 1975", "De 1976 à 1988",
      "De 1989 au 30 juin 1997", "Après le 1er juillet 1997", "Je ne sais pas" ] },
    { id: "niveaux", label: "Nombre de niveaux", type: "number", min: 1, max: 40 },
    { id: "occupe", label: "Le bâtiment est-il occupé ?", type: "select", options: [
      "Occupé", "Partiellement occupé", "Vide" ] }
  ];

  /* ---------- questions propres à chaque mission ---------- */
  var MISSIONS = {
    raat: {
      nom: "Repérage amiante avant travaux",
      champs: [
        { id: "nature", label: "Nature des travaux prévus", type: "textarea", requis: true,
          aide: "Ravalement, remplacement de menuiseries, réfection de toiture, reprise de réseaux…" },
        { id: "perimetre", label: "Périmètre concerné", type: "checks", options: [
          "Façades", "Toiture", "Parties communes intérieures", "Logements",
          "Caves et sous-sol", "Chaufferie et locaux techniques", "Extérieurs" ] },
        { id: "surface", label: "Surface approximative concernée (m²)", type: "number", min: 1 },
        { id: "logements", label: "Nombre de logements concernés", type: "number", min: 0 },
        { id: "dta", label: "Un dossier technique amiante existe-t-il ?", type: "select", options: [
          "Oui, récent (moins de 10 ans)", "Oui, ancien", "Non", "Je ne sais pas" ] },
        { id: "acces", label: "Accès en hauteur nécessaire ?", type: "select", options: [
          "Non", "Échafaudage déjà prévu", "Nacelle nécessaire", "À déterminer" ] }
      ]
    },
    raad: {
      nom: "Repérage amiante avant démolition",
      champs: [
        { id: "nature", label: "Nature de l'opération", type: "select", requis: true, options: [
          "Démolition totale", "Démolition partielle", "Curage avant restructuration" ] },
        { id: "surface", label: "Surface de plancher à démolir (m²)", type: "number", requis: true, min: 1 },
        { id: "batiments", label: "Nombre de bâtiments", type: "number", min: 1 },
        { id: "coupe", label: "Le bâtiment est-il vidé et les fluides coupés ?", type: "select",
          requis: true, options: [
          "Oui, entièrement", "Coupure prévue avant intervention", "Non, encore en service" ],
          aide: "Un repérage avant démolition sur bâtiment en service est nécessairement incomplet" },
        { id: "pemd", label: "Diagnostic PEMD également nécessaire ?", type: "select", options: [
          "Oui, à chiffrer ensemble", "Déjà réalisé", "À déterminer avec vous" ] },
        { id: "plans", label: "Plans disponibles ?", type: "select", options: [
          "Oui, plans complets", "Plans partiels", "Non" ] }
      ]
    },
    dtg: {
      nom: "Diagnostic technique global",
      champs: [
        { id: "motif", label: "Motif de la demande", type: "select", requis: true, options: [
          "Mise en copropriété", "Procédure de péril", "Décision volontaire de l'AG",
          "Préparation d'un plan de travaux", "Projet de rénovation énergétique" ] },
        { id: "lots", label: "Nombre total de lots", type: "number", requis: true, min: 2 },
        { id: "lots_princ", label: "dont lots principaux (logements, commerces)", type: "number", min: 1 },
        { id: "batiments", label: "Nombre de bâtiments", type: "number", min: 1 },
        { id: "cages", label: "Nombre de cages d'escalier", type: "number", min: 1 },
        { id: "equip", label: "Équipements communs présents", type: "checks", options: [
          "Chauffage collectif", "Ascenseur", "Parking souterrain", "Espaces verts",
          "Local vélos ou poussettes", "Ventilation mécanique", "Portail motorisé" ] },
        { id: "docs", label: "Documents disponibles", type: "checks", options: [
          "Règlement de copropriété", "Carnet d'entretien", "Dossier technique amiante",
          "DPE collectif", "Derniers procès-verbaux d'AG", "Plans", "Devis de travaux récents" ] }
      ]
    },
    pppt: {
      nom: "Plan pluriannuel de travaux",
      champs: [
        { id: "lots", label: "Nombre total de lots", type: "number", requis: true, min: 2 },
        { id: "batiments", label: "Nombre de bâtiments", type: "number", min: 1 },
        { id: "dtg_fait", label: "Un DTG a-t-il déjà été réalisé ?", type: "select", options: [
          "Oui, de moins de 10 ans", "Oui, plus ancien", "Non" ],
          aide: "Un DTG récent et complet peut valoir plan pluriannuel" },
        { id: "equip", label: "Équipements communs présents", type: "checks", options: [
          "Chauffage collectif", "Ascenseur", "Parking souterrain", "Ventilation mécanique",
          "Toiture-terrasse", "Façades en pierre", "Menuiseries d'origine" ] },
        { id: "ag", label: "Date de la prochaine assemblée générale", type: "date",
          aide: "Pour caler notre délai sur votre calendrier de vote" },
        { id: "travaux", label: "Travaux déjà envisagés", type: "textarea",
          aide: "Ravalement, toiture, ascenseur, chaufferie… même à l'état d'intention" }
      ]
    },
    autre: {
      nom: "Autre mission",
      champs: [
        { id: "mission", label: "Mission souhaitée", type: "select", requis: true, options: [
          "Dossier technique amiante (DTA)", "Amiante parties privatives (DAPP)",
          "Diagnostic PEMD", "DPE collectif", "Audit énergétique de copropriété",
          "Constat plomb des parties communes", "État parasitaire",
          "Installations collectives gaz et électricité",
          "Conformité assainissement", "Plusieurs missions" ] },
        { id: "detail", label: "Précisions", type: "textarea", requis: true,
          aide: "Décrivez le besoin : nous revenons vers vous avec les questions manquantes" }
      ]
    }
  };

  var DELAI = { id: "delai", label: "Délai souhaité", type: "select", requis: true, options: [
    "Urgent — sous 8 jours", "Sous 15 jours", "Sous un mois",
    "Avant la prochaine assemblée générale", "Pas de contrainte particulière" ] };
  var NOTE = { id: "note", label: "Autre information utile", type: "textarea",
    aide: "Contraintes d'accès, interlocuteur sur place, particularité du bâtiment…" };

  /* ---------- rendu ---------- */
  var form = document.getElementById("devis");
  if (!form) return;
  var zoneMission = document.getElementById("devis-mission");
  var etat = document.getElementById("devis-etat");
  var choix = null;

  function champ(c) {
    var id = "f_" + c.id;
    var req = c.requis ? ' required aria-required="true"' : "";
    var h = '<label class="field" for="' + id + '"><span>' + c.label +
            (c.requis ? ' <abbr title="obligatoire" style="color:#A8321F;text-decoration:none">*</abbr>' : "") +
            "</span>";
    if (c.type === "select") {
      h += '<select id="' + id + '" name="' + c.id + '"' + req + '><option value="">— choisir —</option>' +
           c.options.map(function (o) { return '<option>' + o + "</option>"; }).join("") + "</select>";
    } else if (c.type === "textarea") {
      h += '<textarea id="' + id + '" name="' + c.id + '" rows="3"' + req + "></textarea>";
    } else if (c.type === "checks") {
      h = '<fieldset class="field checks"><legend>' + c.label + "</legend>" +
          c.options.map(function (o, i) {
            return '<label class="check"><input type="checkbox" name="' + c.id +
                   '" value="' + o + '"> <span>' + o + "</span></label>";
          }).join("");
      return h + (c.aide ? '<em>' + c.aide + "</em>" : "") + "</fieldset>";
    } else {
      h += '<input id="' + id + '" name="' + c.id + '" type="' + c.type + '"' + req +
           (c.min !== undefined ? ' min="' + c.min + '"' : "") +
           (c.max !== undefined ? ' max="' + c.max + '"' : "") +
           (c.type === "tel" ? ' inputmode="tel" autocomplete="tel"' : "") +
           (c.type === "email" ? ' inputmode="email" autocomplete="email"' : "") + ">";
    }
    if (c.aide) h += "<em>" + c.aide + "</em>";
    return h + "</label>";
  }

  function bloc(titre, champs) {
    return '<div class="devis__bloc"><h3>' + titre + "</h3>" +
           champs.map(champ).join("") + "</div>";
  }

  function rendre(cle) {
    choix = cle;
    var m = MISSIONS[cle];
    zoneMission.innerHTML =
      bloc("2 · Le bien concerné", BIEN) +
      bloc("3 · " + m.nom, m.champs) +
      bloc("4 · Délai et compléments", [DELAI, NOTE]);
    zoneMission.hidden = false;
    document.getElementById("devis-envoi").hidden = false;
    zoneMission.querySelector("input,select,textarea").focus();
    etat.textContent = "Questionnaire adapté à la mission : " + m.nom + ".";
  }

  document.getElementById("devis-choix").innerHTML =
    Object.keys(MISSIONS).map(function (k) {
      return '<button type="button" class="mission" data-m="' + k + '">' +
             '<b>' + MISSIONS[k].nom + "</b></button>";
    }).join("");

  document.getElementById("devis-choix").addEventListener("click", function (e) {
    var b = e.target.closest(".mission");
    if (!b) return;
    Array.prototype.forEach.call(this.querySelectorAll(".mission"), function (x) {
      x.setAttribute("aria-pressed", x === b ? "true" : "false");
    });
    rendre(b.dataset.m);
  });

  /* ---------- récapitulatif ---------- */
  function collecter() {
    var out = [], vus = {};
    var libelle = {};
    [CONTACT, BIEN, MISSIONS[choix].champs, [DELAI, NOTE]].forEach(function (g) {
      g.forEach(function (c) { libelle[c.id] = c.label; });
    });
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.name === "_gotcha") return;
      if (el.type === "checkbox") {
        if (!el.checked) return;
        vus[el.name] = (vus[el.name] || []).concat(el.value);
        return;
      }
      if (!el.value.trim()) return;
      out.push([libelle[el.name] || el.name, el.value.trim()]);
    });
    Object.keys(vus).forEach(function (k) {
      out.push([libelle[k] || k, vus[k].join(", ")]);
    });
    return out;
  }

  function texte() {
    var l = ["DEMANDE DE DEVIS — " + MISSIONS[choix].nom, ""];
    collecter().forEach(function (p) { l.push(p[0] + " : " + p[1]); });
    l.push("", "Transmis depuis dglmexpertises.fr le " +
      new Date().toLocaleDateString("fr-FR", { day: "2-digit", month: "long", year: "numeric" }));
    return l.join("\n");
  }

  /* ---------- envoi ---------- */
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    if (form.elements._gotcha && form.elements._gotcha.value) return;

    var bouton = document.getElementById("devis-submit");
    bouton.disabled = true;
    etat.className = "devis__etat";
    etat.textContent = "Envoi en cours…";

    if (!CFG.cle) return replier();

    var data = new FormData(form);
    data.append("access_key", CFG.cle);
    data.append("subject", CFG.objet + " — " + MISSIONS[choix].nom);
    data.append("from_name", "Site DGLM Expertises");
    data.append("recapitulatif", texte());

    fetch(CFG.endpoint, { method: "POST", body: data })
      .then(function (r) { return r.json(); })
      .then(function (r) {
        if (!r.success) throw new Error(r.message || "échec");
        succes();
      })
      .catch(replier);
  });

  function succes() {
    form.hidden = true;
    var ok = document.getElementById("devis-succes");
    ok.hidden = false;
    ok.focus();
  }

  function replier() {
    /* Relais indisponible ou non configuré : on passe par la messagerie du
       visiteur, avec le récapitulatif complet déjà rédigé. Rien n'est perdu. */
    var sujet = encodeURIComponent(CFG.objet + " — " + MISSIONS[choix].nom);
    var corps = encodeURIComponent(texte());
    var lien = "mailto:" + CFG.destinataire + "?subject=" + sujet + "&body=" + corps;
    etat.className = "devis__etat devis__etat--warn";
    etat.innerHTML = 'Votre logiciel de messagerie va s\'ouvrir avec la demande ' +
      'pré-remplie. <a href="' + lien + '">Ouvrir maintenant</a> — ou ' +
      '<button type="button" id="copier" class="lien">copier le récapitulatif</button>.';
    document.getElementById("devis-submit").disabled = false;
    try { window.location.href = lien; } catch (x) {}
    var c = document.getElementById("copier");
    if (c) c.addEventListener("click", function () {
      navigator.clipboard.writeText(texte()).then(function () {
        c.textContent = "récapitulatif copié";
      });
    });
  }
})();
