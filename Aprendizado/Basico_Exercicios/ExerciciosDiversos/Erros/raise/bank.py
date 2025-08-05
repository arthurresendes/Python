def saque(saldo,valor):
    if not isinstance(saldo, int) or not isinstance(valor, int):
        raise ValueError("Aceitamos apenas numeros!!")
    if saldo < valor:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

sald = int(input("Digite seu saldo: "))
value = int(input("Digite o valor a sacar: "))
print(saque(sald,value))