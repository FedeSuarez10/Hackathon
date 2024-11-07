# Étape 1 : Construction de l'application React
FROM node:alpine as builder

WORKDIR /app

# Copier le code source et les fichiers de configuration
COPY video-uploader/ .
COPY video-uploader/.env .env
# Installer les dépendances
RUN npm install

# Charger les variables d'environnement et exécuter le build
# RUN export $(cat .env | xargs) && npm run build
RUN set -a && . .env && set +a && npm run build

# Étape 2 : Configuration de Nginx pour servir l'application
FROM nginx:alpine

# Copier les fichiers construits vers le dossier Nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Exposer le port 80 pour le service web
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
