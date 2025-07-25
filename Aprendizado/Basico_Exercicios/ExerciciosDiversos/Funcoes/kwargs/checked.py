def tem_chave(**kwargs):
    if kwargs.get('nome'):
        return True
    else: 
        return False

print(tem_chave(nome = 'Arthur'))
print(tem_chave(idade = 18))