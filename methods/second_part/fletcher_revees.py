import numpy as np
import matplotlib.pyplot as plt
from methods.second_part.funcs import f2, gradient_f2


def fletcher_reeves(x1, x2, tol=1e-6, max_iter=100):
    p = -gradient_f2(x1, x2)
    alpha_start = 0.01
    iter = 0
    points = [(x1, x2)]

    while np.linalg.norm(gradient_f2(x1, x2)) > tol and iter < max_iter:
        iter += 1
        x1_prev, x2_prev = x1, x2
        p_prev = p

        alpha = alpha_start
        while f2(x1 + alpha * p, x2 + alpha * p) >= f2(x1, x2):
            alpha *= 0.5

        x1, x2 = x1 + alpha * p, x2 + alpha * p
        beta = np.dot(gradient_f2(x1, x2), gradient_f2(x1, x2)) / np.dot(gradient_f2(x1_prev, x2_prev),
                                                                         gradient_f2(x1_prev, x2_prev))
        p = -gradient_f2(x1, x2) + beta * p_prev

        points.append((x1_prev, x2_prev))

    return (x1, x2), points


def start_algorithm(x1, x2):
    # Применяем метод Флетчера-Ривса
    solution, points = fletcher_reeves(x1, x2)

    # Выводим результат
    print("Найденное решение:")
    print(solution)

    # Строим график функции
    x_range = np.linspace(-3, 3, 100)
    y_range = np.linspace(-3, 3, 100)
    x, y = np.meshgrid(x_range, y_range)
    z = f2(x, y)

    plt.figure(figsize=(10, 6))
    plt.contour(x, y, z, levels=np.logspace(-1, 3, 10))
    plt.plot(*zip(*points), '-o', color='r')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Метод Флетчера-Ривса для функции f2(x)')
    plt.grid(True)
    plt.show()


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    start_algorithm(x1, x2)


def main():
    start_algorithm(-1.5, 1.5)


if __name__ == '__main__':
    main()
