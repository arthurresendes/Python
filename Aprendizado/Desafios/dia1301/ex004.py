def calculo_pop() -> str:
    populacaoA = 8000
    populacaoB = 200000

    anos = 0
    while populacaoA < populacaoB:
        populacaoA *= 1.03
        populacaoB *= 1.02
        anos += 1

    return f"Demorou {anos} anos para Populacão A: {populacaoA} passar a População B: {populacaoB}"

if __name__ == "__main__":
    print(calculo_pop())