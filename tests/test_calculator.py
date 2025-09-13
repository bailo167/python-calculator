from src.calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 3.5) == 6.0
from src.calculator import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 7) == -7
    assert subtract(2.5, 1.5) == 1.0
from src.calculator import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(2.5, 2) == 5.0
from src.calculator import divide
import pytest

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
