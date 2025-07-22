# ========== pages/1_Upload_Risalah.py ================
import streamlit as st
from utils.transkrip import transkrip_audio, simpan_ke_db
from utils.auth import require_login
import datetime

require_login()
if st.session_state.role not in ["notulis", "admin"]:
    st.error("Anda tidak memiliki akses ke halaman ini.")
    st.stop()

st.title("🔊 Upload Audio Rapat")

with st.form("upload_form"):
    tanggal = st.date_input("📅 Tanggal Rapat", value=datetime.date.today())
    agenda = st.text_input("📝 Agenda Rapat")
    pimpinan = st.text_input("👤 Pimpinan Rapat")
    uploaded_file = st.file_uploader("🎧 File Audio (.mp3/.wav)", type=["mp3", "wav"])
    submitted = st.form_submit_button("🚀 Proses & Simpan")

    if submitted and uploaded_file:
        with st.spinner("Sedang mentranskripsi audio..."):
            hasil = transkrip_audio(uploaded_file)
        simpan_ke_db(str(tanggal), agenda, pimpinan, uploaded_file.name, hasil, st.session_state.username)
        st.success("✅ Transkrip berhasil disimpan!")
        st.subheader("📝 Hasil Transkripsi:")
        st.write(hasil)