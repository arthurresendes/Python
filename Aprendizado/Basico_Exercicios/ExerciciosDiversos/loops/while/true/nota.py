quantidadeNota = 0

valorNota = 0

 

 

while True:

    try:

        nota = int(input("Digite uma nota de 0 a 10(-1 para sair): "))

        if nota == -1:

            break

        valorNota = valorNota + nota

        quantidadeNota += 1

   

    except ValueError:

        print("Caractere digitado invalido")

 

media = valorNota/quantidadeNota

print(f"Sua media em {quantidadeNota} provas foi: {media}")