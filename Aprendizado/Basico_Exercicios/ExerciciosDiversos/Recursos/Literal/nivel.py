from typing import Literal

def nivel(nl: Literal['iniciante', 'intermediario', 'avançado']) -> str:
    return f"Seu nível é {nl}"

print(nivel('iniciante'))