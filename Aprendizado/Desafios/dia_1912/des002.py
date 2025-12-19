def ler_num() -> int:
    while True:
        try:
            number = int(input("Digite um numero: "))
            if isinstance(number,int):
                return number
        except:
            print("Erro, digite um numero valido!!")
    

def soma_n() -> int:
    numero = ler_num()
    
    soma = 0
    for i in range(1,numero + 1):
        soma += i
    return soma


if __name__ == "__main__":
    resultado_final = soma_n()
    print(resultado_final)