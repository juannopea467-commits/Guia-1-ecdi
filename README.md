<div style="text-align:center; font-family:Arial;">

  <img src="https://www.escuelaing.edu.co/assets/uploads/image/logo-ecijg.png" alt="Logo Julio Garavito" height="120">

  <h2>ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO</h2>
  <h3>UNIVERSIDAD</h3>
  <p><strong>VIGILADA MINEDUCACIÓN</strong></p>

  <h3>Departamento de Matemáticas</h3>
  <h2>Guía de trabajo 1: Campo de pendientes</h2>
  <p><strong>Competencias:</strong> R2, RM2, CM2, SP2, C3 – 2026</p>
  <p><strong>Integrante:</strong> Juan Miguel Nope Ascencio</p>

</div>

# Guía de trabajo 1: Campo de pendientes

## Ejercicio 1a
Ecuación diferencial: y' = -y - sin(x), con y(0)=1

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(x, y):
    return -y - np.sin(x)

# Campo de pendientes
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = 1
V = f(X, Y)

N = np.sqrt(U**2 + V**2)
U, V = U/N, V/N

plt.figure(figsize=(8,6))
plt.quiver(X, Y, U, V, angles="xy")
plt.title("Campo de pendientes: y' = -y - sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

sol = solve_ivp(f, [0, 5], [1], t_eval=np.linspace(0, 5, 100))
plt.plot(sol.t, sol.y[0], 'r', label="Solución particular y(0)=1")
plt.legend()
plt.show()
```


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Ecuación diferencial del modelo poblacional
def dP_dt(t, P):
    return P * (P - 1) * (2 - P)

# a) Diagrama de fase
def diagrama_fase():
    P_vals = np.linspace(-0.5, 2.5, 200)
    dP_vals = dP_dt(0, P_vals)

    plt.figure(figsize=(8,5))
    plt.axhline(0, color="black", linewidth=0.8)
    plt.plot(P_vals, dP_vals, label="dP/dt vs P")

    # Puntos de equilibrio
    for eq in [0, 1, 2]:
        plt.plot(eq, 0, "ro")
        plt.text(eq, 0.15, f"P={eq}", ha="center")

    plt.title("Diagrama de fase: dP/dt = P(P-1)(2-P)")
    plt.xlabel("Población (miles)")
    plt.ylabel("dP/dt")
    plt.grid(True)
    plt.legend()
    plt.savefig("fase.png")   # guarda imagen
    plt.close()

# Función para simular evolución de la población
def simular(P0, nombre, t_max=20):
    sol = solve_ivp(dP_dt, [0, t_max], [P0], t_eval=np.linspace(0, t_max, 300))
    plt.figure(figsize=(8,5))
    plt.plot(sol.t, sol.y[0], label=f"P(0)={P0*1000:.0f} ejemplares")
    plt.title(f"Evolución poblacional (P0={P0*1000:.0f})")
    plt.xlabel("Tiempo (años)")
    plt.ylabel("Población (miles)")
    plt.grid(True)
    plt.legend()
    plt.savefig(nombre)   # guarda imagen
    plt.close()

if __name__ == "__main__":
    # a) Diagrama de fase
    diagrama_fase()

    # b) Población inicial 3000 ejemplares
    simular(3, "poblacion_3000.png")

    # c) Población inicial 1500 ejemplares
    simular(1.5, "poblacion_1500.png")

    # d) Población inicial 500 ejemplares
    simular(0.5, "poblacion_500.png")

    # e) Población inicial 900 ejemplares
    simular(0.9, "poblacion_900.png")

```


