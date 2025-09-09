from app.calc import soma, subtrai, multiplica, divide, potencia
import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_potencia():
    assert potencia(2, 3) == 8
