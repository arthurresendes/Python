class Playlist:
    def __init__(self , nome):
        self.musicas = []
        self.nome = nome
    
    def adicionar_musica(self , musica : str):
        self.musicas.append(musica)
    
    def remover_music(self, musica: str):
        if musica in self.musicas:
            self.musicas.remove(musica)
    
    def mostra_playlist(self):
        print(f"Playlist do {self.nome}: ")
        for i in self.musicas:
            print(i)

p1 = Playlist('Arthur')
p1.adicionar_musica('Miss me')
p1.adicionar_musica('Let it hapen')
p1.remover_music('Miss me')
p1.mostra_playlist()