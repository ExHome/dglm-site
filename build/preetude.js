/* PRÉ-ÉTUDE — le formulaire que le syndic remplit avant que nous chiffrions.

   Le devis d'une mission collective se joue sur des informations que nous
   n'avons pas : l'âge de l'immeuble, le nombre de lots, l'existence d'un
   dossier technique amiante, la nature exacte des travaux projetés. Sans
   elles, il faut appeler, relancer, attendre — et le devis part trois jours
   plus tard qu'il n'aurait dû.

   Cette page se transmet par un lien, et ce lien peut arriver PRÉ-REMPLI :
   /pre-etude/?m=dtg&ref=Résidence%20Les%20Tilleuls&c=Mme%20Martin
   Le destinataire trouve la mission et sa référence déjà posées, et ne
   complète que ce que lui seul sait.

   Les paramètres reconnus :
     m    la mission (raat, raad, dtg, pppt, dpe, autre)
     ref  la référence de l'affaire, telle qu'elle nous parle
     c    le nom du contact
     mail son adresse
*/
(function () {
  "use strict";
  var racine = document.getElementById("preetude");
  if (!racine) return;

  var CFG = window.DGLM_PART || {};
  var P = new URLSearchParams(location.search);

  var MISSIONS = {
    raat: {
      nom: "Repérage amiante avant travaux",
      sigle: "RAAT",
      champs: [
        ["travaux", "Nature des travaux projetés", "textarea",
         "Réfection des sols des parties communes, reprise de l'étanchéité de la terrasse…", true],
        ["zones", "Locaux et zones concernés", "textarea",
         "Cages d'escalier, sous-sol, terrasse, logements…", true],
        ["dta", "Existe-t-il un dossier technique amiante ?", "choix",
         ["Oui, je peux le transmettre", "Oui, mais introuvable", "Non", "Je ne sais pas"], false],
        ["entreprise", "L'entreprise de travaux est-elle retenue ?", "choix",
         ["Oui, devis signé", "Consultation en cours", "Pas encore", "Je ne sais pas"], false],
      ],
    },
    raad: {
      nom: "Repérage amiante avant démolition",
      sigle: "RAAD",
      champs: [
        ["demolition", "Démolition totale, partielle ou curage ?", "choix",
         ["Totale", "Partielle", "Curage", "Je ne sais pas encore"], true],
        ["occupation", "Le bâtiment est-il libéré ?", "choix",
         ["Oui, entièrement", "Partiellement", "Non, encore occupé"], true],
        ["surface", "Surface approximative concernée", "texte", "en m², une estimation suffit", false],
        ["plans", "Disposez-vous de plans, même anciens ?", "choix",
         ["Oui", "Non", "À rechercher"], false],
      ],
    },
    dtg: {
      nom: "Diagnostic technique global",
      sigle: "DTG",
      champs: [
        ["motif", "Ce qui motive la demande", "choix",
         ["Obligation légale", "Mise en copropriété", "Préparation de travaux",
          "Demande de l'assemblée générale", "Procédure administrative"], true],
        ["equipements", "Équipements communs présents", "textarea",
         "Chauffage collectif, ascenseur, VMC, chaufferie, vide-ordures…", false],
        ["travaux10", "Travaux importants des dix dernières années", "textarea",
         "Ravalement, toiture, réseaux, ascenseur…", false],
        ["ag", "Date de la prochaine assemblée générale", "texte",
         "Pour caler notre délai sur le vôtre", false],
      ],
    },
    pppt: {
      nom: "Plan pluriannuel de travaux",
      sigle: "PPPT",
      champs: [
        ["dtg_fait", "Un diagnostic technique global a-t-il été réalisé ?", "choix",
         ["Oui, de moins de dix ans", "Oui, plus ancien", "Non", "Je ne sais pas"], true],
        ["dpe_fait", "Un DPE collectif existe-t-il ?", "choix",
         ["Oui", "Non", "En cours", "Je ne sais pas"], false],
        ["fonds", "Un fonds de travaux est-il constitué ?", "choix",
         ["Oui", "Non", "Je ne sais pas"], false],
        ["ag", "Date de la prochaine assemblée générale", "texte",
         "Pour caler notre délai sur le vôtre", false],
      ],
    },
    dpe: {
      nom: "DPE collectif",
      sigle: "DPE",
      champs: [
        ["chauffage", "Mode de chauffage", "choix",
         ["Collectif gaz", "Collectif fioul", "Collectif urbain", "Individuel",
          "Mixte", "Je ne sais pas"], true],
        ["ecs", "Eau chaude sanitaire", "choix",
         ["Collective", "Individuelle", "Je ne sais pas"], false],
        ["travaux_energie", "Travaux d'isolation déjà réalisés", "textarea",
         "Façades, combles, menuiseries, année si connue", false],
      ],
    },
    autre: {
      nom: "Autre mission",
      sigle: "",
      champs: [
        ["besoin", "Décrivez votre besoin", "textarea",
         "Nous vous rappelons pour préciser", true],
      ],
    },
  };

  /* Les champs communs à toutes les missions : sans eux, aucun chiffrage. */
  var COMMUNS = [
    ["adresse", "Adresse de l'immeuble", "texte",
     "Numéro, rue, code postal et commune", true],
    ["lots", "Nombre de lots principaux", "texte", "Une estimation suffit", true],
    ["annee", "Année de construction ou du permis", "texte",
     "Même approximative : elle commande le périmètre du repérage", true],
    ["batiments", "Nombre de bâtiments", "texte", "1, 2, 3…", false],
    ["acces", "Comment accéder sur place", "textarea",
     "Gardien, code, boîte à clés, personne à contacter…", false],
    ["delai", "Vos délais", "texte", "Assemblée générale, chantier, échéance…", false],
  ];

  var mission = (P.get("m") || "").toLowerCase();
  if (!MISSIONS[mission]) mission = "";

  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function champ(c, valeur) {
    var nom = c[0], lib = c[1], type = c[2], aide = c[3], requis = c[4];
    var h = '<label class="pre__champ"><span class="pre__lab">' + esc(lib)
      + (requis ? '<i aria-hidden="true">*</i>' : "") + "</span>";
    if (type === "textarea") {
      h += '<textarea name="' + nom + '" rows="3" placeholder="' + esc(aide) + '"'
        + (requis ? " required" : "") + ">" + esc(valeur || "") + "</textarea>";
    } else if (type === "choix") {
      h += '<div class="pre__opts">';
      aide.forEach(function (o, i) {
        h += '<label class="pre__opt"><input type="radio" name="' + nom + '" value="'
          + esc(o) + '"' + (valeur === o ? " checked" : "") + "><span>" + esc(o)
          + "</span></label>";
      });
      h += "</div>";
    } else {
      h += '<input type="text" name="' + nom + '" placeholder="' + esc(aide) + '"'
        + (requis ? " required" : "") + ' value="' + esc(valeur || "") + '">';
    }
    return h + "</label>";
  }

  function rendre() {
    var m = MISSIONS[mission];
    var h = "";

    if (!mission) {
      h += '<p class="pre__intro">Quelle mission souhaitez-vous faire chiffrer ?</p>'
        + '<div class="pre__missions">';
      Object.keys(MISSIONS).forEach(function (k) {
        h += '<button type="button" class="pre__mission" data-m="' + k + '">'
          + (MISSIONS[k].sigle ? '<span class="pre__sigle">' + MISSIONS[k].sigle + "</span>" : "")
          + "<span>" + esc(MISSIONS[k].nom) + "</span></button>";
      });
      h += "</div>";
      racine.innerHTML = h;
      Array.prototype.forEach.call(racine.querySelectorAll(".pre__mission"), function (b) {
        b.addEventListener("click", function () {
          mission = b.getAttribute("data-m");
          rendre();
          racine.scrollIntoView({ behavior: "smooth", block: "start" });
        });
      });
      return;
    }

    h += '<p class="pre__mission-en-cours">'
      + (m.sigle ? '<span class="pre__sigle">' + m.sigle + "</span>" : "")
      + esc(m.nom) + ' <button type="button" class="pre__changer">changer</button></p>';

    if (P.get("ref")) {
      h += '<p class="pre__ref">Affaire : <b>' + esc(P.get("ref")) + "</b></p>";
    }

    h += '<form class="pre__form" novalidate>'
      + '<h3 class="pre__sous">Qui êtes-vous ?</h3>'
      + champ(["contact", "Votre nom", "texte", "Prénom et nom", true], P.get("c"))
      + champ(["qualite", "À quel titre ?", "choix",
               ["Syndic", "Conseil syndical", "Copropriétaire", "Bailleur",
                "Maître d'ouvrage", "Entreprise de travaux"], false])
      + champ(["courriel", "Votre courriel", "texte", "vous@exemple.fr", true], P.get("mail"))
      + champ(["tel", "Votre téléphone", "texte", "06 12 34 56 78", true])
      + '<h3 class="pre__sous">L\'immeuble</h3>';
    COMMUNS.forEach(function (c) { h += champ(c); });
    h += '<h3 class="pre__sous">La mission</h3>';
    m.champs.forEach(function (c) { h += champ(c); });
    h += '<label class="pre__coche"><input type="checkbox" name="rappel" value="oui">'
      + "<span>Je préfère être rappelé plutôt que de recevoir un courriel</span></label>"
      + '<button type="submit" class="btn pre__envoi">Envoyer ma demande</button>'
      + '<p class="pre__rgpd">Ces informations ne servent qu\'à établir votre devis. '
      + 'Elles ne sont ni vendues ni cédées — voir notre '
      + '<a href="/confidentialite/">politique de confidentialité</a>.</p>'
      + '<div class="pre__etat" role="status"></div></form>';

    racine.innerHTML = h;
    racine.querySelector(".pre__changer").addEventListener("click", function () {
      mission = "";
      rendre();
    });
    brancher(m);
  }

  function brancher(m) {
    var form = racine.querySelector(".pre__form");
    var etat = form.querySelector(".pre__etat");
    var bouton = form.querySelector(".pre__envoi");

    function texte() {
      var lignes = ["MISSION : " + m.nom, ""];
      if (P.get("ref")) lignes.push("AFFAIRE : " + P.get("ref"), "");
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name) return;
        if (el.type === "radio" && !el.checked) return;
        if (el.type === "checkbox") {
          if (el.checked) lignes.push("· rappel téléphonique souhaité");
          return;
        }
        var v = (el.value || "").trim();
        if (v) lignes.push("· " + el.name + " : " + v);
      });
      return lignes.join("\n");
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var manquants = [];
      Array.prototype.forEach.call(form.querySelectorAll("[required]"), function (el) {
        var vide = !(el.value || "").trim();
        el.classList.toggle("pre--vide", vide);
        if (vide) {
          var lab = el.closest(".pre__champ");
          manquants.push(lab ? lab.querySelector(".pre__lab").textContent.replace("*", "")
                             : el.name);
        }
      });
      if (manquants.length) {
        etat.className = "pre__etat pre__etat--warn";
        etat.textContent = "Il manque : " + manquants.join(", ") + ".";
        var premier = form.querySelector(".pre--vide");
        if (premier) premier.scrollIntoView({ behavior: "smooth", block: "center" });
        return;
      }

      bouton.disabled = true;
      bouton.textContent = "Envoi en cours…";
      etat.className = "pre__etat";
      etat.textContent = "";

      var d = new FormData();
      d.append("_subject", "Pré-étude — " + m.nom
        + (P.get("ref") ? " — " + P.get("ref") : ""));
      d.append("_captcha", "false");
      d.append("_template", "table");
      d.append("_replyto", (form.elements.courriel || {}).value || "");
      d.append("mission", m.nom);
      if (P.get("ref")) d.append("affaire", P.get("ref"));
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name) return;
        if (el.type === "radio" && !el.checked) return;
        if (el.type === "checkbox") {
          if (el.checked) d.append("rappel_souhaite", "OUI");
          return;
        }
        var v = (el.value || "").trim();
        if (v) d.append(el.name, v);
      });
      d.append("recapitulatif", texte());

      if (!CFG.endpoint) return replier(form, etat, bouton, texte());

      fetch(CFG.endpoint, { method: "POST", headers: { Accept: "application/json" }, body: d })
        .then(function (r) { return r.json(); })
        .then(function (r) {
          if (String(r.success) !== "true") throw new Error(r.message || "échec");
          racine.innerHTML = '<div class="pre__ok"><p class="pre__ok-t">'
            + "Votre demande nous est parvenue.</p>"
            + "<p>Nous revenons vers vous avec un devis ferme dans la journée ouvrée. "
            + "Si c'est urgent, appelez le "
            + '<a href="tel:' + (CFG.tel_raw || "") + '">' + (CFG.tel || "") + "</a>.</p></div>";
        })
        .catch(function () { replier(form, etat, bouton, texte()); });
    });
  }

  function replier(form, etat, bouton, txt) {
    bouton.disabled = false;
    bouton.textContent = "Envoyer ma demande";
    etat.className = "pre__etat pre__etat--warn";
    etat.innerHTML = "<b>L'envoi n'a pas abouti.</b> Votre demande n'est pas perdue : "
      + 'appelez le <a href="tel:' + (CFG.tel_raw || "") + '">' + (CFG.tel || "") + "</a> "
      + 'ou écrivez à <a href="mailto:' + (CFG.email || "") + '">' + (CFG.email || "") + "</a>. "
      + '<button type="button" class="pre__copier">Copier ma demande</button>';
    var c = etat.querySelector(".pre__copier");
    if (c) c.addEventListener("click", function () {
      navigator.clipboard.writeText(txt).then(function () {
        c.textContent = "Demande copiée ✓";
      }, function () { c.textContent = "Copie impossible"; });
    });
  }

  rendre();
})();
