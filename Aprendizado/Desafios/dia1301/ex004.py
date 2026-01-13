populacaoA = 8000
populacaoB = 200000

anos = 0
while populacaoA < populacaoB:
    populacaoA *= 1.03
    populacaoB *= 1.02
    anos += 1

print(f"Demorou {anos} anos para Populacão A: {populacaoA} passar a População B: {populacaoB}")