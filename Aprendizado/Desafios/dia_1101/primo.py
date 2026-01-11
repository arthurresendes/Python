def verifica_primo(n: int) -> bool:
    cont  = 0
    for i in range(2,n):
        if n % i == 0:
            cont +=1
    if cont==0:
        return True
    else:
        return False

print(verifica_primo(11))
print(verifica_primo(4))