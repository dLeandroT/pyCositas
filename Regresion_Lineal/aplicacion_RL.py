import numpy as np
import matplotlib.pyplot as plt
from numpy.core.records import array

def estimate_b0_b1(x, y):
    n = np.size(x)
    
    # Obtener Promedios de x & y
    m_x = np.mean(x)
    m_y = np.mean(y)

    # Calcular sumatoria de xy y sumatoria de xx
    sumatoria_xy = np.sum(x - m_x) * (y - m_y)
    sumatoria_xx = np.sum(x * (x - m_x))

    # Coeficientes de Regresion 
    b_1 = sumatoria_xy / sumatoria_xx
    b_0 = m_y - b_1 * m_x 

    return(b_0, b_1)

# Funcion de Graficado
def plot_regression(x, y, b):
    """" 
    Plottear la funcion
    Recibe como parametros x, y, b
    """

    plt.plt.scatter(x, y, color = "g", marker = "O", s=30)
    y.pred = b[0] + b[1]*x
    plt.plt.plot(x, y.pred, color = "b")

    # Etquetado
    plt.xlabel('x-Independiente')
    plt.ylabel('y-Dependiente')

    plt.plt.show()


# Funcion Principal
def run():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array ([2, 3, 5, 6, 5])

    # Obtener B1 y B2
    b = estimate_b0_b1(x, y)
    print(f"Los valores de b0 = {b[0]}, b1 = {b[1]}")   

    # Graficar linea de regresion 
    plot_regression(x, y, b) 



if __name__ == '__main__':
    run()



