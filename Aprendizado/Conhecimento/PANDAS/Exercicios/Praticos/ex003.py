import pandas as pd


df_alunos = pd.DataFrame({
    'Aluno': ['Ana','Bruno','Carlos','Daniel','Eduardo','Fernanda','Gabriel','Helena','Isabela','João','Karen','Lucas','Maria','Nina','Otávio','Ana','João'],
    'Curso': ['Engenharia','Direito','Engenharia','Medicina','Direito','Engenharia','Medicina','Direito','Engenharia','Medicina','Direito','Engenharia','Medicina','Direito','Engenharia','Engenharia', 'Direito'],
    'Nota': [9,8,7,6,8,10,9,7,8,6,9,7,10,8,6,3,2]
})

print(df_alunos.value_counts('Curso'))
'''
media = df_alunos.groupby('Aluno')['Nota'].mean()
maxima = df_alunos.groupby('Aluno')['Nota'].max()
minima = df_alunos.groupby('Aluno')['Nota'].min()
'''
resumo = df_alunos.groupby('Aluno')['Nota'].agg(['mean','max','min'])
print(f"Resumo dos alunos:\n{resumo}")