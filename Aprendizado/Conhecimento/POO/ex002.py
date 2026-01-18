class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    def adicionar_nota(self,nota):
        self.notas.append(nota)
    def remover_nota(self):
        for i in self.notas:
            print(i)
        nota_retirada = int(input("Qual nota quer tirar: "))
        for i in self.notas:
            if i == nota_retirada:
                self.notas.remove(i)

    def media(self):
        soma = 0
        for i in self.notas:
            soma += i
        media = soma/len(self.notas)
        return f"Media: {media}"

al1 = Aluno('Arthur', 12345)
al1.adicionar_nota(10)
al1.adicionar_nota(8)
al1.adicionar_nota(6)
al1.remover_nota()
print(al1.media())
