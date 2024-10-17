from unittest import mock
from src.P1_2d_Construye_funciones.ej04_def import fahr_to_celsius

def test_fahr_to_celsius_32():
    with mock.patch('builtins.input', return_value="32"):
        assert fahr_to_celsius() == "Son 0.0ºC (32.0)"
    with mock.patch('builtins.input', return_value="212"):
        assert fahr_to_celsius() == "Son 100.0ºC (212.0)"


