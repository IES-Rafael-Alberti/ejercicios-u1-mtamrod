import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.P1_2d_Construye_funciones.ej01_def import input_nombre

# Definición de la prueba
def test_input_nombre():
    assert input_nombre() == "mario"  
