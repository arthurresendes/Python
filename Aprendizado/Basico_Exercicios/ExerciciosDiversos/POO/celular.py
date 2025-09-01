class Computador:
    def ligar(self):
        return f'Ligando computador'

class Telefone:
    def ligar(self):
        return f'Ligando telefone'

class Smartphone(Computador, Telefone):
    def ligar(self):
        return f'Ligando smartphone'

celular = Smartphone()
print(celular.ligar())