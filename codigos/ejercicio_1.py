import numpy as np
import matplotlib.pyplot as plt

# Datos
A = 17.0           # W
f = 532e3          # Hz
c = 3e8            # m/s

# Distancias y atenuaciones
D1 = 11e3          # m
D2 = 14.5e3        # m
aten1 = 1 - 0.10  # 10% de atenuación
aten2 = 1 - 0.25  # 25% de atenuación

# Retardos
tau1 = D1 / c
tau2 = D2 / c

# Vector de tiempo (unas pocas microsegundos para ver varias ondas)
t = np.linspace(0, 10e-6, 2000)  # 10 microsegundos

# Señales recibidas
x1 = aten1 * A * np.cos(2*np.pi*f*(t - tau1))
x2 = aten2 * A * np.cos(2*np.pi*f*(t - tau2))
xr = x1 + x2

# Graficar
plt.figure(figsize=(10,6))
plt.plot(t*1e6, x1, label='Señal directa (x1)')
plt.plot(t*1e6, x2, label='Señal reflejada (x2)')
plt.plot(t*1e6, xr, label='Suma (x1+x2)', linewidth=2)
plt.xlabel('Tiempo [µs]')
plt.ylabel('Amplitud [W]')
plt.title('Señal directa, reflejada y su suma')
plt.legend()
plt.grid(True)
plt.show()
