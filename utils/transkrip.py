# ================ utils/transkrip.py ===================
import whisper
import sqlite3
import tempfile
import os

def transkrip_audio(uploaded_file):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path, language="indonesian")
    os.remove(tmp_path)
    return result["text"]

def simpan_ke_db(tanggal, agenda, pimpinan, filename, transcript, notulis):
    conn = sqlite3.connect('database/risalah.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO risalah (tanggal, agenda, pimpinan, filename, transcript, notulis)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (tanggal, agenda, pimpinan, filename, transcript, notulis))
    conn.commit()
    conn.close()