import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.prueba1 import n_mayor

def test_n_mayor_numero_mayor():
    assert n_mayor(10, 5) == 10

def test_n_mayor_numeros_iguales():
    assert n_mayor(5, 5) == 0

def test_n_mayor_numero_menor():
    assert n_mayor(3, 7) == 7


