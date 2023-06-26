import numpy as np


def f2(x1, x2):
    return 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def gradient_f2(x1, x2):
    df_dx1 = 2 * x1 - 2 * x1 * (x2 - x1 ** 2) - 2
    df_dx2 = x2 - x1 ** 2
    return np.array([df_dx1, df_dx2])


def f2_xx1(x1, x2):  # производная от функции по х1
    func = 2 * x1 ** 3 + (2 - 2 * x2) * x1 - 2
    return func


def f2_xx2(x1, x2):  # производная от функции по х2
    func = x2 - x1 ** 2
    return func
