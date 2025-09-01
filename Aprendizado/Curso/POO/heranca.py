'''
Herança em Python

Classe - Molde do objeto do mundo real , exemplo: carro , caixa , pessoa,etc
Objeto - Instancia da classe , variavel que recebe a classe , ex : p1 = Pessoa()
Instancia - Ato de criar um objeto a partir de uma classe , ex : p1 = Pessoa('Arthur', 18)
Atributos/Propriedades - Caracteristicas do objeto , ex: Carro tem porta , cor , marca , modelo , etc
Metodos - Ação de tal classe separadas por função, ex: Carro tem acelerar , freiar , trocar marcha , etc
Metodo construtor - __init__()
getter - Metodo para obter o valor do atributo
setter - Metodo para mudar valor do atributo 

Herança permite que uma classe filha receba atributos de uma classe pai.Assim , a classe filha herda os atributos e metodos da classe pai , podendo adicionar novos atributos e metodos ou sobrescrever metodos existentes

'''

class Pessoa:
    def __init__(self, nome,sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f" {self.__nome} + ' ' + {self.__sobrenome}"

class Cliente(Pessoa):
    def __init__(self, nome,sobrenome, cpf, renda):
        super().__init(nome,sobrenome,cpf)
        self.__renda= renda   

    def nome_completo(self):
        return f" {self.__nome} + ' ' + {self.__sobrenome}"

class Funcionario(Pessoa):
    def __init__(self, nome,sobrenome, cpf, matricula):
        super().__init(nome,sobrenome,cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f" {self.__nome} + ' ' + {self.__sobrenome}"


