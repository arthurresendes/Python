def calcular_imposoto(salario_bruto):
    if salario_bruto <= 2112.00:
        imposto = 0.0
        return imposto
    elif salario_bruto <= 2826.25:
        imposto = (salario_bruto * 0.075) - 158.40
        return imposto
    elif salario_bruto <= 3751.05:
        imposto = (salario_bruto * 0.15) - 370.40
        return imposto
    elif salario_bruto <= 4664.68:
        imposto = (salario_bruto * 0.225) - 651.73
        return imposto
    elif salario_bruto >= 4664.69:
        imposto = (salario_bruto * 0.275) - 884.96
        return imposto
    else:
        return "Erro ao calcular"


def fazendo_as_contas():
    while True:
        try:
            salario = float(input("Digite seu salario bruto: "))
            if isinstance(salario,float):
                break
        except:
            print("Erro, digite um número valido")
    imposto = calcular_imposoto(salario)
    print(f"Seu salario bruto: {salario:.2f}")
    print(f"Imposto a ser pago: {imposto:.2f}")
    print(f"Seu salario liquido {salario-imposto:.2f}")


if __name__ == "__main__":
    fazendo_as_contas()
