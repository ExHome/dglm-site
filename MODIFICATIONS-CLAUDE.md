# Modifications apportées — session du 28/07/2026

Reprise du travail sur le site DGLM Expertises (pôle copropriété & travaux).
**Python ne tournant pas sur la machine, le build n'a pas pu être relancé en
local : la CI (`.github/workflows/deploy.yml`) régénère `/site` et lance
`audit_seo.py` + `veille_seo.py` au push.** Pousser puis vérifier l'onglet Actions.

## 1. Relecture réglementaire (chantier n°2 du LISEZ-MOI)

Vérifié conforme à la source, aucune correction : **PPPT** (calendrier lots
2023/2024/2025), **DTG** (CCH L.731-1), **RAAT/RAAD** (permis avant 01/07/1997),
**DPE collectif** (200/51-200/≤50 aux 2024/2025/2026, permis avant 2013),
**PEMD** (>1 000 m² ou substances dangereuses).

**Correction (erreur réelle) — `data/diagnostics_pro.py` + `build/simulateur.js` :**
l'**audit énergétique de copropriété** était présenté comme une obligation en
vigueur. Faux : l'obligation Grenelle II (≥50 lots, chauffage collectif, permis
avant 01/06/2001, échéance 01/01/2017) a pris fin ; depuis la loi Climat, seul le
**DPE collectif** s'impose, l'audit étant volontaire. Source : ANIL. Le récapitulatif
du simulateur ne dit plus « DPE collectif **ou audit énergétique** (obligatoire) ».

**Articles `contenus/` :** ajout du champ `sources:` (références légales) aux 10
articles qui en manquaient. Article 03 : « procédure de péril » → « procédure
d'insalubrité » (le maire/préfet pouvant réclamer un DTG en cas de désordres),
vérifié à la source (ANIL / Service Public).

> ⚠️ Les `sources:` ajoutées citent les textes légaux exacts, mais **sans URL
> Légifrance vérifiée** (je n'ai pas pu tester les identifiants d'article). Une
> passe finale pour ajouter les URL exactes + dates « vérifié le » est recommandée,
> sur le modèle des articles 10 et 11.

## 2. Pages quartiers Mérignac & Pessac (chantier « autre priorité »)

Sur le modèle exact des quartiers de Bordeaux, **sans toucher au code Bordeaux
existant** :

- `data/quartiers.py` : `QUARTIERS_MERIGNAC` (6 quartiers : Arlac, Capeyron, Le
  Burck, Centre/Mérignac-Soleil, Beutre, Chemin Long) et `QUARTIERS_PESSAC` (6 :
  Pessac Centre, Saige, **Cité Frugès–Le Corbusier** [UNESCO], Alouette,
  Haut-Lévêque/Magonty, Châtaigneraie/Arago), + registre `QUARTIERS_PAR_VILLE`.
- `build.py` : fonctions génériques `page_hub_ville()` / `page_quartier_ville()`
  (copies paramétrées des fonctions Bordeaux), boucle de génération, et liens des
  hubs `/merignac/` et `/pessac/` ajoutés à la navigation (profondeur 1 → quartiers
  à 2 clics, invariant respecté).
- Nouvelles pages : 2 hubs + 12 quartiers = **14 pages** (266 → 280).

## 3. Bug SEO corrigé

`build.py` : le `<title>` de l'accueil et un fallback de titre affichaient
« **Jalon Expertises** » (nom résiduel) → remplacé par « **DGLM Expertises** ».

## Fichiers modifiés
- `build.py`, `data/diagnostics_pro.py`, `data/quartiers.py`, `build/simulateur.js`
- `contenus/01`…`09` et `12` (ajout `sources:` ; 03 corrigé au fond)

## À faire ensuite (rappel)
- Vérifier au push que la CI reste verte (audit + veille).
- Passe finale « URL Légifrance + date » sur les `sources:` ajoutées.
- Toujours en attente de votre part : clé formulaire (Web3Forms), `tel_copro`,
  mentions légales (hébergeur/RCP/certif), ordre des portraits d'équipe.
