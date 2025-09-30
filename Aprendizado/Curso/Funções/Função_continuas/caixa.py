import sys
def saque_multiplo_dez(valor: int):
    if valor % 10 == 0:
        return "É multiplo"
    else:
        sys.exit()

# // é divisão inteira

def notas_saque(valor):
    saque_multiplo_dez(valor)
    nota50 = valor // 50
    resto = valor % 50
        
    nota20 = resto // 20
    resto = resto % 20
        
    nota10 = resto // 10
        
    return nota50,nota20,nota10

def valor_saque():
    while True:
        try:
            saque = int(input("Qual valor a ser sacado: "))
            if isinstance(saque,int):
                break
        except:
            print("Digite um número inteiro!!")
    n50,n20,n10 = notas_saque(saque)
    print(f"Notas de 50: {n50}, Notas de 20: {n20}, Notas de 10: {n10}")


if __name__ == "__main__":
    valor_saque()