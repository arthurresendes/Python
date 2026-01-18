import pandas as pd

df14 = pd.DataFrame({
    "Cor": ["Azul", "Verde", "Azul", "Amarelo", "Verde", "Vermelho"]
})
print(df14.nunique())
print(df14.Cor.unique())