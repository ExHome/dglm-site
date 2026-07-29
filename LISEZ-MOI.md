# DGLM Expertises — site copropriété & travaux

264 pages · 0 erreur d'audit · 0 régression · 17,1 Ko par page · profondeur maximale 2 clics.

---

## 1. Ce qui doit être fait avant la mise en ligne

Cinq points, par ordre d'urgence. Les trois premiers sont bloquants.

| # | Action | Où |
|---|---|---|
| 1 | **Vérifier l'ordre des portraits** — voir `planche-portraits.png`. Je les ai extraits de votre présentation dans l'ordre du fichier PDF, pas dans l'ordre visuel. Une erreur d'attribution serait gênante. | `data/marque.py`, champ `photo` |
| 2 | **Relecture réglementaire** : paliers PPPT, calendrier DPE collectif, seuils PEMD, régime de l'audit énergétique. Ma connaissance s'arrête à mai 2026. | `data/services.py`, `data/diagnostics_pro.py` |
| 3 | **Numéro de la ligne copro** acquise | `data/marque.py`, `tel_copro` |
| 4 | Compléter les mentions légales : hébergeur, n° de certification, assureur RCP | `build.py`, `page_mentions()` |
| 5 | Brancher le formulaire de contact (Formspree, Netlify Forms ou votre CRM) | `build.py`, `page_contact()` |

---

## 2. Mise en ligne

```bash
python3 build.py        # génère /site
python3 audit_seo.py    # 8 contrôles anti-cannibalisation — bloquant
python3 veille_seo.py   # 12 indicateurs, détection de régression — bloquant
```

Déposer le dépôt sur GitHub, activer GitHub Pages sur le dossier `site/`, pointer
`www.dglmexpertises.fr` dessus.

Créer ensuite le secret `INDEXNOW_KEY` dans les réglages du dépôt (Settings →
Secrets → Actions), sinon le ping aux moteurs échoue silencieusement.

**Puis, immédiatement :** changer l'URL de votre fiche Google Business Profile pour
pointer ici. C'est le levier le plus puissant du dossier, il est gratuit, et il est
réversible.

---

## 3. Ce qui tourne tout seul

L'action GitHub s'exécute **lundi, mercredi et vendredi à 5 h**, et à chaque
modification :

1. régénère les 264 pages, avec les dates réglementaires recalculées
2. publie le contenu dont la date d'échéance est atteinte
3. lance l'audit anti-cannibalisation — **bloque** en cas de collision
4. lance la veille anti-régression — **bloque** si le site s'est dégradé
5. met à jour `sitemap.xml` avec les `lastmod`
6. déploie et ping les moteurs
7. enregistre la nouvelle référence de veille

Vous n'avez rien à faire. En cas de blocage, l'échec est visible dans l'onglet
Actions du dépôt, avec le motif.

---

## 4. Ajouter du contenu

Créer un fichier dans `contenus/`, sur ce modèle :

```markdown
---
titre: La question, telle qu'elle est posée
question: La même, en une phrase interrogative
meta: 150 caractères qui donnent envie de cliquer
publication: 2026-08-12
tags: PPPT | copropriété
liens: /plan-pluriannuel-de-travaux/
---

La réponse dès la première phrase. C'est ce que reprennent les moteurs IA.

## Puis le développement
```

Le préfixe numérique du nom de fichier ne sert qu'à l'ordre, il disparaît de l'URL.
Rien d'autre à toucher : la page, le maillage, le sitemap et les données structurées
se génèrent seuls.

**Réservoir actuel :** 3 publiés, 6 programmés jusqu'au 10 août.

---

## 5. Le jour de la sortie de contrat du site A

Une seule ligne à changer :

```python
# data/marque.py
SITE_A_SOUS_CONTRAT = False
```

Relancer le build. Le pare-feu de requêtes se lève, le site peut cibler l'ensemble
des diagnostics. Rediriger ensuite l'intégralité de `dglm-expertises.com` en 301 vers
`www.dglmexpertises.fr` — vous récupérez son historique sans changer une URL ici.

---

## 6. Choix techniques, et pourquoi

**Zéro requête externe.** Pas de Google Fonts, pas de framework, pas de script tiers.
Lora est auto-hébergée, réduite au latin (207 Ko → 45 Ko), préchargée. Le corps de
texte utilise la pile système, qui s'affiche instantanément. C'est ce qui donne un
LCP quasi nul sur mobile.

**HTML statique.** Pas de base de données, pas de PHP, rien à mettre à jour, rien à
pirater. Un site qui tiendra dix ans sans maintenance.

**Profondeur 2 clics.** Sur 264 pages, c'est ce qui fait que Google explore tout à
chaque passage au lieu d'ignorer la moitié du site.

**Portraits en WebP** 224 px (751 Ko → 57 Ko), avec repli PNG.

**Séparation par la requête, pas par la marque.** Les deux sites appartiennent à la
même entreprise et Google le verra. Ce qui tue, c'est le contenu dupliqué et le
double ciblage — les deux sont contrôlés automatiquement.

---

## 7. Ce que je ne peux pas garantir

La position. Personne ne le peut, et méfiez-vous de qui vous le promet.

Ce qui est maîtrisé ici : l'architecture, la performance, les données structurées,
la qualité et la fraîcheur du contenu, l'accessibilité, l'absence de cannibalisation.
Ce qui ne l'est pas et se joue ailleurs : vos avis Google, vos liens entrants, et la
concurrence.

Les trois leviers hors-site, par ordre d'impact :

1. **Fiche Google Business** — catégorie, photos, publications hebdomadaires, et
   surtout des avis récents. C'est 40 % du local pack.
2. **Liens entrants** — annuaire FIDI, fédérations de syndics, chambres
   professionnelles, presse locale. Le contenu de `/questions/` est fait pour ça.
3. **Citations cohérentes** — même nom, même adresse, même téléphone partout.

---

## 8. Prochains chantiers, par valeur décroissante

1. **Recharger le réservoir éditorial** avant le 10 août
2. **Vidéos Instagram et Facebook** réhébergées sur le site avec transcription —
   n'intégrez jamais les lecteurs Meta, ils chargent 400 à 900 Ko de scripts tiers
   et Google n'indexe rien
3. **Références de chantiers réels** par commune : c'est ce qui ferait passer la
   similarité entre pages locales de 50 % à moins de 35 %
4. **Grille tarifaire** dans le simulateur, si vous acceptez de l'afficher
5. **Pages quartiers** pour Mérignac et Pessac, sur le modèle de Bordeaux
