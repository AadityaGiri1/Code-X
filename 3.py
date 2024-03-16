import librosa
import librosa.display
import matplotlib.pyplot as plt

def plot_audio_comparison(audio_file1, audio_file2):
    # Load the first speech audio file
    y1, sr1 = librosa.load(audio_file1)

    # Load the second speech audio file
    y2, sr2 = librosa.load(audio_file2)

    # Create a time array for the first audio file
    time1 = librosa.times_like(y1, sr1)

    # Create a time array for the second audio file
    time2 = librosa.times_like(y2, sr2)

    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # Plot waveform of first audio file
    axes[0, 0].plot(time1, y1)
    axes[0, 0].set_title('Waveform of Audio File 1')
    axes[0, 0].set_xlabel('Time (s)')
    axes[0, 0].set_ylabel('Amplitude')

    # Plot waveform of second audio file
    axes[0, 1].plot(time2, y2)
    axes[0, 1].set_title('Waveform of Audio File 2')
    axes[0, 1].set_xlabel('Time (s)')
    axes[0, 1].set_ylabel('Amplitude')

    # Compute the Short-Time Fourier Transform (STFT) for both signals
    D1 = librosa.stft(y1)
    D2 = librosa.stft(y2)

    # Convert amplitude to decibels (log-magnitude) for both signals
    DB1 = librosa.amplitude_to_db(abs(D1))
    DB2 = librosa.amplitude_to_db(abs(D2))

    # Plot the spectrograms of both audio files
    librosa.display.specshow(DB1, sr=sr1, x_axis='time', y_axis='log', ax=axes[1, 0])
    axes[1, 0].set_title('Spectrogram of Audio File 1')
    axes[1, 0].set_xlabel('Time (s)')
    axes[1, 0].set_ylabel('Frequency (Hz)')

    librosa.display.specshow(DB2, sr=sr2, x_axis='time', y_axis='log', ax=axes[1, 1])
    axes[1, 1].set_title('Spectrogram of Audio File 2')
    axes[1, 1].set_xlabel('Time (s)')
    axes[1, 1].set_ylabel('Frequency (Hz)')

    plt.tight_layout()
    plt.show()

# Example usage
audio_file1 = "C:\\Users\Abhishek Mishra\Desktop\sentence dataset\\3.wav"  # Replace with the path to your first audio file
audio_file2 = "C:\\Users\Abhishek Mishra\Desktop\hindi\\3.wav"  # Replace with the path to your second audio file
plot_audio_comparison(audio_file1, audio_file2)
