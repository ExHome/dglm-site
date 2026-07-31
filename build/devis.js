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
  var RECAP = new URLSearchParams(location.search).get("recap") || "";

  var MISSIONS = {
    raat: {
      nom: "Repérage amiante avant travaux",
      champs: [
        { id: "nature", label: "Nature des travaux prévus", type: "textarea", requis: true,
          aide: "Ravalement, remplacement de menuiseries, réfection de toiture, reprise de réseaux…" },
        { id: "perimetre", label: "Périmètre concerné", type: "checks", options: [
          "Façades", "Toiture", "Parties communes intérieures",
          "Intérieur de logements (cuisine, salle de bain, cloisons…)",
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
    dpe: {
      nom: "DPE collectif de copropriété",
      champs: [
        { id: "lots", label: "Nombre total de lots", type: "number", requis: true, min: 2 },
        { id: "batiments", label: "Nombre de bâtiments", type: "number", min: 1 },
        { id: "chauffage", label: "Mode de chauffage", type: "select", options: [
          "Chauffage collectif", "Chauffages individuels", "Mixte", "Je ne sais pas" ] },
        { id: "motif", label: "Motif de la demande", type: "select", options: [
          "Échéance réglementaire", "Projet de rénovation énergétique",
          "Demande de l'assemblée générale", "Autre" ] },
        { id: "dpe_prec", label: "Un DPE collectif a-t-il déjà été réalisé ?", type: "select", options: [
          "Oui, de moins de 10 ans", "Oui, plus ancien", "Non" ] }
      ]
    },
    autre: {
      nom: "Autre mission",
      champs: [
        { id: "mission", label: "Mission souhaitée", type: "select", requis: true, options: [
          "Dossier technique amiante (DTA)", "Amiante parties privatives (DAPP)",
          "Diagnostic PEMD", "Audit énergétique de copropriété",
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
  var PORTEE = { id: "portee", label: "Cette demande concerne", type: "select", options: [
    "Un seul immeuble ou site", "Plusieurs immeubles d'un même portefeuille" ],
    aide: "Gestionnaire d'un parc ? Listez les autres adresses dans le dernier champ : nous chiffrons le tout en une seule fois" };
  var NOTE = { id: "note", label: "Autre information utile", type: "textarea",
    aide: "Contraintes d'accès, interlocuteur sur place, particularité du bâtiment…" };

  /* aide au choix : à quoi sert chaque mission, en une ligne */
  var HINTS = {
    raat: "Vous rénovez, réhabilitez ou entretenez",
    raad: "Vous démolissez ou curez un bâtiment",
    dtg: "L'état complet de l'immeuble, poste par poste",
    pppt: "La feuille de route travaux sur dix ans",
    dpe: "L'étiquette énergie de l'immeuble entier",
    autre: "DTA, DAPP, plomb, PEMD, parasitaire…"
  };

  /* ---------- rendu ---------- */
  var form = document.getElementById("devis");
  if (!form) return;
  var zoneMission = document.getElementById("devis-mission");
  var etat = document.getElementById("devis-etat");
  var choix = null;

  /* ================= pièces jointes =================
     Site statique : aucun serveur ne peut recevoir un fichier. On assemble
     donc le dossier DANS le navigateur, en une seule archive que le client
     joint à l'e-mail préparé. Rien ne quitte son poste avant son geste. */
  var pieces = [];                    // [{fichier, id}]
  var LIMITE_TOTAL = 40 * 1024 * 1024; // au-delà, une messagerie refuse souvent
  var idPiece = 0;

  var TABLE_CRC = (function () {
    var t = new Uint32Array(256), c, n, k;
    for (n = 0; n < 256; n++) {
      c = n;
      for (k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
      t[n] = c >>> 0;
    }
    return t;
  })();

  function crc32(u8) {
    var c = 0xFFFFFFFF;
    for (var i = 0; i < u8.length; i++) c = TABLE_CRC[(c ^ u8[i]) & 0xFF] ^ (c >>> 8);
    return (c ^ 0xFFFFFFFF) >>> 0;
  }

  /* Noms translittérés : le dossier s'ouvre lisiblement sur n'importe quel
     poste, y compris avec les vieux utilitaires d'archive de Windows. */
  function assainirNom(nom) {
    var pt = nom.lastIndexOf("."), ext = "", base = nom;
    if (pt > 0) { ext = nom.slice(pt).toLowerCase(); base = nom.slice(0, pt); }
    base = base.normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/[^A-Za-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60);
    ext = ext.normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9.]/g, "");
    return (base || "piece") + ext;
  }

  function creerZip(fichiers) {
    var enc = new TextEncoder(), morceaux = [], central = [], offset = 0, d = new Date();
    var hh = ((d.getHours() << 11) | (d.getMinutes() << 5) | (d.getSeconds() / 2)) & 0xFFFF;
    var jj = (((d.getFullYear() - 1980) << 9) | ((d.getMonth() + 1) << 5) | d.getDate()) & 0xFFFF;

    fichiers.forEach(function (f) {
      var nom = enc.encode(f.nom), dat = f.donnees, crc = crc32(dat);
      var lh = new DataView(new ArrayBuffer(30));
      lh.setUint32(0, 0x04034B50, true); lh.setUint16(4, 20, true);
      lh.setUint16(6, 0x0800, true); lh.setUint16(8, 0, true);
      lh.setUint16(10, hh, true); lh.setUint16(12, jj, true);
      lh.setUint32(14, crc, true); lh.setUint32(18, dat.length, true);
      lh.setUint32(22, dat.length, true); lh.setUint16(26, nom.length, true);
      lh.setUint16(28, 0, true);
      morceaux.push(new Uint8Array(lh.buffer), nom, dat);

      var ch = new DataView(new ArrayBuffer(46));
      ch.setUint32(0, 0x02014B50, true); ch.setUint16(4, 20, true);
      ch.setUint16(6, 20, true); ch.setUint16(8, 0x0800, true);
      ch.setUint16(10, 0, true); ch.setUint16(12, hh, true); ch.setUint16(14, jj, true);
      ch.setUint32(16, crc, true); ch.setUint32(20, dat.length, true);
      ch.setUint32(24, dat.length, true); ch.setUint16(28, nom.length, true);
      ch.setUint32(42, offset, true);
      central.push(new Uint8Array(ch.buffer), nom);
      offset += 30 + nom.length + dat.length;
    });

    var tailleCentral = central.reduce(function (n, m) { return n + m.length; }, 0);
    var fin = new DataView(new ArrayBuffer(22));
    fin.setUint32(0, 0x06054B50, true);
    fin.setUint16(8, fichiers.length, true); fin.setUint16(10, fichiers.length, true);
    fin.setUint32(12, tailleCentral, true); fin.setUint32(16, offset, true);
    central.push(new Uint8Array(fin.buffer));

    var tout = morceaux.concat(central);
    var total = tout.reduce(function (n, m) { return n + m.length; }, 0);
    var out = new Uint8Array(total), p = 0;
    tout.forEach(function (m) { out.set(m, p); p += m.length; });
    return out;
  }

  function poids(o) {
    if (o < 1024) return o + " o";
    if (o < 1024 * 1024) return Math.round(o / 1024) + " Ko";
    return (o / 1024 / 1024).toFixed(1).replace(".", ",") + " Mo";
  }

  function totalPieces() {
    return pieces.reduce(function (n, p) { return n + p.fichier.size; }, 0);
  }

  function ajouter(liste) {
    Array.prototype.forEach.call(liste, function (f) {
      var doublon = pieces.some(function (p) {
        return p.fichier.name === f.name && p.fichier.size === f.size;
      });
      if (!doublon) pieces.push({ fichier: f, id: ++idPiece });
    });
    rendrePieces();
  }

  function rendrePieces() {
    var ul = document.getElementById("pieces-liste");
    var etatP = document.getElementById("pieces-etat");
    var actions = document.getElementById("pieces-actions");
    if (!ul) return;
    ul.innerHTML = pieces.map(function (p, i) {
      return '<li><span class="pieces__num">' + (i + 1) + '</span>' +
        '<span class="pieces__nom">' + p.fichier.name + "</span>" +
        '<span class="pieces__poids">' + poids(p.fichier.size) + "</span>" +
        '<button type="button" class="pieces__x" data-id="' + p.id +
        '" aria-label="Retirer ' + p.fichier.name + '">retirer</button></li>';
    }).join("");
    var t = totalPieces();
    if (!pieces.length) {
      etatP.textContent = "";
      actions.hidden = true;
    } else {
      etatP.textContent = pieces.length + " document" + (pieces.length > 1 ? "s" : "") +
        " · " + poids(t) +
        (t > LIMITE_TOTAL ? " — au-delà de 40 Mo, beaucoup de messageries refusent l'envoi : privilégiez un lien de partage." : "");
      etatP.className = "pieces__etat" + (t > LIMITE_TOTAL ? " pieces__etat--warn" : "");
      actions.hidden = false;
    }
  }

  function nomDossier() {
    var soc = (form.elements.societe && form.elements.societe.value) || "";
    var d = new Date(), p2 = function (n) { return (n < 10 ? "0" : "") + n; };
    return "DGLM-" + (choix || "devis").toUpperCase() +
      (soc ? "-" + assainirNom(soc).slice(0, 28) : "") +
      "-" + d.getFullYear() + p2(d.getMonth() + 1) + p2(d.getDate()) + ".zip";
  }

  function preparerZip() {
    var bouton = document.getElementById("pieces-zip");
    bouton.disabled = true;
    var libelle = bouton.textContent;
    bouton.textContent = "Préparation…";
    var lus = [];
    var suite = pieces.reduce(function (chaine, p, i) {
      return chaine.then(function () {
        return p.fichier.arrayBuffer().then(function (buf) {
          var p2 = function (n) { return (n < 10 ? "0" : "") + n; };
          lus.push({ nom: p2(i + 1) + "-" + assainirNom(p.fichier.name),
                     donnees: new Uint8Array(buf) });
        });
      });
    }, Promise.resolve());

    suite.then(function () {
      lus.push({ nom: "00-recapitulatif-demande.txt",
                 donnees: new TextEncoder().encode(texte()) });
      var zip = creerZip(lus);
      var url = URL.createObjectURL(new Blob([zip], { type: "application/zip" }));
      var a = document.createElement("a");
      a.href = url; a.download = nomDossier();
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
      bouton.disabled = false; bouton.textContent = libelle;
      document.getElementById("pieces-etat").innerHTML =
        "Dossier <strong>" + nomDossier() + "</strong> enregistré (" +
        pieces.length + " pièce" + (pieces.length > 1 ? "s" : "") +
        " + le récapitulatif). Joignez ce fichier unique à l'e-mail ci-dessous.";
    }).catch(function () {
      bouton.disabled = false; bouton.textContent = libelle;
      document.getElementById("pieces-etat").textContent =
        "La préparation du dossier a échoué. Joignez vos fichiers directement à l'e-mail.";
    });
  }

  /* mémo contextuel : les documents utiles à la mission choisie */
  function rendreMemo(cle) {
    var memo = document.getElementById("pieces-memo");
    var liste = document.getElementById("pieces-memo-liste");
    var docs = (window.DEVIS_DOCS || {})[cle];
    if (!memo || !liste || !docs || !docs.length) { if (memo) memo.hidden = true; return; }
    liste.innerHTML = docs.map(function (d) { return "<li>" + d + "</li>"; }).join("");
    memo.hidden = false;
  }

  var zoneDepot = document.getElementById("pieces-zone");
  if (zoneDepot) {
    document.getElementById("pieces-input").addEventListener("change", function (e) {
      ajouter(e.target.files); e.target.value = "";
    });
    ["dragenter", "dragover"].forEach(function (ev) {
      zoneDepot.addEventListener(ev, function (e) {
        e.preventDefault(); zoneDepot.classList.add("pieces__zone--survol");
      });
    });
    ["dragleave", "drop"].forEach(function (ev) {
      zoneDepot.addEventListener(ev, function (e) {
        e.preventDefault(); zoneDepot.classList.remove("pieces__zone--survol");
      });
    });
    zoneDepot.addEventListener("drop", function (e) {
      if (e.dataTransfer && e.dataTransfer.files) ajouter(e.dataTransfer.files);
    });
    document.getElementById("pieces-liste").addEventListener("click", function (e) {
      var b = e.target.closest(".pieces__x");
      if (!b) return;
      var id = parseInt(b.dataset.id, 10);
      pieces = pieces.filter(function (p) { return p.id !== id; });
      rendrePieces();
    });
    document.getElementById("pieces-zip").addEventListener("click", preparerZip);
  }

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
      bloc("4 · Délai et compléments", [DELAI, PORTEE, NOTE]);
    zoneMission.hidden = false;
    document.getElementById("devis-pieces").hidden = false;
    document.getElementById("devis-envoi").hidden = false;
    rendreMemo(cle);
    zoneMission.querySelector("input,select,textarea").focus();
    if (RECAP) {
      var ta = zoneMission.querySelector("textarea");
      if (ta && !ta.value) { ta.value = RECAP + "\n\n"; }
    }
    etat.textContent = "Questionnaire adapté à la mission : " + m.nom + ".";
  }

  document.getElementById("devis-choix").innerHTML =
    Object.keys(MISSIONS).map(function (k) {
      return '<button type="button" class="mission" data-m="' + k + '">' +
             '<b>' + MISSIONS[k].nom + "</b>" +
             (HINTS[k] ? "<i>" + HINTS[k] + "</i>" : "") + "</button>";
    }).join("");

  /* ---------- particulier : société facultative + orientation ---------- */
  var qualite = document.getElementById("c_qualite");
  var societe = document.getElementById("c_societe");
  var encartPart = document.getElementById("devis-part");
  if (qualite && societe) qualite.addEventListener("change", function () {
    var estPart = qualite.value === "Particulier";
    societe.required = !estPart;
    var lbl = societe.previousElementSibling;
    if (lbl) lbl.textContent = estPart ?
      "Société ou copropriété — facultatif" : "Société ou copropriété";
    if (encartPart) encartPart.hidden = !estPart;
  });

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
    [CONTACT, BIEN, MISSIONS[choix].champs, [DELAI, PORTEE, NOTE]].forEach(function (g) {
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
    if (pieces.length) {
      l.push("", "PIÈCES JOINTES (" + pieces.length + ", " + poids(totalPieces()) + ") :");
      pieces.forEach(function (p, i) {
        l.push("  " + (i + 1) + ". " + p.fichier.name + " (" + poids(p.fichier.size) + ")");
      });
    }
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
    /* Les pièces partent avec la demande si le relais accepte les fichiers
       (offre Pro). Sinon le service ignore ces champs et le récapitulatif
       en garde la liste — le client les envoie alors par retour d'e-mail. */
    pieces.forEach(function (p, i) {
      data.append("piece_" + (i + 1), p.fichier, p.fichier.name);
    });

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
      '<button type="button" id="copier" class="lien">copier le récapitulatif</button>.' +
      (pieces.length ? '<br><strong>N\'oubliez pas de joindre votre dossier ' +
        nomDossier() + '</strong> — préparez-le avec le bouton ci-dessus s\'il ' +
        'n\'est pas encore enregistré.' : '');
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
