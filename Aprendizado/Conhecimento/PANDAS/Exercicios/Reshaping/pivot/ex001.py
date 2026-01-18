import pandas as pd

#Crie um DataFrame com colunas ['Aluno', 'Matéria', 'Nota']. Use pivot para transformar a coluna Matéria em colunas e mostrar as notas de cada aluno.

df = pd.DataFrame({
    'Aluno': ['Jose','Amanda','Jose','Gabriel'],
    'Materia': ['Mat','LP','QUI','Mat'],
    'Nota': [9,3,5,6]
})
print(df)

pivot = df.pivot(index='Aluno', columns='Materia' , values='Nota')
print(pivot)