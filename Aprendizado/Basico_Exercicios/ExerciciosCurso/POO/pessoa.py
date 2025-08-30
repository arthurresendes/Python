class Pessoa:
    def __init__(self,nome,idade,email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
    
    @property
    def ve_info(self):
        return f"Nome: {self.__nome}\nIdade: {self.__idade}\nEmail: {self.__email}"

    @ve_info.setter
    def ve_info(self,novo_email):
        self.__email = novo_email
        return self.__email
p1 = Pessoa('Arthur', 18 ,'arg@gmail.com')
print(p1.ve_info)

p1.ve_info = "arthur.novo@email.com"  # Setter → muda o email
print(p1.ve_info)

# O metodo getter serve para ver informações privadas chamando o property para ver , já o setter serve para alterar essas informações privadas.