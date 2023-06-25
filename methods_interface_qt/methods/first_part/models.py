from pydantic import BaseModel, Field


class MinimizationModel(BaseModel):
    a: float = Field(..., description='Введите левую границу интервала a')
    b: float = Field(..., description='Введите правую границу интервала b')
    epsilon: float = Field(..., description='Введите точность поиска epsilon')
    f_num: int = Field(..., description='Введите номер функции (1 или 2)')
    n: int = Field(..., description='Введите количество шагов n')


class NewtonModel(BaseModel):
    x0: float = Field(..., description="Введите начальное приближение x0")
    a: float = Field(..., description='Введите начало интервала a')
    b: float = Field(..., description='Введите конец интервала b')
    epsilon: float = Field(..., description='Введите величину погрешности epsilon')
    f_num: str = Field(..., description='Введите номер функции (1 или 2)')
    max_iterations: int = Field(..., description='Введите максимальное количество итераций')


class UnimodalityModel(BaseModel):
    x0: float = Field(..., description='Введите начальную точку')
    a: float = Field(..., description='Введите левую границу области поиска')
    b: float = Field(..., description='Введите правую границу области поиска')
    delta: float = Field(..., description='Введите величину параметра шага')
    f_num: int = Field(..., description='Введите номер функции (1 или 2)')
    ran: int = Field(..., description='Введите количество итераций')

