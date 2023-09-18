import random

'''
Criar uma função que gera um número aleatório entre 30 e 100
'''

def numero_aleatorio(a, b):
    return random.randint(a, b)

numero_aleatorio = numero_aleatorio(30, 100)
#print(numero_aleatorio)




'''
Criar uma função que gera uma lista de números aleatórios entre 30 e 100
'''


def lista_aleatoria(a, b, c):
    lista = [random.randint(a, b) for numero in range(c)]

    return lista

lotofacil = lista_aleatoria(1, 25, 15)
print('\n', len(lotofacil), 'numeros aleatórios LOTOFÁCIL:\n', lotofacil)