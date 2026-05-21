import streamlit as st

st.set_page_config(page_title="Data manager")

accueil_page = st.Page("page_accueil.py", title="Accueil")
eval_page = st.Page("page_eval.py", title="Évaluation des documents")

pg = st.navigation([accueil_page, eval_page])
pg.run()