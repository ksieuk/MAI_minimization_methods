import numpy as np
import matplotlib.pyplot as plt
from methods.second_part.funcs import f2, gradient_f2


def davidon_fletcher_powell(x0, epsilon=1e-5, max_iterations=100):
    x1, x2 = np.array(x0)
    B = np.eye(2)  # Инициализируем начальную матрицу Hessian
    iteration = 0

    x_history = [x1, x2]  # Список для сохранения истории точек
    f_history = [f2(x1, x2)]  # Список для сохранения истории значений функции

    while np.linalg.norm(gradient_f2(x1, x2)) > epsilon and iteration < max_iterations:
        p = -np.dot(B, gradient_f2(x1, x2))  # Вычисляем направление спуска

        alpha = line_search(x1, x2, p)  # Выполняем поиск шага по алгоритму "линийный поиск"

        x1_next, x2_next = x1 + alpha * p, x2 + alpha * p  # Вычисляем следующую точку
        s = x1_next - x1  # Вычисляем разность между текущей и следующей точками
        y = gradient_f2(x1_next, x2_next) - gradient_f2(x1, x2)  # Вычисляем разность градиентов в двух точках

        # Обновляем матрицу B по формуле Дэвидона-Флетчера-Пауэлла
        B += np.outer(s, s) / np.dot(s, y) - np.dot(B, np.outer(y, y)).dot(B) / np.dot(y, np.dot(B, y))

        x1, x2 = x1_next, x2_next
        iteration += 1

        x_history.append((x1_next, x2_next))
        f_history.append(f2(x1_next, x2_next))

    return x_history, f_history


def line_search(x1, x2, p):
    alpha = 1.0
    rho = 0.5
    c = 0.5
    while f2(x1 + alpha * p, x2 + alpha * p) > f2(x1, x2) + c * alpha * np.dot(gradient_f2(x1, x2), p):
        alpha *= rho
    return alpha


def start_algorithm(x1, x2):
    # Запуск метода Дэвидона-Флетчера-Пауэлла
    x_values = [x1, x2]
    x_history, f_history = davidon_fletcher_powell(x_values)

    # Вывод результатов
    print("Точки:")
    print('; '.join(map(str, x_history)))
    print("\nЗначения функции:")
    print('; '.join(map(str, f_history)))

    # Построение графика функции
    x1_range = np.linspace(-2, 2, 100)
    x2_range = np.linspace(-1, 3, 100)
    x1, x2 = np.meshgrid(x1_range, x2_range)
    z = f2(x1, x2)

    plt.figure(figsize=(8, 6))
    plt.contour(x1, x2, z, levels=20, colors='gray')  # Контуры функции
    plt.plot(*zip(*x_history), 'ro-')  # Траектория поиска
    plt.plot(*x_history[0], 'go')  # Начальная точка
    plt.plot(*x_history[-1], 'bo')  # Конечная точка
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('График функции f2(x)')
    plt.grid(True)
    plt.show()


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
