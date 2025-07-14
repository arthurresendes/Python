"""

Estruturas lógicas:

And - E (Em C é o &&)

Or - Ou (Em c é o ||)

Not - Valor eh invertido, se for true vira false e vice versa. Nega

Is - Verifica , tipo == , porem == compara os valores já o is comparar a memoria

"""

ativo = True

logado = True


if ativo and logado:

    print("Usuario ativo e logado no sistema!!")

elif ativo or logado:

    print("Usuario esta ou ativo ou logado!!")

# Se não estiver ativo

if not ativo:

    print("Voce tem que ativar sua conta!!")

# Ativo é falso ?

print(ativo is False)