def comer(comida, saudavel: bool):
    if saudavel:
        return f"Estou comendo {comida} porque é saudavel"
    else:
        return f"Estou comendo {comida} porque quero viver"

def dormir(horas: int):
    if horas < 8:
        return "Estou dormindo pouco"
    else:
        return "Estou dormindo muito"
