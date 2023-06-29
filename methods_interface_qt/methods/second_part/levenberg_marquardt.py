import numpy as np
import matplotlib

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.models import LevenbergMarquardtModel
from methods.second_part.funcs import FUNCS


matplotlib.use('QtAgg')


def marquardt_method(x0, epsilon, max_iterations, func_x, gradient):
    x = x0.copy()
    lambd = 0.01  # Initial damping factor
    iteration = 0

    while np.linalg.norm(gradient(*x)) > epsilon and iteration < max_iterations:
        gradient_value = gradient(*x)
        hessian = np.zeros((2, 2))
        hessian[0, 0] = 2 + 12 * x[0] ** 2 - 4 * x[1]
        hessian[0, 1] = -4 * x[0]
        hessian[1, 0] = -4 * x[0]
        hessian[1, 1] = 2

        delta = np.linalg.solve(hessian + lambd * np.eye(2), -gradient_value)
        new_x = x + delta

        if func_x(*new_x) < func_x(*x):
            lambd *= 0.1
            x = new_x
        else:
            lambd *= 10

        iteration += 1

    return x


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, func_x, f_num, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111, projection='3d')

        x1_vals = np.linspace(-2, 2, 100)
        x2_vals = np.linspace(-2, 2, 100)
        x1_mesh, x2_mesh = np.meshgrid(x1_vals, x2_vals)
        f_vals = func_x(x1_mesh, x2_mesh)

        self.axes.plot_surface(x1_mesh, x2_mesh, f_vals, cmap='viridis')
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title(f'График функции f{f_num}(x1, x2)')

        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1: float, x2: float, epsilon, max_iterations, f_num):
    funcs = FUNCS[f_num]
    func, gradient = funcs['func'], funcs['gradient']

    x0 = np.array([x1, x2])

    # Выполняем метод Марквардта
    result = marquardt_method(x0, epsilon, max_iterations, func, gradient)

    # Создаем график функции
    graph = MplCanvas(func, f_num, width=5, height=4, dpi=100)

    return f"Найденные точки:\nx1 = {result[0]}\nx2 = {result[1]}", graph


def start_from_model(model: LevenbergMarquardtModel):
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
