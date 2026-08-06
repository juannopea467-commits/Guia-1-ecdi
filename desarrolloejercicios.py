import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definimos la función diferencial
def f(x, y):
    return -y - np.sin(x)

# Campo de pendientes
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = 1
V = f(X, Y)

# Normalizamos las flechas
N = np.sqrt(U**2 + V**2)
U, V = U/N, V/N

plt.figure(figsize=(8,6))
plt.quiver(X, Y, U, V, angles="xy")
plt.title("Campo de pendientes: y' = -y - sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Solución particular con condición inicial y(0)=1
sol = solve_ivp(f, [0, 5], [1], t_eval=np.linspace(0, 5, 100))

plt.plot(sol.t, sol.y[0], 'r', label="Solución particular y(0)=1")
plt.legend()
plt.show()
