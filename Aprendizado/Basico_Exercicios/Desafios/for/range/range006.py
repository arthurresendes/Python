soma = 0
media = 0

for i in range(1,11):
    numero = float(input(f"Digite o numero {i}: "))
    soma += numero

media = soma /10
print(f"A media dos numeros eh {media}")