import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Función para graficar campo de pendientes y solución particular
def graficar(f, x_range=(-5,5), y_range=(-5,5), cond_inicial=None, titulo=""):
    x_vals = np.linspace(x_range[0], x_range[1], 20)
    y_vals = np.linspace(y_range[0], y_range[1], 20)
    X, Y = np.meshgrid(x_vals, y_vals)
    U = 1
    V = f(X, Y)
    N = np.sqrt(U**2 + V**2)
    U, V = U/N, V/N

    plt.figure(figsize=(8,6))
    plt.quiver(X, Y, U, V, angles="xy")
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    if cond_inicial:
        sol = solve_ivp(f, [x_range[0], x_range[1]], [cond_inicial[1]],
                        t_eval=np.linspace(x_range[0], x_range[1], 200))
        plt.plot(sol.t, sol.y[0], 'r', label=f"Solución particular y({cond_inicial[0]})={cond_inicial[1]}")
        plt.legend()

    plt.show()

# a) y' = -y - sin(x), y(0)=1
graficar(lambda x,y: -y - np.sin(x), cond_inicial=(0,1), titulo="a) y' = -y - sin(x)")

# b) y' = x + y, y(-2)=2
graficar(lambda x,y: x + y, cond_inicial=(-2,2), titulo="b) y' = x + y")

# c) y' = -x^2 + sin(y), ejemplo con y(0)=0
graficar(lambda x,y: -x**2 + np.sin(y), cond_inicial=(0,0), titulo="c) y' = -x^2 + sin(y)")

# d) (x^2+1)y' + 3xy = 6x → y' = (6x - 3xy)/(x^2+1)
graficar(lambda x,y: (6*x - 3*x*y)/(x**2+1), cond_inicial=(0,0), titulo="d) y' = (6x - 3xy)/(x^2+1)")

# e) y' = x e^y, ejemplo con y(0)=0
graficar(lambda x,y: x*np.exp(y), cond_inicial=(0,0), titulo="e) y' = x e^y")

# f) y' = x - y, y(1)=1
graficar(lambda x,y: x - y, cond_inicial=(1,1), titulo="f) y' = x - y")
