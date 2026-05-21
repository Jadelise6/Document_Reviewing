import json
from pathlib import Path
import streamlit as st
from st_supabase_connection import SupabaseConnection

TASKS_FILE = Path("./45_Q&A.json")

if "pseudo" not in st.session_state:
    st.stop()

conn = st.connection("supabase", type=SupabaseConnection)

def save_evaluation(pseudo, task):
    conn.client.table("evaluations").upsert({
        "pseudo": pseudo,
        "task_id": int(task["id"]),
        "doc1_score": int(st.session_state[f"doc1_{task['id']}"]),
        "doc2_score": int(st.session_state[f"doc2_{task['id']}"]),
    }, on_conflict="pseudo,task_id").execute()

with open(TASKS_FILE, "r", encoding="utf-8") as f:
    tasks = json.load(f)

task_id = st.session_state.get("task_id", 0)

if task_id >= len(tasks):
    st.success("Fin de l'évaluation.")
    st.stop()

task = tasks[task_id]
pseudo = st.session_state["pseudo"]

st.header(f"Requête {task['id']}")
st.subheader(f"Connecté en tant que: {pseudo}")
st.divider()
st.write(task["Q"])
st.divider()
st.write("Doc1")
st.write(task["Model1_A"])
st.slider("Note Doc1", 1, 5, key=f"doc1_{task['id']}")
st.divider()
st.write("Doc2")
st.write(task["Model2_1"])
st.slider("Note Doc2", 1, 5, key=f"doc2_{task['id']}")

if st.button("Passer à la question suivante"):
    save_evaluation(pseudo, task)
    st.session_state["task_id"] = task_id + 1
    st.rerun()

