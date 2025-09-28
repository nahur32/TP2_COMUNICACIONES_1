import numpy as np
import matplotlib.pyplot as plt
import os

# Crear carpeta si no existe
os.makedirs("imagenes/Actividad_3", exist_ok=True)

# Funcion para generar muestras segun la transformada inversa
def sample_from_density(n):
    u = np.random.rand(n)
    x = np.empty_like(u)
    mask = u <= 0.5
    x[mask] = np.sqrt(2 * u[mask])             # Para 0 <= x <= 1
    x[~mask] = 2 - np.sqrt(2 * (1 - u[~mask])) # Para 1 < x <= 2
    return x

# Generar 500 muestras
np.random.seed(27)  # Semilla para reproducibilidad
muestras = sample_from_density(500)

# Calcular media y varianza empiricas
media_emp = np.mean(muestras)
var_emp = np.var(muestras)
print("Media empírica:", media_emp)
print("Varianza empírica:", var_emp)

# Graficar histograma
plt.hist(muestras, bins=20, density=True, edgecolor="black", alpha=0.7)
plt.title("Histograma de 500 muestras")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.savefig("imagenes/Actividad_3/histograma.png")
plt.close()

# Graficar la CDF teorica
x_vals = np.linspace(0, 2, 200)
F_vals = np.piecewise(x_vals,
    [x_vals <= 0,
     (x_vals > 0) & (x_vals <= 1),
     (x_vals > 1) & (x_vals <= 2),
     x_vals > 2],
    [0,
     lambda t: t**2/2,
     lambda t: -t**2/2 + 2*t - 1,
     1])

plt.plot(x_vals, F_vals, label="CDF teórica", color="blue")
plt.title("Función de distribución acumulada")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(True)
plt.savefig("imagenes/Actividad_3/cdf.png")
plt.close()
