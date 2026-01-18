def calculando(peso: float,altura:float):
    return peso/(altura ** 2)

def avaliacao(imc):
    if imc <= 19:
        return "Abaixo do peso"
    elif imc <= 24:
        return "Na media"
    elif imc <= 30:
        return "Obesidade Grau1"
    elif imc <= 34:
        return "Obesidade Grau 2"
    elif imc <= 40:
        return "Sobrepeso"

pessoa = calculando(66.5,1.75)
print(avaliacao(pessoa)) 