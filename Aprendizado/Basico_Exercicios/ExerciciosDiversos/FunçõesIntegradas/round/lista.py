numerosR2 = [4.7, 2.2, 5.5, 3.9]
# Use round() em cada item da lista → [5, 2, 6, 4]

nova = []
for num in numerosR2:
    arredonda = round(num)
    nova.append(arredonda)
print(nova)

# Ou
arredonda2 = list(round(num) for num in numerosR2)
print(arredonda2)

