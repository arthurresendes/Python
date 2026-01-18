import requests

# Exemplo: dólar para real
requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

# Verificando se ta tudo certo
print(requisicao)

# Mostra a resposta em JSON
#print(requisicao.json())

dic_requisi = requisicao.json()
dados = dic_requisi['USDBRL']
number = float(dados['bid'])
print(number * 200)
print(dic_requisi['USDBRL'])
print(dic_requisi['BTCBRL'])
print(dic_requisi['EURBRL'])