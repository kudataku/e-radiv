# ======================== app.py ========================
import streamlit as st
from utils.auth import login

st.set_page_config(page_title="E-Risalah DPRD", layout="wide")
login()

st.title("📄 E-Risalah DPRD Kabupaten Lebak")
st.info("Gunakan sidebar untuk navigasi.")