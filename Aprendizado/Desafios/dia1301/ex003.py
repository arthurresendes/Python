def informacao_pessoa() -> dict:
    nome = input("Digite seu nome: ")
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0 and idade < 151:
                break
        except:
            print("Idade só pode ser de 1 até 150: ")
            
    while True:
        try:
            salario = float(input("Digite seu salario: "))
            if salario > 0:
                break
        except:
            print("Digite um salario valido")
            
    while True:
        try:
            sexo = input("Digite seu sexo (F ou M): ").upper()
            if sexo == 'F' or sexo == 'M':
                break
        except:
            print("Digite um sexo valido")
            
    while True:
        try:
            estado_civil = input("Digite seu estado civil (S,C,V,D): ").upper()
            if estado_civil == 'C' or estado_civil == 'S'or estado_civil == 'V'or estado_civil == 'D':
                break
        except:
            print("Digite um estado civil valido")
        
    return {"Nome: ": nome, "Idade": idade, "Sexo": sexo, "Salario": salario, "Estado Civil": estado_civil}


if __name__ == "__main__":
    print(informacao_pessoa())