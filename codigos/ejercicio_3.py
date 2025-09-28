import numpy as np
import matplotlib.pyplot as plt

######## Ejercicio 4b ########
# Definición de la función de distribución acumulada
def F(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x**2 / 2
    elif 1 < x <= 2:
        return 2*x - (x**2)/2 - 1
    else:
        return 1

# Vector de valores para graficar
x_vals = np.linspace(-0.5, 2.5, 500)
F_vals = [F(x) for x in x_vals]

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x_vals, F_vals, label=r'$F_X(x)$', color='blue')
plt.title("Función de Distribución Acumulada (FDA)")
plt.xlabel("x")
plt.ylabel(r"$F_X(x)$")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()



######## Ejercicio 4d ########

import numpy as np
import matplotlib.pyplot as plt

# Generar 500 muestras de u uniforme
np.random.seed(42)  # Para reproducibilidad, opcional
u = np.random.rand(500)

# Inicializar array para x
x = np.zeros(500)

# Aplicar la inversa de la CDF
for i in range(500):
    if u[i] <= 0.5:
        x[i] = np.sqrt(2 * u[i])
    else:
        x[i] = 2 - np.sqrt(2 * (1 - u[i]))

# Calcular media y varianza
media = np.mean(x)
varianza = np.var(x)

print("\n Media muestral:\n", media)
print("\n Varianza muestral:\n", varianza)

# Superponer la PDF teórica
x_teorico = np.linspace(0, 2, 100)
pdf_teorico = np.piecewise(x_teorico, 
                           [x_teorico <= 1, x_teorico > 1],
                           [lambda x: x, lambda x: 2 - x])
plt.plot(x_teorico, pdf_teorico, 'r-', label='Teórico')
plt.legend()

# Graficar histograma
plt.hist(x, bins=20, density=True, alpha=0.7, edgecolor='black')
plt.title('Histograma de 500 muestras aleatorias')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.show()
