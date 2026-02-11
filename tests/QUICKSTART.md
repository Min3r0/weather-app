# 🚀 Guide de Démarrage Rapide - Tests

Guide rapide pour commencer à utiliser la suite de tests.

## ⚡ Installation Express

```bash
# 1. Installer les dépendances
pip install -r requirements-test.txt

# 2. Lancer les tests
pytest
```

C'est tout ! 🎉

## 📝 Commandes Essentielles

### Tests de base

```bash
# Tous les tests
pytest

# Mode verbose
pytest -v

# Avec couverture
pytest --cov=weather_app

# Rapport HTML
pytest --cov=weather_app --cov-report=html
```

### Tests spécifiques

```bash
# Un fichier
pytest tests/test_location.py

# Une classe
pytest tests/test_location.py::TestStation

# Une méthode
pytest tests/test_location.py::TestStation::test_station_creation
```

### Utilisation du Makefile (Linux/Mac)

```bash
# Voir toutes les commandes
make help

# Tests avec couverture
make test-coverage

# Rapport HTML
make test-cov-html

# Pipeline complète
make ci
```

### Scripts (Multi-plateforme)

```bash
# Linux/Mac
chmod +x run_tests.sh
./run_tests.sh -c

# Windows
run_tests.bat -c
```

## 📊 Vérifier la Couverture

```bash
# Terminal
pytest --cov=weather_app --cov-report=term-missing

# HTML (puis ouvrir htmlcov/index.html)
pytest --cov=weather_app --cov-report=html
```

## 🎯 Objectifs de Qualité

- ✅ Tous les tests doivent passer
- ✅ Couverture de code : 100%
- ✅ Temps d'exécution : < 5 secondes
- ✅ Aucun test flakey (instable)

## 🆘 Dépannage

### Les tests ne se lancent pas

```bash
# Vérifier l'installation de pytest
pytest --version

# Réinstaller les dépendances
pip install --force-reinstall -r requirements-test.txt
```

### Import errors

```bash
# S'assurer que le PYTHONPATH est correct
export PYTHONPATH="${PYTHONPATH}:${PWD}"

# Ou installer le package en mode développement
pip install -e .
```

### Tests lents

```bash
# Identifier les tests lents
pytest --durations=10

# Exclure les tests lents
pytest -m "not slow"
```

## 📚 Ressources

- [README complet](README_TESTS.md)
- [Documentation pytest](https://docs.pytest.org/)
- [Guide du Makefile](Makefile)

## 💡 Tips

1. **Lancer les tests fréquemment** - après chaque modification
2. **Utiliser le mode watch** - `ptw` ou `pytest-watch`
3. **Vérifier la couverture** - viser 100%
4. **Lire les erreurs** - pytest donne des messages clairs

---

Pour plus de détails, consultez le [README_TESTS.md](README_TESTS.md) complet.