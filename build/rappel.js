/* LE FORMULAIRE DE FIN DE SIMULATEUR, PARTAGÉ.

   Les simulateurs du site donnaient leur réponse puis laissaient le visiteur
   se débrouiller : celui des aides et celui des validités n'offraient aucune
   sortie — pas un bouton, pas un lien. Quelqu'un qui vient de constater qu'il
   a une obligation à remplir n'avait aucun moyen de nous le dire.

   Ce module pose un formulaire identique à la fin de chacun. Il est appelé
   après l'affichage du résultat : le visiteur obtient toujours sa réponse
   complète d'abord, sans rien donner. Il choisit ensuite.

   Emploi :
     DGLM_RAPPEL(conteneur, {
       objet: "Demande de devis — simulateur d'obligations",
       recap: "SITUATION\n\n· 42 lots\n· permis de 1974",
       titre: "Nous établissons ce dossier.",
       phrase: "Il nous manque l'adresse de l'immeuble et vos délais."
     });
*/
(function (global) {
  "use strict";

  function champ(nom, libelle, type, aide, requis) {
    var auto = { nom: "name", tel: "tel", courriel: "email", adresse: "street-address" };
    return '<label class="simu__champ"><span class="simu__lab">' + libelle
      + (requis ? '<i aria-hidden="true">*</i>' : "") + "</span>"
      + '<input type="' + type + '" name="' + nom + '" placeholder="' + aide + '"'
      + (requis ? " required" : "") + ' autocomplete="' + (auto[nom] || "off") + '"></label>';
  }

  global.DGLM_RAPPEL = function (conteneur, opts) {
    if (!conteneur) return;
    opts = opts || {};
    var CFG = global.DGLM_PART || global.DEVIS_CFG || {};
    var tel = CFG.tel || "", telRaw = CFG.tel_raw || "", mail = CFG.email || CFG.destinataire || "";
    var endpoint = CFG.endpoint || "";

    var bloc = document.createElement("div");
    bloc.className = "simu__fin";
    bloc.innerHTML =
      '<p class="simu__fin-t">' + (opts.titre || "Nous nous en chargeons.") + "</p>"
      + "<p>" + (opts.phrase
        || "Dites-nous où se trouve le bien et vos délais : nous répondons avec un "
         + "prix ferme, dans la journée ouvrée.") + "</p>"
      + '<form class="simu__form" novalidate>'
      + champ("nom", "Votre nom", "text", "Prénom et nom", true)
      + champ("tel", "Votre téléphone", "tel", "06 12 34 56 78", true)
      + champ("courriel", "Votre courriel", "email", "vous@exemple.fr", true)
      + champ("adresse", "Adresse du bien", "text", "Numéro, rue, code postal et commune", true)
      + champ("surface", "Surface approximative", "text", "en m² — une estimation suffit", false)
      + champ("delai", "Vos délais", "text", "Assemblée générale, compromis, chantier…", false)
      + '<label class="simu__coche"><input type="checkbox" name="rappel" value="oui">'
      + "<span>Je préfère être rappelé plutôt que de recevoir un courriel</span></label>"
      + '<div class="simu__creneau" hidden>'
      + champ("creneau", "Quand vous joindre", "text", "Matin, après-midi, un jour précis…", false)
      + "</div>"
      + '<button type="submit" class="btn simu__envoi">Recevoir mon devis</button>'
      + '<p class="simu__rgpd">Ces informations ne servent qu\'à établir votre devis. '
      + 'Elles ne sont ni vendues ni cédées — voir notre '
      + '<a href="/confidentialite/">politique de confidentialité</a>.</p>'
      + '<div class="simu__etat" role="status"></div>'
      + "</form>"
      + (tel ? '<p class="simu__ou">Ou appelez-nous directement : '
              + '<a href="tel:' + telRaw + '">' + tel + "</a></p>" : "");
    conteneur.appendChild(bloc);

    var form = bloc.querySelector(".simu__form");
    var etatBox = form.querySelector(".simu__etat");
    var bouton = form.querySelector(".simu__envoi");
    var coche = form.querySelector('input[name="rappel"]');
    var creneau = bloc.querySelector(".simu__creneau");

    /* Le créneau n'apparaît que si le rappel est demandé : un formulaire ne
       réclame jamais ce dont il n'a pas l'usage. */
    if (coche && creneau) {
      coche.addEventListener("change", function () {
        creneau.hidden = !coche.checked;
        if (coche.checked) {
          var i = creneau.querySelector("input");
          if (i) i.focus();
        }
      });
    }

    function texteComplet() {
      var lignes = [];
      if (opts.recap) lignes.push(opts.recap, "");
      lignes.push("COORDONNÉES", "");
      Array.prototype.forEach.call(form.querySelectorAll("input"), function (i) {
        if (i.type === "checkbox") {
          if (i.checked) lignes.push("· rappel téléphonique souhaité");
          return;
        }
        if (i.value.trim()) lignes.push("· " + i.name + " : " + i.value.trim());
      });
      return lignes.join("\n");
    }

    function replier() {
      bouton.disabled = false;
      bouton.textContent = "Recevoir mon devis";
      etatBox.className = "simu__etat simu__etat--warn";
      etatBox.innerHTML = "<b>L'envoi n'a pas abouti.</b> Votre demande n'est pas "
        + 'perdue : appelez le <a href="tel:' + telRaw + '">' + tel + "</a>, ou écrivez à "
        + '<a href="mailto:' + mail + '">' + mail + "</a>. "
        + '<button type="button" class="simu__copier">Copier ma demande</button>';
      var c = etatBox.querySelector(".simu__copier");
      if (c) c.addEventListener("click", function () {
        navigator.clipboard.writeText(texteComplet()).then(
          function () { c.textContent = "Demande copiée ✓"; },
          function () { c.textContent = "Copie impossible"; });
      });
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var manquants = [];
      Array.prototype.forEach.call(form.querySelectorAll("input[required]"), function (i) {
        i.classList.toggle("simu--vide", !i.value.trim());
        if (!i.value.trim()) manquants.push(i.previousElementSibling
          ? i.previousElementSibling.textContent.replace("*", "").toLowerCase()
          : i.name);
      });
      if (manquants.length) {
        etatBox.className = "simu__etat simu__etat--warn";
        etatBox.textContent = "Il manque : " + manquants.join(", ") + ".";
        return;
      }

      bouton.disabled = true;
      bouton.textContent = "Envoi en cours…";
      etatBox.className = "simu__etat";
      etatBox.textContent = "";

      var d = new FormData();
      d.append("_subject", opts.objet || "Demande de devis — simulateur");
      d.append("_captcha", "false");
      d.append("_template", "table");
      Array.prototype.forEach.call(form.querySelectorAll("input"), function (i) {
        if (i.type === "checkbox") {
          if (i.checked) d.append("rappel_souhaite", "OUI — le client préfère être rappelé");
          return;
        }
        if (i.value.trim()) d.append(i.name, i.value.trim());
      });
      d.append("_replyto", (form.elements.courriel || {}).value || "");
      if (opts.recap) d.append("recapitulatif", opts.recap);

      if (!endpoint) return replier();

      fetch(endpoint, { method: "POST", headers: { Accept: "application/json" }, body: d })
        .then(function (x) { return x.json(); })
        .then(function (x) {
          if (String(x.success) !== "true") throw new Error(x.message || "échec");
          form.innerHTML = '<p class="simu__ok"><b>Votre demande est partie.</b><br>'
            + "Nous vous répondons avec un prix ferme, dans la journée ouvrée."
            + (tel ? ' Si c\'est urgent, appelez le <a href="tel:' + telRaw + '">'
                     + tel + "</a>." : "") + "</p>";
        })
        .catch(replier);
    });
  };
})(window);
