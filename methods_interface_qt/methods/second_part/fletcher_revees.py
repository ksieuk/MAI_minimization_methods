import numpy as np

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.funcs import f2, f2_gradient
from methods.second_part.models import FletcherReveesModel




# def f(x):
#     return 0.5 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
#
#
# def grad_f(x):
#     df_dx1 = 2 * (x[0] ** 3 - x[0] * x[1]) + 2 * (x[0] - 1)
#     df_dx2 = x[1] - x[0] ** 2
#     return np.array([df_dx1, df_dx2])


def fletcher_reeves(x1, x2, tol=1e-6, max_iter=100, func=f2, gradient=f2_gradient):
    p = -f2_gradient(x1, x2)
    alpha_start = 0.01
    iter = 0
    points = [(x1, x2)]

    while np.linalg.norm(f2_gradient(x1, x2)) > tol and iter < max_iter:
        iter += 1
        x1_prev, x2_prev = x1, x2
        p_prev = p

        alpha = alpha_start
        while f2(x1 + alpha * p, x2 + alpha * p) >= f2(x1, x2):
            alpha *= 0.5

        x1, x2 = x1 + alpha * p, x2 + alpha * p
        beta = np.dot(f2_gradient(x1, x2), f2_gradient(x1, x2)) / np.dot(f2_gradient(x1_prev, x2_prev),
                                                                         f2_gradient(x1_prev, x2_prev))
        p = -f2_gradient(x1, x2) + beta * p_prev

        points.append((x1_prev, x2_prev))

    return (x1, x2), points


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, points, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        x_range = np.linspace(-3, 3, 100)
        y_range = np.linspace(-3, 3, 100)
        x, y = np.meshgrid(x_range, y_range)
        z = f2(x, y)

        self.axes.contour(x, y, z, levels=np.logspace(-1, 3, 10))
        self.axes.plot(*zip(*points), '-o', color='r')
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title('Метод Флетчера-Ривса для функции')
        self.axes.grid(True)
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1: float, x2: float):
    # Применяем метод Флетчера-Ривса
    solution, points = fletcher_reeves(x1, x2)

    # Строим график функции
    graph = MplCanvas(points, width=5, height=4, dpi=100)

    # Выводим результат
    return f"Найденное решение: {solution}", graph


def start_from_model(model: FletcherReveesModel):
    return start_algorithm(
        model.x1,
        model.x2
    )


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    start_algorithm(x1, x2)


def main():
    start_algorithm(-1.5, 1.5)


if __name__ == '__main__':
    main()
