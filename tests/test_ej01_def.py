import pytest
from src.P1_2d_Construye_funciones.ej01_def import input_nombre

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('mario', "mario"),
        ('emma', "emma"),
        ('juanma', "juanma"),
    ]
)
def test_input_nombre(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert input_nombre() == expected

    