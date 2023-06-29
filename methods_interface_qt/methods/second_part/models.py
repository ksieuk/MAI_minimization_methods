from base_models import (
    CoordinatesModel,
    MaxIterationModel,
    EpsilonModel,
    FirstArrival,
)


class FletcherPowellModel(CoordinatesModel):
    """Метод Флетчера-Пауэлла"""


class FletcherReveesModel(CoordinatesModel):
    """Метод Флетчера-Ривса"""


class KoshiModel(
    MaxIterationModel,
    EpsilonModel,
    CoordinatesModel,
    FirstArrival
):
    """Метод Коши"""


class LevenbergMarquardtModel(CoordinatesModel):
    """Метод Левенберга-Марквардта"""


class NewtonModel(CoordinatesModel):
    """Метод Ньютона"""


class NewtonModifiedModel(CoordinatesModel):
    """Модифицированный метод Ньютона"""
