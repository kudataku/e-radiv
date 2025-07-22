# ================ database/init_db.py ==================
import sqlite3

conn = sqlite3.connect('database/risalah.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS risalah (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    agenda TEXT,
    pimpinan TEXT,
    filename TEXT,
    transcript TEXT,
    notulis TEXT
)
''')

conn.commit()
conn.close()