import doctest

def soma(a,b):
    """
    >>> soma(2,3)
    5
    
    >>> soma(-1,2)
    'Erro'
    
    """
    if a < 0 or b < 0:
        return 'Erro'
    return a + b



def duplicar(lista):
    """
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    
    >>> duplicar([])
    Traceback (most recent call last):
    ...
    AssertionError: Erro
    
    """
    assert len(lista) != 0, 'Erro'
    listaOrganizada = []
    for i in lista:
        i = i * 2
        listaOrganizada.append(i)
    return listaOrganizada

if __name__ == "__main__":
    print(soma(2,3))
    print(duplicar([1, 2, 3, 4]))
    doctest.testmod()
