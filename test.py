from dotenv import load_dotenv
load_dotenv()
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
import os

# https://www.youtube.com/watch?v=09JYAZEoOOk

print("KEY LOADED: ", os.getenv("SARVAM_API_KEY"))
print("CWD: ", os.getcwd())


source = "https://www.youtube.com/watch?v=XBzTiBefPWY"
language = "hinglish"


chunks = process_input(source)
data = transcribe_all(chunks, language=language)

print(data)