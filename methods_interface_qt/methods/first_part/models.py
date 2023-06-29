from pydantic import BaseModel, Field, validator
from base_models import (
    LimitsModel,
    MaxIterationModel,
    EpsilonModel,
    FirstArrival
)


class BaseFirstPartFuncNumModel(BaseModel):
    f_num: int = Field(1, description='Введите номер функции (1 или 2)')

    @validator('f_num')
    def f_num_must_contains(cls, value):
        if value not in (1, 2):
            raise ValueError('Функции с таким номером нет.'
                             'Ожидаемое значение "1" или "2"')
        return value


class BaseFirstPartModel(EpsilonModel, LimitsModel, BaseFirstPartFuncNumModel):
    """Базовая модель для одномерных методов"""


class UniformCostSearchModel(MaxIterationModel, BaseFirstPartModel):
    """Равномерный поиск"""


class HalfDivisionModel(BaseFirstPartModel):
    """Метод половинного деления"""


class GoldenSectionSearchModel(BaseFirstPartModel):
    """Метод золотого сечения"""


class BaseNewtonModel(MaxIterationModel, BaseFirstPartModel):
    """Базовая модель для одномерных методов Ньютона"""


class NewtonRaphsonModel(BaseNewtonModel, FirstArrival):
    """Метод Ньютона-Рафсона"""


class BoltsanoModel(BaseNewtonModel):
    """Метод Больцано"""


class SecantMethodModel(BaseNewtonModel):
    """Метод секущих"""


class BaseUnimodalityModel(MaxIterationModel, BaseFirstPartFuncNumModel, LimitsModel, FirstArrival):
    """Базовая модель для поиска интервала унимодальности"""

    delta: float = Field(0.001, description='Введите величину параметра шага')


class ConstStepModel(BaseUnimodalityModel):
    """С постоянным шагом"""


class PropStepModel(BaseUnimodalityModel):
    """С пропорциональным шагом"""


class SvennStepModel(BaseUnimodalityModel):
    """С шагом Свенна"""
