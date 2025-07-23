import json
import os

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

def simpan_ke_db(tanggal, agenda, pimpinan, filename, hasil_transkrip):
    data = {
        "tanggal": tanggal,
        "agenda": agenda,
        "pimpinan": pimpinan,
        "filename": filename,
        "hasil_transkrip": hasil_transkrip
    }

    nama_file = os.path.join(DATA_PATH, f"{tanggal}_{filename}.json")

    with open(nama_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
