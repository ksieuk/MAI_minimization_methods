import numpy as np
import matplotlib.pyplot as plt


def f2(x):
    x1, x2 = x
    return 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def gradient_f2(x):
    x1, x2 = x
    df_dx1 = -2 * (x2 - x1 ** 2) * (2 * x1) - 2 * (1 - x1)
    df_dx2 = 2 * (x2 - x1 ** 2)
    return np.array([df_dx1, df_dx2])


def hessian_f2(x):
    x1, x2 = x
    d2f_dx1dx1 = 2 * (2 * x1 ** 2) - 2 * (x2 - x1 ** 2) * 2 + 2
    d2f_dx1dx2 = -2 * x1
    d2f_dx2dx2 = 2
    return np.array([[d2f_dx1dx1, d2f_dx1dx2], [d2f_dx1dx2, d2f_dx2dx2]])


def newton_method(start_point, gradient, hessian, max_iterations=100, tolerance=1e-6):
    x = np.array(start_point, dtype=float)  # Изменение типа данных на float
    trajectory = [x]
    for _ in range(max_iterations):
        grad = gradient(x)
        hess = hessian(x)
        direction = np.linalg.solve(hess, -grad)
        x += direction
        trajectory.append(x)
        if np.linalg.norm(grad) < tolerance:
            break
    return x, trajectory


def start_algorithm(x1, x2, y1, y2):
    start_points = [[x1, x2], [y1, y2]]

    # Применяем метод Ньютона для каждой начальной точки
    for start_point in start_points:
        x_optimal, trajectory = newton_method(start_point, gradient_f2, hessian_f2)
        print("Начальная точка:", start_point)
        print("Оптимальная точка:", x_optimal)
        print()

        # Рисуем график функции
        x1_vals = np.linspace(-3, 3, 100)
        x2_vals = np.linspace(-3, 3, 100)
        x1, x2 = np.meshgrid(x1_vals, x2_vals)
        z = f2([x1, x2])
        plt.contour(x1, x2, z, levels=20, alpha=0.5, cmap="viridis")
        plt.plot(*zip(*trajectory), marker='o', color='red')
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.title('Метод Ньютона для функции f2(x)')
        plt.show()


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))
    y1 = float(input('Введите первую точку y1: '))
    y2 = float(input('Введите вторую точку y2: '))

    start_algorithm(x1, x2, y1, y2)


def main():
    # Задаем начальные точки
    x1, x2, y1, y2 = -1, -1, 2, 2

    start_algorithm(x1, x2, y1, y2)


if __name__ == '__main__':
    main()
