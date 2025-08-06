# Entrada: valor como string

# Ex: "3.14" ✅, "abc" ❌

 

string = input("Digite um valor float: ")
converte = None
try:
    converte = float(string)
except ValueError:
    print("Valor inválido!")
else:
    print(f"Valor convertido com sucesso: {converte}")
finally:
    print("Fim da execução.")