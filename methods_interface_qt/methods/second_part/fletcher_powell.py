import numpy as np
import matplotlib

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.funcs import f2, f2_gradient


from methods.second_part.models import FletcherPowellModel

matplotlib.use('QtAgg')


def davidon_fletcher_powell(x0, epsilon=1e-5, max_iterations=100, func=f2, gradient=f2_gradient):
    x1, x2 = np.array(x0)
    B = np.eye(2)  # Инициализируем начальную матрицу Hessian
    iteration = 0

    x_history = [x1, x2]  # Список для сохранения истории точек
    f_history = [func(x1, x2)]  # Список для сохранения истории значений функции

    while np.linalg.norm(gradient(x1, x2)) > epsilon and iteration < max_iterations:
        p = -np.dot(B, gradient(x1, x2))  # Вычисляем направление спуска

        alpha = line_search(x1, x2, p)  # Выполняем поиск шага по алгоритму "линийный поиск"

        x1_next, x2_next = x1 + alpha * p, x2 + alpha * p  # Вычисляем следующую точку
        s = x1_next - x1  # Вычисляем разность между текущей и следующей точками
        y = gradient(x1_next, x2_next) - gradient(x1, x2)  # Вычисляем разность градиентов в двух точках

        # Обновляем матрицу B по формуле Дэвидона-Флетчера-Пауэлла
        B += np.outer(s, s) / np.dot(s, y) - np.dot(B, np.outer(y, y)).dot(B) / np.dot(y, np.dot(B, y))

        x1, x2 = x1_next, x2_next
        iteration += 1

        x_history.append((x1_next, x2_next))
        f_history.append(func(x1_next, x2_next))

    return x_history, f_history


def line_search(x1, x2, p, func=f2, gradient=f2_gradient):
    alpha = 1.0
    rho = 0.5
    c = 0.5
    while func(x1 + alpha * p, x2 + alpha * p) > (func(x1, x2) + c * alpha * np.dot(gradient(x1, x2), p)):
        alpha *= rho
    return alpha


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, x_history, width=5, height=4, dpi=100):
        plt_ = Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        x1_range = np.linspace(-2, 2, 100)
        x2_range = np.linspace(-1, 3, 100)
        x1, x2 = np.meshgrid(x1_range, x2_range)
        z = f2([x1, x2])
        self.axes.contour(x1, x2, z, levels=20, colors='gray')  # Контуры функции
        self.axes.plot(*zip(*x_history), 'ro-')  # Траектория поиска
        self.axes.plot(*x_history[0], 'go')  # Начальная точка
        self.axes.plot(*x_history[-1], 'bo')  # Конечная точка
        self.axes.set_xlabel('x1')
        self.axes.set_ylabel('x2')
        self.axes.set_title('График функции')
        self.axes.grid(True)
        super(MplCanvas, self).__init__(plt_)


def start_algorithm(x1: float, x2: float):
    # Запуск метода Дэвидона-Флетчера-Пауэлла
    x_values = [x1, x2]
    x_history, f_history = davidon_fletcher_powell(x_values)

    # Построение графика функции
    graph = MplCanvas(x_history, width=5, height=4, dpi=100)

    # Вывод результатов
    return f"Точки:\n{'; '.join(map(str, x_history))}\nЗначения функции:\n{'; '.join(map(str, f_history))}",\
        graph


def start_from_model(model: FletcherPowellModel):
    return start_algorithm(
        model.x1,
        model.x2
    )


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    print(start_algorithm(x1, x2))


def main():
    # Начальные точки
    x1, x2 = 0, 0

    print(start_algorithm(x1, x2))


if __name__ == '__main__':
    main()
