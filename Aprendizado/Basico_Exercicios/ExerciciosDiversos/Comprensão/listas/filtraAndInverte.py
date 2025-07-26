lista = ["arthur", "pedro", "isac"]
print([inversao for inversao in lista if len(inversao) > 4])
print([inversao[::-1] for inversao in lista if len(inversao) > 4])