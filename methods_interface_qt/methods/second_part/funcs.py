import numpy as np


def f1(x1, x2):
    return 12 * x1 ** 2 + 6 * x1 * x2 + 2 * x2 ** 2 - 2 * x1 - x2


def f1_xx1(x1, x2):
    return 24 * x1 + 6 * x2 - 2


def f1_xx2(x1, x2):
    return 4 * x2 + 6 * x1 - 1


def f1_gradient(x1, x2):
    df_dx1 = f1_xx1(x1, x2)
    df_dx2 = f1_xx2(x1, x2)
    return np.array([df_dx1, df_dx2])


def f1_hessian(x1, x2):
    hessian_x11 = 24
    hessian_x12 = 6
    hessian_x21 = 6
    hessian_x22 = 4
    return np.array([[hessian_x11, hessian_x12], [hessian_x21, hessian_x22]])


def f2(x1, x2):
    return 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f2_xx1(x1, x2):  # производная от функции по х1
    func = 2 * x1 ** 3 + (2 - 2 * x2) * x1 - 2
    return func


def f2_xx2(x1, x2):  # производная от функции по х2
    func = x2 - x1 ** 2
    return func


def f2_gradient(x1, x2):
    df_dx1 = f2_xx1(x1, x2)
    df_dx2 = f2_xx2(x1, x2)
    return np.array([df_dx1, df_dx2])


def f2_hessian(x1, x2):
    hessian_x11 = 6 * x1 ** 2 - 2 * x2 + 2
    hessian_x12 = -2 * x1
    hessian_x21 = -2 * x1
    hessian_x22 = 1
    return np.array([[hessian_x11, hessian_x12], [hessian_x21, hessian_x22]])


def f3(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f3_xx1(x1, x2):
    return 400 * x1 ** 3 + (2 - 400 * x2) * x1 - 2


def f3_xx2(x1, x2):
    return 200 * x2 - 200 * x1 ** 2


def f3_gradient(x1, x2):
    df_dx1 = f3_xx1(x1, x2)
    df_dx2 = f3_xx2(x1, x2)
    return np.array([df_dx1, df_dx2])


def f3_hessian(x1, x2):
    hessian_x11 = 1200 * x1 ** 2 - 400 * x2 + 2
    hessian_x12 = -400 * x1
    hessian_x21 = -400 * x1
    hessian_x22 = 200
    return np.array([[hessian_x11, hessian_x12], [hessian_x21, hessian_x22]])


FUNCS = {
    1: {
        'func': f1,
        'f_xx1': f1_xx1,
        'f_xx2': f1_xx2,
        'gradient': f1_gradient,
        'hessian': f1_hessian,
    },
    2: {
        'func': f2,
        'f_xx1': f2_xx1,
        'f_xx2': f2_xx2,
        'gradient': f2_gradient,
        'hessian': f2_hessian,
    },
    3: {
        'func': f3,
        'f_xx1': f3_xx1,
        'f_xx2': f3_xx2,
        'gradient': f3_gradient,
        'hessian': f3_hessian,
    },
}
