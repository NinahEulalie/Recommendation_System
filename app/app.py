import streamlit as st
import json
from utils import save_job_details, load_json, display_recommendations
from recommender import recommend_cvs

# Chemins des fichiers
CVS_FILE = "./data/cv_francais.json"
OUTPUT_FILE = "./data/output.json"
MODEL_FILE = "./model/Sys_Rec_06_12.keras"

# Chargement du modèle
st.title("Recommandation de CV")

# Formulaire utilisateur
st.header("Publier une offre d'emploi ou de stage")
with st.form("job_form"):
    Titre_emploi = st.text_input("Titre de l'emploi")
    Breve_description = st.text_area("Brève description")
    Exigences = st.text_area("Exigences")
    submitted = st.form_submit_button("Publier")

if submitted:
    job_details = {
        "Titre_emploi": Titre_emploi,
        "Breve_description": Breve_description,
        "Exigences": Exigences,
    }
    save_job_details(job_details, OUTPUT_FILE)

    st.success("Poste enregistré!")
    
    cvs = load_json(CVS_FILE)
    top_cvs = recommend_cvs(job_details, cvs, MODEL_FILE)

    display_recommendations(top_cvs)
