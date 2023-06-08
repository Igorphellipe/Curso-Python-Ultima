from test_aula_unitario_Ex02 import venda_lanche
import pytest
def test_lanche():
    assert venda_lanche(codigos=[100]) == 9.00

def test_lanche():
    assert venda_lanche(codigos=[101]) == 11.00

def test_lanche():
    assert venda_lanche(codigos=[102]) == 12.00

def test_lanche():
    assert venda_lanche(codigos=[103]) == 12.00

def test_lanche():
    assert venda_lanche(codigos=[104]) == 14.00

def test_lanche():
    assert venda_lanche(codigos=[105]) == 17.00

def test_lanche():
    assert venda_lanche(codigos=[200]) == 5.00

def test_lanche():
    assert venda_lanche(codigos=[201]) == 4.00




