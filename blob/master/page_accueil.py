import json
from pathlib import Path
import streamlit as st
from st_supabase_connection import SupabaseConnection

conn = st.connection("supabase", type=SupabaseConnection)

def get_last_state(pseudo):
    result = conn.client.table("evaluations") \
        .select("task_id") \
        .eq("pseudo", pseudo) \
        .execute()
    if not result.data:
        return 0
    return max(r["task_id"] for r in result.data) + 1

st.header("Plateforme d'Évaluation de Documents")

def load_json(path, default):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


with st.container():
    st.subheader("Consignes")
    st.markdown("""
    - Évaluez les deux documents pour chaque requête.
    - Donnez une note de 1 à 5 à chaque document.
    - Si vous vous reconnectez avec le même pseudo, vous reprenez là où vous vous étiez arrêté.
    """)
    st.divider()
    st.write("Veuillez entrer un pseudo que vous garderez tout au long de cette évaluation.")
    pseudo = st.text_input("Pseudo")

    if st.button("Se connecter / Créer un compte"):
        if not pseudo.strip():
            st.error("Veuillez entrer un pseudo")
        else:
            st.session_state["pseudo"] = pseudo.strip()
            st.session_state["task_id"] = get_last_state(pseudo.strip())
            st.switch_page("page_eval.py")