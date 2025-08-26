def verifica_usuario(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper



@verifica_usuario
def painel(usuario):
    if usuario != 'admin':
            print("Acesso negado!")
    else:
        print(f"Bem-vindo ao painel, {usuario}")

painel("Admin".lower())
