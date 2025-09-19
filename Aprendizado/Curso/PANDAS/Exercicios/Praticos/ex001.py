import pandas as pd

df = pd.DataFrame({
    'Produto': ['Notebook', 'Celular', 'Cadeira', 'Mesa', 'Fone', 'Monitor', 'Teclado', 'Mouse', 'Geladeira', 'TV'],
    'Categoria': ['Eletrônicos','Eletrônicos','Móveis','Móveis','Eletrônicos','Eletrônicos','Eletrônicos','Eletrônicos','Eletrodoméstico','Eletrodoméstico'],
    'Preço': [3500, 2500, 400, 800, 300, 1200, 150, 100, 2800, 3200],
    'Estoque': [10, 25, 15, 5, 50, 20, 30, 40, 8, 12]
})

df_caros = df[df['Preço'] > 1000].sort_values('Preço')
print(df_caros)
