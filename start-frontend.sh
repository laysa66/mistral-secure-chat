#!/bin/bash

echo " Lancement du frontend Mistral Chat..."
echo ""

# Vérifier si Node.js est installé
echo " Vérification des dépendances frontend..."
if ! command -v npm &> /dev/null; then
    echo " npm n'est pas installé"
    exit 1
fi

echo " npm trouvé"

# Aller dans le répertoire frontend
cd frontend

# Installer les dépendances si nécessaire
echo " Installation des dépendances Node.js..."
npm install

echo ""
echo " Lancement du serveur frontend..."
echo "Frontend sera disponible sur: http://localhost:3000"
echo ""
echo " Assurez-vous que le backend tourne sur http://localhost:8000"
echo ""

# Lancer le serveur
npm run dev