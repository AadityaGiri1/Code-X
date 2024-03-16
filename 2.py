import librosa
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

def align_audio(audio_file1, audio_file2):
    # Load the first speech audio file
    y1, sr1 = librosa.load(audio_file1)

    # Load the second speech audio file
    y2, sr2 = librosa.load(audio_file2)

    # Compute feature vectors for both audio files
    mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
    mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)

    # Transpose the feature matrices to have frames as rows and features as columns
    mfcc1 = mfcc1.T
    mfcc2 = mfcc2.T

    # Fit KNN model
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(mfcc2)

    # Find nearest neighbors in the second audio for each frame in the first audio
    distances, indices = knn.kneighbors(mfcc1)

    # Compute the time stretch factor
    time_stretch_factor = len(y2) / len(y1)

    # Adjust the time range of the first audio file to match the second audio file
    new_y1 = librosa.effects.time_stretch(y1, time_stretch_factor)

    return new_y1, sr1, y2, sr2

# Example usage
audio_file1 = "C:\\Users\Abhishek Mishra\Desktop\sentence dataset\\3.wav"  # Replace with the path to your first audio file
audio_file2 = "C:\\Users\Abhishek Mishra\Desktop\hindi\\3.wav"  # Replace with the path to your second audio file

# Align the audio files
aligned_y1, sr1, y2, sr2 = align_audio(audio_file1, audio_file2)

# Plot the waveforms
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
librosa.display.waveshow(aligned_y1, sr=sr1)
plt.title('Waveform of Aligned Audio File 1')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
librosa.display.waveshow(y2, sr=sr2)
plt.title('Waveform of Audio File 2')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
