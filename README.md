# 📸 InstBot - Générateur de légendes Instagram

Application Streamlit multi-page pour générer des légendes Instagram personnalisées à partir de photos ou d'actualités.

## 🚀 Fonctionnalités

### 📝 Page Legend
- **Upload d'images** : Supporté PNG, JPG, JPEG
- **Génération intelligente** : Création de légendes basées sur l'analyse d'image
- **Personnalisation** : Choix du ton (professionnel, décontracté, inspirant, etc.)
- **Intégration N8N** : Envoi automatique vers webhook pour traitement IA
- **Hashtags automatiques** : Génération de hashtags pertinents

### 💡 Page Ideas  
- **Actualités trending** : Légendes basées sur les tendances du moment
- **Catégories variées** : Tech, Business, Sport, Lifestyle, etc.
- **Ciblage audience** : Adaptation selon l'âge et le type d'audience
- **Options avancées** : Call-to-action, mots-clés personnalisés
- **Templates prêts** : Idées de légendes immédiatement utilisables

## 🛠️ Installation

### Prérequis
- Python 3.7+
- pip

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Lancement de l'application
```bash
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

## ⚙️ Configuration

### Webhook N8N (Page Legend)
1. Configurez votre workflow N8N pour recevoir les données d'image
2. Copiez l'URL du webhook dans la barre latérale de la page Legend
3. Format des données envoyées :
```json
{
  "image": "base64_encoded_image",
  "tone": "selected_tone",
  "length": "selected_length", 
  "include_hashtags": true/false,
  "context": "user_context",
  "filename": "image_name.jpg"
}
```

## 📁 Structure du projet

```
instabot_streamlit/
├── app.py                 # Page d'accueil principale
├── pages/
│   ├── 1_Legend.py       # Page génération à partir d'image
│   └── 2_Ideas.py        # Page idées basées sur l'actualité
├── requirements.txt       # Dépendances Python
└── README.md             # Documentation
```

## 🎯 Utilisation

### Page Legend
1. Accédez à la page "Legend" via la barre latérale
2. Configurez l'URL de votre webhook N8N
3. Uploadez votre image
4. Sélectionnez le ton et la longueur souhaités
5. Ajoutez du contexte si nécessaire
6. Cliquez sur "Générer la légende"

### Page Ideas
1. Accédez à la page "Ideas" via la barre latérale  
2. Sélectionnez la catégorie d'actualité
3. Choisissez le type de contenu et l'audience cible
4. Configurez les options avancées si besoin
5. Cliquez sur "Générer des idées de légendes"

## 🔧 Dépendances

- **streamlit** : Framework web pour l'interface utilisateur
- **requests** : Gestion des appels HTTP vers le webhook
- **Pillow** : Traitement des images uploadées

## 💡 Conseils d'utilisation

### Pour de meilleures légendes :
- Utilisez des images de haute qualité
- Ajoutez du contexte détaillé pour les images complexes
- Expérimentez avec différents tons selon votre audience
- Les hashtags augmentent significativement la visibilité

### Optimisation de l'engagement :
- Publiez aux heures de pointe (18h-21h)
- Utilisez 5-10 hashtags pertinents maximum
- Posez des questions pour encourager l'interaction
- Mentionnez l'actualité avec subtilité

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Reporter des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation
- Optimiser le code existant

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🆘 Support

Pour toute question ou problème :
1. Vérifiez que toutes les dépendances sont installées
2. Assurez-vous que l'URL du webhook N8N est correcte
3. Consultez les logs Streamlit pour les erreurs détaillées

---

Développé avec ❤️ pour optimiser votre présence Instagram