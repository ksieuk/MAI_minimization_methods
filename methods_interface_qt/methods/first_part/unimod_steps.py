import numpy as np

from methods.first_part.models import (
    ConstStepModel,
    PropStepModel,
    SvennStepModel,
)


def f(x, f_num):
    if f_num == 1:
        res = (np.sin(x)) ** 11
    else:
        res = 2 * (x - 1) ** 2 + 0.01 / (1 - 2 * x ** 2)

    if np.isnan(res):
        raise ValueError(f'Ошибка при вычислении значения функции. Попробуйте изменить границы')
    return res


def const_step(x, k, xp, delta, f_num):
    xk = x + delta
    if f(xk, f_num) > f(x, f_num):
        a = xp
        b = xk
        print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b, k
    return const_step(x=xk, k=k + 1, xp=x, delta=delta, f_num=f_num)


def prop_step(x, k, xp, delta, f_num):
    xk = x + k * delta
    if f(xk, f_num) > f(x, f_num):
        a = xp
        b = xk
        print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b, k
    return prop_step(x=xk, k=k + 1, xp=x, delta=delta, f_num=f_num)


def svenn_step(x, k, xp, delta, f_num):
    xk = x + pow(2, k) * delta
    if f(xk, f_num) > f(x, f_num):
        a = xp
        b = xk
        print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b, k
    return svenn_step(x=xk, k=k + 1, xp=x, delta=delta, f_num=f_num)


def unimod(x, delta, a, b, f_num, algorithm_type):
    fa = f(x, f_num)
    fb = f(x + delta, f_num)
    fc = f(x - delta, f_num)
    k = 0

    if fc >= fa <= fb:
        return a, b, k

    if fc <= fa <= fb:
        delta = -delta
    a, b, k = step(x=x, k=0, xp=x, delta=delta, algorithm_type=algorithm_type, f_num=f_num)

    return a, b, k


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
    hist = []
    for i in range(ran):
        print(i + 1, end=': ')
        a, b, k = unimod(x0, delta, a, b, f_num, algorithm_type)
        delta += 0.001
        hist.append(f"{i + 1}\t{b}\t{b - a}\t{k}")
    hist.append(f"Интервал унимодальности [a, b] = [{a}, {b}]")
    return '\n'.join(hist)


def start_first(model: ConstStepModel):
    return start_algorithm(
        model.x0,
        model.a,
        model.b,
        model.delta,
        model.n,
        model.f_num,
        algorithm_type='1'
    )


def start_second(model: PropStepModel):
    return start_algorithm(
        model.x0,
        model.a,
        model.b,
        model.delta,
        model.n,
        model.f_num,
        algorithm_type='2'
    )


def start_third(model: SvennStepModel):
    return start_algorithm(
        model.x0,
        model.a,
        model.b,
        model.delta,
        model.n,
        model.f_num,
        algorithm_type='3'
    )

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
