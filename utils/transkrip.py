import openai
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()  # Load API Key dari .env

def transkrip_audio(uploaded_file):
    # Simpan audio ke file sementara
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Transkrip audio dengan OpenAI API
    with open(tmp_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)

    os.remove(tmp_path)  # Hapus file sementara

    return response["text"]
