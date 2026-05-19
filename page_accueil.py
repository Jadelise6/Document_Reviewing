import streamlit as st
import json

st.header("Plateforme d'Évaluation de Documents")

# Fichier pour stocker les pseudos
users_file = "./users.json"

# Fonctions pour la connexion / création des utilisateurs
def load_users():
    """ Charger les pseudos existants """
    with open(users_file, "r") as f:
        content = f.read()
        return json.loads(content)


def save_users(users):
    """ Sauvegarder les pseudos """
    with open(users_file, "w") as f:
        json.dump(users, f)

# Afficher le contenu
with st.container():
    # Consignes
    st.subheader("Consignes")
    st.markdown("""
    - **Évaluation :** à chaque étape, vous évaluerez le premier document retourné par deux modèles.
    - **Notes :** pour chaque document, vous attribuerez une note de 1 à 5 en fonction de sa pertinence par rapport à la requête.
    - **Reprise :** pour reprendre votre progression plus tard, entrez exactement le même identifiant en faisant attention aux majuscules et aux espaces.
    """)
    st.divider()

    st.write("Veuillez entrer un pseudo anonyme que vous garderez tout au long de cette évaluation.")
    pseudo = st.text_input("Pseudo")
    
    if st.button("Se connecter / Créer un compte"):
        if not pseudo:
            st.error("Veuillez entrer un pseudo")
        else:
            # Vérifier si l'utilisateur existe
            users = load_users()
            
            if pseudo not in users:
                # Créer un nouveau compte
                users.append(pseudo)
                save_users(users)
                st.success(f"Compte créé pour {pseudo}!")
            else:
                st.success(f"Bienvenue {pseudo}!")
            
            # Stocker le pseudo en session
            st.session_state["pseudo"] = pseudo
            st.session_state["page"] = "eval"
            st.switch_page("page_eval.py")