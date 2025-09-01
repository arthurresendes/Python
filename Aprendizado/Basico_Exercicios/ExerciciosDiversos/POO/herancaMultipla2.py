class Rock:
    def tocar(self):
        return f"Tocando rock"

class Jazz:
    def tocar(self):
        return f"Tocando Jazz"

class Fusion(Rock,Jazz):
    def tocar(self):
        return f"Tocando rock e Jazz junto"

musica1 = Fusion()
musica2 = Rock()
musica3 = Jazz()
print(musica1.tocar())
print(musica2.tocar())
print(musica3.tocar())