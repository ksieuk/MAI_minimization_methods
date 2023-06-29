import numpy as np
import matplotlib

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.models import NewtonModifiedModel
from methods.second_part.funcs import FUNCS


matplotlib.use('QtAgg')


def hessian_f2(x):
    x1, x2 = x
    hessian_x11 = 2 + 4 * (x2 - x1 ** 2) + 8 * x1 ** 2
    hessian_x12 = -4 * x1
    hessian_x21 = -4 * x1
    hessian_x22 = 2
    return np.array([[hessian_x11, hessian_x12], [hessian_x21, hessian_x22]])


def modified_newton_method(x0, epsilon, max_iter, gradient, hessian):
    x = np.array(x0, dtype=float)
    trajectory = [x]

    for _ in range(max_iter):
        gradient_value = gradient(*x)
        hessian_value = hessian(*x)

        delta = np.linalg.solve(hessian_value, -gradient_value)
        x += delta
        trajectory.append(x)

        if np.linalg.norm(delta) < epsilon:
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

    solution, trajectory = modified_newton_method(
        start_point, epsilon, max_iterations, gradient, hessian
    )

    print("Найденная точка: ", solution)
    print("Траектория поиска: ", trajectory)

    # Рисуем график функции
    graph = MplCanvas(func, f_num, trajectory, width=5, height=4, dpi=100)

    return f"Найденная точка: {solution}\nТраектория поиска: {trajectory}", graph


def start_from_model(model: NewtonModifiedModel):
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
