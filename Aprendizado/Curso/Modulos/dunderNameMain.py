'''
Dunder name -> __name__
Dunder main -> "__main__"

Em py são utilizados dunder para criar funções , atributos , propriedades , etc

Main eh o arquivo principal , porém se algum arquivo for importado o nome do arquivo sera o novo __main__

Quando você roda um arquivo diretamente, o Python define __name__ como "__main__".
Isso significa: "Eu sou o arquivo principal da execução" → então o código dentro do if __name__ == "__main__": é executado.

Quando você importa um arquivo, o __name__ vira o nome do módulo ("util", "meu_pacote.jogo", etc.).
Nesse caso, o código dentro do if __name__ == "__main__": não é executado, só o que está fora dele.

Isso seria como um int main do C , onde eh executado o programa principal
if __name__ == "__main__":

'''

def impar(*n):
    resultados = []
    for num in n:
        if num % 2 == 1:
            resultados.append(f"{num} é ímpar")
        else:
            resultados.append(f"{num} não é ímpar")
    return resultados

if __name__ == "__main__":
    print(impar(3, 4, 5))