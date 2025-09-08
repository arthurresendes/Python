def aluno_status(nota:float) -> str:
    if nota > 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

print(aluno_status(7.5))
print(aluno_status(5.5))