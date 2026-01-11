def soma_pares(n: int) -> int:
    soma = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            soma += i
    return soma


print(soma_pares(11))