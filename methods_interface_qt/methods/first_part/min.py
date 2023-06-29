import math
import numpy as np

from methods.first_part.models import (
    UniformCostSearchModel,
    HalfDivisionModel,
    GoldenSectionSearchModel,
)


def f(x, f_num):
    if f_num == 1:
        return (np.sin(x)) ** 11
    else:
        return 2 * (x - 1) ** 2 + 0.01 / (1 - 2 * x ** 2)


def uniform_search(a, b, epsilon, f_num, n):
    step = (b - a) / n
    if step < epsilon:
        raise ValueError("Количество шагов слишком велико для заданной точности")
    min_func = f(a, f_num)
    min_arg = a

    i = 0
    for k in range(int(n)):
        x = a + k * step
        fx = f(x, f_num)
        if fx < min_func:
            min_func = fx
            min_arg = x
        i += 1

    return min_arg, i


def bisection_search(a, b, epsilon, f_num):
    i = 0
    while abs(b - a) > epsilon:
        x = (a + b) / 2
        if derivative(f_num, x) > 0:
            b = x
        else:
            a = x
        i += 1

    return (a + b) / 2, i


def derivative(f_num, x, h=1e-7):
    return (f(x + h, f_num) - f(x - h, f_num)) / (2 * h)


def golden_section_search(a, b, epsilon, f_num):
    i = 0
    golden_ratio = (1 + math.sqrt(5)) / 2
    c = b - (b - a) / golden_ratio
    d = a + (b - a) / golden_ratio

    while abs(c - d) > epsilon:
        if f(c, f_num) < f(d, f_num):
            b = d
        else:
            a = c
        i += 1

        c = b - (b - a) / golden_ratio
        d = a + (b - a) / golden_ratio
    return (b + a) / 2, i


algorithms_ru = {
    "1": "Равномерный поиск",
    "2": "Метод половинного деления",
    "3": "Метод золотого сечения",
}

algorithm_funcs = {
    "1": uniform_search,
    "2": bisection_search,
    "3": golden_section_search,
}


def start_algorithm(a, b, epsilon, algorithm_type, f_num, n=None):
    print(f'{n=}')
    if n is not None:
        minimum, iteration_number = algorithm_funcs[algorithm_type](a, b, epsilon, f_num, n)
    else:
        minimum, iteration_number = algorithm_funcs[algorithm_type](a, b, epsilon, f_num)
    return f"Минимум функции на заданном интервале находится в точке\nx = {minimum}," \
           f" количество итераций = {iteration_number}"


def start_first(model: UniformCostSearchModel) -> str:
    print(model.n)
    return start_algorithm(
        model.a, model.b,
        model.epsilon,
        algorithm_type='1',
        f_num=model.f_num,
        n=model.n
    )


def start_second(model: HalfDivisionModel) -> str:
    return start_algorithm(
        model.a, model.b,
        model.epsilon,
        algorithm_type='2',
        f_num=model.f_num,
    )


def start_third(model: GoldenSectionSearchModel):
    return start_algorithm(
        model.a, model.b,
        model.epsilon,
        algorithm_type='3',
        f_num=model.f_num,
    )


def start_input():
    for key, value in algorithms_ru.items():
        print(f"{key}: {value}")
    algorithm_number = input('\nВыберите алгоритм поиска. Укажите номер алгоритма: ')

    if algorithm_number not in algorithms_ru:
        raise ValueError('Такого алгоритма поиска не существует')

    f_num = int(input("Введите номер функции (1 или 2): "))
    a = float(input("Введите левую границу интервала a: "))
    b = float(input("Введите правую границу интервала b: "))
    epsilon = float(input("Введите точность поиска epsilon: "))
    n = int(input("Введите количество шагов N: "))

    start_algorithm(a, b, epsilon, algorithm_number, f_num, n)


def main():
    start_input()


if __name__ == '__main__':
    main()
