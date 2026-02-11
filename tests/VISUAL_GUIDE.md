# 🎨 Guide Visuel des Tests

Guide visuel avec exemples concrets d'utilisation de la suite de tests.

## 📸 Exemples d'Exécution

### 1. Lancement Basique

```bash
$ pytest
```

**Sortie attendue :**
```
======================== test session starts =========================
platform linux -- Python 3.11.0, pytest-7.4.3, pluggy-1.3.0
rootdir: /path/to/project
plugins: cov-4.1.0, mock-3.12.0
collected 229 items

tests/test_api_service.py .................... [ 8%]
tests/test_builders.py ....................... [ 18%]
tests/test_command.py ........................ [ 29%]
tests/test_decorator.py ...................... [ 38%]
tests/test_linked_list.py .................... [ 53%]
tests/test_location.py ....................... [ 65%]
tests/test_measurement.py .................... [ 72%]
tests/test_observer.py ................       [ 80%]
tests/test_queue.py .................         [ 87%]
tests/test_singleton_config.py .............. [100%]

======================== 229 passed in 3.42s =========================
```

---

### 2. Mode Verbose

```bash
$ pytest -v
```

**Sortie attendue :**
```
tests/test_linked_list.py::TestNode::test_node_creation PASSED         [ 0%]
tests/test_linked_list.py::TestNode::test_node_with_different_data_types PASSED [ 1%]
tests/test_linked_list.py::TestLinkedList::test_empty_list_creation PASSED [ 2%]
tests/test_linked_list.py::TestLinkedList::test_append_single_element PASSED [ 3%]
tests/test_linked_list.py::TestLinkedList::test_append_multiple_elements PASSED [ 4%]
...
======================== 229 passed in 3.45s =========================
```

---

### 3. Avec Couverture de Code

```bash
$ pytest --cov=weather_app --cov-report=term-missing
```

**Sortie attendue :**
```
======================== test session starts =========================
...
======================== 229 passed in 3.89s =========================

---------- coverage: platform linux, python 3.11.0 -----------
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
weather_app/__init__.py                     2      0   100%
weather_app/config/singleton_config.py    78      0   100%
weather_app/data_structures/linked_list.py 45     0   100%
weather_app/data_structures/queue.py       28      0   100%
weather_app/models/builders.py             42      0   100%
weather_app/models/location.py             67      0   100%
weather_app/models/measurement.py          32      0   100%
weather_app/patterns/command.py           112      0   100%
weather_app/patterns/decorator.py          58      0   100%
weather_app/patterns/observer.py           34      0   100%
weather_app/services/api_service.py        56      0   100%
---------------------------------------------------------------------
TOTAL                                     554      0   100%
```

---

### 4. Test d'un Fichier Spécifique

```bash
$ pytest tests/test_location.py -v
```

**Sortie attendue :**
```
tests/test_location.py::TestPays::test_pays_creation PASSED           [ 3%]
tests/test_location.py::TestPays::test_pays_inherits_from_location PASSED [ 7%]
tests/test_location.py::TestPays::test_add_ville_to_pays PASSED       [10%]
tests/test_location.py::TestPays::test_add_multiple_villes PASSED     [14%]
tests/test_location.py::TestPays::test_add_ville_twice_ignored PASSED [17%]
tests/test_location.py::TestPays::test_get_info PASSED                [21%]
tests/test_location.py::TestPays::test_get_villes_returns_copy PASSED [25%]
tests/test_location.py::TestVille::test_ville_creation PASSED         [28%]
...
======================== 28 passed in 0.52s ==========================
```

---

### 5. Test d'une Classe Spécifique

```bash
$ pytest tests/test_location.py::TestStation -v
```

**Sortie attendue :**
```
tests/test_location.py::TestStation::test_station_creation PASSED
tests/test_location.py::TestStation::test_station_inherits_from_location PASSED
tests/test_location.py::TestStation::test_station_auto_added_to_ville PASSED
tests/test_location.py::TestStation::test_api_url_getter PASSED
tests/test_location.py::TestStation::test_api_url_setter PASSED
tests/test_location.py::TestStation::test_add_measurement PASSED
tests/test_location.py::TestStation::test_add_multiple_measurements PASSED
tests/test_location.py::TestStation::test_clear_measurements PASSED
tests/test_location.py::TestStation::test_get_info PASSED
tests/test_location.py::TestStation::test_get_measurements_returns_copy PASSED

======================== 10 passed in 0.21s ==========================
```

---

### 6. Test d'une Méthode Spécifique

```bash
$ pytest tests/test_location.py::TestStation::test_add_measurement -v
```

