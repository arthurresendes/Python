def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

lista = [1,2,3,4,5,6]
nome = 'Arthur Resende'
meu_for(lista)
meu_for(nome)

