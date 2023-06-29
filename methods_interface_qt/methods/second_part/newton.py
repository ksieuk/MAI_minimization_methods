import numpy as np
import matplotlib

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.models import NewtonModel
from methods.second_part.funcs import FUNCS


matplotlib.use('QtAgg')


def hessian_f2(x):
    x1, x2 = x
    d2f_dx1dx1 = 2 * (2 * x1 ** 2) - 2 * (x2 - x1 ** 2) * 2 + 2
    d2f_dx1dx2 = -2 * x1
    d2f_dx2dx2 = 2
    return np.array([[d2f_dx1dx1, d2f_dx1dx2], [d2f_dx1dx2, d2f_dx2dx2]])


def newton_method(start_point, epsilon, max_iterations, gradient, hessian):
    x = np.array(start_point, dtype=float)  # Изменение типа данных на float
    trajectory = [x]
    for _ in range(max_iterations):
        grad = gradient(*x)
        hess = hessian(*x)
        direction = np.linalg.solve(hess, -grad)
        x += direction
        trajectory.append(x)
        if np.linalg.norm(grad) < epsilon:
            break
    return x, trajectory


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, func, f_num, trajectory, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        x1_vals = np.linspace(-3, 3, 100)
        x2_vals = np.linspace(-3, 3, 100)
        x1, x2 = np.meshgrid(x1_vals, x2_vals)
        z = func(x1, x2)
        self.axes.contour(x1, x2, z, levels=20, alpha=0.5, cmap="viridis")
        self.axes.plot(*zip(*trajectory), marker='o', color='red')
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title(f'Метод Ньютона для функции f{f_num}(x1, x2)')
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1: float, x2: float, epsilon, max_iterations, f_num):
    start_point = [x1, x2]
    funcs = FUNCS[f_num]
    func, gradient, hessian = funcs['func'], funcs['gradient'], funcs['hessian']

    # Применяем метод Ньютона для каждой начальной точки

    x_optimal, trajectory = newton_method(
        start_point, epsilon, max_iterations, gradient, hessian
    )

    # Рисуем график функции
    graph = MplCanvas(func, f_num, trajectory, width=5, height=4, dpi=100)

    return f"Начальная точка: {start_point}\nОптимальная точка: {x_optimal}", graph


def start_from_model(model: NewtonModel):
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
    # Начальные точки
    x1, x2 = 0, 0
    epsilon = 0.001
    max_iterations = 100
    f_num = 2

    print(start_algorithm(x1, x2, epsilon, max_iterations, f_num))


if __name__ == '__main__':
    main()
