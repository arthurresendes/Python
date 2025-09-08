from typing import Optional

def saudacao_opcional(nome:Optional[str]= None) -> str:
    if nome:
        return f"Olá {nome}"
    else:
        return "Ola visitante"

print(saudacao_opcional("Arthur"))
print(saudacao_opcional())