# Image de base Python 3.11
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . .

# Définir la variable d'environnement pour Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

# Exposer le port si nécessaire (optionnel pour une app CLI)
# EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "-m", "weather_app"]