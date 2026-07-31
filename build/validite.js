/* Simulateur de validité des diagnostics — DGLM Expertises.
   On saisit ce qu'on a et quand il a été fait ; l'outil dit ce qui tient
   encore, ce qui expire bientôt, et ce qui est à refaire.

   Les durées sont celles du guide « Combien de temps chaque diagnostic
   reste-t-il valable ? » : une seule source, pour que le site ne se
   contredise jamais. Aucune donnée n'est transmise ni conservée. */
(function () {
  "use strict";

  var form = document.getElementById("valid-form");
  if (!form) return;

  /* Durée en mois. null = pas de péremption calendaire, mais une condition
     à vérifier — ces cas sont traités à part, jamais réduits à « illimité ». */
  var DIAGS = [
    { cle: "dpe", nom: "Diagnostic de performance énergétique (DPE)",
      vente: 120, location: 120,
      note: "Les DPE établis avant le 1<sup>er</sup> juillet 2021 ne sont plus valables, " +
            "quelle que soit leur date d'échéance théorique : la méthode de calcul a changé." },
    { cle: "amiante", nom: "État d'amiante (parties privatives)",
      vente: null, location: null,
      cond: "Sans limite de durée si le rapport conclut à l'absence d'amiante. " +
            "En revanche, un rapport établi avant 2013 doit être refait : le champ " +
            "du repérage a été élargi depuis. Et si de l'amiante a été repéré, " +
            "l'état de conservation se contrôle périodiquement.",
      alerte2013: true },
    { cle: "plomb", nom: "Constat de risque d'exposition au plomb (CREP)",
      vente: 12, location: 72,
      cond: "Ces durées ne s'appliquent que si du plomb a été détecté. Si le constat " +
            "conclut à l'absence de plomb, il vaut sans limite de durée.",
      siNegatifIllimite: true, avant1949: true },
    { cle: "termites", nom: "État relatif à la présence de termites",
      vente: 6, location: null,
      note: "Exigible dans les zones délimitées par arrêté préfectoral — la Gironde " +
            "est classée dans sa totalité." },
    { cle: "gaz", nom: "État de l'installation intérieure de gaz",
      vente: 36, location: 72,
      note: "Exigible si l'installation a plus de quinze ans." },
    { cle: "elec", nom: "État de l'installation intérieure d'électricité",
      vente: 36, location: 72,
      note: "Exigible si l'installation a plus de quinze ans." },
    { cle: "erp", nom: "État des risques (ERP)",
      vente: 6, location: 6,
      note: "Six mois seulement : c'est le premier à périmer. Il doit être à jour " +
            "à la signature, pas seulement à la mise en vente." },
    { cle: "assain", nom: "Contrôle d'assainissement non collectif",
      vente: 36, location: null,
      note: "Uniquement si le bien n'est pas raccordé au réseau public." },
    { cle: "surface", nom: "Mesurage (loi Carrez ou loi Boutin)",
      vente: null, location: null,
      cond: "Sans limite de durée, tant qu'aucun travail n'a modifié la surface. " +
            "Une cloison déposée, une véranda fermée, un comble aménagé : le mesurage " +
            "est caduc." },
  ];

  var MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
              "août", "septembre", "octobre", "novembre", "décembre"];

  function dateFr(d) {
    return d.getDate() + " " + MOIS[d.getMonth()] + " " + d.getFullYear();
  }

  function ajouterMois(d, n) {
    var r = new Date(d.getTime());
    var jour = r.getDate();
    r.setMonth(r.getMonth() + n);
    if (r.getDate() < jour) r.setDate(0);   // 31 janvier + 1 mois → 28/29 février
    return r;
  }

  /* ---------- construction du formulaire ---------- */
  var zone = document.getElementById("valid-liste");
  zone.innerHTML = DIAGS.map(function (d) {
    return '<div class="vd"><label class="vd__case">' +
      '<input type="checkbox" id="v_' + d.cle + '"> <span>' + d.nom + "</span></label>" +
      '<label class="vd__date" for="d_' + d.cle + '">' +
      '<span class="sr">Date du ' + d.nom + "</span>" +
      '<input type="date" id="d_' + d.cle + '" disabled></label></div>';
  }).join("");

  DIAGS.forEach(function (d) {
    var c = document.getElementById("v_" + d.cle);
    var dt = document.getElementById("d_" + d.cle);
    c.addEventListener("change", function () {
      dt.disabled = !c.checked;
      if (c.checked) dt.focus();
      else dt.value = "";
    });
  });

  /* ---------- calcul ---------- */
  function usage() {
    var u = document.querySelector('input[name="usage"]:checked');
    return u ? u.value : "vente";
  }

  function etat(d, saisie, u) {
    var duree = d[u];
    var r = { nom: d.nom, note: d.note || "", cond: d.cond || "" };

    if (!saisie) { r.classe = "manque"; r.verdict = "Date non renseignée"; return r; }
    var faite = new Date(saisie + "T12:00:00");
    if (isNaN(faite)) { r.classe = "manque"; r.verdict = "Date illisible"; return r; }

    var auj = new Date(); auj.setHours(12, 0, 0, 0);
    r.faiteLe = dateFr(faite);

    if (faite > auj) { r.classe = "manque"; r.verdict = "Date postérieure à aujourd'hui"; return r; }

    /* DPE : la réforme de juillet 2021 prime sur la durée de dix ans. */
    if (d.cle === "dpe" && faite < new Date("2021-07-01T12:00:00")) {
      r.classe = "perime";
      r.verdict = "À refaire";
      r.detail = "Établi avant le 1er juillet 2021 : cette génération de DPE n'est plus " +
        "recevable, même si dix ans ne sont pas écoulés.";
      return r;
    }
    if (d.cle === "amiante" && faite < new Date("2013-01-01T12:00:00")) {
      r.classe = "perime";
      r.verdict = "À refaire";
      r.detail = "Repérage antérieur à 2013 : le champ réglementaire a été élargi depuis, " +
        "un rapport plus ancien ne couvre pas tous les matériaux aujourd'hui visés.";
      return r;
    }

    if (duree === null) {
      r.classe = "condition";
      r.verdict = "Sans échéance de date";
      r.detail = d.cond || "Pas de durée calendaire : c'est une condition qu'il faut vérifier.";
      return r;
    }

    var fin = ajouterMois(faite, duree);
    var jours = Math.round((fin - auj) / 86400000);
    r.expireLe = dateFr(fin);
    r.duree = duree >= 12 ? (duree / 12) + " an" + (duree > 12 ? "s" : "") : duree + " mois";

    if (jours < 0) {
      r.classe = "perime";
      r.verdict = "Périmé";
      r.detail = "Échu depuis le " + r.expireLe + ".";
    } else if (jours <= 60) {
      r.classe = "bientot";
      r.verdict = "Expire bientôt";
      r.detail = "Valable jusqu'au " + r.expireLe + ", soit " + jours + " jour" +
        (jours > 1 ? "s" : "") + ".";
    } else {
      r.classe = "ok";
      r.verdict = "Valable";
      r.detail = "Jusqu'au " + r.expireLe + ".";
    }
    return r;
  }

  /* ---------- rendu ---------- */
  var sortie = document.getElementById("valid-resultat");
  var synthese = document.getElementById("valid-synthese");
  var manque = document.getElementById("valid-manque");
  var etabli = false;

  function analyser() {
    var u = usage();
    var choisis = DIAGS.filter(function (d) {
      return document.getElementById("v_" + d.cle).checked;
    });
    if (!choisis.length) {
      manque.textContent = "Cochez au moins un diagnostic pour lancer l'analyse.";
      manque.className = "simu-manque simu-manque--warn";
      return;
    }
    manque.textContent = ""; manque.className = "simu-manque";
    etabli = true;

    var res = choisis.map(function (d) {
      return etat(d, document.getElementById("d_" + d.cle).value, u);
    });

    var nb = { perime: 0, bientot: 0, ok: 0, condition: 0, manque: 0 };
    res.forEach(function (r) { nb[r.classe]++; });

    var titre, cls;
    if (nb.perime) { titre = nb.perime + " diagnostic" + (nb.perime > 1 ? "s" : "") +
      " à refaire avant de signer"; cls = "non"; }
    else if (nb.bientot) { titre = "Tout tient encore, mais " + nb.bientot +
      " arrive" + (nb.bientot > 1 ? "nt" : "") + " à échéance"; cls = "attention"; }
    else if (nb.manque) { titre = "Analyse partielle : il manque des dates"; cls = "attention"; }
    else { titre = "Votre dossier est à jour"; cls = "oui"; }

    var h = '<div class="simu-verdict simu-verdict--' + (cls === "non" ? "non" : cls === "oui" ? "oui" : "") +
      '"><strong>' + titre + "</strong></div>";

    h += '<ul class="vres">' + res.map(function (r) {
      return '<li class="vres__' + r.classe + '">' +
        '<span class="vres__etat">' + r.verdict + "</span>" +
        "<b>" + r.nom + "</b>" +
        (r.faiteLe ? '<i>Réalisé le ' + r.faiteLe + (r.duree ? " · validité " + r.duree : "") + "</i>" : "") +
        (r.detail ? "<p>" + r.detail + "</p>" : "") +
        (r.note ? '<p class="vres__note">' + r.note + "</p>" : "") +
        "</li>";
    }).join("") + "</ul>";

    h += '<p class="simu-suite">Cette analyse porte sur les seules dates saisies. ' +
      'Trois événements rendent un diagnostic caduc avant son échéance : des travaux qui ' +
      'modifient ce qu\'il décrit, un changement de réglementation, et la découverte d\'une ' +
      'anomalie qu\'il ne mentionnait pas. ' +
      '<a href="/questions/duree-validite-diagnostics/">Le guide complet des durées →</a></p>';

    sortie.querySelector(".simu-corps").innerHTML = h;
    sortie.hidden = false;

    if (synthese) synthese.textContent = titre + ". " +
      (nb.perime ? nb.perime + " à refaire. " : "") +
      (nb.bientot ? nb.bientot + " à renouveler bientôt. " : "") +
      (nb.ok ? nb.ok + " valable" + (nb.ok > 1 ? "s" : "") + ". " : "");

    var r0 = sortie.getBoundingClientRect();
    if (r0.top < 0 || r0.top > window.innerHeight - 80) {
      sortie.scrollIntoView({
        behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
        block: "start"
      });
    }
  }

  form.addEventListener("submit", function (e) { e.preventDefault(); analyser(); });
  form.addEventListener("change", function () { if (etabli) analyser(); });
})();