**Sortie attendue :**
```
tests/test_location.py::TestStation::test_add_measurement PASSED    [100%]

======================== 1 passed in 0.08s ===========================
```

---

### 7. Avec Makefile

```bash
$ make test-coverage
```

**Sortie attendue :**
```
═══════════════════════════════════════════════════════
   Tests Unitaires - Application Météo
═══════════════════════════════════════════════════════

📊 Exécution des tests avec couverture...
...
======================== 229 passed in 3.89s =========================
...
TOTAL                                     554      0   100%

✅ Tests terminés
```

---

### 8. Génération du Rapport HTML

```bash
$ pytest --cov=weather_app --cov-report=html
```

**Sortie attendue :**
```
======================== 229 passed in 4.12s =========================

Coverage HTML written to dir htmlcov
```

**Puis ouvrir htmlcov/index.html :**

```
Coverage Report - 100%

Module                          Statements  Missing  Coverage
───────────────────────────────────────────────────────────
config/singleton_config.py           78        0      100%
data_structures/linked_list.py       45        0      100%
data_structures/queue.py             28        0      100%
models/builders.py                   42        0      100%
models/location.py                   67        0      100%
models/measurement.py                32        0      100%
patterns/command.py                 112        0      100%
patterns/decorator.py                58        0      100%
patterns/observer.py                 34        0      100%
services/api_service.py              56        0      100%
───────────────────────────────────────────────────────────
TOTAL                               554        0      100%
```

---

### 9. En Cas d'Échec

```bash
$ pytest
```

**Exemple de sortie avec échec :**
```
======================== test session starts =========================
...
tests/test_location.py::TestStation::test_add_measurement FAILED    [65%]

=========================== FAILURES ===================================
______________ TestStation.test_add_measurement ________________________

self = <tests.test_location.TestStation object at 0x7f8b3c4d5e90>

    def test_add_measurement(self):
        """Test l'ajout d'une mesure."""
        pays = Pays("fr001", "France")
        ville = Ville("v001", "Toulouse", pays)
        station = Station("s001", "Montaudran", ville, "https://api.com")
        
        measurement = Measurement(
            heure="2025-02-11T10:00:00+00:00",
            temperature=20.0,
            humidite=70,
            pression=101000
        )
        
        station.add_measurement(measurement)
        
        measurements = station.get_measurements()
>       assert len(measurements) == 1
E       AssertionError: assert 0 == 1
E        +  where 0 = len([])

tests/test_location.py:234: AssertionError
===================== 1 failed, 228 passed in 3.67s ====================
```

---

### 10. Tests les Plus Lents

```bash
$ pytest --durations=10
```

**Sortie attendue :**
```
======================== slowest 10 durations ==========================
0.45s call     tests/test_api_service.py::TestApiService::test_fetch_data_success
0.32s call     tests/test_singleton_config.py::TestConfigurationSingleton::test_persistence
0.18s call     tests/test_decorator.py::TestExecutionTimeDecorator::test_decorator_measures_time
0.12s call     tests/test_observer.py::TestObserverIntegration::test_station_selection_triggers_data_loading
0.09s call     tests/test_command.py::TestCommandIntegration::test_command_sequence_with_invoker
0.07s setup    tests/test_singleton_config.py::TestConfigurationSingleton::test_singleton_instance
0.05s call     tests/test_builders.py::TestStationBuilder::test_build_complete_station
0.04s call     tests/test_location.py::TestLocationHierarchy::test_full_hierarchy
0.03s call     tests/test_queue.py::TestQueue::test_multiple_operations_sequence
0.02s call     tests/test_linked_list.py::TestLinkedList::test_iteration
======================== 229 passed in 3.42s =========================
```

---

## 🎯 Scénarios d'Utilisation

### Développement Quotidien

```bash
# Rapide : Lancer les tests après chaque modification
pytest

# Si tout passe, vérifier la couverture
pytest --cov=weather_app --cov-report=term-missing
```

### Avant un Commit

```bash
# Pipeline complète avec Makefile
make ci

# Ou manuellement
make clean
make install
make test-coverage
make lint
```

### Debugging d'un Test

```bash
# Lancer avec plus de détails
pytest tests/test_location.py::TestStation::test_add_measurement -vv -s

# Arrêter au premier échec
pytest -x

# Afficher les variables locales
pytest --showlocals
```

### Développement d'une Nouvelle Fonctionnalité

```bash
# 1. Écrire le test
# 2. Lancer uniquement ce test
pytest tests/test_new_feature.py::TestNewFeature::test_basic_functionality -v

# 3. Une fois que ça passe, lancer tous les tests
pytest

# 4. Vérifier qu'on n'a pas cassé la couverture
pytest --cov=weather_app --cov-fail-under=100
```

