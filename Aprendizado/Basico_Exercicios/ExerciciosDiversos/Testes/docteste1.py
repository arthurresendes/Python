import doctest
def potencia(base: int , expoente: int):
    '''
    Retorna a potencia da base elevado ao expoente 
    >>> potencia(2,3)
    8
    
    >>> potencia(5, 0)
    1
    '''
    return base ** expoente

if __name__ == "__main__":
    print(potencia(2,3))
    doctest.testmod()