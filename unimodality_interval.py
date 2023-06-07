from dataclasses import dataclass


@dataclass
class UnimodInput:
    x0: float = 0.0
    a: int = 0
    b: int = 2
    delta: float = 0.001
    step: float = 0.001
    max_iterations: int = 25

    def __post_init__(self):
        if not isinstance(self.x0, float):
            raise ValueError("x0 must be a float.")
        if not isinstance(self.delta, float) or self.delta < 0:
            raise ValueError("delta must be a positive float.")


def f(x):
    return 2 * (x - 1) ** 2 + 0.01 / (1 - 2 * x ** 2)


def get_step(x, k, xp, delta):
    xk = x + k * delta
    if f(xk) > f(x):
        a = xp
        b = xk
        # print(f'[{a:.3f}; {b:.3f}] {(b - a):.3f}, k = {k}')
        return a, b
    return get_step(x=xk, k=k + 1, xp=x, delta=delta)


def unimod(x, delta, a, b):
    f1 = f(x)
    f2 = f(x + delta)
    f3 = f(x - delta)

    if f3 >= f1 <= f2:
        return (a + b) / 2

    if f3 <= f1 <= f2:
        delta = -delta
    a, b = get_step(x=x, k=0, xp=x, delta=delta)

    return (a + b) / 2


def on_unimod(
        x0: float = 0.0,
        a: int = 0,
        b: int = 2,
        delta: float = '0.001',
        step: float = 0.001,
        max_iterations: int = 25
) -> float:
    input_data = UnimodInput(
        x0=x0,
        a=a,
        b=b,
        delta=delta,
        step=step,
        max_iterations=max_iterations
    )

    result = 0
    for i in range(input_data.max_iterations):
        try:
            result = unimod(x=input_data.x0, delta=input_data.delta, a=input_data.a, b=input_data.b)
        except TypeError as e:
            print(e)
        input_data.delta += input_data.step
    return result


def main():
    on_unimod()


if __name__ == '__main__':
    main()
