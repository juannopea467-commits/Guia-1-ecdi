import sys, site

# Detectar librerías del usuario en IDLE
sys.path.append(site.getusersitepackages())

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ---------------------------------------------------------
# 1. Definición de las Ecuaciones Diferenciales Autónomas
# ---------------------------------------------------------
def eq_a(y, x): return y * (3 - y) * (y - 2)
def eq_b(y, x): return y**2 - y**3
def eq_c(y, x): return (y + 2) * (10 + 3*y - y**2)
def eq_d(y, x): return y**5 - 4*y**3 - 5*y**2
def eq_e(y, x): return (1 - y) * (y - 2)**3

# Configuración de ecuaciones con sus Puntos Críticos y Estabilidad
# Formato: (Título, Función, Límites Y, Puntos Críticos [(y_val, tipo, color)])
ecuaciones = [
    ("a) dy/dx = y(3-y)(y-2)", eq_a, (-1, 4), [
        (3.0, "Estable", "green"),
        (2.0, "Inestable", "red"),     # ⚠️ Añadida y marcada explícitamente la solución y=2
        (0.0, "Estable", "green")
    ]),
    ("b) dy/dx = y² - y³", eq_b, (-1, 2), [
        (1.0, "Estable", "green"),
        (0.0, "Semiestable", "orange")
    ]),
    ("c) dy/dx = (y+2)(10+3y-y²)", eq_c, (-4, 7), [
        (5.0, "Estable", "green"),
        (-2.0, "Semiestable", "orange")
    ]),
    ("d) dy/dx = y⁵ - 4y³ - 5y²", eq_d, (-2, 3.5), [
        (2.791, "Inestable", "red"),
        (0.0, "Semiestable", "orange"),
        (-1.0, "Inestable", "red"),
        (-1.791, "Estable", "green")
    ]),
    ("e) dy/dx = (1-y)(y-2)³", eq_e, (0, 3.2), [
        (2.0, "Estable", "green"),
        (1.0, "Inestable", "red")
    ])
]

# ---------------------------------------------------------
# 2. Generación del Campo de Direcciones y Curvas Solución
# ---------------------------------------------------------
fig, axes = plt.subplots(3, 2, figsize=(13, 15))
axes = axes.flatten()

x = np.linspace(-3, 3, 20)
x_sol = np.linspace(-3, 3, 200)

for idx, (titulo, f, y_lim, puntos_criticos) in enumerate(ecuaciones):
    ax = axes[idx]
    
    # Malla para el campo de direcciones
    y = np.linspace(y_lim[0], y_lim[1], 20)
    X, Y = np.meshgrid(x, y)
    
    # Campo de vectores (quiver)
    dy = f(Y, X)
    dx = np.ones(dy.shape)
    modulo = np.sqrt(dx**2 + dy**2)
    U = dx / modulo
    V = dy / modulo
    ax.quiver(X, Y, U, V, color='lightgray', alpha=0.7)
    
    # 1. Graficar trayectorias solución dinámicas
    y0_vals = np.linspace(y_lim[0] + 0.1, y_lim[1] - 0.1, 8)
    for y0 in y0_vals:
        sol = odeint(f, y0, x_sol)
        ax.plot(x_sol, sol, color='steelblue', alpha=0.5, linewidth=1.2)

    # 2. ✏️ Marcar explícitamente los PUNTOS DE EQUILIBRIO y su ESTABILIDAD
    for yc, tipo, color in puntos_criticos:
        # Trazar la solución exacta de equilibrio (línea continua de color)
        sol_eq = odeint(f, yc, x_sol)
        ax.plot(x_sol, sol_eq, color=color, linewidth=2.5, linestyle='--')
        
        # 📌 Añadir etiqueta explicativa de estabilidad en el gráfico
        ax.text(1.2, yc + (y_lim[1]-y_lim[0])*0.02, f"y={yc:g} ({tipo})", 
                color=color, fontweight='bold', fontsize=9,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=color, alpha=0.8))

    ax.set_xlim(-3, 3)
    ax.set_ylim(y_lim)
    ax.set_title(titulo, fontweight='bold', fontsize=11)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, linestyle=':', alpha=0.6)

# Ocultar la última subfigura vacía
fig.delaxes(axes[5])

plt.tight_layout()
plt.savefig('punto2_completo.png', dpi=300)
plt.show()
