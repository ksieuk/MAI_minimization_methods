from pydantic import BaseModel, Field, validator


class LimitsModel(BaseModel):
    a: float = Field(-1, description='Введите левую границу интервала (a)')
    b: float = Field(1, description='Введите правую границу интервала (b)')

    @validator('b')
    def check_limits(cls, value, values):
        if 'a' in values and values['a'] > value:
            raise ValueError('Левая граница (a) не может быть больше правой (b)')
        return value


class MaxIterationModel(BaseModel):
    n: int = Field(100, description='Введите количество шагов (n)')

    @validator('n')
    def max_iterations_limits(cls, value):
        assert value > 0, ValueError('Максимальное количество итераций должно быть больше 0')
        return value


class EpsilonModel(BaseModel):
    epsilon: float = Field(0.001, description='Введите точность поиска (epsilon)')

    @validator('epsilon')
    def epsilon_limits(cls, value):
        assert 0 < value < 1, ValueError("Погрешность имеет границы (0, 1)")
        return value


class FirstArrival(BaseModel):
    """Начальное приближение"""
    x0: float = Field(0, description="Введите начальное приближение x0")


class CoordinatesModel(BaseModel):
    x1: float = Field(0, description='Введите первую координату точки x1')
    x2: float = Field(0, description='Введите первую координату точки x2')

