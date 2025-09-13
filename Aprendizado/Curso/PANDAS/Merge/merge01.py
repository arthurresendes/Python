import pandas as pd

cadastro_a = {
    'Id': ['AA290', 'BB456', 'CC2139', 'DE2521', 'GT342', 'HH1158'],
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Gabriel', 'Helena'],
    'CEP': ['01001-000', '02045-100', '03058-200', '04077-300', '05090-400', '06005-500'],
    'Idade': [25, 32, 29, 41, 36, 27]
}
df = pd.DataFrame(cadastro_a)

cadastro_b = {
    'Id': ['BB456', 'GT342', 'LL324', 'MM567', 'NN890'],
    'Nome': ['Bruno Silva', 'Gabriel Souza', 'Larissa', 'Marcos', 'Nathalia'],
    'CEP': ['02045-100', '05090-400', '09033-200', '10044-300', '11055-400'],
    'Idade': [33, 37, 22, 39, 28]
}
df2 = pd.DataFrame(cadastro_b)

compras = {
    'Id': ['AA290', 'CC2139', 'GT342', 'JJ778', 'MM567', 'BB456'],
    'Produto': ['Notebook', 'Celular', 'Livro', 'Tablet', 'Cadeira', 'Fone de Ouvido'],
    'Valor': [3500, 1800, 60, 1200, 450, 200]
}
df3 = pd.DataFrame(compras)


print(df)
print(df2)
print(df3)

interseccao = pd.merge(df, df2[['Id', 'Nome', 'Idade']] , on='Id', how='inner')
print(interseccao)

esquerda = pd.merge(df,df2 , on="Id", how="left")
print(esquerda)

todos = pd.concat([df,df2])
juncao_compras = pd.merge(todos , df3 , on="Id" , how="inner")
print(juncao_compras)