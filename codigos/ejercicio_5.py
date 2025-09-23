import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Parámetros
fs = 800  # Frecuencia de muestreo (Hz)
T = 0.5    # Duración (segundos)
t = np.linspace(0, T, int(fs * T), endpoint=False)

# Frecuencias, amplitudes y fases
f1, A1, phi1 = 50, 1.0, np.pi/2
f2, A2, phi2 = 120, 0.5, np.pi/2
f3, A3, phi3 = 200, 0.3, np.pi/2

# Señal compuesta
signal = (A1 * np.sin(2 * np.pi * f1 * t + phi1) +
          A2 * np.sin(2 * np.pi * f2 * t + phi2) +
          A3 * np.sin(2 * np.pi * f3 * t + phi3))

# Calcular FFT
N = len(signal)
fft_values = fft(signal)
freq = fftfreq(N, 1/fs)
magnitude = 2 * np.abs(fft_values) / N  # Magnitud normalizada

# Frecuencias positivas y magnitudes
positive_freq = freq[:N//2]
positive_mag = magnitude[:N//2]

# Graficar señal compuesta y espectros
fig, axs = plt.subplots(2, 1, figsize=(12, 7))

# Señal compuesta en el tiempo
axs[0].plot(t, signal, color='b')
axs[0].set_title('Señal Compuesta', fontsize=12, pad=12)
axs[0].set_xlabel('Tiempo (s)', fontsize=11, labelpad=8)
axs[0].set_ylabel('Amplitud', fontsize=11)
axs[0].grid(True)

# Espectro FFT
axs[1].stem(positive_freq, positive_mag, linefmt='b-', markerfmt='bo', basefmt='r-')
axs[1].set_title('Espectro de Magnitud (FFT)', fontsize=12, pad=12)
axs[1].set_xlabel('Frecuencia (Hz)', fontsize=11, labelpad=8)
axs[1].set_ylabel('Magnitud', fontsize=11)
axs[1].set_xlim(0, 250)
axs[1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Más espacio arriba para el título general
plt.subplots_adjust(hspace=1)         # Más espacio entre subplots

############################ --- Añadir ruido ---#################################
np.random.seed(0)  # para reproducibilidad
ruido_bajo = np.random.normal(0, 0.1, size=signal.shape)
ruido_alto = np.random.normal(0, 8, size=signal.shape)

signal_ruido_bajo = signal + ruido_bajo
signal_ruido_alto = signal + ruido_alto

# Función auxiliar para FFT y gráficas
def plot_signal_and_fft(sig, fs, title):
    N = len(sig)
    fft_values = fft(sig)
    freq = fftfreq(N, 1/fs)
    mag = 2*np.abs(fft_values)/N
    pos_freq = freq[:N//2]
    pos_mag = mag[:N//2]
    
    fig, axs = plt.subplots(2, 1, figsize=(12, 6))
    axs[0].plot(t, sig)
    axs[0].set_title(f'{title} en el tiempo')
    axs[0].set_xlabel('Tiempo (s)')
    axs[0].set_ylabel('Amplitud')
    axs[0].grid(True)

    axs[1].stem(pos_freq, pos_mag, linefmt='b-', markerfmt='bo', basefmt='r-')
    axs[1].set_title(f'Espectro de magnitud ({title})')
    axs[1].set_xlabel('Frecuencia (Hz)')
    axs[1].set_ylabel('Magnitud')
    axs[1].set_xlim(0, 250)
    axs[1].grid(True)
    plt.tight_layout()
    #plt.show()

# Graficar señal + ruido bajo y alto
plot_signal_and_fft(signal_ruido_bajo, fs, 'Señal con ruido bajo')
plot_signal_and_fft(signal_ruido_alto, fs, 'Señal con ruido alto')
plt.show()

# Potencia de la señal pura
signal_potencia = np.mean(signal**2)

# Potencias de los ruidos
rudio_bajo = signal_ruido_bajo - signal
ruido_alto = signal_ruido_alto - signal

ruido_potencia_bajo = np.mean(ruido_bajo**2)
ruido_potencia_alto = np.mean(ruido_alto**2)

# SNR en dB
SNR_bajo = 10*np.log10(signal_potencia/ ruido_potencia_bajo)
SNR_alto = 10*np.log10(signal_potencia / ruido_potencia_alto)


print(f"SNR con ruido bajo: {SNR_bajo:.2f} dB")

print(f"SNR con ruido alto: {SNR_alto:.2f} dB")

