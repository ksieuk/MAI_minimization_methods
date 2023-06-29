import numpy as np
import matplotlib

from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from methods.second_part.models import FletcherPowellModel

matplotlib.use('QtAgg')


def f2(x):
    return 0.5 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def gradient_f2(x):
    df_dx1 = 2 * x[0] - 2 * x[0] * (x[1] - x[0] ** 2) - 2
    df_dx2 = x[1] - x[0] ** 2
    return np.array([df_dx1, df_dx2])


def davidon_fletcher_powell(x0, epsilon=1e-5, max_iterations=100):
    x = np.array(x0)
    B = np.eye(2)  # Инициализируем начальную матрицу Hessian
    iteration = 0

    x_history = [x]  # Список для сохранения истории точек
    f_history = [f2(x)]  # Список для сохранения истории значений функции

    while np.linalg.norm(gradient_f2(x)) > epsilon and iteration < max_iterations:
        p = -np.dot(B, gradient_f2(x))  # Вычисляем направление спуска

        alpha = line_search(x, p)  # Выполняем поиск шага по алгоритму "линийный поиск"

        x_next = x + alpha * p  # Вычисляем следующую точку
        s = x_next - x  # Вычисляем разность между текущей и следующей точками
        y = gradient_f2(x_next) - gradient_f2(x)  # Вычисляем разность градиентов в двух точках

        # Обновляем матрицу B по формуле Дэвидона-Флетчера-Пауэлла
        B += np.outer(s, s) / np.dot(s, y) - np.dot(B, np.outer(y, y)).dot(B) / np.dot(y, np.dot(B, y))

        x = x_next
        iteration += 1

        x_history.append(x)
        f_history.append(f2(x))

    return x_history, f_history


def line_search(x, p):
    alpha = 1.0
    rho = 0.5
    c = 0.5
    while f2(x + alpha * p) > f2(x) + c * alpha * np.dot(gradient_f2(x), p):
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
