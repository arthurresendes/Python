import numpy as np

def sem_duplicatas(lista: list[int]) -> list[int]:
    arr_unico = np.unique(lista)
    return arr_unico

print(sem_duplicatas([1,1,2,2,3,4,5,6,7,7]))