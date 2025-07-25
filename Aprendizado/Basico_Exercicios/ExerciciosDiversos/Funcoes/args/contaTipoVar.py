def conta_tipo(*valores):
    qtdString = 0
    qtdInt = 0
    qtdFloat = 0    
    
    for valor in valores:
        if isinstance(valor,int):
            qtdInt += 1
        elif isinstance(valor,float):
            qtdFloat += 1
        elif isinstance(valor, str):
            qtdString +=1
    return f"Inteiros: {qtdInt}, Floats: {qtdFloat}, Strings: {qtdString}"

print(conta_tipo("Ola",1,2,3.5,4.2,1,2,"Oi"))