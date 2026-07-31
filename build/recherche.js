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

  /* On tape une question entière : « qui paie le diagnostic ? ». Les mots
     outils ne figurent dans aucun index — les exiger ferait tout échouer.
     On ne garde donc que les mots porteurs de sens. */
  var VIDES = ("le la les un une des du de d a au aux en et ou est sont ce cet cette c " +
    "qui que quoi quel quelle quels quelles comment pourquoi quand combien ou " +
    "faut il elle on nous vous je tu mon ma mes votre vos notre nos leur leurs " +
    "se sa son ses pour par sur dans avec sans plus moins tout tous toute toutes " +
    "y ne pas ni na l s t qu aussi meme etre avoir fait faire doit dois peut " +
    "puis alors donc mais car si oui non alors alors-que").split(" ");

  function motsUtiles(q) {
    var bruts = norm(q).split(/[^a-z0-9]+/).filter(Boolean);
    var utiles = bruts.filter(function (m) {
      return m.length > 1 && VIDES.indexOf(m) < 0;
    });
    return utiles.length ? utiles : bruts;
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
    var termes = motsUtiles(q);
    if (!termes.length) return [];
    /* Un seul mot reconnu suffit à retenir une page : une question posée en
       langage courant ne doit jamais tomber dans le vide. Le classement fait
       le tri — les pages qui portent TOUS les mots passent devant.
       Un mot rare (« mérule », « tantièmes ») en dit plus long qu'un mot
       omniprésent (« diagnostic ») : on le pèse en conséquence. */
    var poids = termes.map(function (t) {
      var n = 0;
      for (var k = 0; k < IDX.length; k++) if (IDX[k].n.indexOf(t) >= 0) n++;
      return n ? Math.max(1, Math.log(IDX.length / n)) : 1;
    });
    var out = [];
    for (var i = 0; i < IDX.length; i++) {
      var e = IDX[i], s = 0, ok = 0, titre = norm(e.t);
      for (var j = 0; j < termes.length; j++) {
        if (e.n.indexOf(termes[j]) >= 0) {
          ok++;
          s += poids[j] * (titre.indexOf(termes[j]) >= 0 ? 3 : 1);
        }
      }
      if (ok) out.push([ok * 100 + s, e]);
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
