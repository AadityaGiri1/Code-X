import os
import librosa
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram(filename, title):
    # Load the audio file
    y, sr = librosa.load(filename)

    # Compute the Short-Time Fourier Transform (STFT)
    D = librosa.stft(y)

    # Convert the STFT into magnitude and phase
    magnitude, phase = librosa.magphase(D)

    # Calculate the power of the magnitude
    power = magnitude**2

    # Take the square root to get the amplitude
    amplitude = np.sqrt(power)

    # Convert the amplitude to decibels
    db = librosa.amplitude_to_db(amplitude, ref=np.max)

    # Plot the spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(db, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title(title)
    plt.tight_layout()
    plt.show()

# Define the dataset directory
dataset_dir = ""

# Iterate through the audio files in the dataset directory
for filename in os.listdir(dataset_dir):
    if filename.endswith(".mp3"):
        file_path = os.path.join(dataset_dir, filename)
        plot_spectrogram(file_path, filename)