import numpy as np


def f(x, f_num):
    if f_num == '1':
        return (np.sin(x)) ** 11
    else:
        return 2 * (x - 1) ** 2 + 0.01 / (1 - 2 * x ** 2)


def const_step(x, k, xp, delta, f_num):
    xk = x + delta
    if f(xk, f_num) > f(x, f_num):
        a = xp
        b = xk
        print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b
    return const_step(x=xk, k=k + 1, xp=x, delta=delta, f_num=f_num)


def prop_step(x, k, xp, delta, f_num):
    xk = x + k * delta
    if f(xk, f_num) > f(x, f_num):
        a = xp
        b = xk
        print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b
    return prop_step(x=xk, k=k + 1, xp=x, delta=delta, f_num=f_num)


def svenn_step(x, k, xp, delta, f_num):
    xk = x + pow(2, k) * delta
    if f(xk, f_num) > f(x, f_num):
        a = xp
        b = xk
        print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b
    return svenn_step(x=xk, k=k + 1, xp=x, delta=delta, f_num=f_num)


def unimod(x, delta, a, b, f_num, algorithm_type):
    fa = f(x, f_num)
    fb = f(x + delta, f_num)
    fc = f(x - delta, f_num)

    if fc >= fa <= fb:
        return (a + b) / 2

    if fc <= fa <= fb:
        delta = -delta
    a, b = step(x=x, k=0, xp=x, delta=delta, algorithm_type=algorithm_type, f_num=f_num)

    return (a + b) / 2


def step(x, k, xp, delta, f_num, algorithm_type):
    if algorithm_type == '1':
        return const_step(x, k, xp, delta, f_num)
    elif algorithm_type == '2':
        return prop_step(x, k, xp, delta, f_num)
    else:
        return svenn_step(x, k, xp, delta, f_num)


algorithm_names = {
    "1": "С постоянным шагом",
    "2": "С пропорциональным шагом",
    "3": "С шагом Свенна",
}


def start_algorithm(x0, a, b, delta, ran, f_num, algorithm_type):
    result = 0
    for i in range(ran):
        result = unimod(x0, delta, a, b, f_num, algorithm_type)
        delta += 0.001
        print(i + 1, end=': ')
    return f"Интервал унимодальности находится в точке {result:.6f}, " \
           f"значение функции в этой точке {f(result, f_num):.6f}"


def start_first(x0, a, b, delta, f_num, ran):
    return start_algorithm(x0, a, b, delta, ran, f_num, algorithm_type='1')


def start_second(x0, a, b, delta, f_num, ran):
    return start_algorithm(x0, a, b, delta, ran, f_num, algorithm_type='2')


def start_third(x0, a, b, delta, f_num, ran):
    return start_algorithm(x0, a, b, delta, ran, f_num, algorithm_type='3')


def start_input():
    for key, value in algorithm_names.items():
        print(f"{key}: {value}")

    algorithm_number = input('\nВыберите алгоритм поиска. Укажите номер алгоритма: ')
    if algorithm_number not in algorithm_names:
        raise ValueError('Такого алгоритма поиска не существует')

    f_num = input("Введите номер функции (1 или 2): ")
    if f_num not in ("1", "2"):
        raise ValueError('Такого номера функции не существует')

    x0 = float(input("Введите начальную точку: "))
    a = float(input("Введите левую границу области поиска: "))
    b = float(input("Введите правую границу области поиска: "))
    delta = float(input("Введите величину параметра шага: "))
    ran = int(input("Введите количество итераций: "))

    start_algorithm(x0, a, b, delta, ran, f_num, algorithm_number)


def main():
    start_input()


if __name__ == '__main__':
    main()
