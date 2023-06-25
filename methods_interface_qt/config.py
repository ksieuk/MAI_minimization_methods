from methods.first_part.models import (
    MinimizationModel,
    NewtonModel as SingleNewtonModel,
    UnimodalityModel,
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
    'Минимизация: Равномерный поиск': (MinimizationModel, min.start_first),
    'Метод половинного деления': (MinimizationModel, min.start_second),
    'Метод золотого сечения': (MinimizationModel, min.start_third),

    'Метод Ньютона-Рафсона': (SingleNewtonModel, newton_min.start_first),
    'Метод Больцано': (SingleNewtonModel, newton_min.start_second),
    'Метод секущих': (SingleNewtonModel, newton_min.start_third),

    'Интервал унимодальности c постоянным шагом': (UnimodalityModel, unimod_steps.start_first),
    'Интервал унимодальности c пропорциональным шагом': (UnimodalityModel, unimod_steps.start_second),
    'Интервал унимодальности c шагом Свенна': (UnimodalityModel, unimod_steps.start_third),

    'Метод Флетчера-Пауэлла': (FletcherPowellModel, fletcher_powell.start_algorithm),
    'Метод Флетчера-Ривса': (FletcherReveesModel, fletcher_revees.start_algorithm),
    'Метод Коши': (KoshiModel, koshi.start_algorithm),
    'Метод Левенберга-Марквардта': (LevenbergMarquardtModel, levenberg_marquardt.start_algorithm),
    'Метод Ньютона': (NewtonModel, newton.start_algorithm),
    'Модифицированный метод Ньютона': (NewtonModifiedModel, newton_modified.start_algorithm),
}
