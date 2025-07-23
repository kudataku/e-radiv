import streamlit as st
from datetime import date
from utils.transkrip import transkrip_audio
from utils.database import simpan_ke_db
from dotenv import load_dotenv
import os

# Load API key dari .env
load_dotenv()

st.set_page_config(page_title="Upload Risalah", page_icon="📄")
st.title("📄 Upload Risalah Rapat")

# Form input
with st.form("upload_form"):
    tanggal = st.date_input("📅 Tanggal Rapat", value=date.today())
    agenda = st.text_input("📝 Agenda Rapat")
    pimpinan = st.text_input("👤 Pimpinan Rapat")
    uploaded_file = st.file_uploader("🎤 Upload file audio risalah (.mp3/.wav)", type=["mp3", "wav", "m4a"])

    submitted = st.form_submit_button("🚀 Proses Transkrip")

    if submitted and uploaded_file:
        with st.spinner("⏳ Sedang mentranskripsi audio..."):
            try:
                hasil = transkrip_audio(uploaded_file)
                simpan_ke_db(str(tanggal), agenda, pimpinan, uploaded_file.name, hasil)
                st.success("✅ Transkrip berhasil disimpan!")
                st.subheader("📝 Hasil Transkripsi:")
                st.write(hasil)
            except Exception as e:
                st.error(f"Terjadi error saat transkripsi: {e}")
    elif submitted and not uploaded_file:
        st.warning("⚠️ Harap upload file audio terlebih dahulu.")
