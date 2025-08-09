salario = float(input("Digite seu salario: "))
if salario > 4.664:
    imposto = salario * 0.275
    print(f"Imposto a ser pago -> {imposto}")
elif salario > 3.500:
    imposto = salario * 0.15
    print(f"Imposto a ser pago -> {imposto}")
else:
    imposto = 0
    print(f"Imposto a ser pago -> {imposto}")