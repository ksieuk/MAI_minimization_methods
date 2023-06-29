import numpy as np
import matplotlib

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.funcs import FUNCS


from methods.second_part.models import FletcherPowellModel

matplotlib.use('QtAgg')


def davidon_fletcher_powell(x0, epsilon, max_iterations, func, gradient):
    x = x0
    b = np.eye(2)  # Инициализируем начальную матрицу Hessian
    iteration = 0

    x_history = [x]  # Список для сохранения истории точек
    f_history = [func(*x)]  # Список для сохранения истории значений функции

    while np.linalg.norm(gradient(x[0], x[1])) > epsilon and iteration < max_iterations:
        p = -np.dot(b, gradient(x[0], x[1]))  # Вычисляем направление спуска

        alpha = line_search(x, p, func, gradient)  # Выполняем поиск шага по алгоритму "линийный поиск"

        x_next = x + alpha * p  # Вычисляем следующую точку
        s = x_next - x  # Вычисляем разность между текущей и следующей точками
        y = gradient(x_next[0], x_next[1]) - gradient(x[0], x[1])  # Вычисляем разность градиентов в двух точках

        x = x_next
        iteration += 1

        x_history.append(x)
        f_history.append(func(*x))

        # Обновляем матрицу B по формуле Дэвидона-Флетчера-Пауэлла
        dot_1, dot_2 = np.dot(s, y), np.dot(y, np.dot(b, y))
        if dot_1 == 0 or dot_2 == 0:
            break
        b += np.outer(s, s) / dot_1 - np.dot(b, np.outer(y, y)).dot(b) / dot_2

    return x_history, f_history


def line_search(x, p, func, gradient):
    alpha = 1.0
    rho = 0.5
    c = 0.5
    while func(*(x + alpha * p)) > func(*x) + c * alpha * np.dot(gradient(*x), p):
        alpha *= rho
    return alpha


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, func, f_num, x_history, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        x1_range = np.linspace(-2, 2, 100)
        x2_range = np.linspace(-1, 3, 100)
        x1, x2 = np.meshgrid(x1_range, x2_range)
        z = func(x1, x2)
        self.axes.contour(x1, x2, z, levels=20, colors='gray')  # Контуры функции
        self.axes.plot(*zip(*x_history), 'ro-')  # Траектория поиска
        self.axes.plot(*x_history[0], 'go')  # Начальная точка
        self.axes.plot(*x_history[-1], 'bo')  # Конечная точка
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title(f'График функции f{f_num}(x1, x2)')
        self.axes.grid(True)
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1: float, x2: float, epsilon, max_iterations, f_num):
    # Запуск метода Дэвидона-Флетчера-Пауэлла
    funcs = FUNCS[f_num]
    func, gradient = funcs['func'], funcs['gradient']
    x_values = [x1, x2]
    x_history, f_history = davidon_fletcher_powell(
        x_values, epsilon, max_iterations, func, gradient
    )

    # Построение графика функции
    graph = MplCanvas(func, f_num, x_history, width=5, height=4, dpi=100)

    # Вывод результатов
    res_x_history, res_f_history = '\n'.join(map(str, x_history)), '\n'.join(map(str, f_history))
    return f"Точки:\n{res_x_history}\nЗначения функции:\n{res_f_history}",\
        graph


def start_from_model(model: FletcherPowellModel):
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
