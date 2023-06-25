import numpy as np


def f(x, f_num):
    if f_num == '1':
        return (np.sin(x)) ** 11
    else:
        return 2 * (x - 1) ** 2 + 0.01 / (1 - 2 * x ** 2)


def derivative(x, f_num, h=1e-7):
    return (f(x + h, f_num) - f(x - h, f_num)) / (2 * h)


def second_derivative(x, f_num, h=1e-7):
    return (f(x + h, f_num) - 2 * f(x, f_num) + f(x - h, f_num)) / h ** 2


def newton_raphson(x0, a, b, epsilon, max_iterations, f_num):
    iterations = 0
    array = []
    while abs(derivative(x0, f_num, h=1e-7)) > epsilon and iterations < max_iterations:
        x0 = x0 - derivative(x0, f_num, h=1e-7) / second_derivative(x0, f_num, h=1e-7)

        if x0 < a or x0 > b:
            print(f"Текущее приближение вышло за пределы интервала, x0 = {x0}")
            return None
        array.append(x0)
        iterations += 1

    print(f"Количество итераций {iterations}:", array)
    return x0


def boltsano(a, b, epsilon, max_iterations, f_num):
    iterations = 0
    array = []

    while abs(b - a) > epsilon and iterations < max_iterations:
        midpoint = (a + b) / 2
        if derivative(midpoint, f_num, h=1e-7) > 0:
            b = midpoint
        else:
            a = midpoint
        array.append(midpoint)
        iterations += 1

    print(f"Количество итераций {iterations}:", array)
    return (a + b) / 2


def secant_method(a, b, epsilon, max_iterations, f_num):
    x0, x1 = a, b
    array = []
    for _ in range(max_iterations):
        if abs(x1 - x0) < epsilon:
            print(f"Количество итераций {_}:", array)
            return x1
        try:
            x0, x1 = x1, x1 - derivative(x1, f_num, h=1e-7) * (
                    (x1 - x0) / (derivative(x1, f_num, h=1e-7) - derivative(x0, f_num, h=1e-7)))
            array.append(x1)
        except ZeroDivisionError:
            break
    if x1 < a or x1 > b:
        print(f"Текущее приближение вышло за пределы интервала, x0 = {x0}")
        return None
    return x1


algorithm_names = {
    '1': "Метод Ньютона-Рафсона",
    '2': "Метод Больцано",
    '3': "Метод секущих"
}

algorithm_funcs = {
    '1': newton_raphson,
    '2': boltsano,
    '3': secant_method
}


def start_algorithm(a, b, f_num, algorithm_type, epsilon, max_iterations, x0=None):
    print(a, b, epsilon, max_iterations, f_num)
    if algorithm_type == '1':
        minimum = algorithm_funcs[algorithm_type](x0, a, b, epsilon, max_iterations, f_num)
    else:
        minimum = algorithm_funcs[algorithm_type](a, b, epsilon, max_iterations, f_num)

    return f"Минимум функции на заданном интервале находится в точке x = {minimum}"


def start_first(x0, a, b, epsilon, f_num, max_iterations):
    return start_algorithm(a, b, f_num, algorithm_type='1', epsilon=epsilon, max_iterations=max_iterations, x0=x0)


def start_second(x0, a, b, epsilon, f_num, max_iterations):
    return start_algorithm(a, b, f_num, algorithm_type='2', epsilon=epsilon, max_iterations=max_iterations, x0=x0)


def start_third(x0, a, b, epsilon, f_num, max_iterations):
    return start_algorithm(a, b, f_num, algorithm_type='3', epsilon=epsilon, max_iterations=max_iterations, x0=x0)


def start_input():
    for key, value in algorithm_names.items():
        print(f"{key}: {value}")
    algorithm_number = input('\nВыберите алгоритм поиска. Укажите номер алгоритма: ')

    if algorithm_number not in algorithm_names:
        raise ValueError('Такого алгоритма поиска не существует')

    f_num = input("Введите номер функции (1 или 2): ")
    if f_num not in ("1", "2"):
        raise ValueError('Такого номера функции не существует')

    if algorithm_number == '1':
        x0 = float(input("Введите начальное приближение x0: "))
    else:
        x0 = None

    a = float(input("Введите начало интервала a: "))
    b = float(input("Введите конец интервала b: "))
    epsilon = float(input("Введите величину погрешности epsilon: "))
    max_iterations = int(input("Введите максимальное количество итераций: "))

    start_algorithm(a, b, f_num, algorithm_number, epsilon, max_iterations, x0=x0)


def main():
    start_input()


if __name__ == '__main__':
    main()
