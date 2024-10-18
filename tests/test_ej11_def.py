import pytest
from src.P1_2d_Construye_funciones.ej11_def import operador

def test_operador():
    assert operador(10) == 55

def test_operador1():
    assert operador(50) == 1275

def test_operador2():
    assert operador(6) == 21
