import random

class Jogo:
    def __init__(self,nome:str,dificuldade:int):
        self.nome = nome
        self.dificuldade = dificuldade
    def jogar(self):
        if self.dificuldade == 1:
            numPc = random.randint(1,10)
            numUser = None
            while numUser is None or numUser < 1 or numUser > 10:
                try:
                    numUser = int(input("Digite um número entre 1 e 10: "))
                except:
                    print("Erro")
            if numUser == numPc:
                return f"Parabéns {self.nome}, você acertou! O número era {numPc}."
            else:
                return f"Você errou, {self.nome}. O número era {numPc}."


        elif self.dificuldade == 2:
            numPc = random.randint(1,20)
            numUser = None
            while numUser is None or numUser < 1 or numUser > 20:
                try:
                    numUser = int(input("Digite um número entre 1 e 20: "))
                except:
                    print("Erro")
            if numUser == numPc:
                return f"Parabéns {self.nome}, você acertou! O número era {numPc}."
            else:
                return f"Você errou, {self.nome}. O número era {numPc}."

        elif self.dificuldade == 3:
            numPc = random.randint(1,50)
            numUser = None
            while numUser is None or numUser < 1 or numUser > 50:
                try:
                    numUser = int(input("Digite um número entre 1 e 50: "))
                except:
                    print("Erro")
            if numUser == numPc:
                return f"Parabéns {self.nome}, você acertou! O número era {numPc}."
            else:
                return f"Você errou, {self.nome}. O número era {numPc}."
        else:
            print("Número não existe nesse jogo!!")

jog1 = Jogo('Arthur', 3)
print(jog1.jogar())