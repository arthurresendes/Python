from typing import Union

def converte(palavra) -> Union[str | float]:
    if isinstance(palavra, str):
        return float(palavra)
    elif isinstance(palavra, float):
        return str(palavra)
    else:
        raise ValueError("Erro")

var1 = converte("5")
var2 = converte(5.5)
print(var1)
print(type(var1))
print(var2)
print(type(var2))
#print(converte("a"))