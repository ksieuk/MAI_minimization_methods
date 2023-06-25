import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.5 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def grad_f(x):
    df_dx1 = 2 * (x[0] ** 3 - x[0] * x[1]) + 2 * (x[0] - 1)
    df_dx2 = x[1] - x[0] ** 2
    return np.array([df_dx1, df_dx2])


def fletcher_reeves(x0, tol=1e-6, max_iter=100):
    x = x0
    p = -grad_f(x)
    alpha_start = 0.01
    iter = 0
    points = [x]

    while np.linalg.norm(grad_f(x)) > tol and iter < max_iter:
        iter += 1
        x_prev = x
        p_prev = p

        alpha = alpha_start
        while f(x + alpha * p) >= f(x):
            alpha *= 0.5

        x = x + alpha * p
        beta = np.dot(grad_f(x), grad_f(x)) / np.dot(grad_f(x_prev), grad_f(x_prev))
        p = -grad_f(x) + beta * p_prev

        points.append(x)

    return x, points


def start_algorithm(x1, x2):
    # Начальные точки
    x0 = np.array([x1, x2])

    # Применяем метод Флетчера-Ривса
    solution, points = fletcher_reeves(x0)

    # Строим график функции
    x_range = np.linspace(-3, 3, 100)
    y_range = np.linspace(-3, 3, 100)
    x, y = np.meshgrid(x_range, y_range)
    z = f([x, y])

    plt.figure(figsize=(10, 6))
    plt.contour(x, y, z, levels=np.logspace(-1, 3, 10))
    plt.plot(*zip(*points), '-o', color='r')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Метод Флетчера-Ривса для функции f2(x)')
    plt.grid(True)
    plt.show()

    # Выводим результат
    return f"Найденное решение: {solution}"


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    start_algorithm(x1, x2)


def main():
    start_algorithm(-1.5, 1.5)


if __name__ == '__main__':
    main()
