FROM node:18-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier package.json et package-lock.json
COPY package.json package-lock.json* ./

# Installer les dépendances
RUN npm ci

# Copier tout le code source
COPY . .

# Supprimer le dossier .next s'il existe (pour éviter les conflits)
RUN rm -rf .next

# Builder l'application Next.js
RUN npm run build

# Vérifier que le build s'est bien passé
RUN ls -la .next && echo "Build Next.js"

# Créer un utilisateur non-root
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Changer les permissions
RUN chown -R nextjs:nodejs /app
USER nextjs

# Exposer le port
EXPOSE 3000

# Variables d'environnement
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# Lancer l'application
CMD ["npm", "start"]