def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    lista_nums = []
    for _ in range(2, n + 1):
        proximo = a + b
        a = b
        b = proximo
        lista_nums.append(b) 
    return lista_nums

print(fibonacci_iterativo(12)) 
