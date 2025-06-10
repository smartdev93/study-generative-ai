import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

# Parametrized test for the add() method
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5), # 2 + 3 = 5
        (0, 0, 0), # 0 + 0 = 0
        (-1, 1, 0),# -1 + 1 = 0
    ]
)
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, exc_type", [
    (5, 0, ZeroDivisionError),  
    ("a", 2, TypeError),        
])
def test_divide_error_returns_exception(calc, a, b, exc_type):
    """
    Call calc.divide(a, b). Since the method catches exceptions and returns the exception object,
    verify that the returned object is an instance of exc_type (ZeroDivisionError or TypeError).
    """
    result = calc.divide(a, b)
    assert isinstance(result, exc_type)
