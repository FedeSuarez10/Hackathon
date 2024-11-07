# Utilisez une image Python légère
FROM python:3.10-slim

# Désactive l'écriture de fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Désactive le buffering de sortie pour une meilleure lisibilité des logs
ENV PYTHONUNBUFFERED=1

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier principal de l'application
COPY app.py /app/app.py
# Copier le dossier de téléchargement
COPY uploads /app/uploads

# Installer Flask et Flask-CORS
RUN pip install Flask Flask-CORS

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]
