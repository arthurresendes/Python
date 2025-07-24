def saudacao(nome, tempo='dia'):
    if tempo == 'dia':
        return f"Bom dia, {nome}"
    elif tempo == 'tarde':
        return f"Boa tarde, {nome}"
    else:
        return f"Boa noite, {nome}"
    
print(saudacao("Arthur"))
print(saudacao("Arthur" , 'tarde'))
print(saudacao("Arthur" , 'noite'))