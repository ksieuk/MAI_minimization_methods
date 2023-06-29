from methods.first_part.models import (
    UniformCostSearchModel,
    HalfDivisionModel,
    GoldenSectionSearchModel,

    NewtonRaphsonModel,
    BoltsanoModel,
    SecantMethodModel,

    ConstStepModel,
    PropStepModel,
    SvennStepModel,
)

from methods.second_part.models import (
    FletcherPowellModel,
    FletcherReveesModel,
    KoshiModel,
    LevenbergMarquardtModel,
    NewtonModel,
    NewtonModifiedModel
)

from methods.first_part import (
    min,
    newton as newton_min,
    unimod_steps
)

from methods.second_part import (
    fletcher_powell,
    fletcher_revees,
    koshi,
    levenberg_marquardt,
    newton,
    newton_modified
)

METHODS = {
    'Поиск интервала унимодальности c постоянным шагом': (ConstStepModel, unimod_steps.start_first),
    'Поиск интервала унимодальности c пропорциональным шагом': (PropStepModel, unimod_steps.start_second),
    'Поиск интервала унимодальности c шагом Свенна': (SvennStepModel, unimod_steps.start_third),

    'Равномерный поиск': (UniformCostSearchModel, min.start_first),
    'Метод половинного деления': (HalfDivisionModel, min.start_second),
    'Метод золотого сечения': (GoldenSectionSearchModel, min.start_third),

    'Метод Ньютона-Рафсона': (NewtonRaphsonModel, newton_min.start_first),
    'Метод Больцано (введите любое x0)': (BoltsanoModel, newton_min.start_second),
    'Метод секущих (введите любое x0)': (SecantMethodModel, newton_min.start_third),

    'Метод Флетчера-Пауэлла': (FletcherPowellModel, fletcher_powell.start_from_model),
    'Метод Флетчера-Ривса': (FletcherReveesModel, fletcher_revees.start_from_model),
    'Метод Коши': (KoshiModel, koshi.start_from_model),
    'Метод Левенберга-Марквардта': (LevenbergMarquardtModel, levenberg_marquardt.start_from_model),
    'Метод Ньютона': (NewtonModel, newton.start_from_model),
    'Модифицированный метод Ньютона': (NewtonModifiedModel, newton_modified.start_from_model),
}


FIELD_DEFAULT_TYPE = str | int | float | None
