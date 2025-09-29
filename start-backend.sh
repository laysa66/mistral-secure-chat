#!/bin/bash

echo "Lancement du chat avec IA Mistral..."
echo ""

# Vérifier si les dépendances sont installées
echo " Vérification des dépendances backend..."
if ! command -v python3 &> /dev/null; then
    echo " Python3 n'est pas installé"
    exit 1
fi

echo "Python3 trouvé"

# Aller dans le répertoire backend
cd backend

# Installer les dépendances si nécessaire
echo " Installation des dépendances Python..."
pip3 install -r requirements.txt

echo ""
echo "Configuration de l'API Mistral..."

# Vérifier si la clé API est configurée
if grep -q "your_mistral_api_key_here" .env 2>/dev/null; then
    echo "  ATTENTION: Clé API Mistral non configurée!"
    echo ""
    echo " Pour avoir de vraies réponses IA:"
    echo "   1. Allez sur https://console.mistral.ai/"
    echo "   2. Créez un compte et obtenez votre clé API"
    echo "   3. Modifiez backend/.env et remplacez 'your_mistral_api_key_here' par votre clé"
    echo ""
    echo " L'application fonctionnera quand même, mais sans IA réelle"
    echo ""
else
    echo " Clé API Mistral configurée"
fi

echo " Lancement du serveur backend..."
echo "Backend sera disponible sur: http://localhost:8000"
echo ""

# Lancer le serveur - utiliser le chemin Python utilisateur
# Lancer le serveur - utiliser le chemin Python utilisateur
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000