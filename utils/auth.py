# =================== utils/auth.py =====================
import streamlit as st

USERS = {
    "notulis": {"password": "1234", "role": "notulis"},
    "admin": {"password": "admin", "role": "admin"},
}

def login():
    st.sidebar.title("🔐 Login Pengguna")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""

    if not st.session_state.logged_in:
        username = st.sidebar.text_input("👤 Username")
        password = st.sidebar.text_input("🔑 Password", type="password")
        if st.sidebar.button("Login"):
            user = USERS.get(username)
            if user and user["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = user["role"]
                st.success(f"Selamat datang, {username}!")
                st.rerun()
            else:
                st.error("Login gagal. Coba lagi.")
    else:
        st.sidebar.success(f"👋{st.session_state.username} ({st.session_state.role})")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

def require_login():
    if not st.session_state.get("logged_in", False):
        st.warning("Silakan login untuk mengakses fitur ini.")
        st.stop()
