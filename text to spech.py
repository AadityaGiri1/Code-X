import librosa
import numpy as np

def load_audio(filepath):
    audio, sr = librosa.load(filepath, sr=None)
    return audio, sr

def compare_audio_eng_hin(eng_filepath, hin_filepath, eng_audio, hin_audio):
    eng_duration = librosa.get_duration(y=eng_audio)
    hin_duration = librosa.get_duration(y=hin_audio)
    
    print("English Audio Duration:", eng_duration, "seconds")
    print("Hindi Audio Duration:", hin_duration, "seconds")
    
    if eng_duration == hin_duration:
        print("Both audios have the same duration.")
    else:
        print("Audios have different durations.")
    
    eng_energy = np.sum(np.abs(eng_audio)**2)
    hin_energy = np.sum(np.abs(hin_audio)**2)
    
    print("English Audio Energy:", eng_energy)
    print("Hindi Audio Energy:", hin_energy)
    
    energy_ratio = eng_energy / hin_energy
    
    print("Energy Ratio (English/Hindi):", energy_ratio)

# Load English audio
eng_audio, eng_sr = load_audio("F:/eng/clip_01.wav")

# Load Hindi audio
hin_audio, hin_sr = load_audio("F:/hin/clip_01.wav")

# Compare audio samples
compare_audio_eng_hin("F:/eng/clip_01.wav", "F:/hin/clip_01.wav", eng_audio, hin_audio)

# Allow user to input sample path
sample_path = input("Enter the path of the sample audio file: ")

# Load user sample audio
sample_audio, sample_sr = load_audio(sample_path)

# Compare user sample with English and Hindi audios
compare_audio_eng_hin("F:/eng/clip_01.wav", "F:/hin/clip_01.wav", eng_audio, hin_audio)
compare_audio_eng_hin("F:/eng/clip_01.wav", "F:/hin/clip_01.wav", sample_audio, hin_audio)
