palavra = input("Digite uma palavra: ").lower()
# Vai filtrar se tiver vogal não passa
sem_vogais = [letra for letra in palavra if letra not in "aeiou"]