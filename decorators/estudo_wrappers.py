import time

texto = 'Gustavo Rosas'


def medir_tempo(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time() - t1

        print(f'Demorou {t2} segundos')

    return wrapper


@medir_tempo
def imprimir_texto(str):
    inicio = 0
    fim = 5

    while inicio < fim:
        inicio += 1
        if str is not None:
            print(str)
            time.sleep(1)

# Executa a função
# imprimir_texto(texto)
