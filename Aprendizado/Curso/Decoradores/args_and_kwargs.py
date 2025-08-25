import time

def meu_decorador(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs) # Passa todos os argumentos para a função original
        fim = time.time()
        print(f"A função demorou {fim - inicio:.4f} segundos para executar.")
        return resultado
    return wrapper

@meu_decorador
def somar(a, b):
    time.sleep(0.1) # Simula que a função demora um pouco
    return a + b
print(somar(5,5))

def meu_decorador2(func):
    def wrapper(*args, **kwargs):
        print("Antes da execução da função")
        resultado = func(*args, **kwargs)
        print("Depois")
        return resultado
    return wrapper

@meu_decorador2
def apresentar(nome, idade = ''):
    print(f"{nome} e tenho {idade} anos")

apresentar('Arthur', 18)