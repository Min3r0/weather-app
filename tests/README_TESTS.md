# 🧪 Tests Unitaires - Application Météo

Suite complète de tests unitaires pour l'application météo, développée selon les principes du Clean Code et les bonnes pratiques de testing.

## 📋 Table des Matières

- [Principes de Test](#principes-de-test)
- [Structure des Tests](#structure-des-tests)
- [Installation](#installation)
- [Exécution des Tests](#exécution-des-tests)
- [Couverture de Code](#couverture-de-code)
- [Détails des Tests](#détails-des-tests)

## 🎯 Principes de Test

Les tests suivent les principes **FIRST** :

- **F**ast : Tests rapides pour feedback immédiat
- **I**ndependent : Chaque test est indépendant
- **R**epeatable : Résultats reproductibles
- **S**elf-validating : Pass/Fail automatique
- **T**imely : Écrits en même temps que le code

### Méthodologie AAA

Chaque test suit le pattern **Arrange-Act-Assert** :

```python
def test_example():
    # Arrange - Préparer les données
    station = Station("id", "nom", ville, "url")
    
    # Act - Exécuter l'action
    result = station.get_info()
    
    # Assert - Vérifier le résultat
    assert "Station: nom" in result
```

### Clean Code dans les Tests

- ✅ Noms de tests descriptifs et explicites
- ✅ Un seul concept testé par test
- ✅ Fixtures pour réutilisation
- ✅ Mocks pour isoler les dépendances
- ✅ Tests lisibles comme de la documentation

## 📁 Structure des Tests

```
tests/
├── __init__.py                    # Initialisation du package
├── conftest.py                    # Fixtures communes
├── test_linked_list.py            # Tests de la liste chaînée
├── test_queue.py                  # Tests de la file
├── test_measurement.py            # Tests des mesures météo
├── test_location.py               # Tests des localisations (héritage)
├── test_builders.py               # Tests du pattern Builder
├── test_observer.py               # Tests du pattern Observer
├── test_command.py                # Tests du pattern Command
├── test_decorator.py              # Tests du pattern Decorator
├── test_api_service.py            # Tests du service API
└── test_singleton_config.py       # Tests du Singleton Configuration
```

## 🚀 Installation

### 1. Installer les dépendances de test

```bash
pip install -r requirements-test.txt
```

### 2. Dépendances installées

- `pytest` : Framework de test
- `pytest-cov` : Couverture de code
- `pytest-mock` : Mocking facilité
- `requests` : Dépendance du projet

## ▶️ Exécution des Tests

### Tous les tests

```bash
pytest
```

### Tests avec affichage détaillé

```bash
pytest -v
```

### Tests d'un fichier spécifique

```bash
pytest tests/test_linked_list.py
```

### Tests d'une classe spécifique

```bash
pytest tests/test_location.py::TestStation
```

### Tests d'une méthode spécifique

```bash
pytest tests/test_location.py::TestStation::test_station_creation
```

### Tests avec sortie détaillée

```bash
pytest -vv -s
```

### Tests avec markers

```bash
# Tests unitaires uniquement
pytest -m unit

# Tests d'intégration
pytest -m integration

# Exclure les tests lents
pytest -m "not slow"
```

### Arrêter au premier échec

```bash
pytest -x
```

### Mode parallèle (si pytest-xdist installé)

```bash
pytest -n auto
```

## 📊 Couverture de Code

### Générer un rapport de couverture

```bash
pytest --cov=weather_app --cov-report=html
```

### Afficher la couverture dans le terminal

```bash
pytest --cov=weather_app --cov-report=term-missing
```

### Exiger une couverture minimale

```bash
pytest --cov=weather_app --cov-fail-under=80
```

### Visualiser le rapport HTML

Après avoir généré le rapport HTML :

```bash
# Ouvrir le fichier htmlcov/index.html dans un navigateur
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## 📝 Détails des Tests

### test_linked_list.py (34 tests)

Tests de la structure de données Liste Chaînée :

- ✅ Création et manipulation de nœuds
- ✅ Ajout et suppression d'éléments
- ✅ Accès par index
- ✅ Itération
- ✅ Gestion des erreurs (IndexError)

**Couverture** : 100% de linked_list.py

### test_queue.py (17 tests)

Tests de la structure de données File (Queue) :

- ✅ Opérations FIFO
- ✅ Enqueue/Dequeue
- ✅ Peek sans modification
- ✅ Gestion de file vide
- ✅ Types de données variés

**Couverture** : 100% de queue.py

### test_measurement.py (16 tests)

Tests de la classe Measurement :

- ✅ Création et propriétés
- ✅ Formatage des dates
- ✅ Gestion de dates invalides
- ✅ Représentations string et repr
- ✅ Valeurs extrêmes (négatives, zéro)

**Couverture** : 100% de measurement.py

### test_location.py (28 tests)

Tests de la hiérarchie Location (héritage) :

- ✅ Classes Pays, Ville, Station
- ✅ Relations parent-enfant
- ✅ Auto-ajout aux parents
- ✅ get_info() pour chaque type
- ✅ Hiérarchies complexes

**Couverture** : 100% de location.py

### test_builders.py (23 tests)

Tests du pattern Builder :

- ✅ Construction progressive
- ✅ Interface fluide (method chaining)
- ✅ Validation des champs obligatoires
- ✅ Reset et réutilisation
- ✅ StationBuilder et VilleBuilder

**Couverture** : 100% de builders.py

### test_observer.py (18 tests)

Tests du pattern Observer :

- ✅ Attach/Detach d'observateurs
- ✅ Notifications avec arguments
- ✅ StationSelector et DataLoader
- ✅ Tests d'intégration Observer
- ✅ Gestion de multiples observateurs

**Couverture** : 100% de observer.py

### test_command.py (25 tests)

Tests du pattern Command :

- ✅ Toutes les commandes (Add, Remove, Update)
- ✅ CommandInvoker et historique
- ✅ Exécution et résultats
- ✅ Séquences de commandes
- ✅ Success et failure cases

**Couverture** : 100% de command.py

### test_decorator.py (20 tests)

Tests du pattern Decorator :

- ✅ display_measurements_decorator
- ✅ execution_time_decorator
- ✅ error_handler_decorator
- ✅ Combinaisons de décorateurs
- ✅ Préservation des métadonnées

**Couverture** : 100% de decorator.py

### test_api_service.py (20 tests)

Tests du service API :

- ✅ Appels API réussis
- ✅ Gestion timeout et erreurs réseau
- ✅ Parsing de données JSON
- ✅ Validation d'URLs
- ✅ Utilisation de la Queue
- ✅ Mocking avec requests

**Couverture** : 100% de api_service.py

### test_singleton_config.py (28 tests)

Tests du Singleton Configuration :

- ✅ Pattern Singleton (instance unique)
- ✅ CRUD pour Pays, Villes, Stations
- ✅ Suppression en cascade
- ✅ Persistance JSON
- ✅ Filtrage par ID parent
- ✅ get_all_stations_list

**Couverture** : 100% de singleton_config.py

## 🎨 Bonnes Pratiques Appliquées

### Isolation des Tests

- Utilisation de fixtures pour les dépendances communes
- Mocking des appels externes (API, fichiers)
- Réinitialisation du Singleton entre tests

### Nommage Descriptif

```python
def test_station_auto_added_to_ville(self):
    """Test que la station est automatiquement ajoutée à la ville."""
```

### Organisation AAA

```python
def test_add_measurement(self):
    # Arrange
    station = Station(...)
    measurement = Measurement(...)
    
    # Act
    station.add_measurement(measurement)
    
    # Assert
    assert measurement in station.get_measurements()
```

### Tests de Cas Limites

- Listes vides
- Valeurs None
- Index invalides
- Erreurs réseau
- Données malformées

### Documentation

- Docstrings pour chaque test
- Commentaires pour logique complexe
- README détaillé

## 📈 Statistiques

- **Nombre total de tests** : ~230 tests
- **Couverture de code** : 100% visé
- **Temps d'exécution** : < 5 secondes
- **Fichiers testés** : 10 modules principaux

## 🔍 Commandes Utiles

### Lister tous les tests

```bash
pytest --collect-only
```

### Tests en mode verbose avec traceback complet

```bash
pytest -vv --tb=long
```

### Afficher les 10 tests les plus lents

```bash
pytest --durations=10
```

### Mode watch (nécessite pytest-watch)

```bash
ptw
```

### Générer un rapport JUnit XML

```bash
pytest --junitxml=report.xml
```

## 💡 Conseils

1. **Exécuter les tests fréquemment** : Après chaque modification
2. **Maintenir 100% de couverture** : Objectif de qualité
3. **Tests rapides** : Moins de 5 secondes pour la suite complète
4. **Tests indépendants** : Ordre d'exécution n'importe pas
5. **Mocking approprié** : Ne pas dépendre de services externes

## 🤝 Contribution

Lors de l'ajout de nouvelles fonctionnalités :

1. Écrire les tests **avant** le code (TDD optionnel)
2. Assurer une couverture de 100% du nouveau code
3. Suivre les conventions de nommage existantes
4. Documenter les tests complexes
5. Tester les cas limites et erreurs

## 📚 Références

- [Documentation pytest](https://docs.pytest.org/)
- [Clean Code by Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Test-Driven Development by Kent Beck](https://www.oreilly.com/library/view/test-driven-development/0321146530/)