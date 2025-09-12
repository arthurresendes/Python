import pandas as pd

dados = {
    "Aluno": ['Arthur', 'Jose', 'Maria'],
    "Prova1": [9,7,6],
    "Prova2": [4,3,6]
}
df = pd.DataFrame(dados, index=['LIN1','LIN2','LIN3'])

df['Soma'] = df['Prova1'] + df['Prova2']

df['Media'] = df['Soma'] / 2
df['Situação'] = df['Media'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')
print(df)
df.to_excel("NotasAlunos.xlsx", index=True)