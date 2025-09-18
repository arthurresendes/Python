import pandas as pd

df10 = pd.DataFrame({
    "Filme": ["A", "B", "C", "D"],
    "Avaliação": [4.5, 3.2, 4.8, 3.2]
})
print(df10.sort_values(by="Avaliação", ascending=True, kind="stable"))
