import pandas as pd

# Criando um DataFrame de exemplo
dados = {
    'Produto': ['Notebook', 'Celular', 'Mouse', 'Teclado', 'Monitor', 'Celular', 'Mouse'],
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Periféricos', 'Periféricos', 'Eletrônicos', 'Eletrônicos', 'Periféricos'],
    'Preço': [3500, 2000, 150, 300, 1200, 2200, 180],
    'Quantidade': [5, 10, 15, 7, 3, 5, 20]
}

df = pd.DataFrame(dados)

# Mostrando o DataFrame
print("DataFrame Original:\n", df)

# 1. Sumarização básica numérica
print("\nResumo estatístico:\n", df.describe())

# 2. Soma total de preços e quantidades
soma = df[['Preço', 'Quantidade']].sum()
print("\nSoma de Preços e Quantidades:\n", soma)

# 3. Média de preços
media_preco = df['Preço'].mean()
print("\nMédia de Preço:", media_preco)

# 4. Contagem de produtos por categoria
contagem_categoria = df['Categoria'].value_counts()
print("\nContagem por Categoria:\n", contagem_categoria)

# 5. Sumarização agrupada (por Categoria)
resumo_categoria = df.groupby('Categoria').agg({
    'Preço': ['mean', 'sum', 'max'],
    'Quantidade': ['sum', 'mean']
})
print("\nResumo por Categoria:\n", resumo_categoria)