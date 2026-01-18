import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [150, 200, 300, 250, 400, 350],
    "Lucro": [50, 80, 120, 100, 150, 130],
    "Despesas": [100, 120, 180, 150, 250, 220]
})

print(df)

# =============================
# 1️⃣ Gráfico de linha simples
# =============================
plt.figure(figsize=(8,4))               # Define o tamanho da figura
plt.plot(df["Mês"], df["Vendas"], marker='o', linestyle='-', color='blue', label='Vendas')
plt.title("Vendas por Mês")             # Título do gráfico
plt.xlabel("Mês")                        # Rótulo eixo X
plt.ylabel("Vendas")                     # Rótulo eixo Y
plt.grid(True, linestyle='--', alpha=0.5) # Grid no gráfico
plt.legend()                             # Legenda
plt.show()

# =============================
# 2️⃣ Gráfico de barras
# =============================
plt.figure(figsize=(8,4))
plt.bar(df["Mês"], df["Lucro"], color='green', alpha=0.7) # alpha = transparência
plt.title("Lucro por Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.show()

# =============================
# 3️⃣ Gráfico de barras horizontal
# =============================
plt.figure(figsize=(8,4))
plt.barh(df["Mês"], df["Despesas"], color='red', alpha=0.6)
plt.title("Despesas por Mês")
plt.xlabel("Despesas")
plt.ylabel("Mês")
plt.show()

# =============================
# 4️⃣ Gráfico de pizza
# =============================
plt.figure(figsize=(6,6))
plt.pie(df["Vendas"], labels=df["Mês"], autopct="%1.1f%%", startangle=90, shadow=True)
plt.title("Distribuição de Vendas")
plt.show()

# =============================
# 5️⃣ Gráfico de dispersão (scatter)
# =============================
plt.figure(figsize=(8,4))
plt.scatter(df["Vendas"], df["Lucro"], color='purple', s=100) # s = tamanho dos pontos
plt.title("Lucro x Vendas")
plt.xlabel("Vendas")
plt.ylabel("Lucro")
plt.grid(True)
plt.show()

# =============================
# 6️⃣ Subplots
# =============================
fig, axs = plt.subplots(2, 2, figsize=(12,8))
fig.suptitle("Gráficos Combinados", fontsize=16)

# Linha
axs[0,0].plot(df["Mês"], df["Vendas"], marker='o', color='blue')
axs[0,0].set_title("Vendas")

# Barra
axs[0,1].bar(df["Mês"], df["Lucro"], color='green')
axs[0,1].set_title("Lucro")

# Scatter
axs[1,0].scatter(df["Despesas"], df["Lucro"], color='orange', s=80)
axs[1,0].set_title("Lucro x Despesas")

# Pizza (usando inset)
axs[1,1].pie(df["Vendas"], labels=df["Mês"], autopct="%1.1f%%", startangle=90)
axs[1,1].set_title("Distribuição de Vendas")

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajusta espaçamento
plt.show()
