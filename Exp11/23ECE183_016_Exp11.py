import numpy as np
import wave
import matplotlib.pyplot as plt


def load_audio(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        samplerate = wav_file.getframerate()
        frames = wav_file.readframes(wav_file.getnframes())
        data = np.frombuffer(frames, dtype=np.int16)
    return data, samplerate


def write_audio(file_path, data, samplerate):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(samplerate)
        wav_file.writeframes(data.astype(np.int16).tobytes())


def change_speed(y, speed_factor):
    new_length = int(len(y) * speed_factor)
    new_audio = np.interp(np.linspace(0, len(y), new_length), np.arange(len(y)), y)
    return new_audio


def check_linearity(y1, y2, alpha=0.5, beta=0.5, speed_factor=1):
    max_length = max(len(y1), len(y2))
    y1 = np.pad(y1, (0, max_length - len(y1)), mode='constant')
    y2 = np.pad(y2, (0, max_length - len(y2)), mode='constant')
    
    output1 = change_speed(y1, speed_factor)
    output2 = change_speed(y2, speed_factor)
    
    combined_input = alpha * y1 + beta * y2
    output_combined = change_speed(combined_input, speed_factor)
    
    return np.allclose(alpha * output1 + beta * output2, output_combined)

def check_time_invariance(y, shift=100, speed_factor=1):
    y_padded = np.pad(y, (shift, 0), mode='constant')
    y_shifted = np.roll(y_padded, shift)
    
    output_original = change_speed(y_padded, speed_factor)
    output_shifted = change_speed(y_shifted, speed_factor)
    
    return np.allclose(np.roll(output_original, shift), output_shifted)


def plot_frequency_spectrum(signal, sr, title):
    N = len(signal)
    freqs = np.fft.fftfreq(N, 1 / sr)
    fft_values = np.fft.fft(signal)
    plt.plot(freqs[:N // 2], np.abs(fft_values[:N // 2]))  
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()


y_orig, sr_orig = load_audio("voc.wav")
y_bg, sr_bg = load_audio("bgm.wav")


y_orig = change_speed(y_orig, 1)
y_bg = change_speed(y_bg, 1)


max_len = max(len(y_orig), len(y_bg))
y_orig = np.pad(y_orig, (0, max_len - len(y_orig)), mode='constant')
y_bg = np.pad(y_bg, (0, max_len - len(y_bg)), mode='constant')


mix_ratio = 0.7
y_mixed = y_orig + mix_ratio * y_bg
y_mixed = y_mixed / np.max(np.abs(y_mixed)) * 32767  


write_audio("OUTPUT.wav", y_mixed, sr_orig)


linear = check_linearity(y_orig, y_bg, speed_factor=1)
time_invariant = check_time_invariance(y_orig, speed_factor=1)
print(f"System Linearity: {'Linear' if linear else 'Non-Linear'}")
print(f"System Time-Invariance: {'Time-Invariant' if time_invariant else 'Time-Variant'}")


plt.figure(figsize=(14, 8))
plt.subplot(3, 1, 1)
plt.plot(y_orig, alpha=0.6)
plt.title("Vocal (Time-Scaled)")

plt.subplot(3, 1, 2)
plt.plot(y_bg, alpha=0.6, color='orange')
plt.title("Background Music")

plt.subplot(3, 1, 3)
plt.plot(y_mixed, alpha=0.6, color='purple')
plt.ylim(-32767, 32767)
plt.title("Mixed Audio (Final Output)")

plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 6))
plt.subplot(3, 1, 1)
plot_frequency_spectrum(y_orig, sr_orig, "Vocal Frequency Spectrum")

plt.subplot(3, 1, 2)
plot_frequency_spectrum(y_bg, sr_orig, "Background Music Spectrum")

plt.subplot(3, 1, 3)
plot_frequency_spectrum(y_mixed, sr_orig, "Mixed Audio Spectrum")

plt.tight_layout()
plt.show()
