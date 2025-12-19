def ler_num() -> int:
    while True:
        try:
            number = int(input("Digite um numero: "))
            if isinstance(number,int):
                return number
        except:
            print("Erro, digite um numero valido!!")
    

def par_impar() -> str:
    numero = ler_num()
    
    if numero % 2  == 0:
        return "Par"
    else:
        return "Impar"


if __name__ == "__main__":
    resultado_final = par_impar()
    print(resultado_final)