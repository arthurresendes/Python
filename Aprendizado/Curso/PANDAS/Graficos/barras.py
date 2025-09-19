import pandas as pd
import matplotlib.pyplot as plt

df_barras = pd.DataFrame({
    "Produto": ["Arroz", "Feijão", "Macarrão", "Leite"],
    "Lucro": [50, 80, 120, 100]
})
print(df_barras)

plt.figure(figsize=(8,4))
plt.bar(df_barras["Produto"], df_barras["Lucro"], color='green', alpha=0.7) # alpha = transparência
plt.title("Lucro por Produto")
plt.xlabel("Produto")
plt.ylabel("Lucro")
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.show()