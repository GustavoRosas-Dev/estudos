import unittest


vazio = None

def teste_string(str):
    return {'vazio': str}

class TestEmptyString(unittest.TestCase):
    def testar_funcao(self):

        resultado = teste_string(vazio)

        self.assertEqual(resultado['vazio'], None)
