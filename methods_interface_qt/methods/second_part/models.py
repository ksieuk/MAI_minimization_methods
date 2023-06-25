from pydantic import BaseModel, Field


class FletcherPowellModel(BaseModel):
    x1: float = Field(..., description='Введите первую точку x1')
    x2: float = Field(..., description='Введите вторую точку x2')


class FletcherReveesModel(BaseModel):
    x1: float = Field(..., description='Введите первую точку x1')
    x2: float = Field(..., description='Введите вторую точку x2')


class KoshiModel(BaseModel):
    t: float = Field(..., description='Введите значение t (первое приближение)')
    x1: float = Field(..., description='Введите первую точку x1')
    x2: float = Field(..., description='Введите вторую точку x2')
    max_iterations: int = Field(..., description='Введите максимальное количество итераций')
    epsilon: float = Field(..., description='Введите значение эпсилон')


class LevenbergMarquardtModel(BaseModel):
    x1: float = Field(..., description='Введите первую точку x1')
    x2: float = Field(..., description='Введите вторую точку x2')


class NewtonModel(BaseModel):
    x1: float = Field(..., description='Введите первую точку x1')
    x2: float = Field(..., description='Введите вторую точку x2')


class NewtonModifiedModel(BaseModel):
    x1: float = Field(..., description='Введите первую точку x1')
    x2: float = Field(..., description='Введите вторую точку x2')