import time
from threading import Thread

CONTADOR = 50000000

def contagem_regresiva(x):
    while x > 0:
        x = x - 1

t1 = Thread(target=contagem_regresiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regresiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f"Demorou {fim - inicio} segundos")