import numpy as np


def f1(x1, x2):
    return 24 * x1 + 6 * x2 - 2


def f1_xx1(x1, x2):
    return 24 * x1 + 6 * x2 - 2


def f1_xx2(x1, x2):
    return 4 * x2 + 6 * x1 - 1


def f1_gradient(x1, x2):
    df_dx1 = f1_xx1(x1, x2)
    df_dx2 = f1_xx2(x1, x2)
    return np.array([df_dx1, df_dx2])


def f2(x1, x2):
    return 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f2_gradient(x1, x2):
    df_dx1 = f2_xx1(x1, x2)
    df_dx2 = f2_xx2(x1, x2)
    return np.array([df_dx1, df_dx2])


def f2_xx1(x1, x2):  # производная от функции по х1
    func = 2 * x1 ** 3 + (2 - 2 * x2) * x1 - 2
    return func


def f2_xx2(x1, x2):  # производная от функции по х2
    func = x2 - x1 ** 2
    return func


def f3(x1, x2):
    return 400 * x1 ^ 3 + (2 - 400 * x2) * x1 - 2


def f3_xx1(x1, x2):
    return 400 * x1 ^ 3 + (2 - 400 * x2) * x1 - 2


def f3_xx2(x1, x2):
    return 200 * x2 - 200 * x1 ** 2


def f3_gradient(x1, x2):
    df_dx1 = f3_xx1(x1, x2)
    df_dx2 = f3_xx2(x1, x2)
    return np.array([df_dx1, df_dx2])
