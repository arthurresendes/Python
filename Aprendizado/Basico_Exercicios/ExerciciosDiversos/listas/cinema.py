assentos = ['O','O','O','O','O','O','O','O','O','O']

print(assentos)

 

# Primeira reserva

print("Reserve um assento: ")

numero = -1

while numero < 0 or numero > 9 or assentos[numero] == 'X':

    numero = int(input("Número de 1 a 10: ")) - 1

    if numero < 0 or numero > 9:

        print("Número inválido.")

    elif assentos[numero] == 'X':

        print("Assento já está ocupado.")

 

assentos[numero] = "X"

print(assentos)

 

# Segunda reserva

print("Reserve outro assento: ")

numero2 = -1

while numero2 < 0 or numero2 > 9 or assentos[numero2] == 'X':

    numero2 = int(input("Número de 1 a 10: ")) - 1

    if numero2 < 0 or numero2 > 9:

        print("Número inválido.")

    elif assentos[numero2] == 'X':

        print("Assento já está ocupado.")

 

assentos[numero2] = "X"

print(assentos)

 

# Terceira reserva

print("Reserve outro assento: ")

numero3 = -1

while numero3 < 0 or numero3 > 9 or assentos[numero3] == 'X':

    numero3 = int(input("Número de 1 a 10: ")) - 1

    if numero3 < 0 or numero3 > 9:

        print("Número inválido.")

    elif assentos[numero3] == 'X':

        print("Assento já está ocupado.")

 

assentos[numero3] = "X"

print("Assentos finais:", assentos)