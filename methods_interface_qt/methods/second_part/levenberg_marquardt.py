import numpy as np
import matplotlib.pyplot as plt


def f2(x):
    return 0.5 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def gradient_f2(x):
    grad = np.zeros(2)
    grad[0] = -2 * (1 - x[0]) - 2 * (x[1] - x[0] ** 2) * 2 * x[0]
    grad[1] = 2 * (x[1] - x[0] ** 2)
    return grad


def marquardt_method(x0, f, gradient_f, epsilon=1e-6, max_iterations=100):
    x = x0.copy()
    lambd = 0.01  # Initial damping factor
    iteration = 0

    while np.linalg.norm(gradient_f(x)) > epsilon and iteration < max_iterations:
        gradient = gradient_f(x)
        hessian = np.zeros((2, 2))
        hessian[0, 0] = 2 + 12 * x[0] ** 2 - 4 * x[1]
        hessian[0, 1] = -4 * x[0]
        hessian[1, 0] = -4 * x[0]
        hessian[1, 1] = 2

        delta = np.linalg.solve(hessian + lambd * np.eye(2), -gradient)
        new_x = x + delta

        if f(new_x) < f(x):
            lambd *= 0.1
            x = new_x
        else:
            lambd *= 10

        iteration += 1

    return x


def start_algorithm(x1, x2):
    x0 = np.array([x1, x2])

    # Выполняем метод Марквардта
    result = marquardt_method(x0, f2, gradient_f2)

    # Создаем график функции
    x1_vals = np.linspace(-2, 2, 100)
    x2_vals = np.linspace(-2, 2, 100)
    x1_mesh, x2_mesh = np.meshgrid(x1_vals, x2_vals)
    f_vals = f2([x1_mesh, x2_mesh])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x1_mesh, x2_mesh, f_vals, cmap='viridis')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x)')
    plt.title('График функции')
    plt.show()

    return f"Найденные точки:\nx1 = {result[0]}\nx2 = {result[1]}"


def start_input():
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))

    start_algorithm(x1, x2)


def main():
    # Начальные точки
    x1, x2 = 0.5, 0.5

    start_algorithm(x1, x2)


if __name__ == '__main__':
    main()
