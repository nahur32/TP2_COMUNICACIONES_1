import numpy as np
import matplotlib.pyplot as plt

# Parámetros dados
A = 17  # W
f1 = 532e3  # Hz (532 kHz)
f2 = 600e3  # Hz (600 kHz)
c = 3e8  # m/s
D1 = 11e3  # m (11 km)
D2 = 14.5e3  # m (14.5 km)
A1_atenuacion = 0.10  # 10%
A2_atenuacion = 0.25  # 25%

# Amplitudes después de atenuación
a1 = A * (1 - A1_atenuacion)
a2 = A * (1 - A2_atenuacion)

# Retardos
tau1 = D1 / c
tau2 = D2 / c

# Tiempo de simulación
t = np.linspace(0, 5e-5, 1000)  # 50 microsegundos

# Función para calcular y graficar
def graficar_señal(frecuencia, titulo):
    # Señales individuales
    y1 = a1 * np.cos(2 * np.pi * frecuencia * (t - tau1))
    y2 = a2 * np.cos(2 * np.pi * frecuencia * (t - tau2))
    y_total = y1 + y2
    
    # Gráfico
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(t * 1e6, y1, 'b', label='Señal directa', linewidth=2)
    plt.plot(t * 1e6, y2, 'r', label='Señal reflejada', linewidth=2)
    plt.ylabel('Amplitud (W)')
    plt.title(f'{titulo} - Señales individuales')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(t * 1e6, y_total, 'g', label='Señal total', linewidth=3)
    plt.xlabel('Tiempo (μs)')
    plt.ylabel('Amplitud (W)')
    plt.title('Señal resultante en el receptor')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Información adicional
    print(f"\n{titulo}:")
    print(f"Amplitud señal directa: {a1:.2f} W")
    print(f"Amplitud señal reflejada: {a2:.2f} W")
    print(f"Amplitud máxima posible (suma): {a1 + a2:.2f} W")
    print(f"Amplitud máxima observada: {np.max(y_total):.2f} W")
    
    return y_total

# Ejecutar para f1 = 532 kHz
print("="*60)
print("EJERCICIO 1 - SIMULACIÓN DE INTERFERENCIA POR MULTITRAYECTO")
print("="*60)
y_total_532 = graficar_señal(f1, "f = 532 kHz")

# Ejecutar para f2 = 600 kHz
print("\n" + "="*60)
y_total_600 = graficar_señal(f2, "f = 600 kHz")

# c) Buscar frecuencia donde hay cancelación total
print("\n" + "="*60)
print("ANÁLISIS DE CANCELACIÓN (mismas atenuaciones)")
print("="*60)

# Suponer mismas atenuaciones (10% para ambas)
a1_equal = A * (1 - 0.10)
a2_equal = A * (1 - 0.10)

delta_D = D2 - D1
f_cancel = c / (2 * delta_D)

print(f"Diferencia de camino: {delta_D/1000:.1f} km")
print(f"Primera frecuencia de cancelación: {f_cancel/1000:.3f} kHz")

# Verificar cancelación
def verificar_cancelacion(frecuencia):
    y1_test = a1_equal * np.cos(2 * np.pi * frecuencia * (t - tau1))
    y2_test = a2_equal * np.cos(2 * np.pi * frecuencia * (t - tau2))
    y_total_test = y1_test + y2_test
    
    amplitud_max = np.max(np.abs(y_total_test))
    return amplitud_max

amplitud_cancel = verificar_cancelacion(f_cancel)
print(f"Amplitud máxima a {f_cancel/1000:.3f} kHz: {amplitud_cancel:.6f} W")
print(f"¿Cancelación casi total? {'Sí' if amplitud_cancel < 0.1 else 'No'}")

# Encontrar más frecuencias de cancelación
print(f"\nOtras frecuencias de cancelación (k = 0, 1, 2):")
for k in range(3):
    f_k = ((2*k + 1) * c) / (2 * delta_D)
    amp_k = verificar_cancelacion(f_k)
    print(f"k={k}: f = {f_k/1000:.3f} kHz → Amplitud = {amp_k:.6f} W")