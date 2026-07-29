# CLAUDE.md — Site DGLM Expertises

Contexte pour Claude Code. À lire avant toute modification.

---

## Ce qu'est ce projet

Générateur de site statique en Python pur, sans dépendance, sans framework, sans
base de données. Il produit 266 pages HTML pour **DGLM Expertises**, société de
diagnostics immobiliers à Bordeaux.

Le site cible le segment **copropriété, travaux et démolition**, distinct du segment
vente/location traité par un autre site (voir § « Deux sites »).

**Domaine cible :** `https://www.dglmexpertises.fr` (détenu par la cliente, aucune
page indexée à ce jour, à déployer sur GitHub Pages).

---

## Commandes

```bash
python3 build.py               # génère /site — toujours en premier
python3 audit_seo.py           # 8 contrôles anti-cannibalisation — BLOQUANT
python3 veille_seo.py          # 12 indicateurs, détection de régression — BLOQUANT
python3 veille_seo.py --init   # réinitialise la référence (à éviter)
python3 veille_reglementaire.py # surveille les fiches Service Public (réseau requis)
```

**Après toute modification, exécuter les trois premières dans l'ordre.**
Un code de sortie non nul signale une régression : la corriger, ne pas la contourner.

---

## Contraintes non négociables

Ces règles ont été posées avec la cliente. Ne pas les assouplir sans lui demander.

1. **Zéro requête externe.** Pas de Google Fonts, pas de CDN, pas de framework, pas de
   script tiers, pas d'iframe Meta ou YouTube. Lora est auto-hébergée en woff
   (sous-ensemble latin), le corps de texte utilise la pile système.
2. **Zéro stockage navigateur.** Ni `localStorage`, ni `sessionStorage`, ni cookie.
3. **Profondeur maximale de 2 clics** depuis l'accueil. Vérifié par `veille_seo.py`.
4. **Budget de 70 Ko par page HTML.** Actuellement ~17 Ko de moyenne.
5. **Aucune page orpheline.** Toute page doit recevoir au moins un lien interne.
6. **Données structurées sur chaque page indexable.**
7. **Aucune allégation de supériorité** (« n°1 », « le meilleur », « leader »).
   Le site concurrent en porte une : ne pas reproduire cette erreur.

---

## Deux sites — le pare-feu de requêtes

La cliente est liée jusqu'au **27 août 2028** à un contrat portant un autre site,
`dglm-expertises.com`, qui cible les requêtes de **vente et location**.

Tant que ce site est en ligne, celui-ci ne doit **pas** cibler ses requêtes : deux
sites d'une même entreprise sur les mêmes mots-clés se cannibalisent.

- `data/marque.py > REQUETES_SITE_A` liste 31 requêtes réservées
- `data/marque.py > SITE_A_SOUS_CONTRAT = True` pilote le pare-feu
- `audit_seo.py` contrôle 2 bloque toute page qui les cible

**Exception importante :** les pages informationnelles de `/questions/` échappent au
pare-feu. « Combien de temps est valable un DPE » et « DPE Bordeaux » ne partagent
aucune page de résultats — il n'y a donc pas de collision. La distinction est faite
par les motifs `INFORMATIONNEL` et `COMMERCIAL` dans `audit_seo.py`.

**Le jour de la sortie de contrat :** passer `SITE_A_SOUS_CONTRAT = False`, relancer
le build, puis rediriger l'ancien site en 301.

---

## Charte graphique

Relevée sur les documents réels de la marque. **Ne pas inventer de couleurs.**

| Rôle | Valeur |
|---|---|
| Vert (encre, logo) | `#093F30` |
| Vert profond (hero, footer) | `#002924` |
| Or (accent) | `#C09048` |
| Or clair | `#D9B778` |
| Crème (fond) | `#FAF8F3` |
| Crème 2 | `#F4F1E9` |
| Encre | `#1E2E28` |

**Typographie :** Lora (auto-hébergée, romain + italique) pour les titres, les chapôs
et les citations ; pile système pour le corps ; pile mono système pour les données.

**Registre visuel : planche d'architecte.** Blanc dominant, filets d'un pixel, angles
vifs, aucune ombre, sections numérotées en marge, blancs généreux. L'or ne sert qu'aux
citations, au filet du hero et aux schémas. Ne pas ajouter de cartes ombrées, de coins
arrondis ni de dégradés.

---

## Architecture des fichiers

```
build.py                  générateur — toutes les pages
audit_seo.py              8 contrôles anti-cannibalisation
veille_seo.py             12 indicateurs + historique .seo-history.json
veille_reglementaire.py   surveille les fiches Service Public

data/
  marque.py               identité, équipe (7 membres), pare-feu, config formulaire
  communes.py             28 communes de Bordeaux Métropole
  territoires.py          28 communes Gironde élargie + Landes
  quartiers.py            11 quartiers de Bordeaux (bâti réel par quartier)
  services.py             4 missions cœur (RAAT, RAAD, DTG, PPPT)
  diagnostics_pro.py      9 diagnostics collectifs
  normes.py               référentiel normes/arrêtés + fiches surveillées
  schemas_svg.py          5 schémas explicatifs générés en SVG
  contenus.py             moteur de publication différée

contenus/*.md             file d'attente éditoriale (voir § suivant)
build/                    sources statiques copiées vers site/assets
site/                     SORTIE GÉNÉRÉE — ne jamais éditer à la main
```

