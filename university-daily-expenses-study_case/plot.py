from cmath import nan
import matplotlib.pyplot as plt
import numpy as np

def makeplot(x, y, x_label: str, y_label: str, title: str, x_points, y_points, filename: str, x_labels_discret=None):
    plt.figure(figsize=(12, 6))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    #plt.plot(x, y, color='r')
    plt.scatter(x, y, color='b', zorder=2)
    plt.xticks(x, x_labels_discret)

    plt.legend()
    plt.grid(True, zorder=1, axis='both', which='both')
    plt.gca().set_xticks(x)
    plt.gca().set_yticks(np.arange(0, 50, 10))
    plt.savefig(f"{filename}.png")
    plt.show()

def G(x) -> float:
    if x in [1, 3, 5]: return 32.70
    elif x in [2, 4]: return 41.70
    else: return np.nan


if __name__ == "__main__":


    #x = [1, 2, 3, 4, 5]
    #y = [2*a for a in x if a % 2 == 1]

    x_axis = np.array([1, 2, 3, 4, 5])
    y_axis = np.array([G(x) for x in x_axis])

    makeplot(
    x_axis, 
    y_axis, 
    "Tempo (Dias)", 
    "Gasto (R$)", 
    "Gastos diários na universidade ao longo de 1 mês - Caso 1",
    None,
    None, 
    filename="daily_expenses_case1.png",
    x_labels_discret=["Segunda", "Terça", "Quarta", "Quinta", "Sexta"])