import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def translate_text(text, source_lang='en', dest_lang='hi'):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=dest_lang)
    return translation.text

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    return tts

def save_audio_to_file(audio, filename):
    audio.save(filename)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    # Specify the path to the input MP3 file
    mp3_file_path = input("Enter the file path of the MP3 file: ")


    # Initialize recognizer
    recognizer = sr.Recognizer()

    try:
        # Load the MP3 file
        with sr.AudioFile(mp3_file_path) as source:
            print("Transcribing audio...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            # Capture audio input
            audio_input = recognizer.record(source)
            print("Audio input received, transcribing...")

        # Convert audio to text
        input_text = recognizer.recognize_google(audio_input)
        print("Input text:", input_text)

        # Translate text
        translated_text = translate_text(input_text)
        print("Translated text:", translated_text)

        # Generate speech
        audio = text_to_speech(translated_text, lang='hi')

        # Save speech to file
        output_file = "translated_audio.mp3"
        save_audio_to_file(audio, output_file)

    except sr.UnknownValueError:
        print("Sorry, could not transcribe audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))