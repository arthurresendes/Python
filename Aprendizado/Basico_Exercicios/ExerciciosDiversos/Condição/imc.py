try: 
    peso = float(input("Digite seu peso: "))
except:
    print("Digite valor float!!")
else:
    print(peso)
try: 
    altura = float(input("Digite sua altura: "))
except:
    print("Digite valor float!!")
else:
    print(altura)

imc = peso / (altura**2)
print(imc)
if imc > 40:
    print("Obesidade grave")
elif imc > 30:
    print("Esta obeso(a)")
elif imc < 18.5:
    print("Magreza")
elif imc <= 29.9 and imc >= 25:
    print("Sobrepeso")
else:
    print("No peso")