import tensorflow as tf
import numpy as np

def preprocess_input(job_details):
    """Prépare les données du poste pour le modèle."""
    return [job_details['Titre_emploi'], job_details['Breve_description'], job_details['Exigences']]

def recommend_cvs(job_details, cvs, model_path):
    """Trouve les 5 CV les plus pertinents pour un poste."""
    model = tf.keras.models.load_model(model_path)
    
    # Préparer les données d'entrée
    job_input = preprocess_input(job_details)
    job_vector = model.predict([job_input])

    # Calculer les scores
    recommendations = []
    for cv in cvs:
        cv_vector = preprocess_input(cv)
        score = np.dot(job_vector, cv_vector)  # Similarité par produit scalaire
        cv['score'] = score
        recommendations.append(cv)

    # Trier par pertinence
    top_cvs = sorted(recommendations, key=lambda x: x['score'], reverse=True)[:5]
    return top_cvs
