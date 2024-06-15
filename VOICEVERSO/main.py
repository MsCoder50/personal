# Install the necessary libraries first
# !pip install SpeechRecognition pydub

import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribe_audio(audio_path, language="en-US"):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Convert audio to a compatible format if necessary
    if audio_path.split('.')[-1] not in ['wav', 'aiff', 'aif']:
        sound = AudioSegment.from_file(audio_path)
        audio_path = "converted_audio.wav"
        sound.export(audio_path, format="wav")
    
    # Load the audio file
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    
    # Try to recognize the speech in the audio file
    try:
        transcription = recognizer.recognize_google(audio, language=language)
        print(f"Transcription: {transcription}")
        return transcription
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Path to the audio file
    audio_path = "/home/mscoder/Music/Faded Memories.mp3"  # Replace with your audio file path
    language_code = "en-US"  # You can change this to the desired language code, e.g., 'fr-FR' for French

    # Transcribe the audio
    transcribe_audio(audio_path, language_code)
