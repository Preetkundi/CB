import requests
import os
from pytube import YouTube
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Downloads video and extracts audio as MP3
def download_audio_from_youtube(url: str, filename: str = "temp_audio.mp3") -> str:
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(filename=filename)
    return audio_path

# Sends audio to Groq ASR endpoint for transcription
def transcribe_with_groq(audio_path: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }
    files = {
        "file": open(audio_path, "rb")
    }
    data = {
        "model": "whisper-large-v3",
        "response_format": "text"
    }

    response = requests.post("https://api.groq.com/openai/v1/audio/transcriptions", headers=headers, files=files, data=data)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error in transcription: {response.status_code}, {response.text}")
        return ""

# Wrapper function: downloads audio + transcribes
def get_transcript(video_url: str) -> str:
    try:
        audio_path = download_audio_from_youtube(video_url)
        transcript = transcribe_with_groq(audio_path)
        os.remove(audio_path)  # Clean up
        return transcript
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""
