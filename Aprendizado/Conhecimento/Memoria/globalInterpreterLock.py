import time
from threading import Thread

CONTADOR = 50000000

def contagem_regresiva(x):
    while x > 0:
        x = x - 1

inicio = time.time()
contagem_regresiva(CONTADOR)
fim = time.time()

print(f"Demorou {fim - inicio} segundos")