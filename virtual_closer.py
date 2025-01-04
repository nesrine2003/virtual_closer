import os
import streamlit as st
from PIL import Image

# Chemin du dossier principal contenant tous les sous-dossiers
# Chemin relatif vers le dossier "armoire"
dossier_principal = os.path.join(os.path.dirname(__file__), "ARMOIRE")

# Vérification si le dossier principal existe
if not os.path.exists(dossier_principal):
    raise FileNotFoundError(f"Le dossier principal {dossier_principal} n'existe pas.")

# Vérification si le dossier principal existe
if not os.path.exists(dossier_principal):
    st.error(f"Le dossier principal {dossier_principal} n'existe pas.")
else:
    # Récupération des catégories (sous-dossiers)
    categories = [categorie for categorie in os.listdir(dossier_principal) if os.path.isdir(os.path.join(dossier_principal, categorie))]

    # Interface de l'application
    st.title("Virtual Closet")

    # Choisir une catégorie
    categorie = st.selectbox("Choisir une catégorie", categories)

    # Afficher les images de la catégorie
    if categorie:
        chemin_categorie = os.path.join(dossier_principal, categorie)
        fichiers = [f for f in os.listdir(chemin_categorie) if os.path.isfile(os.path.join(chemin_categorie, f))]

        for fichier in fichiers:
            chemin_fichier = os.path.join(chemin_categorie, fichier)
            try:
                # Charger l'image
                img = Image.open(chemin_fichier)
                img = img.resize((150, 150))  # Redimensionner l'image
                st.image(img, caption=f"{categorie} - {fichier}")
            except Exception as e:
                st.error(f"Erreur lors du chargement de l'image {chemin_fichier}: {e}")

