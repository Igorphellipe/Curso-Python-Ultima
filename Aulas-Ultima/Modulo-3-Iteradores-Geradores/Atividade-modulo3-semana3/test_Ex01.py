from test_aula_unitario_Ex01 import calculo_desconto
import pytest


def test_desconto_1():
    assert calculo_desconto(10 and 99) == 0.95

def test_desconto_2():
    assert calculo_desconto(100 and 999) == 0.90

def test_desconto_3():
    assert calculo_desconto(1000) == 0.85