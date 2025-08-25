import time

def calcula_tempo(func):
    def wrapper():
        tempo_inicio = time.time()
        resultado = func()
        tempo_final = time.time()
        print(f"Tempo de execução: {tempo_final - tempo_inicio:.5f} segundos")
        return resultado
    return wrapper

@calcula_tempo
def soma():
    return sum(range(1000000))

print(soma())