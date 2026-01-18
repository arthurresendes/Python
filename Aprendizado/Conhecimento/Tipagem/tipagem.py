"""
Usando para definir os tipos de dados

"""

def cumprimentar(nome: str) -> str:
    return f"Ola {nome}"

print(cumprimentar("Arthur"))

def cabecalho(texto: str, alinhamento: bool = False) -> str:
    if alinhamento:
        return f"{texto.title()}\n {'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, '-')

print(cabecalho("Arthur Resende"))