import requests

cep = input("Digite seu cep(Apenas numeros): ")
url = f"https://cep.awesomeapi.com.br/json/{cep}"

requisicao = requests.get(url)

print(requisicao)
if requisicao.status_code == 200:
    dados = requisicao.json()
    print(dados)
    print(dados['address'])
    print(dados['district'])