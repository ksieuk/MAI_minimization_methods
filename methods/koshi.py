def f_x(x1, x2):  # функция от х
    func = 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2
    return func


def f_xx1(x1, x2):  # производная от функции по х1
    func = 2 * x1 ** 3 + (2 - 2 * x2) * x1 - 2
    return func


def f_xx2(x1, x2):  # производная от функции по х2
    func = x2 - x1 ** 2
    return func


def f(x1, x2):  # функция от х для минимизации t
    func = 0.5 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2
    return func


def main():
    N = 10
    E1 = 0.0000001
    E2 = 0.0000001
    t = 0.9

    k = 0
    x1, x2 = -0.6, -0.6
    F = f_x(x1, x2)

    print(f"k = 0, x1 = {x1}, x2 = {x2}, f(x) = {F}, t = {t}, grad = 1:{f_xx1(x1, x2)} 2:{f_xx2(x1, x2)}")

    while k <= N:
        if (abs(t * f_xx1(x1, x2))) < E1 and (abs(t * f_xx2(x1, x2))) < E1:
            break
        # минимизируем T методом золотого сечения
        c = 2
        a = -c
        b = c
        interval_half_1 = a
        interval_half_2 = b
        while abs(f(x1 - interval_half_1 * f_xx1(x1, x2), x2 - interval_half_1 * f_xx2(x1, x2)) - f(
                x1 - interval_half_2 * f_xx1(x1, x2),
                x2 - interval_half_2 * f_xx2(x1, x2))) > E2:
            interval_half_1 = (a + b - E2) / 2
            interval_half_2 = (a + b + E2) / 2
            if f(x1 - interval_half_1 * f_xx1(x1, x2), x2 - interval_half_1 * f_xx2(x1, x2)) < f(
                    x1 - interval_half_2 * f_xx1(x1, x2),
                    x2 - interval_half_2 * f_xx2(x1, x2)):
                b = interval_half_2
            else:
                a = interval_half_1

        print(a, b, interval_half_1, interval_half_2)
        t = (a + b) / 2
        # доминимизировались
        x1, x2 = x1 - f_xx1(x1, x2) * t, x2 - f_xx2(x1, x2) * t

        k += 1

        print(
            f"k = {k}, x1 = {x1}, x2 = {x2}, f(x) = {f_x(x1, x2)}, t = {t}, grad = 1:{f_xx1(x1, x2)} 2:{f_xx2(x1, x2)}\n")

        if abs(f_xx2(x1, x2)) <= E1 and abs(f_xx1(x1, x2)) <= E1:
            break

    print(
        f"k = {k}, t = {t}, x1 = {x1}, x2 = {x2}, f(x) = {f_x(x1, x2)}, t = {t}, grad = 1:{f_xx1(x1, x2)} 2:{f_xx2(x1, x2)} fin")


if __name__ == '__main__':
    main()
