'''
df.head() -> Ver o começo da tabela 
df.tail() -> Ver a o final da tabela
df.index
df.columns
df.to_numpy() -> Retorna os valores da tabela
df.T -> transforma linha em coluna e coluna em linha


concatena = pd.concat([df,df1,df2]), keys=['f1','f2','f3'] -> Concatena os dataframes e passa linha chave para cada dataframe

print(concatena.loc['f1']) -> Loc localiza algo na tabela

pd.merge(tabela_esquerda, tabela_direita, on="coluna_que_liga" , how="right,left,inner,outrt")

drop -> remove
drop_duplicate -> remove duplicata


agrupamento = df.groupby(['Coluna']).sum() 

df.t -> Transforma linha em coluna e coluna em linha
df.shape -> Mostra as linhas e colunas

df.pivot(index= , columns= ,values=) -> deixa tabela mais organizada

df.pivot_table(index= , columns= ,values=.aggfunc='sum') -> Passa função como soma , etc

'''