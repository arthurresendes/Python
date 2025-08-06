# Entrada: número

# try/except para tratar erro

# finally: print("Fim da execução")


try:
    num = int(input("Digite um num: "))
    print(num)
except ValueError:
    print("Digite um número válido!!")
finally:
    print("Fim da execução")