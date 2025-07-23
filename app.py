# ======================== app.py ========================
import streamlit as st
from utils.auth import login

st.set_page_config(page_title="RADIV - DPRD Kab. Lebak", layout="wide")
login()

st.title("📄 RADIV - DPRD Kabupaten Lebak")
st.info("(Risalah Autentik Digital Verifikasi) Mengabadikan Setiap Diskusi, Memajukan Tata Kelola Publik")
