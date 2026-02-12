# 🌤️ Application Météo - Clean Code & Design Patterns

Application Python complète pour consulter les données météorologiques en temps réel, développée selon les principes du Clean Code et utilisant plusieurs design patterns classiques du génie logiciel.

## 📋 Table des Matières

- [À Propos](#à-propos)
- [Architecture & Principes](#architecture--principes)
- [Structure du Projet](#structure-du-projet)
- [Design Patterns Implémentés](#design-patterns-implémentés)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)
- [Sources de Données](#sources-de-données)

## 🎯 À Propos

Cette application démontre l'application pratique des principes de développement logiciel suivants :

- **SOLID** : Séparation claire des responsabilités, interfaces bien définies
- **DRY** (Don't Repeat Yourself) : Code réutilisable, éviter la duplication
- **KISS** (Keep It Simple, Stupid) : Solutions simples et compréhensibles
- **YAGNI** (You Aren't Gonna Need It) : Implémentation uniquement du nécessaire

L'application permet de :
- Gérer une hiérarchie de localisations (Pays → Villes → Stations météo)
- Récupérer des données météorologiques depuis des APIs publiques
- Afficher les mesures de manière formatée et structurée
- Persister la configuration entre les sessions

## 🏗️ Architecture & Principes

### Principes SOLID Appliqués

#### Single Responsibility Principle (SRP)
Chaque classe a une responsabilité unique :
- `ConfigurationSingleton` : gestion de la configuration uniquement
- `ApiService` : appels API uniquement
- `Measurement` : représentation d'une mesure météo uniquement
- `LinkedList` / `Queue` : structures de données spécialisées

#### Open/Closed Principle (OCP)
- La classe abstraite `Location` est ouverte à l'extension (nouvelles localisations) mais fermée à la modification
- Les décorateurs permettent d'ajouter des fonctionnalités sans modifier le code existant

#### Liskov Substitution Principle (LSP)
- `Pays`, `Ville`, et `Station` peuvent tous être utilisés comme des `Location`
- Les classes filles respectent le contrat de la classe mère

#### Interface Segregation Principle (ISP)
- Interfaces minimalistes : `Observer` n'a qu'une méthode `update()`
- `Command` n'a qu'une méthode `execute()`

#### Dependency Inversion Principle (DIP)
- Le code dépend d'abstractions (`Observer`, `Command`) et non d'implémentations concrètes
- L'injection de dépendances est utilisée (ex: `DataLoader` reçoit `ApiService`)

## 📁 Structure du Projet

```
weather_app/
├── __main__.py                 # Point d'entrée de l'application
├── requirements.txt            # Dépendances Python
│
├── Configuration & Persistence
│   ├── singleton_config.py     # Pattern Singleton pour la configuration
│   └── config.json            # Stockage JSON de la configuration
│
├── Modèles de Données
│   ├── location.py            # Hiérarchie : Location → Pays → Ville → Station
│   ├── measurement.py         # Représentation d'une mesure météo
│   └── builders.py            # Pattern Builder pour Station et Ville
│
├── Structures de Données
│   ├── linked_list.py         # Liste Chaînée pour l'affichage des stations
│   └── queue.py               # File FIFO pour les requêtes API
│
├── Design Patterns
│   ├── observer.py            # Pattern Observer pour la sélection de station
│   ├── decorator.py           # Pattern Decorator pour l'affichage
│   └── command.py             # Pattern Command pour les actions utilisateur
│
├── Services
│   ├── api_service.py         # Service d'appel à l'API météo
│   └── menu.py                # Interface utilisateur (UI)
│
└── Tests Unitaires
    ├── conftest.py            # Fixtures PyTest réutilisables
    ├── test_singleton_config.py
    ├── test_location.py
    ├── test_measurement.py
    ├── test_builders.py
    ├── test_linked_list.py
    ├── test_queue.py
    ├── test_observer.py
    ├── test_decorator.py
    ├── test_command.py
    └── test_api_service.py
```

## 🎨 Design Patterns Implémentés

### 1. Singleton Pattern
**Fichier** : `singleton_config.py`

**Objectif** : Garantir une instance unique de la configuration partagée dans toute l'application.

```python
# Une seule instance pour toute l'application
config1 = ConfigurationSingleton()
config2 = ConfigurationSingleton()
assert config1 is config2  # True
```

**Avantages** :
- Point d'accès global à la configuration
- Évite les incohérences entre différentes parties de l'application
- Gestion centralisée de la persistence

### 2. Builder Pattern
**Fichier** : `builders.py`

**Objectif** : Construction progressive et validée d'objets complexes (Station, Ville).

```python
station = (StationBuilder()
    .set_id("s001")
    .set_nom("Montaudran")
    .set_ville(toulouse)
    .set_api_url("https://api.example.com")
    .build())
```

**Avantages** :
- Interface fluide et lisible
- Validation au moment du `build()`
- Réutilisation du builder avec `reset()`

### 3. Observer Pattern
**Fichier** : `observer.py`

**Objectif** : Notification automatique et chargement des données lors de la sélection d'une station.

```
StationSelector (Subject)
    ↓ notify()
DataLoader (Observer)
    ↓ update()
ApiService
```

**Avantages** :
- Couplage faible entre composants
- Ajout facile de nouveaux observateurs
- Séparation des préoccupations

### 4. Command Pattern
**Fichier** : `command.py`

**Objectif** : Encapsulation des actions utilisateur pour faciliter l'historique, l'annulation, et la journalisation.

**Commandes implémentées** :
- `SelectStationCommand` : sélectionner une station
- `RefreshDataCommand` : rafraîchir les données
- `DisplayMeasurementsCommand` : afficher les mesures
- `AddCountryCommand`, `RemoveCountryCommand`
- `AddCityCommand`, `RemoveCityCommand`
- `AddStationCommand`, `RemoveStationCommand`, `UpdateStationUrlCommand`

**Avantages** :
- Historique des commandes (via `CommandInvoker`)
- Possibilité d'ajouter undo/redo facilement
- Séparation entre demande et exécution

### 5. Decorator Pattern
**Fichier** : `decorator.py`

**Objectif** : Ajouter dynamiquement des fonctionnalités d'affichage et de logging.

**Décorateurs disponibles** :
- `@display_measurements_decorator` : formatage avancé des mesures en colonnes
- `@execution_time_decorator` : mesure du temps d'exécution
- `@error_handler_decorator` : gestion élégante des erreurs

```python
@display_measurements_decorator
def _display_station_measurements(self, station: Station):
    command = DisplayMeasurementsCommand(station)
    return self._command_invoker.execute_command(command)
```

### 6. Héritage & Polymorphisme
**Fichier** : `location.py`

**Hiérarchie** :
```
Location (ABC)
    ├── Pays
    ├── Ville (contient Pays)
    └── Station (contient Ville)
```

Chaque classe hérite de `Location` et implémente `get_info()`.

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner le projet** :
```bash
git clone <repository-url>
cd weather_app
```

2. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

Les dépendances incluent :
- `requests` : pour les appels API
- `pytest` : pour les tests unitaires
- `pytest-cov` : pour la couverture de code
- `pytest-mock` : pour les mocks dans les tests

## ▶️ Utilisation

### Lancement de l'application

```bash
python __main__.py
```

ou

```bash
python -m weather_app
```

### Premier démarrage

Au premier lancement, l'application crée automatiquement :
- Un répertoire `data/` (si inexistant)
- Un fichier `config.json` vide

Vous devez configurer la hiérarchie :

1. **Menu Configuration** → **Gérer les pays** → **Ajouter un pays**
   - Exemple : `France`

2. **Gérer les villes** → **Ajouter une ville**
   - Sélectionner le pays créé
   - Exemple : `Toulouse`

3. **Gérer les stations** → **Ajouter une station**
   - Sélectionner la ville créée
   - Entrer le nom : `Compans-Cafarelli`
   - Entrer l'URL de l'API (voir section [Sources de Données](#sources-de-données))

### Navigation dans l'application

#### 📍 Menu Principal
```
1. Voir la météo      → Consulter les stations configurées
2. Configuration      → Gérer pays, villes, stations
0. Quitter           → Sortir de l'application
```

#### 🌦️ Voir la Météo
```
- Liste numérotée de toutes les stations
- Sélection d'une station
  ├── 1. Afficher les mesures     (décorateur d'affichage)
  ├── 2. Rafraîchir les données   (nouvelle requête API)
  └── 0. Retour
```

#### ⚙️ Configuration

**Gérer les pays** :
- Lister : affiche tous les pays avec nombre de villes
- Ajouter : nom du pays
- Supprimer : suppression en cascade (+ villes + stations)

**Gérer les villes** :
- Lister : affiche toutes les villes avec pays et nombre de stations
- Ajouter : sélection du pays, nom de la ville
- Supprimer : suppression en cascade (+ stations)

**Gérer les stations** :
- Lister : affiche toutes les stations avec villes, pays, et URL
- Ajouter : sélection de la ville, nom, URL API (avec validation)
- Modifier URL : test de validité de la nouvelle URL
- Supprimer : suppression simple

## 🧪 Tests

Le projet inclut une suite complète de tests unitaires avec **PyTest**.

### Exécution des tests

```bash
# Tous les tests
pytest

# Avec couverture de code
pytest --cov=. --cov-report=html

# Un fichier spécifique
pytest test_singleton_config.py

# Verbeux
pytest -v
```

### Couverture de code

Les tests couvrent :
- ✅ Pattern Singleton (instances uniques, persistence)
- ✅ Pattern Builder (validation, interface fluide)
- ✅ Pattern Observer (notifications, observers multiples)
- ✅ Pattern Command (exécution, historique)
- ✅ Pattern Decorator (affichage, temps d'exécution, erreurs)
- ✅ Structures de données (LinkedList, Queue)
- ✅ Modèles (Location, Measurement)
- ✅ Service API (mocks, erreurs réseau, parsing)

### Fixtures PyTest

Le fichier `conftest.py` fournit des fixtures réutilisables :
- `temp_config_file` : fichier temporaire pour la configuration
- `temp_data_dir` : répertoire temporaire pour les tests
- `mock_pays`, `mock_ville`, `mock_station` : mocks des modèles
- `mock_measurement` : mock d'une mesure
- `sample_api_response` : réponse API exemple
- `mock_api_service`, `mock_config` : mocks des services

## 📊 Sources de Données

L'application utilise l'API ouverte de **Toulouse Métropole**.

### Format attendu

```json
{
  "total_count": 100,
  "results": [
    {
      "heure_de_paris": "2025-02-11T10:00:00+00:00",
      "temperature_en_degre_c": 15.5,
      "humidite": 75,
      "pression": 101325
    }
  ]
}
```

### Stations disponibles

#### Station Compans-Cafarelli (Toulouse)
```
URL: https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/42-station-meteo-toulouse-parc-compans-cafarelli/records?select=heure_de_paris%2C%20humidite%2C%20temperature_en_degre_c%2C%20pression&order_by=heure_de_paris%20DESC&limit=100
```

#### Station Montaudran (Toulouse)
```
URL: https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/12-station-meteo-toulouse-montaudran/records?select=heure_de_paris%2C%20humidite%2C%20temperature_en_degre_c%2C%20pression&order_by=heure_de_paris%20DESC&limit=100
```

### Validation des URLs

Lors de l'ajout ou de la modification d'une station, l'application :
1. Teste l'URL avec une requête HTTP
2. Vérifie la présence de la clé `results` dans la réponse
3. Propose de continuer même si la validation échoue

## 🔧 Fonctionnalités Détaillées

### Affichage des Mesures

Le décorateur `@display_measurements_decorator` fournit :
- **Groupement par date** : mesures organisées par journée
- **Affichage en colonnes** : adaptation automatique à la largeur du terminal
- **Formatage des heures** : conversion ISO 8601 → JJ/MM/AAAA HH:MM
- **Statistiques** : nombre total de mesures

Exemple d'affichage :
```
================================================================================
                         📊 MESURES MÉTÉOROLOGIQUES                           
================================================================================

📍 Nombre total de mesures: 100

────────────────────────────────────────────────────────────────────────────────
                              📅 11/02/2025                                    
────────────────────────────────────────────────────────────────────────────────
Heure        10h00        11h00        12h00        13h00      
Temp         15.5°C       16.2°C       17.8°C       18.5°C     
Hum          75%          73%          70%          68%        
Press        101325 Pa    101300 Pa    101280 Pa    101250 Pa  
```

### Gestion des Erreurs

**Erreurs réseau** :
- Timeout (10 secondes)
- Connexion refusée
- DNS invalide

**Erreurs de parsing** :
- JSON invalide
- Champs manquants (valeurs par défaut)
- Types incorrects (ignorés)

**Erreurs utilisateur** :
- Validation des choix de menu
- Confirmation avant suppression
- Messages d'erreur clairs

### Persistance

La configuration est sauvegardée automatiquement dans `config.json` :
- Format JSON avec indentation
- Encodage UTF-8
- Sauvegarde après chaque modification

Structure :
```json
{
  "pays": {
    "799c3dc8": { "nom": "France" }
  },
  "villes": {
    "f52f253f": { "nom": "Toulouse", "pays_id": "799c3dc8" }
  },
  "stations": {
    "3aab4c15": {
      "nom": "Compans-Cafarelli",
      "ville_id": "f52f253f",
      "api_url": "https://..."
    }
  }
}
```

## 💡 Bonnes Pratiques Appliquées

### Code Quality

- ✅ **Type Hints** : tous les paramètres et retours sont typés
- ✅ **Docstrings** : documentation complète en français
- ✅ **Nommage** : variables et fonctions explicites
- ✅ **PyLint** : respect des conventions PEP 8
- ✅ **Tests** : couverture > 90%

### Patterns FIRST (tests)

- **F**ast : tests rapides (mocks)
- **I**ndependent : tests indépendants
- **R**epeatable : résultats déterministes
- **S**elf-validating : pass/fail automatique
- **T**imely : écrits avec le code

### Patterns AAA (tests)

```python
def test_something(self):
    # Arrange : préparation
    config = ConfigurationSingleton()
    
    # Act : exécution
    config.add_pays("fr001", "France")
    
    # Assert : vérification
    assert "fr001" in config.get_pays()
```

## 🔮 Évolutions Possibles

### Nouvelles Fonctionnalités
- Export des données (CSV, Excel)
- Graphiques avec matplotlib
- Alertes météo
- API REST pour consultation externe
- Interface graphique (Tkinter, PyQt)

### Nouveaux Patterns
- **Strategy** : différentes stratégies d'affichage
- **Factory** : création dynamique de stations selon le type
- **Adapter** : support d'autres APIs météo
- **Facade** : simplification de l'interface pour scripts externes

## 📚 Ressources

### Documentation Python
- [PEP 8 – Style Guide](https://pep8.org/)
- [Type Hints – PEP 484](https://www.python.org/dev/peps/pep-0484/)
- [Abstract Base Classes](https://docs.python.org/3/library/abc.html)

### Design Patterns
- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [Source Making](https://sourcemaking.com/design_patterns)
- "Design Patterns: Elements of Reusable Object-Oriented Software" (Gang of Four)

### Clean Code
- "Clean Code" by Robert C. Martin
- "The Pragmatic Programmer" by Hunt & Thomas

## 📝 Licence

Projet éducatif démontrant l'application des principes du Clean Code et des design patterns en Python.
