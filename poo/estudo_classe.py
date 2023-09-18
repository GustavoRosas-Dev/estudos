'''
Criar uma classe que contenha 3 tipos de gatos diferentes com as seguintes características nome, sexo e cor predominante
'''

class Gato:
    def __init__(self, nome, sexo, cor, local) -> None:
        self.nome = nome
        self.sexo = sexo
        self.cor = cor
        self.local = local

gato1 = Gato(nome='Calvin', sexo='macho', cor='preto e branco', local='Vila Maria Alta')
gato2 = Gato(nome='Tom', sexo='macho', cor='branco', local='Vila Maria Alta')
gato3 = Gato(nome='Malu', sexo='femea', cor='rajada', local='Vila Maria Alta')


print(gato1.nome, gato1.sexo, gato1.cor, gato1.local)