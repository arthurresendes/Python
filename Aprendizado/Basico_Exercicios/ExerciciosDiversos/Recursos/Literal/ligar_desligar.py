from typing import Literal
def liga_desliga(metodo: Literal['on','off']) -> str:
    return f"Você esta {metodo}"

print(liga_desliga('on'))