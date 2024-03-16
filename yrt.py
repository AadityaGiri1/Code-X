import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def speech_to_speech(source_language, target_language):
    # Initialize Speech Recognition
    r = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Please speak in", source_language)
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language=source_language)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

    # Translate the recognized text to the target language
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language).text

    # Convert translated text to speech in the target language
    tts = gTTS(text=translated_text, lang=target_language, slow=False)

    # Save the speech to a file
    tts.save("output.mp3")

    # Play the translated speech
    os.system("start output.mp3")

if __name__ == "__main__":
    source_language = "en"  # Change as needed
    target_language = "hi"  # Change as needed
    speech_to_speech(source_language, target_language)
