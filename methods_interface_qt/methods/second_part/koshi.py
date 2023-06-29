from methods.second_part.models import KoshiModel
from methods.second_part.funcs import FUNCS


def koshi(
        max_iterations, epsilon, x0, x1, x2,
        func_x, func_xx1, func_xx2,
):
    k = k_method = 0
    print(f"{k=}\n{x0=}\n{x1=}\n{x2=}\n{func_x(x1, x2)=}\n"
          f"grad1={func_xx1(x1, x2)}\ngrad2={func_xx2(x1, x2)}")
    while k <= max_iterations:
        if (abs(x0 * func_xx1(x1, x2))) < epsilon and (abs(x0 * func_xx2(x1, x2))) < epsilon:
            break
        # минимизируем T методом золотого сечения
        c = 2
        a = -c
        b = c
        interval_half_1 = a
        interval_half_2 = b

        k_method = 0
        while abs(func_x(x1 - interval_half_1 * func_xx1(x1, x2), x2 - interval_half_1 * func_xx2(x1, x2)) - func_x(
                x1 - interval_half_2 * func_xx1(x1, x2), x2 - interval_half_2 * func_xx2(x1, x2))) > epsilon and \
                k_method <= (max_iterations * 100):

            interval_half_1 = (a + b - epsilon) / 2
            interval_half_2 = (a + b + epsilon) / 2
            if func_x(x1 - interval_half_1 * func_xx1(x1, x2), x2 - interval_half_1 * func_xx2(x1, x2)) < func_x(
                    x1 - interval_half_2 * func_xx1(x1, x2),
                    x2 - interval_half_2 * func_xx2(x1, x2)):
                b = interval_half_2
            else:
                a = interval_half_1

            k_method += 1

        print(a, b, interval_half_1, interval_half_2)
        x0 = (a + b) / 2
        # доминимизировались
        x1, x2 = x1 - func_xx1(x1, x2) * x0, x2 - func_xx2(x1, x2) * x0

        k += 1

        print(f"{k=}\n{x0=}\n{x1=}\n{x2=}\n{func_x(x1, x2)=}\n"
              f"grad1={func_xx1(x1, x2)}\ngrad2={func_xx2(x1, x2)}")

        if abs(func_xx2(x1, x2)) <= epsilon and abs(func_xx1(x1, x2)) <= epsilon:
            break

    if k_method == (max_iterations * 10):
        raise RuntimeError(f'Превышено количество итераций ({max_iterations}) внутри метода')

    return f"{k=}\n{x0=}\n{x1=}\n{x2=}\n{func_x(x1, x2)=}\n" \
           f"grad1={func_xx1(x1, x2)}\ngrad2={func_xx2(x1, x2)}\n\n"


def start_algorithm(max_iterations, epsilon, t, x1, x2, f_num):
    funcs = FUNCS[f_num]
    func, f_xx1, f_xx2 = funcs['func'], funcs['f_xx1'], funcs['f_xx2']

    return koshi(
        max_iterations, epsilon, t, x1, x2, func, f_xx1, f_xx2
    )


def start_from_model(model: KoshiModel):
    return start_algorithm(
        model.n,
        model.epsilon,
        model.x0,
        model.x1,
        model.x2,
        model.f_num,
    )


def start_input():
    t = float(input('Введите значение t (первое приближение): '))
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))
    max_iterations = int(input('Введите максимальное количество итераций: '))
    epsilon = float(input('Введите значение эпсилон: '))
    f_num = int(input('Введите номер функции (1, 2 или 3)'))

    start_algorithm(max_iterations, epsilon, t, x1, x2, f_num)


def main():
    max_iterations = 10
    epsilon = 0.0000001
    t = 0.9
    f_num = 2

    x1, x2 = -0.6, -0.6
    start_algorithm(max_iterations, epsilon, t, x1, x2, f_num)


if __name__ == '__main__':
    main()
