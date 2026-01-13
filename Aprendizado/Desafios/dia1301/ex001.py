def pedir_num() -> int:
    while True:
        try:
            x = int(input("Digite a nota de 1 até 10: "))
            if x > 0 and x < 11:
                return x
        except:
            print("Digite um valro valido!!")


if __name__ == "__main__":
    print(pedir_num())