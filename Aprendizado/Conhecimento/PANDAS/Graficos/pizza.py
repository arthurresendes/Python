import pandas as pd
import matplotlib.pyplot as plt

df_pizza = pd.DataFrame({
    "Canal": ["Online", "Loja Física", "Revenda", "Parceiros"],
    "Vendas": [300, 200, 150, 100]
})


plt.figure(figsize=(6,6))
plt.pie(df_pizza["Vendas"], labels=df_pizza["Canal"], autopct="%1.1f%%", startangle=90, shadow=True)
plt.title("Vendas por Canal")
plt.show()
