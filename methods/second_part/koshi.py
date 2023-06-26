from methods.second_part.funcs import f2, f2_xx1, f2_xx2


def start_algorithm(max_iterations, epsilon, t, x1, x2):
    func = f2(x1, x2)

    print(f"k = 0, x1 = {x1}, x2 = {x2}, f(x) = {func}, t = {t}, grad = 1:{f2_xx1(x1, x2)} 2:{f2_xx2(x1, x2)}")
    k = k_method = 0
    while k <= max_iterations:
        if (abs(t * f2_xx1(x1, x2))) < epsilon and (abs(t * f2_xx2(x1, x2))) < epsilon:
            break
        # минимизируем T методом золотого сечения
        c = 2
        a = -c
        b = c
        interval_half_1 = a
        interval_half_2 = b

        k_method = 0
        while abs(f2(x1 - interval_half_1 * f2_xx1(x1, x2), x2 - interval_half_1 * f2_xx2(x1, x2)) - f2(
                x1 - interval_half_2 * f2_xx1(x1, x2), x2 - interval_half_2 * f2_xx2(x1, x2))) > epsilon and \
                k_method <= (max_iterations * 100):

            interval_half_1 = (a + b - epsilon) / 2
            interval_half_2 = (a + b + epsilon) / 2
            if f2(x1 - interval_half_1 * f2_xx1(x1, x2), x2 - interval_half_1 * f2_xx2(x1, x2)) < f2(
                    x1 - interval_half_2 * f2_xx1(x1, x2),
                    x2 - interval_half_2 * f2_xx2(x1, x2)):
                b = interval_half_2
            else:
                a = interval_half_1

            k_method += 1

        print(a, b, interval_half_1, interval_half_2)
        t = (a + b) / 2
        # доминимизировались
        x1, x2 = x1 - f2_xx1(x1, x2) * t, x2 - f2_xx2(x1, x2) * t

        k += 1

        print(
            f"k = {k}, x1 = {x1}, x2 = {x2}, f(x) = {f2(x1, x2)}, t = {t}, grad = 1:{f2_xx1(x1, x2)} 2:{f2_xx2(x1, x2)}\n")

        if abs(f2_xx2(x1, x2)) <= epsilon and abs(f2_xx1(x1, x2)) <= epsilon:
            break

    if k_method == (max_iterations * 10):
        raise RuntimeError(f'Превышено количество итераций ({max_iterations}) внутри метода')

    print(
        f"k = {k}, t = {t}, x1 = {x1}, x2 = {x2}, f(x) = {f2(x1, x2)}, t = {t}, grad = 1:{f2_xx1(x1, x2)} 2:{f2_xx2(x1, x2)} fin")


def start_input():
    t = float(input('Введите значение t (первое приближение): '))
    x1 = float(input('Введите первую точку x1: '))
    x2 = float(input('Введите вторую точку x2: '))
    max_iterations = int(input('Введите максимальное количество итераций: '))
    epsilon = float(input('Введите значение эпсилон: '))

    start_algorithm(max_iterations, epsilon, t, x1, x2)


def main():
    max_iterations = 10
    epsilon = 0.0000001
    t = 0.9

    x1, x2 = -0.6, -0.6
    start_algorithm(max_iterations, epsilon, t, x1, x2)


if __name__ == '__main__':
    main()
