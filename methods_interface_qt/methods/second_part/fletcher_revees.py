import numpy as np

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.funcs import FUNCS
from methods.second_part.models import FletcherReveesModel


def fletcher_reeves(x1, x2, epsilon, max_iter, func, gradient):
    x = [x1, x2]
    p = -gradient(*x)
    alpha_start = 0.01
    k = 0
    points = [x]

    while np.linalg.norm(gradient(*x)) > epsilon and k < max_iter:
        k += 1
        x_prev = x
        p_prev = p

        alpha = alpha_start

        max_iter2 = max_iter * 10
        k2 = 0
        while func(*(x + alpha * p)) >= func(*x) and k2 < max_iter2:
            k2 += 1
            alpha *= 0.5

        x = x + alpha * p
        beta = np.dot(gradient(*x), gradient(*x)) / np.dot(gradient(*x_prev), gradient(*x_prev))
        p = -gradient(*x) + beta * p_prev

        points.append(x)

    return x, points


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, func, f_num, points, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        x_range = np.linspace(-3, 3, 100)
        y_range = np.linspace(-3, 3, 100)
        x, y = np.meshgrid(x_range, y_range)
        z = func(x, y)

        self.axes.contour(x, y, z, levels=np.logspace(-1, 3, 10))
        self.axes.plot(*zip(*points), '-o', color='r')
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title(f'Метод Флетчера-Ривса для функции f{f_num}(x1, x2)')
        self.axes.grid(True)
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1: float, x2: float, epsilon, max_iterations, f_num):
    funcs = FUNCS[f_num]
    func, gradient = funcs['func'], funcs['gradient']

    # Применяем метод Флетчера-Ривса
    solution, points = fletcher_reeves(x1, x2, epsilon, max_iterations, func, gradient)

    # Строим график функции
    graph = MplCanvas(func, f_num, points, width=5, height=4, dpi=100)

    # Выводим результат
    return f"Найденное решение: {solution}", graph


def start_from_model(model: FletcherReveesModel):
    return start_algorithm(
        model.x1,
        model.x2,
        model.epsilon,
        model.n,
        model.f_num,
    )


def start_input():
    x1 = float(input('Введите первую координату точки x1: '))
    x2 = float(input('Введите вторую координату точки x2: '))
    epsilon = float(input('Введите погрешность epsilon: '))
    max_iterations = int(input('Введите максимальное количество итераций n: '))
    f_num = int(input('Введите номер функции (1, 2 или 3)'))

    print(start_algorithm(x1, x2, epsilon, max_iterations, f_num))


def main():
    x1, x2 = 0, 0
    epsilon = 0.001
    max_iterations = 100
    f_num = 2

    print(start_algorithm(x1, x2, epsilon, max_iterations, f_num))


if __name__ == '__main__':
    main()
