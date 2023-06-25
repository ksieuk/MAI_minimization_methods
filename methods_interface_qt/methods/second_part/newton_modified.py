import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('QtAgg')


def f2(x):
    x1, x2 = x
    return 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def gradient_f2(x):
    x1, x2 = x
    grad_x1 = -2 * (1 - x1) - 2 * (x2 - x1 ** 2) * 2 * x1
    grad_x2 = 2 * (x2 - x1 ** 2)
    return np.array([grad_x1, grad_x2])


def hessian_f2(x):
    x1, x2 = x
    hessian_x11 = 2 + 4 * (x2 - x1 ** 2) + 8 * x1 ** 2
    hessian_x12 = -4 * x1
    hessian_x21 = -4 * x1
    hessian_x22 = 2
    return np.array([[hessian_x11, hessian_x12], [hessian_x21, hessian_x22]])


def modified_newton_method(f, grad_f, hessian_f, x0, max_iter=100, epsilon=1e-6):
    x = np.array(x0, dtype=float)
    trajectory = [x]

    for _ in range(max_iter):
        gradient = grad_f(x)
        hessian = hessian_f(x)

        delta = np.linalg.solve(hessian, -gradient)
        x += delta
        trajectory.append(x)

        if np.linalg.norm(delta) < epsilon:
            break

    return x, trajectory


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111, projection='3d')

        x1_values = np.linspace(-2, 2, 100)
        x2_values = np.linspace(-1, 3, 100)
        x1, x2 = np.meshgrid(x1_values, x2_values)
        z = f2([x1, x2])

        self.axes.plot_surface(x1, x2, z, cmap='viridis')
        self.axes.set_xlabel('X1')
        self.axes.set_ylabel('X2')
        self.axes.set_zlabel('f2(X1, X2)')
        self.axes.set_title('График функции f2(X1, X2)')
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1, x2):
    x0 = [x1, x2]
    # Применяем модифицированный метод Ньютона
    solution, trajectory = modified_newton_method(f2, gradient_f2, hessian_f2, x0)

    # Выводим результаты
    print("Найденная точка: ", solution)
    print("Траектория поиска: ", trajectory)

    # Построение графика функции
    graph = MplCanvas(width=5, height=4, dpi=100)

    return f"Найденная точка: {solution}\nТраектория поиска: {trajectory}", graph



def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    start_algorithm(x1, x2)


def main():
    # Начальные точки
    x1, x2 = 0, 0

    start_algorithm(x1, x2)


if __name__ == '__main__':
    main()
