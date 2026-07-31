/* Recherche depuis le bandeau — DGLM Expertises.
   On tape sa question directement dans la barre du haut : les suggestions
   apparaissent sous le champ, la touche Entrée mène à la page de résultats.

   L'index (/assets/recherche.json) est le MÊME que celui de la page
   /recherche/ : une seule source, chargée à la demande au premier usage,
   puis gardée en cache par le navigateur. Aucun doublon. */
(function () {
  "use strict";

  var champ = document.getElementById("navq");
  if (!champ) return;                       // page de recherche : pas de doublon
  var panneau = document.getElementById("navq-sug");
  var IDX = null, chargement = null, dernier = "";

  function norm(s) {
    return s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }

  function charger() {
    if (chargement) return chargement;
    chargement = fetch("/assets/recherche.json")
      .then(function (r) { return r.json(); })
      .then(function (d) { IDX = d.idx; return IDX; })
      .catch(function () { IDX = []; return IDX; });
    return chargement;
  }

  function chercher(q) {
    var termes = norm(q).split(/\s+/).filter(Boolean);
    if (!termes.length) return [];
    var out = [];
    for (var i = 0; i < IDX.length; i++) {
      var e = IDX[i], s = 0, ok = 0;
      for (var j = 0; j < termes.length; j++) {
        if (e.n.indexOf(termes[j]) >= 0) { ok++; s += norm(e.t).indexOf(termes[j]) >= 0 ? 3 : 1; }
      }
      if (ok === termes.length) out.push([s, e]);
    }
    out.sort(function (a, b) { return b[0] - a[0]; });
    return out.slice(0, 7).map(function (x) { return x[1]; });
  }

  function fermer() {
    panneau.hidden = true;
    champ.setAttribute("aria-expanded", "false");
  }

  function afficher(q, res) {
    if (!res.length) {
      panneau.innerHTML = '<p class="navsug__vide">Aucun résultat pour « ' +
        q.replace(/[<>&]/g, "") + " ». Essayez un sigle (DTG, RAAT), " +
        "un thème (amiante, énergie) ou une commune.</p>";
    } else {
      panneau.innerHTML = res.map(function (e) {
        var v = e.i ? '<img src="/assets/photos/' + e.i + '" alt="" loading="lazy">' : "";
        return '<a class="navsug__item' + (e.i ? " navsug__item--photo" : "") +
          '" href="' + e.u + '">' + v + "<span><b>" + e.t + "</b><i>" + e.d.slice(0, 90) +
          "</i></span></a>";
      }).join("") +
        '<a class="navsug__tous" href="/recherche/?q=' + encodeURIComponent(q) +
        '">Voir tous les résultats pour « ' + q.replace(/[<>&]/g, "") + " » →</a>";
    }
    panneau.hidden = false;
    champ.setAttribute("aria-expanded", "true");
  }

  function saisie() {
    var q = champ.value.trim();
    if (q === dernier) return;
    dernier = q;
    if (q.length < 2) { fermer(); return; }
    charger().then(function () {
      if (champ.value.trim() !== q) return;   // saisie plus récente : on abandonne
      afficher(q, chercher(q));
    });
  }

  champ.addEventListener("input", saisie);
  champ.addEventListener("focus", charger);   // pré-chargement dès l'intention

  /* Entrée : on ouvre la page de résultats complète, avec la question posée. */
  champ.closest("form").addEventListener("submit", function (e) {
    e.preventDefault();
    var q = champ.value.trim();
    if (q.length < 2) return;
    location.href = "/recherche/?q=" + encodeURIComponent(q);
  });

  /* Navigation au clavier dans les suggestions. */
  champ.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { fermer(); champ.blur(); return; }
    if (e.key !== "ArrowDown" || panneau.hidden) return;
    e.preventDefault();
    var premier = panneau.querySelector("a");
    if (premier) premier.focus();
  });
  panneau.addEventListener("keydown", function (e) {
    var liens = [].slice.call(panneau.querySelectorAll("a"));
    var i = liens.indexOf(document.activeElement);
    if (e.key === "Escape") { fermer(); champ.focus(); return; }
    if (e.key === "ArrowDown" && i < liens.length - 1) { e.preventDefault(); liens[i + 1].focus(); }
    if (e.key === "ArrowUp") {
      e.preventDefault();
      if (i > 0) liens[i - 1].focus(); else champ.focus();
    }
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".navq")) fermer();
  });
})();
