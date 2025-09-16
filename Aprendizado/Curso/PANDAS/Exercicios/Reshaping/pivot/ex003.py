import pandas as pd

def main():
    df = pd.DataFrame({
    'Temperatura': ['32C','28C','23C','12C'],
    'Cidade': ['Osasco','SP','Belo horizonte','RJ'],
    'Mes': [9,3,5,6]
    })
    pivot = df.pivot(index='Temperatura', columns='Cidade' , values='Mes')
    print(pivot)

if __name__ == "__main__":
    main()