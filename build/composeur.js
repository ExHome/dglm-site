/* COMPOSEUR DE LIEN DE PRÉ-ÉTUDE — outil interne.

   On choisit la mission, on nomme l'affaire, et on obtient deux choses : le
   lien à coller, et le message qui va avec. Le destinataire trouve la mission
   et sa référence déjà posées, et ne complète que ce que lui seul sait.

   Rien n'est envoyé, rien n'est enregistré : cette page ne fait que fabriquer
   une adresse. */
(function () {
  "use strict";
  var racine = document.getElementById("composeur");
  if (!racine) return;

  var MISSIONS = [
    ["dtg", "DTG", "Diagnostic technique global"],
    ["pppt", "PPPT", "Plan pluriannuel de travaux"],
    ["raat", "RAAT", "Repérage amiante avant travaux"],
    ["raad", "RAAD", "Repérage amiante avant démolition"],
    ["dpe", "DPE", "DPE collectif"],
    ["autre", "", "Autre mission"],
  ];

  var etat = { m: "dtg", ref: "", c: "", mail: "" };

  function lien() {
    var base = location.origin + "/pre-etude/";
    var p = new URLSearchParams();
    if (etat.m) p.set("m", etat.m);
    if (etat.ref.trim()) p.set("ref", etat.ref.trim());
    if (etat.c.trim()) p.set("c", etat.c.trim());
    if (etat.mail.trim()) p.set("mail", etat.mail.trim());
    var q = p.toString();
    return base + (q ? "?" + q : "");
  }

  function nomMission() {
    var m = MISSIONS.find(function (x) { return x[0] === etat.m; });
    return m ? m[2] : "votre mission";
  }

  function message() {
    var civ = etat.c.trim() ? etat.c.trim() : "Madame, Monsieur";
    return civ + ",\n\n"
      + "Pour établir votre devis de " + nomMission().toLowerCase()
      + (etat.ref.trim() ? " concernant " + etat.ref.trim() : "")
      + ", nous avons besoin de quelques précisions sur l'immeuble.\n\n"
      + "Le plus simple est ce formulaire, qui prend trois minutes et vous évite "
      + "un échange téléphonique :\n\n"
      + lien() + "\n\n"
      + "Ce que vous ne savez pas, laissez-le vide : nous le verrons ensemble. "
      + "Nous revenons vers vous avec un prix ferme dans la journée ouvrée.\n\n"
      + "Bien cordialement,\n\n"
      + "DGLM Expertises\n06 07 35 15 05 — contact@dglmexpertises.fr";
  }

  function rendre() {
    var h = '<div class="pre__form">'
      + '<label class="pre__champ"><span class="pre__lab">Mission</span>'
      + '<div class="pre__opts">';
    MISSIONS.forEach(function (m) {
      h += '<label class="pre__opt"><input type="radio" name="m" value="' + m[0] + '"'
        + (etat.m === m[0] ? " checked" : "") + "><span>"
        + (m[1] ? m[1] + " — " : "") + m[2] + "</span></label>";
    });
    h += "</div></label>"
      + champ("ref", "Référence de l'affaire", "Résidence Les Tilleuls, 12 rue X…")
      + champ("c", "Nom du destinataire", "Mme Martin — facultatif")
      + champ("mail", "Son courriel", "facultatif, pour pré-remplir le formulaire")
      + '<div class="comp__sortie">'
      + '<p class="pre__lab">Le lien à envoyer</p>'
      + '<p class="comp__lien"></p>'
      + '<p class="comp__actions">'
      + '<button type="button" class="btn" data-copie="lien">Copier le lien</button> '
      + '<button type="button" class="btn btn--ghost" data-copie="message">Copier le message complet</button> '
      + '<a class="btn btn--ghost comp__mail" href="#">Ouvrir dans ma messagerie</a></p>'
      + '<details class="comp__apercu"><summary>Voir le message</summary>'
      + '<pre class="comp__texte"></pre></details>'
      + '<p class="comp__essai"><a href="#" target="_blank" rel="noopener">'
      + "Ouvrir le formulaire tel que le verra le destinataire →</a></p>"
      + "</div></div>";
    racine.innerHTML = h;
    brancher();
    maj();
  }

  function champ(nom, lib, aide) {
    return '<label class="pre__champ"><span class="pre__lab">' + lib + "</span>"
      + '<input type="text" data-k="' + nom + '" placeholder="' + aide + '" value="'
      + String(etat[nom]).replace(/"/g, "&quot;") + '"></label>';
  }

  function maj() {
    var l = lien();
    racine.querySelector(".comp__lien").textContent = l;
    racine.querySelector(".comp__texte").textContent = message();
    racine.querySelector(".comp__essai a").href = l;
    racine.querySelector(".comp__mail").href = "mailto:"
      + (etat.mail.trim() ? encodeURIComponent(etat.mail.trim()) : "")
      + "?subject=" + encodeURIComponent("Devis " + nomMission()
        + (etat.ref.trim() ? " — " + etat.ref.trim() : ""))
      + "&body=" + encodeURIComponent(message());
  }

  function brancher() {
    Array.prototype.forEach.call(racine.querySelectorAll("input[data-k]"), function (i) {
      i.addEventListener("input", function () { etat[i.getAttribute("data-k")] = i.value; maj(); });
    });
    Array.prototype.forEach.call(racine.querySelectorAll('input[name="m"]'), function (i) {
      i.addEventListener("change", function () { etat.m = i.value; maj(); });
    });
    Array.prototype.forEach.call(racine.querySelectorAll("[data-copie]"), function (b) {
      b.addEventListener("click", function () {
        var quoi = b.getAttribute("data-copie") === "lien" ? lien() : message();
        var avant = b.textContent;
        navigator.clipboard.writeText(quoi).then(function () {
          b.textContent = "Copié ✓";
          setTimeout(function () { b.textContent = avant; }, 2200);
        }, function () { b.textContent = "Copie impossible"; });
      });
    });
  }

  rendre();
})();
