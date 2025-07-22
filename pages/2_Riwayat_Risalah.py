# ========== pages/2_Riwayat_Risalah.py ================
import streamlit as st
import sqlite3
from utils.auth import require_login

require_login()

st.title("📚 Riwayat Risalah")

conn = sqlite3.connect('database/risalah.db')
cursor = conn.cursor()
cursor.execute("SELECT id, tanggal, agenda, pimpinan FROM risalah ORDER BY id DESC")
rows = cursor.fetchall()

if rows:
    for row in rows:
        with st.expander(f"📅 {row[1]} - {row[2]} (Pimpinan: {row[3]})"):
            cursor.execute("SELECT transcript, notulis FROM risalah WHERE id = ?", (row[0],))
            data = cursor.fetchone()
            st.caption(f"\u270d\ufe0f Notulis: {data[1]}")
            st.write(data[0])
else:
    st.info("Belum ada risalah yang disimpan.")

conn.close()