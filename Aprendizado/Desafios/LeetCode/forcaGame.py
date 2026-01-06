class Solution:
    def forcaGame(self) -> None:
        import random
        palavras_nivel = {1:['Casa','Bola','Gato'],2:['Janela','Cadeira','Escola'],3:['Enigma','Labirinto','Quimera']}
        
        while True:
            try:
                nivel = int(input("Escolha o nível da palavra:\n1-Fácil\n2-Médio\n3-Dificil\n:"))
                if nivel < 4 and nivel > 0:
                    break
            except:
                print("Digite o numero de 1 até 3!!")
        
        lista_palavra = palavras_nivel[nivel]
        palavra_aleatoria = random.choice(lista_palavra).lower()
        
        vida = 5
        lista_letras = []
        while True:
            letra = input("Digite uma letra: ").lower()
            if letra not in palavra_aleatoria:
                vida = vida - 1
                print("Você errou !!")
            else:
                print(f"Parabens a letras {letra} esta na palavra")
                lista_letras.append(letra)
            for i in palavra_aleatoria:
                if i in lista_letras:
                    print(i,end='')
                else:
                    print("_", end='')
            
            print(f"\nVidas: {vida}")
            if vida == 0:
                print(f"Perdeu o jogo, a palavra era: {palavra_aleatoria.title()}")
                break
            
            if all(letra.lower() in [l.lower() for l in lista_letras] for letra in palavra_aleatoria):
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_aleatoria.title()}")
                break

if __name__ == "__main__":
    solucao = Solution()
    solucao.forcaGame()