import pytest
from estudo_wrappers import imprimir_texto, texto

# dados


def test_estudo_wrappers():

    try:
        # quando
        resultado = imprimir_texto(texto)

        assert resultado == texto


    except Exception as e:
        pytest.fail(f"A função gerou uma exceção: {str(e)}")

