/* Simulateur d'aides financières — copropriétés (MaPrimeRénov' Copropriété)
   DGLM Expertises. Conçu pour un double usage : le syndic qui veut un ordre
   de grandeur, et l'étude technique (DTG, PPPT, audit) qui a besoin du
   détail ligne à ligne, imprimable et copiable.

   RÈGLE ABSOLUE : aucun chiffre inventé. Tous les barèmes sont dans BAREME,
   datés, sourcés sur la page. Estimation indicative : seule l'instruction
   du dossier par l'Anah fait foi. Aucun framework, aucune donnée conservée. */
(function () {
  "use strict";

  /* ---------- barèmes en vigueur (consultés le 31/07/2026) ---------- */
  var BAREME = {
    plafondTravauxParLogement: 25000, // assiette maximale par logement (€ HT)
    tauxGain35: 30,                   // % d'aide si gain énergétique >= 35 %
    tauxGain50: 45,                   // % d'aide si gain >= 50 %
    bonusSortiePassoire: 10,          // +10 points si F ou G avant, D ou mieux après
    bonusFragile: 20,                 // +20 points si copropriété fragile ou en difficulté
    primeTresModeste: 3000,           // prime individuelle par ménage très modeste (€)
    primeModeste: 1500,               // prime individuelle par ménage modeste (€)
    amoTaux: 0.5,                     // l'AMO est prise en charge à 50 %…
    amoPlafondParLogement: 300,       // …dans la limite de 300 € par logement…
    amoPlancher: 3000,                // …avec un minimum de 3 000 € par copropriété
    seuilRP20lotsOuMoins: 0.65,       // 65 % de résidences principales si <= 20 lots
    seuilRPPlusDe20lots: 0.75,        // 75 % au-delà de 20 lots
    gainMinimum: 35                   // % de gain énergétique exigé
  };

  var EUR = function (n) {
    return Math.round(n).toLocaleString("fr-FR") + " €";
  };

  /* ---------- moteur de calcul (fonction pure, testable) ---------- */
  function calculer(d) {
    var r = { motifs: [], lignes: [], avertissements: [] };

    /* éligibilité */
    var seuil = d.lots <= 20 ? BAREME.seuilRP20lotsOuMoins : BAREME.seuilRPPlusDe20lots;
    var partRP = d.lots > 0 ? d.rp / d.lots : 0;
    if (!(d.lots >= 2)) r.motifs.push("Une copropriété compte au moins 2 lots.");
    if (partRP < seuil) r.motifs.push("Résidences principales : " + Math.round(partRP * 100) +
      " % des lots — il en faut au moins " + Math.round(seuil * 100) +
      " % (règle officiellement appréciée en tantièmes).");
    if (d.immat !== "oui") r.motifs.push("La copropriété doit être immatriculée (et à jour) au registre national.");
    if (d.age !== "oui") r.motifs.push("Le bâtiment doit être achevé depuis plus de 15 ans.");
    if (d.gain < BAREME.gainMinimum) r.motifs.push("Le programme doit viser au moins " +
      BAREME.gainMinimum + " % de gain énergétique (c'est ce que chiffrent le DTG, le PPPT ou l'audit).");
    r.eligible = r.motifs.length === 0;

    /* assiette plafonnée */
    var plafond = BAREME.plafondTravauxParLogement * d.lots;
    var assiette = Math.min(d.travaux, plafond);
    r.lignes.push(["Assiette de travaux retenue",
      "min(" + EUR(d.travaux) + " ; " + EUR(BAREME.plafondTravauxParLogement) + " × " +
      d.lots + " logements)", EUR(assiette)]);
    if (d.travaux > plafond) r.avertissements.push("Travaux au-delà du plafond : " +
      EUR(d.travaux - plafond) + " restent hors assiette (mais bénéficient de la TVA à 5,5 % s'ils sont éligibles).");

    /* taux */
    var taux = d.gain >= 50 ? BAREME.tauxGain50 : (d.gain >= 35 ? BAREME.tauxGain35 : 0);
    var detailTaux = "taux de base " + taux + " % (gain " + (d.gain >= 50 ? "≥ 50" : "≥ 35") + " %)";
    var bonus = 0;
    if (d.passoire === "oui") { bonus += BAREME.bonusSortiePassoire; detailTaux += " + " + BAREME.bonusSortiePassoire + " % sortie de passoire"; }
    if (d.fragile === "oui") { bonus += BAREME.bonusFragile; detailTaux += " + " + BAREME.bonusFragile + " % copropriété fragile"; }
    var tauxTotal = taux + bonus;
    r.lignes.push(["Taux d'aide", detailTaux, tauxTotal + " %"]);

    /* aide collective */
    var socle = assiette * tauxTotal / 100;
    r.lignes.push(["Aide collective (au syndicat)", EUR(assiette) + " × " + tauxTotal + " %", EUR(socle)]);

    /* primes individuelles */
    var primes = d.tm * BAREME.primeTresModeste + d.m * BAREME.primeModeste;
    if (primes > 0) r.lignes.push(["Primes individuelles",
      d.tm + " ménage(s) très modeste(s) × " + EUR(BAREME.primeTresModeste) + " + " +
      d.m + " modeste(s) × " + EUR(BAREME.primeModeste), EUR(primes)]);

    /* AMO */
    var amoAide = 0;
    if (d.amo > 0) {
      amoAide = Math.min(Math.max(Math.min(d.amo * BAREME.amoTaux, BAREME.amoPlafondParLogement * d.lots), BAREME.amoPlancher), d.amo);
      r.lignes.push(["Aide sur l'AMO (obligatoire)",
        "50 % de " + EUR(d.amo) + ", plafond " + EUR(BAREME.amoPlafondParLogement) +
        "/logement, plancher " + EUR(BAREME.amoPlancher), EUR(amoAide)]);
    }

    r.total = socle + primes + amoAide;
    r.resteACharge = d.travaux + d.amo - r.total;
    r.parLogement = d.lots > 0 ? r.resteACharge / d.lots : 0;
    return r;
  }

  /* ---------- lecture du formulaire ---------- */
  var form = document.getElementById("simu-aides");
  if (!form) return;
  var zone = document.getElementById("aides-resultat");

  function val(id) { return parseFloat((document.getElementById(id) || {}).value) || 0; }
  function sel(id) { return (document.getElementById(id) || {}).value || ""; }

  function lire() {
    return {
      lots: Math.round(val("a_lots")),
      rp: Math.round(val("a_rp")),
      travaux: val("a_travaux"),
      amo: val("a_amo"),
      gain: parseInt(sel("a_gain"), 10) || 0,
      immat: sel("a_immat"), age: sel("a_age"),
      passoire: sel("a_passoire"), fragile: sel("a_fragile"),
      tm: Math.round(val("a_tm")), m: Math.round(val("a_m"))
    };
  }

  /* ---------- rendu ---------- */
  function rendre() {
    var d = lire();
    if (!(d.lots > 0) || !(d.travaux > 0)) { zone.hidden = true; return; }
    var r = calculer(d);
    var h = "";
    if (!r.eligible) {
      h += '<div class="simu-verdict simu-verdict--non"><strong>Conditions non remplies en l’état.</strong><ul>' +
        r.motifs.map(function (m) { return "<li>" + m + "</li>"; }).join("") +
        "</ul><p>Le détail ci-dessous reste calculé à titre indicatif, comme si les conditions étaient remplies.</p></div>";
    } else {
      h += '<div class="simu-verdict simu-verdict--oui"><strong>Copropriété éligible</strong> aux critères principaux de MaPrimeRénov’ Copropriété, sous réserve d’instruction du dossier par l’Anah.</div>';
    }
    h += '<div class="tabwrap"><table class="tabsimple simu-table"><thead><tr><th>Poste</th><th>Détail du calcul</th><th>Montant</th></tr></thead><tbody>';
    r.lignes.forEach(function (l) {
      h += "<tr><td>" + l[0] + "</td><td>" + l[1] + "</td><td><strong>" + l[2] + "</strong></td></tr>";
    });
    h += '</tbody><tfoot>' +
      '<tr><td>Total des aides estimées</td><td></td><td><strong>' + EUR(r.total) + "</strong></td></tr>" +
      '<tr><td>Reste à charge collectif</td><td>travaux + AMO − aides</td><td><strong>' + EUR(r.resteACharge) + "</strong></td></tr>" +
      '<tr><td>Soit par logement (moyenne)</td><td>répartition réelle aux tantièmes</td><td><strong>' + EUR(r.parLogement) + "</strong></td></tr></tfoot></table></div>";
    if (r.avertissements.length) {
      h += "<ul class='simu-avert'>" + r.avertissements.map(function (a) { return "<li>" + a + "</li>"; }).join("") + "</ul>";
    }
    h += '<p class="simu-suite">Pour financer le reste à charge : éco-PTZ (voir le guide ci-dessous), ' +
      'CEE cumulables (valorisation variable, sur devis), TVA à 5,5 % déjà appliquée sur les factures ' +
      'de travaux éligibles, et aides locales éventuelles.</p>';
    zone.querySelector(".simu-corps").innerHTML = h;
    zone.hidden = false;
  }

  /* ---------- export texte (pour les études et les PV d'AG) ---------- */
  function texte() {
    var d = lire(), r = calculer(d), l = [];
    l.push("SIMULATION D'AIDES — MaPrimeRénov' Copropriété");
    l.push("DGLM Expertises — estimation indicative du " +
      new Date().toLocaleDateString("fr-FR") + " (barèmes consultés le 31/07/2026)");
    l.push("");
    l.push("Hypothèses : " + d.lots + " lots d'habitation dont " + d.rp + " résidences principales ; " +
      "travaux " + EUR(d.travaux) + " HT ; AMO " + EUR(d.amo) + " HT ; gain visé ≥ " + d.gain + " %" +
      (d.passoire === "oui" ? " ; sortie de passoire (F/G → D ou mieux)" : "") +
      (d.fragile === "oui" ? " ; copropriété fragile" : ""));
    l.push(r.eligible ? "Éligibilité : critères principaux remplis (sous réserve d'instruction Anah)."
      : "Éligibilité : NON REMPLIE — " + r.motifs.join(" | "));
    l.push("");
    r.lignes.forEach(function (x) { l.push(x[0] + " : " + x[2] + "   [" + x[1] + "]"); });
    l.push("TOTAL AIDES ESTIMÉES : " + EUR(r.total));
    l.push("RESTE À CHARGE : " + EUR(r.resteACharge) + " (" + EUR(r.parLogement) + " par logement en moyenne)");
    l.push("");
    l.push("Estimation non contractuelle. Seules l'instruction du dossier par l'Anah et sa décision");
    l.push("d'octroi font foi. Compléments possibles : éco-PTZ, CEE, TVA 5,5 %, aides locales.");
    return l.join("\n");
  }

  form.addEventListener("input", rendre);
  form.addEventListener("change", rendre);

  var bCopie = document.getElementById("aides-copier");
  if (bCopie) bCopie.addEventListener("click", function () {
    navigator.clipboard.writeText(texte()).then(function () {
      bCopie.textContent = "Simulation copiée";
      setTimeout(function () { bCopie.textContent = "Copier le détail (pour une étude ou un PV)"; }, 2500);
    });
  });
  var bImp = document.getElementById("aides-imprimer");
  if (bImp) bImp.addEventListener("click", function () { window.print(); });
})();
