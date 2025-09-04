def soma_inteiros(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return 'Erro'

print(soma_inteiros(1,2))
print(soma_inteiros('1',2))