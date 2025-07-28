# Strip remove espaços em branco de uma string e o title deixa a primeira maiuscula e arruma o resto
nomeCompleto = lambda x, y : x.strip().title() + ' ' + y.strip().title()

print(nomeCompleto('  arthur  ' , ' resendE '))