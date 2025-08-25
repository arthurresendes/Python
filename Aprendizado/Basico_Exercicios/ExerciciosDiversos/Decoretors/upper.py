def maiusculo(func):
    def wrapper():
        print("Transformando em upper")
        result = func().upper()
        return result
    return wrapper


@maiusculo
def nome():
    return "arthur"

print(nome())