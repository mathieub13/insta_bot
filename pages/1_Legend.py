import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Legend", page_icon="📝")

st.title("📝 Legend - Génération de légende à partir d'un texte")

st.markdown("""
A quel poste penses-tu ? """)

input = st.text_input("A quoi penses-tu ?")

# Configuration du webhook N8N
webhook_url = st.secrets["N8N_WEBHOOK_URL"]


if st.button("🚀 Générer la légende", type="primary"):
        if not webhook_url:
            st.error("⚠️ Veuillez entrer l'URL du webhook N8N dans la barre latérale")
        else:
            with st.spinner("Génération de la légende en cours..."):
                try:
                    # Convertir l'image en base64
                    # Préparer les données pour le webhook
                    payload = {
                        "input": "legend",
                        "type": type
                    }

                    # Envoyer au webhook N8N
                    response = requests.post(webhook_url, json=payload, timeout=30)

                    if response.status_code == 200:
                        result = response.json()

                        st.success("✅ Légende générée avec succès !")

                        # Afficher la légende générée
                        if "caption" in result:
                            st.subheader("📝 Légende proposée:")
                            st.markdown(f"```\n{result['caption']}\n```")

                            # Bouton pour copier la légende
                            if st.button("📋 Copier la légende"):
                                st.write("Légende copiée dans le presse-papier !")

                        # Afficher d'autres informations si disponibles
                        if "hashtags" in result and result["hashtags"]:
                            st.subheader("🏷️ Hashtags suggérés:")
                            st.write(" ".join(result["hashtags"]))

                    else:
                        st.error(f"❌ Erreur lors de la génération: {response.status_code}")
                        st.error(f"Détails: {response.text}")

                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Erreur de connexion: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Erreur inattendue: {str(e)}")
