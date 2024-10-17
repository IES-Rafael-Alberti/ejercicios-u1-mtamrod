import pytest
from src.P1_2d_Construye_funciones.ej02_def import inputs, operador

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (["2", "15.5"], (2, 15.5)),
        (["3", "20"], (3, 20.0)),
    ]
)
def test_inputs(mock_inputs, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_inputs.pop(0))
    assert inputs() == expected


@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (["5", "5.0"], 25.0),
        (["-5", "5.0"], -25.0),
        (["3", "10.0"], 30.0),
    ]
)
def test_operador(mock_inputs, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_inputs.pop(0))
    assert operador() == expected
