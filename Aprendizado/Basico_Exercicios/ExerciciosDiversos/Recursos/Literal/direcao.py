from typing import Literal

def direcao(direc: Literal['norte', 'sul', 'leste', 'oeste']) -> str:
    return f"Você esta na direção {direc}"

print(direcao('norte'))