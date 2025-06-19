# frontend/app.py
import streamlit as st
import requests
import urllib
import time
import random
import uuid  # For generating dynamic keys

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Magic Notes", layout="centered", page_icon="🪄")
st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            color: #4A4A4A;
            text-align: center;
            margin-bottom: 10px;
        }
        .note-box {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
        }
        .note-content {
            font-size: 1em;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

spells = [
    "✨ Summoning spell...",
    "🔮 Brewing authentication potion...",
    "🧙‍♂️ Whispering magic words...",
    "📜 Writing ancient scrolls...",
    "💫 Casting the secure spell..."
]

spell_placeholder = st.empty()

def show_magic_animation():
    for _ in range(6):
        spell = random.choice(spells)
        spell_placeholder.markdown(f"<h3 style='text-align:center;'>{spell}</h3>", unsafe_allow_html=True)
        time.sleep(0.5)

if "user" not in st.session_state:
    st.markdown("<h1 class='main-title'>🔐 Magic Notes Login</h1>", unsafe_allow_html=True)
    token = st.query_params.get("token")
    if token:
        res = requests.post(f"{API_URL}/auth/verify", json={"token": token})
        if res.status_code == 200:
            st.session_state["user"] = res.json()["email"]
            st.query_params.clear()
            st.rerun()
        else:
            st.error("❌ Invalid or expired login link.")
    else:
        with st.form("login_form"):
            email = st.text_input("📧 Enter your email")
            submitted = st.form_submit_button("🚀 Send Magic Link")
            if submitted and email:
                show_magic_animation()
                res = requests.post(f"{API_URL}/auth/send?email={urllib.parse.quote(email)}")
                spell_placeholder.empty()
                if res.status_code == 200:
                    st.success("✅ Magic link sent! Check your email.")
                else:
                    st.error("❌ Failed to send email.")
else:
    st.markdown(f"<h1 class='main-title'>📝 Welcome, {st.session_state['user']}</h1>", unsafe_allow_html=True)

    if st.button("🔓 Logout"):
        del st.session_state["user"]
        st.rerun()

    st.markdown("## ➕ Add a New Note")

    if "note_input_dynamic_key" not in st.session_state:
        st.session_state.note_input_dynamic_key = str(uuid.uuid4())

    def handle_note_save(note):
        if note.strip():
            res = requests.post(f"{API_URL}/note/add", json={"email": st.session_state['user'], "content": note.strip()})
            if res.status_code == 200:
                st.success("✅ Note saved!")
                st.session_state.note_input_dynamic_key = str(uuid.uuid4())  # regenerate key to reset
                st.rerun()

    with st.form("add_note_form"):
        note = st.text_area("What's on your mind?", height=100, key=st.session_state.note_input_dynamic_key)
        submitted = st.form_submit_button("💾 Save Note")
        if submitted:
            handle_note_save(note)

    st.markdown("---")
    st.markdown("## 🔍 Search Notes")
    search_query = st.text_input("Search notes...").lower()

    st.markdown("## 📚 Your Notes")
    notes = requests.get(f"{API_URL}/note/list", params={"email": st.session_state['user']}).json()
    filtered_notes = [n for n in notes if search_query in n["content"].lower()]

    for n in filtered_notes:
        with st.expander(n["content"][:30] + "..."):
            with st.container():
                st.markdown(f"<div class='note-box'><div class='note-content'>{n['content']}</div></div>", unsafe_allow_html=True)
                edited = st.text_area("✏️ Edit this note", n["content"], key=n["note_id"])
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Update", key=n["note_id"] + "_update"):
                        requests.post(f"{API_URL}/note/update", json={"note_id": n["note_id"], "content": edited})
                        st.rerun()
                with col2:
                    if st.button("🗑️ Delete", key=n["note_id"] + "_delete"):
                        requests.post(f"{API_URL}/note/delete", json={"note_id": n["note_id"]})
                        st.rerun()
