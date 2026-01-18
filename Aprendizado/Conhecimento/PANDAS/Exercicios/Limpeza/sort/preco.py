import pandas as pd

df6 = pd.DataFrame({
    "Produto": ["Arroz", "Feijão", "Macarrão", "Leite"],
    "Preço": [5.0, 7.5, 4.5, 3.0]
})
print(df6.sort_values(by="Preço"))
