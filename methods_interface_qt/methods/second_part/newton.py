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
    df_dx1 = -2 * (x2 - x1 ** 2) * (2 * x1) - 2 * (1 - x1)
    df_dx2 = 2 * (x2 - x1 ** 2)
    return np.array([df_dx1, df_dx2])


def hessian_f2(x):
    x1, x2 = x
    d2f_dx1dx1 = 2 * (2 * x1 ** 2) - 2 * (x2 - x1 ** 2) * 2 + 2
    d2f_dx1dx2 = -2 * x1
    d2f_dx2dx2 = 2
    return np.array([[d2f_dx1dx1, d2f_dx1dx2], [d2f_dx1dx2, d2f_dx2dx2]])


def newton_method(start_point, gradient, hessian, max_iterations=100, tolerance=1e-6):
    x = np.array(start_point, dtype=float)  # Изменение типа данных на float
    trajectory = [x]
    for _ in range(max_iterations):
        grad = gradient(x)
        hess = hessian(x)
        direction = np.linalg.solve(hess, -grad)
        x += direction
        trajectory.append(x)
        if np.linalg.norm(grad) < tolerance:
            break
    return x, trajectory


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, trajectory, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        x1_vals = np.linspace(-3, 3, 100)
        x2_vals = np.linspace(-3, 3, 100)
        x1, x2 = np.meshgrid(x1_vals, x2_vals)
        z = f2([x1, x2])
        self.axes.contour(x1, x2, z, levels=20, alpha=0.5, cmap="viridis")
        self.axes.plot(*zip(*trajectory), marker='o', color='red')
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title('Метод Ньютона для функции')
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1, x2):
    start_point = [x1, x2]

    # Применяем метод Ньютона для каждой начальной точки
    # start_point = x_optimal = 0

    # for start_point in start_points:
    x_optimal, trajectory = newton_method(start_point, gradient_f2, hessian_f2)
    print("Начальная точка:", start_point)
    print("Оптимальная точка:", x_optimal)
    print()

    # Рисуем график функции
    graph = MplCanvas(trajectory, width=5, height=4, dpi=100)

    return f"Начальная точка: {start_point}\nОптимальная точка: {x_optimal}", graph


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    start_algorithm(x1, x2)


def main():
    # Задаем начальные точки
    x1, x2 = -1, -1

    start_algorithm(x1, x2)


if __name__ == '__main__':
    main()