---

## Chaîne éditoriale

Chaque fichier de `contenus/` porte une date de publication. Le build ne rend que
ceux dont la date est atteinte. L'action GitHub tourne **lundi, mercredi et vendredi
à 5 h** : un contenu paraît seul, le sitemap et le maillage se recalculent.

```markdown
---
titre: La question telle qu'elle est posée
question: La même, en une phrase interrogative
meta: 150 caractères
publication: 2026-08-12
tags: PPPT | copropriété
liens: /plan-pluriannuel-de-travaux/
sources: Service Public — Fiche (F10798)~https://…~7 mars 2025 | Légifrance…
---

La réponse dès la première phrase. C'est ce que reprennent les moteurs IA.

## Puis le développement
```

**Règles de rédaction :**

- La réponse en première phrase, jamais d'introduction qui tourne autour
- Le préfixe numérique du nom de fichier sert à l'ordre, il disparaît de l'URL
- **Toujours sourcer sur Service Public, Légifrance ou l'ADEME**, avec la date de
  vérification officielle. Le champ `sources` alimente le balisage `citation`
- Ne jamais affirmer un seuil réglementaire sans l'avoir vérifié à la source

⚠️ **Seuls deux articles sur douze ont été vérifiés à la source.** Les autres ont été
rédigés de mémoire et doivent être repris fiche par fiche avant publication. La
réglementation du diagnostic est un domaine où une erreur engage la cliente.

---

## Formulaire de devis

Site statique, donc pas de serveur. Le formulaire poste vers un relais de courriel.

`data/marque.py > FORMULAIRE > cle` est **vide**. Tant qu'elle l'est, le formulaire
bascule automatiquement sur la messagerie du visiteur avec la demande pré-rédigée.
Pour l'activer : créer un compte Web3Forms et coller la clé.

---

## À faire — par ordre de valeur

1. **Renseigner `FORMULAIRE > cle`** (Web3Forms, 5 minutes)
2. **Vérifier les 10 articles non sourcés** de `contenus/`
3. **Renseigner `MARQUE > tel_copro`** — ligne dédiée acquise, non communiquée
4. **Compléter les mentions légales** — hébergeur, certification, assureur RCP
5. **Intégrer les schémas SVG dans les pages** — `data/schemas_svg.py` est écrit mais
   n'est appelé que dans un aperçu autonome
6. **Compléter `data/normes.py`** — 4 entrées marquées `etabli` ou `a_verifier`
   restent à confirmer à la source (DTA, CREP, électricité, assainissement, gaz)
7. **Vidéos** — réhéberger les fichiers Instagram/Facebook avec transcription et
   balisage `VideoObject`. **Ne jamais intégrer les lecteurs Meta** : 400 à 900 Ko de
   scripts tiers, et Google n'indexe rien
8. **Références de chantiers par commune** — abaisserait la similarité entre pages
   locales de 50 % à moins de 35 %
9. **Pages quartiers pour Mérignac et Pessac**, sur le modèle de Bordeaux

---

## Déploiement

GitHub Pages sur le dossier `site/`, domaine `www.dglmexpertises.fr`.

Le domaine renvoie actuellement `ERR_SSL_PROTOCOL_ERROR` : il n'a pas de certificat
valide. GitHub Pages en délivre un automatiquement, ce qui règle le problème.

⚠️ **Lors du changement DNS chez OVH : ne toucher qu'aux enregistrements A, AAAA et
CNAME. Ne jamais toucher aux MX** — ils portent les courriels de l'entreprise
(`contact@dglmexpertises.fr`).

Créer le secret `INDEXNOW_KEY` dans les réglages du dépôt, sinon le ping aux moteurs
échoue silencieusement.

---

## État mesuré au 28 juillet 2026

| Indicateur | Valeur |
|---|---|
| Pages | 266 |
| Indexables | 264 |
| Mots par page | 693 |
| Poids HTML moyen | 17,3 Ko |
| Profondeur maximale | 2 clics |
| Pages orphelines | 0 |
| Pages sans données structurées | 0 |
| Erreurs d'audit | 0 |
| Régressions | 0 |

---

## Ce qu'il ne faut pas faire

- Éditer `site/` à la main — tout est régénéré
- Ajouter une dépendance externe, en Python comme en front
- Contourner un blocage d'audit plutôt que corriger la cause
- Inventer un chiffre, un seuil ou une référence réglementaire
- Publier un contenu dont la source n'a pas été vérifiée
- Promettre une position Google, sur le site comme en discussion
