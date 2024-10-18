import pytest
from src.P1_2d_Construye_funciones.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(100, 121) == "El precio final del artículo con IVA (21.0) es 121.0€"

def test_calcula_precio1():
    assert calcula_precio(100, -5) == "El precio final del artículo con IVA (21.0) es 121.0€"

def test_calcula_precio2():
    assert calcula_precio(100, 48) == "El precio final del artículo con IVA (48.0) es 148.0€"
