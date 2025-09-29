import numpy as np
import matplotlib.pyplot as plt

# a) Señal de amplitud aleatoria uniforme, distribuida entre [8 40]
t = np.arange(0, 1, 0.0001)
A = np.random.uniform(8, 40, size=len(t))
x1 = A * np.cos(2 * np.pi * 10 * t)
varianza_x1 = np.var(x1)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.title('Amplitud aleatoria')
C1 = np.correlate(x1, x1, mode='full')
plt.subplot(2, 1, 2)
plt.plot(C1)
plt.savefig('imagenes/Actividad_4/senal_a.png')
plt.show()

# b) Señal de fase aleatoria uniforme, distribuida entre [-0.8π, 0.8π]
A2 = 5
fi = np.random.uniform(-0.25 * np.pi, 0.25 * np.pi, size=len(t))
x2 = A2 * np.cos(2 * np.pi * 10 * t + fi)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x2)
plt.title('Fase aleatoria')
C2 = np.correlate(x2, x2, mode='full')
plt.subplot(2, 1, 2)
plt.plot(C2)
plt.savefig('imagenes/Actividad_4/senal_b.png')
plt.show()

# c) Señal de frecuencia aleatoria uniforme, distribuida entre [0 20]
f = np.random.uniform(0, 20, size=len(t))
x3 = A2 * np.cos(2 * np.pi * f * t)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x3)
plt.title('Frecuencia aleatoria')
C3 = np.correlate(x3, x3, mode='full')
plt.subplot(2, 1, 2)
plt.plot(C3)
plt.savefig('imagenes/Actividad_4/senal_c.png')
plt.show()

# d) Señal de amplitud, fase y frecuencia aleatoria
x4 = A * np.cos(2 * np.pi * f * t + fi)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x4)
plt.title('Amplitud, Fase y Frecuencia aleatoria')
C4 = np.correlate(x4, x4, mode='full')
plt.subplot(2, 1, 2)
plt.plot(C4)
plt.savefig('imagenes/Actividad_4/senal_d.png')
plt.show()
