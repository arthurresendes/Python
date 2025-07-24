def medias(*notas):
    if len(notas) == 0:
        return "Sem notas"
    else:
        return sum(notas)/len(notas)

print(medias(1,8,6,5))
print(medias(8,6))
print(medias())

# Com o * antes do parametro , voce pode colocar varios valores ou colocar nenhum