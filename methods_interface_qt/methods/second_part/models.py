from pydantic import BaseModel, Field, validator

from base_models import (
    CoordinatesModel,
    MaxIterationModel,
    EpsilonModel,
    FirstArrival,
)


class SecondPartFuncNumModel(BaseModel):
    f_num: int = Field(1, description='Введите номер функции (1 или 2)')

    @validator('f_num')
    def f_num_must_contains(cls, value):
        if value not in (1, 2, 3):
            raise ValueError('Функции с таким номером нет.'
                             'Ожидаемое значение "1", "2" или "3"')
        return value


class BaseSecondPartModel(
    MaxIterationModel,
    EpsilonModel,
    CoordinatesModel,
    SecondPartFuncNumModel
):
    """Базовый класс для многомерных методов"""


class FletcherPowellModel(BaseSecondPartModel):
    """Метод Флетчера-Пауэлла"""


class FletcherReveesModel(BaseSecondPartModel):
    """Метод Флетчера-Ривса"""


class KoshiModel(BaseSecondPartModel, FirstArrival):
    """Метод Коши"""


class LevenbergMarquardtModel(BaseSecondPartModel):
    """Метод Левенберга-Марквардта"""


class NewtonModel(BaseSecondPartModel):
    """Метод Ньютона"""


class NewtonModifiedModel(BaseSecondPartModel):
    """Модифицированный метод Ньютона"""