---

## 📊 Visualisation de la Couverture

### Rapport Terminal (Résumé)

```
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
weather_app/__init__.py                     2      0   100%
weather_app/config/singleton_config.py    78      0   100%
...
TOTAL                                     554      0   100%
```

### Rapport Terminal (Détaillé avec lignes manquantes)

```
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
weather_app/__init__.py                     2      0   100%
weather_app/config/singleton_config.py    78      0   100%
weather_app/data_structures/linked_list.py 45     0   100%
...
TOTAL                                     554      0   100%
```

### Rapport HTML (Exemple pour un fichier)

```
weather_app/models/location.py - Coverage: 100%

 1  """Modèles pour les localisations avec héritage."""
 2  from typing import List
 3  from abc import ABC, abstractmethod
 4  
 5  
 6  class Location(ABC):
 7      """Classe abstraite de base."""
 8      
 9      def __init__(self, identifier: str, nom: str):
10          self._id = identifier          [✓ Covered]
11          self._nom = nom                [✓ Covered]
...

Green lines = Covered ✓
Red lines = Not covered ✗
```

---

## 🔄 Workflow Visuel

```
┌─────────────────────────────────────────────────┐
│          DÉVELOPPEUR                             │
│                                                  │
│  1. Modifier le code                            │
│  2. pytest                                      │
│  3. Tous les tests passent ? ─── Non ──┐       │
│              │                          │       │
│             Oui                         │       │
│              │                          │       │
│  4. pytest --cov=...                    │       │
│  5. 100% couverture ? ─────── Non ──────┤       │
│              │                          │       │
│             Oui                         │       │
│              │                          │       │
│  6. git commit & push                   │       │
│                                         │       │
│              │                          │       │
│              └──────────────────────────┘       │
│                  Corriger                       │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│            CI/CD (GitHub Actions)               │
│                                                  │
│  1. Pull Request créée                          │
│  2. make ci                                     │
│  3. Tests passent ? ──── Non ──┐               │
│              │                  │               │
│             Oui                 │               │
│              │                  │               │
│  4. Coverage 100% ? ─── Non ────┤               │
│              │                  │               │
│             Oui                 │               │
│              │                  │               │
│  5. Lint OK ? ────────── Non ───┤               │
│              │                  │               │
│             Oui                 │               │
│              │                  │               │
│  6. ✅ MERGE APPROUVÉ            │               │
│                                 │               │
│              │                  │               │
│              └──────────────────┘               │
│              ❌ PR REJETÉE                       │
└─────────────────────────────────────────────────┘
```

---

## 💡 Astuces Visuelles

### Symboles de Statut

```
✅  Test passé
❌  Test échoué
⏩  Test ignoré (skip)
⚠️   Warning
🔄  En cours
```

### Codes de Couleur (Terminal)

```
PASSED  = Vert   ✅
FAILED  = Rouge  ❌
SKIPPED = Jaune  ⏩
ERROR   = Rouge  🔴
```

### Progression

```
[==================>           ] 65% (148/229)
```

---

## 📈 Métriques de Qualité

```
┌──────────────────────────────────────┐
│     Tableau de Bord Qualité          │
├──────────────────────────────────────┤
│                                       │
│  Tests Totaux      │  229   │ 100%  │
│  Tests Réussis     │  229   │ 100%  │
│  Tests Échoués     │    0   │   0%  │
│                    │        │        │
│  Couverture Code   │  554   │ 100%  │
│  Lignes Testées    │  554   │ 100%  │
│  Lignes Manquantes │    0   │   0%  │
│                    │        │        │
│  Temps Exécution   │ 3.42s  │  ✅   │
│  Tests Lents (>0.1s)│   10   │  ✅   │
│                    │        │        │
└──────────────────────────────────────┘
```

---

## 🎓 Légende

| Symbole | Signification |
|---------|---------------|
| `.` | Test passé |
| `F` | Test échoué |
| `E` | Erreur dans le test |
| `s` | Test ignoré (skipped) |
| `x` | Échec attendu (xfail) |
| `X` | Réussite inattendue (xpass) |

---

**Ce guide visuel complète la documentation technique avec des exemples concrets d'utilisation.**

Pour plus de détails techniques, consultez :
- [README_TESTS.md](README_TESTS.md) - Documentation complète
- [QUICKSTART.md](QUICKSTART.md) - Démarrage rapide
- [TESTS_SUMMARY.md](TESTS_SUMMARY.md) - Récapitulatif