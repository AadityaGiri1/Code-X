import os
from gtts import gTTS

def text_to_audio(text, output_folder):
    # Ensure the output folder exists, create it if not
    os.makedirs(output_folder, exist_ok=True)

    # Iterate 20 times to create 20 audio clips
    for i in range(1, 21):
        # Generate speech from text
        tts = gTTS(text=f"सीरियल नंबर {i}. {text}", lang='hi')
        
        # Save the audio to a file
        output_file = os.path.join(output_folder, f"clip_{i:02d}.wav")
        tts.save(output_file)

if __name__ == "__main__":
    # Get user input text
    user_text = input("Enter the Hindi text to convert to audio clips: ")

    # Set output folder
    output_folder = "audio_clips"

    # Convert text to audio clips
    text_to_audio(user_text, output_folder)

    print("Audio clips generated successfully!")
