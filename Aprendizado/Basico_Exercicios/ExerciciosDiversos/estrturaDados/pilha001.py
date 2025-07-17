pilha = []

quantidadeValor = int(input("Quantos valores quer adicionar à pilha: "))
for i in range(quantidadeValor):

    valor = input(f"Digite o {i + 1}º valor da pilha: ")
    pilha.append(valor) 

print("\nValores na pilha:")

for i in pilha:
    print(i)

print("\nRemovendo elemento da pilha:")
print(pilha.pop()) 
print("\nValores na pilha:")

for i in pilha:
    print(i)