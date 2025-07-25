def exibir_formatado(**dados):
    return f"Nome: {dados['nome']}\nIdade: {dados['idade']}\nCidade: {dados['cidade']}\n"


print(exibir_formatado(nome = 'Arthur' , idade = 18, cidade = 'SP'))