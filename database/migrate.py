import sqlite3

conn = sqlite3.connect("database/risalah.db")
cursor = conn.cursor()

# Tambahkan kolom 'notulis' jika belum ada
try:
    cursor.execute("ALTER TABLE risalah ADD COLUMN notulis TEXT;")
    print("Kolom 'notulis' berhasil ditambahkan.")
except sqlite3.OperationalError as e:
    print("Gagal menambahkan kolom (mungkin sudah ada):", e)

conn.commit()
conn.close()
