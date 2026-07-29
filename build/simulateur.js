/* Simulateur d'obligations de copropriété — DGLM Expertises
   Vanilla JS, aucune dépendance, aucune donnée envoyée à un serveur. */
(function () {
  "use strict";

  var ANNEE = new Date().getFullYear();

  // Paliers d'entrée en vigueur (nombre de lots -> année)
  function paliePPPT(lots) {
    if (lots > 200) return 2023;
    if (lots >= 51) return 2024;
    return 2025;
  }
  function palierDPE(lots) {
    if (lots > 200) return 2024;
    if (lots >= 51) return 2025;
    return 2026;
  }

  var form = document.getElementById("sim");
  var out = document.getElementById("resultat");
  if (!form || !out) return;

  function val(name) {
    var el = form.elements[name];
    if (!el) return "";
    if (el.type === "number") return el.value === "" ? null : parseInt(el.value, 10);
    return el.value;
  }

  function ligne(statut, titre, corps, action) {
    var cls = { obligatoire: "ko", retard: "ko", attention: "warn", ok: "ok", info: "info" }[statut] || "info";
    var label = {
      retard: "En retard", obligatoire: "Obligatoire", attention: "À anticiper",
      ok: "À jour", info: "Pour information"
    }[statut];
    return '<article class="verdict verdict--' + cls + '">' +
      '<p class="verdict__tag">' + label + "</p>" +
      "<h3>" + titre + "</h3><p>" + corps + "</p>" +
      (action ? '<p class="verdict__act">' + action + "</p>" : "") +
      "</article>";
  }

  function calcule() {
    var destination = val("destination");
    var annee = val("annee");
    var lots = val("lots");
    var miseEnCopro = val("misecopro");
    var anneePPPT = val("anneepppt");
    var anneeDTG = val("anneedtg");
    var anneeDPE = val("anneedpe");
    var travaux = val("travaux");

    if (!annee || !lots) {
      out.innerHTML = '<p class="verdict__empty">Renseignez au minimum l’année d’achèvement et le nombre de lots.</p>';
      return;
    }

    var age = ANNEE - annee;
    var habitation = destination === "totale" || destination === "partielle";
    var blocs = [];
    var aFaire = [];

    /* ---------- Plan pluriannuel de travaux ---------- */
    if (!habitation) {
      blocs.push(ligne("info", "Plan pluriannuel de travaux",
        "L’obligation vise les copropriétés à destination totale ou partielle d’habitation. " +
        "Un immeuble exclusivement professionnel n’est pas concerné, mais un plan volontaire " +
        "reste l’outil le plus fiable pour piloter le budget."));
    } else if (age < 15) {
      var dansXans = 15 - age;
      blocs.push(ligne("ok", "Plan pluriannuel de travaux",
        "L’immeuble a " + age + " ans. L’obligation s’applique à partir de 15 ans, soit en <strong>" +
        (annee + 15) + "</strong> (dans " + dansXans + " an" + (dansXans > 1 ? "s" : "") + ")."));
    } else {
      var palier = paliePPPT(lots);
      if (anneePPPT && ANNEE - anneePPPT < 10) {
        blocs.push(ligne("ok", "Plan pluriannuel de travaux",
          "Votre plan date de " + anneePPPT + ". Il reste valable jusqu’en <strong>" +
          (anneePPPT + 10) + "</strong>, date à laquelle il devra être actualisé."));
      } else if (anneePPPT) {
        blocs.push(ligne("retard", "Plan pluriannuel de travaux",
          "Votre plan date de " + anneePPPT + " : il a dépassé sa durée de dix ans et doit être actualisé.",
          "Actualisation à inscrire à l’ordre du jour de la prochaine assemblée générale."));
        aFaire.push("Actualisation du plan pluriannuel de travaux (plan de " + anneePPPT + ", échu)");
      } else {
        var retard = ANNEE - palier;
        blocs.push(ligne("retard", "Plan pluriannuel de travaux",
          "Immeuble de " + age + " ans, " + lots + " lots : l’obligation s’applique depuis le " +
          "<strong>1<sup>er</sup> janvier " + palier + "</strong>" +
          (retard > 0 ? ", soit " + retard + " an" + (retard > 1 ? "s" : "") + " de retard" : "") + ".",
          "Le projet doit être présenté à la première assemblée générale qui suit son élaboration."));
        aFaire.push("Projet de plan pluriannuel de travaux (obligatoire depuis " + palier + ")");
      }
    }

    /* ---------- Diagnostic technique global ---------- */
    if (miseEnCopro === "oui") {
      if (anneeDTG) {
        blocs.push(ligne("ok", "Diagnostic technique global",
          "Obligatoire dans votre situation (mise en copropriété d’un immeuble de plus de dix ans). " +
          "Réalisé en " + anneeDTG + "."));
      } else {
        blocs.push(ligne("obligatoire", "Diagnostic technique global",
          "La mise en copropriété d’un immeuble de plus de dix ans rend le diagnostic technique " +
          "global <strong>obligatoire</strong>.",
          "Un DTG comportant l’ensemble des éléments requis peut tenir lieu de plan pluriannuel de travaux : une seule mission au lieu de deux."));
        aFaire.push("Diagnostic technique global (obligatoire — mise en copropriété)");
      }
    } else if (!anneePPPT && habitation && age >= 15) {
      blocs.push(ligne("attention", "Diagnostic technique global",
        "Non obligatoire dans votre cas, mais c’est la voie la plus économique : un DTG complet " +
        "vaut plan pluriannuel de travaux et documente en même temps l’état réel de l’immeuble.",
        "À inscrire à l’ordre du jour : l’assemblée générale se prononce sur sa réalisation."));
    } else if (anneeDTG) {
      blocs.push(ligne("ok", "Diagnostic technique global",
        "Réalisé en " + anneeDTG + ". Aucune obligation de renouvellement à date fixe."));
    }

    /* ---------- Volet énergétique ---------- */
    if (habitation && annee < 2013) {
      var pd = palierDPE(lots);
      if (anneeDPE && ANNEE - anneeDPE < 10) {
        blocs.push(ligne("ok", "Diagnostic de performance énergétique collectif",
          "Réalisé en " + anneeDPE + ", valable dix ans, soit jusqu’en <strong>" + (anneeDPE + 10) + "</strong>."));
      } else if (pd <= ANNEE) {
        blocs.push(ligne("obligatoire", "Diagnostic de performance énergétique collectif",
          "Avec " + lots + " lots, l’obligation s’applique depuis le <strong>1<sup>er</sup> janvier " +
          pd + "</strong>. Elle vise les immeubles d’habitation dont le permis est antérieur à 2013.",
          "Ce volet s’intègre au diagnostic technique global : le faire réaliser séparément coûte plus cher."));
        aFaire.push("DPE collectif (obligatoire depuis " + pd + ")");
      } else {
        blocs.push(ligne("attention", "Diagnostic de performance énergétique collectif",
          "Obligation applicable à partir du <strong>1<sup>er</sup> janvier " + pd + "</strong> pour une copropriété de " + lots + " lots."));
      }
    }

    /* ---------- Repérage amiante avant travaux ---------- */
    if (travaux === "oui") {
      if (annee < 1998) {
        blocs.push(ligne("obligatoire", "Repérage amiante avant travaux",
          "Des travaux sont prévus sur un immeuble achevé en " + annee + ". Dès lors que le permis " +
          "est antérieur au <strong>1<sup>er</sup> juillet 1997</strong>, le repérage avant travaux " +
          "est obligatoire et incombe au donneur d’ordre — donc au syndic pour les parties communes.",
          "Le rapport doit être remis aux entreprises dès la consultation, pas au démarrage du chantier."));
        aFaire.push("Repérage amiante avant travaux (parties communes)");
      } else {
        blocs.push(ligne("ok", "Repérage amiante avant travaux",
          "Immeuble achevé en " + annee + " : hors champ de l’obligation de repérage amiante, " +
          "sous réserve que le permis de construire soit postérieur au 1<sup>er</sup> juillet 1997."));
      }
    }

    /* ---------- Fonds de travaux ---------- */
    if (habitation && age >= 15) {
      blocs.push(ligne("info", "Fonds de travaux",
        "Lorsque le plan pluriannuel fait apparaître des travaux nécessaires dans les dix ans, la " +
        "cotisation annuelle est calculée par référence au montant des travaux prévus au plan. " +
        "Sans plan chiffré, le fonds est dimensionné à l’aveugle."));
    }

    var recap = "";
    if (aFaire.length) {
      recap = '<div class="recap"><p class="eyebrow">À porter à l’ordre du jour</p><ol>' +
        aFaire.map(function (x) { return "<li>" + x + "</li>"; }).join("") + "</ol>" +
        '<div class="recap__act">' +
        '<a class="btn" href="mailto:contact@dglmexpertises.fr?subject=' +
        encodeURIComponent("Demande de devis copropriété — " + lots + " lots, " + annee) +
        "&body=" + encodeURIComponent(
          "Bonjour,\n\nCopropriété :\n- Année d’achèvement : " + annee +
          "\n- Nombre de lots : " + lots +
          "\n- Destination : " + destination +
          "\n\nMissions identifiées :\n" + aFaire.map(function (x) { return "- " + x; }).join("\n") +
          "\n\nAdresse de l’immeuble :\nContact :\n\nMerci de m’adresser un devis.\n") +
        '">Recevoir un devis pour ces missions</a>' +
        '<button type="button" class="btn btn--ghost" id="copier">Copier le récapitulatif</button>' +
        "</div></div>";
    }

    out.innerHTML = '<p class="eyebrow">Situation de la copropriété</p>' + blocs.join("") + recap +
      '<p class="verdict__note">Cette analyse est indicative et repose sur les seules informations ' +
      'saisies. Elle ne remplace pas l’examen du règlement de copropriété et des procès-verbaux ' +
      'd’assemblée. Aucune donnée n’est transmise ni enregistrée.</p>';

    var btn = document.getElementById("copier");
    if (btn) {
      btn.addEventListener("click", function () {
        var t = "Copropriété — " + lots + " lots, achevée en " + annee + "\n\n" +
          aFaire.map(function (x, i) { return (i + 1) + ". " + x; }).join("\n");
        navigator.clipboard.writeText(t).then(function () {
          btn.textContent = "Récapitulatif copié";
          setTimeout(function () { btn.textContent = "Copier le récapitulatif"; }, 2500);
        });
      });
    }
    out.setAttribute("aria-busy", "false");
  }

  form.addEventListener("submit", function (e) { e.preventDefault(); calcule(); });
  form.addEventListener("change", calcule);
})();
