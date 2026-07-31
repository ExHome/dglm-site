# -*- coding: utf-8 -*-
"""
MARQUE ET STRATÉGIE D'OCCUPATION.

Décision : le site est DGLM Expertises. Pas de marque tierce.
Objectif final = ce site absorbe le site A à la sortie de contrat, donc tout
actif construit sous un autre nom serait à jeter le jour de la migration.

Conséquence sur la séparation : on ne sépare PAS les identités (c'est la même
entreprise, et Google le verra de toute façon). On sépare les REQUÊTES.
La duplication de contenu et le double ciblage tuent ; deux sites d'une même
entreprise sur deux sujets différents, non.
"""

MARQUE = dict(
    nom="DGLM Expertises",
    nom_long="DGLM Expertises",
    baseline="Copropriété & travaux",
    signature="L'expertise en action",
    endossement="Structure familiale indépendante, certifiée, créée en 2020",
    domaine="https://www.dglmexpertises.fr",

    rue="27 ter rue des Sables",
    cp="33320",
    ville="Eysines",
    lat="44.8846",
    lon="-0.6503",
    tel="06 07 35 15 05",
    tel_raw="+33607351505",
    # Ligne dédiée copropriété — utilisée sur tout ce site (attribution des appels).
    tel_copro="06 07 35 15 05",
    tel_copro_raw="+33607351505",
    email="contact@dglmexpertises.fr",
    # Fiche Google Business (avis) — levier n°1 du référencement local.
    google_avis="https://share.google/dLH73ZQHhsA1tVdGg",
    # Avis certifiés DiagAdvisor (spécialisé diagnostiqueurs).
    diagadvisor="https://www.diagadvisor.fr/avis-dglm-expertises-33000.html",

    societe="DGLM Expertises",
    siret="89128707000017",
    rcs="891 287 070 R.C.S. Bordeaux",
    depuis="2020",
    federation="Alliance du Diagnostic Immobilier",

    site_a_url="https://www.dglm-expertises.com/",
    site_a_nom="DGLM Expertises — vente et location",
    site_a_ancre="Particuliers — vente et location",
)

# ---------------------------------------------------------------------------
# INTERRUPTEUR DE MIGRATION
# Tant que le site A est sous contrat : True (le pare-feu de requêtes est actif).
# À la sortie de contrat : passer à False, relancer build.py, et 301 le site A.
# Les pages de vente/location viendront alors se poser sans changer une URL.
# ---------------------------------------------------------------------------
SITE_A_SOUS_CONTRAT = True

REQUETES_SITE_A = [
    "diagnostic immobilier", "diagnostiqueur immobilier", "dpe",
    "diagnostic de performance énergétique", "diagnostic de performances energetiques",
    "diagnostic amiante", "état d'amiante", "dapp", "dta", "dossier technique amiante",
    "diagnostic plomb", "crep", "constat de risque d'exposition au plomb",
    "diagnostic termites", "diagnostic gaz", "état de l'installation gaz",
    "diagnostic électricité", "diagnostic electricite", "loi carrez",
    "diagnostic loi carrez", "loi boutin", "mesurage", "surface habitable",
    "erp", "état des risques", "assainissement", "dossier de diagnostic technique",
    "ddt", "diagnostic vente", "diagnostic location", "devis diagnostic immobilier",
]
if not SITE_A_SOUS_CONTRAT:
    REQUETES_SITE_A = []

REQUETES_SITE_B = [
    "repérage amiante avant travaux", "raat",
    "repérage amiante avant démolition", "raad",
    "diagnostic technique global", "dtg",
    "plan pluriannuel de travaux", "pppt",
    "fonds de travaux", "dpe collectif", "obligations copropriété", "syndic",
]

QUALIFICATIFS = [
    "collectif", "collective", "collectives", "copropriété", "copropriétés",
    "parties communes", "parties privatives", "avant travaux", "avant démolition",
    "syndic", "bailleur", "immeuble", "pemd", "professionnel", "patrimoine",
    "avant acquisition", "avant réhabilitation",
]

LIENS_MAX_VERS_SITE_A = 1

# ---------------------------------------------------------------------------
# ÉQUIPE — signal E-E-A-T. Des diagnostiqueurs nommés et certifiés valent
# davantage qu'une page « à propos ». Le site A n'a rien de tel.
# ---------------------------------------------------------------------------
EQUIPE = [
    dict(photo="portrait-1", nom="Aude de Gentile", role="Co-gérante — direction financière et développement",
         bio="Cofondatrice de DGLM Expertises en 2020. Pilote le développement du pôle "
             "copropriété et travaux et la relation avec les syndics et administrateurs "
             "de biens.", cert=""),
    dict(photo="portrait-2", nom="Thibault Le Moine", role="Co-gérant — directeur conformité",
         bio="Cofondateur. Garant de la conformité des méthodes, des certifications et "
             "des rapports remis.", cert=""),
    dict(photo="portrait-4", nom="Amaury Molinier", role="Directeur opérationnel technique et diagnostiqueur",
         bio="Encadre les équipes terrain et les missions techniques complexes : "
             "repérages avant travaux et avant démolition, diagnostics techniques globaux.",
         cert=""),
    dict(photo="portrait-5", nom="Nicolas Louvet", role="Diagnostiqueur certifié",
         bio="Interventions amiante, plomb, termites et performance énergétique sur "
             "Bordeaux Métropole.",
         cert="Certifié LCC Qualixpert — amiante, plomb, termites, DPE"),
    dict(photo="portrait-6", nom="Nicolas Péré", role="Diagnostiqueur certifié",
         bio="Missions de repérage et de diagnostic sur immeubles collectifs et "
             "patrimoines gérés.", cert=""),
    dict(photo="portrait-7", nom="Virgile Poulain", role="Diagnostiqueur certifié",
         bio="Missions de repérage avant travaux et de diagnostic sur bâti ancien et "
             "copropriétés.", cert=""),
    dict(photo="portrait-3", nom="Isabelle Doussau de Bazignan", role="Assistante de direction",
         bio="Planification des interventions, suivi des rapports et interface avec les "
             "conseils syndicaux.", cert=""),
]


# ---------------------------------------------------------------------------
# FORMULAIRE DE DEVIS
# Site statique : pas de serveur, donc pas de PHP. Le formulaire poste vers un
# service de relais qui expédie le message par courriel.
#
# Mise en service (5 minutes, gratuit) :
#   1. créer un compte sur https://web3forms.com avec contact@dglmexpertises.fr
#   2. copier la clé d'accès reçue
#   3. la coller ci-dessous, relancer build.py
#
# Tant que la clé est vide, le formulaire bascule automatiquement sur un envoi
# par le logiciel de messagerie du visiteur, avec le récapitulatif pré-rempli :
# le site reste utilisable dès le premier jour.
# ---------------------------------------------------------------------------
FORMULAIRE = dict(
    endpoint="https://api.web3forms.com/submit",
    cle="",                                   # ⚠ à renseigner
    destinataire="contact@dglmexpertises.fr",
    objet="Demande de devis — site copropriété",
)
