import streamlit as st

# Vérifier que l'utilisateur est connecté
if "pseudo" not in st.session_state:
    st.stop()

pseudo = st.session_state["pseudo"]

num_page = 1
st.header(f"Requête {num_page}")
st.subheader(f"Connecté en tant que: {pseudo}")
st.divider()

with st.container():
    # Requête
    st.write("Query")
    st.divider()

    # Document 1
    st.write("Doc1")
    st.slider("Sélectionnez une note de 1 à 5 pour la pertinence de ce document", 0, 5, key="doc1")
    st.divider()

    # Document 2
    st.write("Doc2")
    st.slider("Sélectionnez une note de 1 à 5 pour la pertinence de ce document",0, 5, key="doc2")
    
    # Fin
    st.button("Passer à la question suivante")