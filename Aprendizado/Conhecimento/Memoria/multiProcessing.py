import time
from multiprocessing import Pool  

CONTADOR = 50_000_000

def contagem_regressiva(x):
    while x > 0:
        x -= 1

if __name__ == "__main__":
    pool = Pool(processes=2)  # cria pool com 2 processos
    inicio = time.time()
    
    # executa em paralelo
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    
    pool.close()  # não aceita mais tarefas
    pool.join()   # espera os processos terminarem
    
    fim = time.time()
    print(f"Demorou {fim - inicio:.2f} segundos")
