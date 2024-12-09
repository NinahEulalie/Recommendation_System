import json
import streamlit as st

def save_job_details(job_details, output_file):
    """Sauvegarde les détails du poste sous format JSON."""
    with open(output_file, "w") as f:
        json.dump(job_details, f)

def load_json(filepath):
    """Charge un fichier JSON."""
    with open(filepath, "r") as f:
        return json.load(f)

def display_recommendations(recommendations):
    """Affiche les recommandations dans Streamlit."""
    st.header("Top 5 CV recommandés")
    for i, rec in enumerate(recommendations, start=1):
        st.subheader(f"#{i}: {rec['nom']} {rec['prenom']}")
        st.write(f"Score de pertinence: {rec['score']:.2f}")
        st.write(f"Domaine: {rec['domaine']}")
        st.write(f"Expériences: {rec['experiences']}")
        st.write(f"Compétences: {', '.join(rec['competences'])}")
        st.write("---")
