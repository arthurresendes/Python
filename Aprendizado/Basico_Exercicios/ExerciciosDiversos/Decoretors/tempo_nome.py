import datetime
from functools import wraps

def recebe(func):
    @wraps(func)
    def wrapper():
        data_e_hora_atuais = datetime.datetime.now()
        print(data_e_hora_atuais)
        return func()
    return wrapper

@recebe
def ve_nome():
    return 'oi'

print(ve_nome.__name__)
print(ve_nome())