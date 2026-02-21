# Meteo_projet

Pipeline Python de collecte, nettoyage, stockage et visualisation de données météo publiques de Toulouse Métropole.

## Objectif

Ce projet récupère les mesures de plusieurs stations météo via API, applique un nettoyage de base (valeurs manquantes, doublons, outliers), puis enregistre les données consolidées dans un CSV.

## Fonctionnalités

- Collecte des données météo depuis l'API OpenData de Toulouse Métropole.
- Traitement multi-stations (`montaudran`, `pech-david`, `compans-cafarelli`, `marengo`).
- Nettoyage des données via une classe dédiée.
- Sauvegarde incrémentale dans `data/cleaned_data.csv`.
- Visualisation console de la ligne la plus récente.
- Architecture orientée interfaces + pipeline builder.

## Structure du projet

```text
Meteo_projet/
├── __main__.py                  # Point d'entrée principal
├── DataPipeline.py              # Pipeline et builder
├── src/
│   ├── collectors/              # Sources de données (API, CSV)
│   ├── cleaners/                # Logique de nettoyage
│   ├── storage/                 # Persistance (CSV)
│   ├── visualizers/             # Affichage / visualisation
│   ├── models/                  # Objets métier (StationMeteo, MesureMeteo)
│   ├── Interface/               # Contrats abstraits
│   └── commands/                # Command pattern
├── utils/
│   ├── APIClient.py             # Client API + liste des stations
│   └── ListeChaine.py           # Structure LinkedList utilitaire
└── tests/
```

## Prérequis

- Python 3.10+
- `pip`
- Connexion internet (appel API externe)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
pip install pandas requests
```

## Exécution

Depuis la racine du projet :

```bash
# Toutes les stations
python __main__.py

# Une ou plusieurs stations précises
python __main__.py --stations montaudran pech-david

# Afficher la liste des stations disponibles
python __main__.py --list-stations
```

Le pipeline :
1. interroge chaque station,
2. nettoie les données,
3. écrit les résultats dans `data/cleaned_data.csv`,
4. affiche la dernière mesure traitée,
5. supprime les doublons globaux en fin d'exécution.

## Composants principaux

- **Collecte** : `src/collectors/APIDataCollector.py`
- **Nettoyage** : `src/cleaners/DataCleaner.py`
- **Stockage** : `src/storage/CSVStorage.py`
- **Visualisation** : `src/visualizers/Visualizer.py`
- **Orchestration** : `DataPipeline.py` + `__main__.py`

## Notes techniques

- Le `APIClient` est implémenté en singleton : l'instance est partagée.
- Le stockage CSV est en mode append.
- Le nettoyage ajoute `nom_station` et sépare `heure_de_paris` en colonnes `date` et `time`.

## Pistes d'amélioration

- Ajouter un `requirements.txt` ou `pyproject.toml`.
- Ajouter des tests unitaires pour `DataCleaner` et `DataPipeline`.
- Ajouter une visualisation graphique (matplotlib/plotly) en plus de la sortie console.
- Ajouter un dossier `data/` créé automatiquement si absent.
