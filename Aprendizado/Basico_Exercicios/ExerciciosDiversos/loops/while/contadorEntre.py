cont25 = 0
cont50 = 0
cont75 = 0
cont100 = 0
cont10000= 0
contOutros = 0

while True:
    num = int(input("Digite um numero (0 para sair): "))
    if num == 0:
        break
    
    if num <= 25:
        cont25 += 1
    elif num <= 50:
        cont50 += 1
    elif num <= 75:
        cont75 += 1
    elif num <= 100:
        cont100 += 1
    elif num <= 10000:
        cont10000 += 1
    else:
        contOutros += 1

print(f"Numeros entre (0-25): {cont25}")
print(f"Numeros entre (26-50): {cont50}")
print(f"Numeros entre (51-75): {cont75}")
print(f"Numeros entre (76-100): {cont100}")
print(f"Numeros entre (10000 acima): {contOutros}")