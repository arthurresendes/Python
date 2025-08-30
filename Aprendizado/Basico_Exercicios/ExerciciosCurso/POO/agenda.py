class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contatos = []
    
    def aramzena_contato(self, contato: Contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} adicionado com sucesso!")
    def remover_contato(self, contato:Contato):
        if contato in self.contatos:
            self.contatos.remove(contato)
            print(f"Contato {contato.nome} removido com sucesso!")
        else:
            print("Contato não encontrado.")
    
    def busca(self, nome:str):
        for i , contato in enumerate(self.contatos):
            if contato.nome.lower() == nome.lower():
                return i
        return -1
    
    def imprimir_agenda(self):
        if not self.contatos:
            print("Sem contatos")
        else:
            for i in self.contatos:
                print(i)
    
    def imprimir_contato(self , indice : int):
        if 0 <= indice < len(self.contatos):
            print(self.contatos[indice])
        else:
            print("Índice inválido.")


c1 = Contato("Arthur", 999999, 'arg@gmail')

