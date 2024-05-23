import numpy as np
import matplotlib.pyplot as plt

def tracer_fonction(fonction, xmin, xmax, num_points=100):
    x = np.linspace(xmin, xmax, num_points)
    y = fonction(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Tracé de la fonction')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1.5)  # Ligne horizontale pour l'axe des ordonnées
    plt.axvline(0, color='black', linewidth=1.5)  # Ligne verticale pour l'axe des abscisses (plus épaisse)
    plt.show()

# Test avec une fonction quadratique
def f(x):
    return 1/x
tracer_fonction(f, -1, 1)
