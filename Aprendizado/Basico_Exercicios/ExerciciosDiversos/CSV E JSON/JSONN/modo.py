import json

config = {
    "usuario": "Arthur",
    "modo": "claro",
    "volume": 75,
    "notificacoes": True
}

# Salvar config inicial
with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

# Ler e alterar
with open("config.json", "r") as file:
    dados = json.load(file)

dados["modo"] = "escuro"

# Regravar atualizado
with open("config.json", "w") as file:
    json.dump(dados, file, indent=4)

print("Configuração atualizada:", dados)