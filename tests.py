import pytest
from unimodality_interval import on_unimod


def test_unimod_example_1():
    x0 = 0.0
    a = 0
    b = 2
    delta = 0.001
    step = 0.001
    max_iterations = 25

    significant_sign = 4

    result = on_unimod(x0, a, b, delta, step, max_iterations)

    assert round(result, significant_sign) == 0.5375


def test_unimod_error_delta():
    x0 = 0.0
    a = 0
    b = 2
    delta = '0.001'
    step = 0.001
    max_iterations = 25

    with pytest.raises(ValueError) as error:
        on_unimod(x0, a, b, delta, step, max_iterations)

    assert str(error.value) == 'delta must be a float.'

