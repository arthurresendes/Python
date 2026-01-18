'''
['Cidade', 'Produto', 'Vendas']
'''

import pandas as pd

def main():
    df = pd.DataFrame({
    'Produto': ['PC','Cafe','Livros','Cafe'],
    'Cidade': ['Osasco','SP','Belo horizonte','SP'],
    'Vendas': [200,300,552,236]
    })
    pivot = df.pivot_table(index='Cidade', columns='Produto' , values='Vendas', aggfunc="max")
    print(pivot)

if __name__ == "__main__":
    main()