class Animal:
    def __init__(self, quantidade_patas: int,raca: str, tamanho_cm: int):
        self._quantidade_patas = quantidade_patas
        self._raca = raca            
        self._tamanho_cm = tamanho_cm

    def emitir_som(self):
        print("Animal base")

    def get_quantidade_patas(self):
        return self._quantidade_patas

    def get_raca(self):
        return self._raca

    def get_tamanho_cm(self):
        return self._tamanho_cm


class Cachorro(Animal):
    def __init__(self, quantidade_patas:int, raca:str, tamanho_cm:int, nome: str):
        super().__init__(quantidade_patas,raca, tamanho_cm)
        self._nome = nome              

    def emitir_som(self):
        print("Au au!")

    def get_nome(self):
        return self._nome
   
    def setCentimetros(self,new_height: int):
        self._tamanho_cm = new_height


if __name__ == "__main__":
    cachorro1 = Cachorro(4, "Labrador", 60, "Rex")

    print("Nome:", cachorro1.get_nome())
    print("Raça:", cachorro1.get_raca())
    print("Tamanho (cm):", cachorro1.get_tamanho_cm())
    cachorro1.setCentimetros(70)
    print("Tamanho (cm) atualizado:", cachorro1.get_tamanho_cm())
    print("Quantidade de patas:", cachorro1.get_quantidade_patas())

    cachorro1.emitir_som()