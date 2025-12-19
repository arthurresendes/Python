def ler_num() -> int:
    while True:
        try:
            number = int(input("Digite um numero para ver seu fatorial: "))
            if isinstance(number,int):
                return number
        except:
            print("Erro, digite um numero valido!!")
    

def fatorial() -> int:
    numero = ler_num()
    
    fatorial = 1
    for i in range(1,numero + 1):
        fatorial *= i
    return fatorial


if __name__ == "__main__":
    resultado_final = fatorial()
    print(resultado_final)