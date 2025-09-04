import doctest

def eh_par(n):
    """
    Verificando se o numero é par
    
    >>> eh_par(2)
    'Eh par'
    
    >>> eh_par(3)
    'Eh impar'
    """
    if n % 2 == 0:
        return 'Eh par'
    else:
        return 'Eh impar'

if __name__ == "__main__":
    print(eh_par(6))
    print(eh_par(3))
    doctest.testmod()