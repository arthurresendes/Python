def saudacao_personalizada(**kwargs):
    return kwargs


print(saudacao_personalizada(
    nomes=['Arthur', 'José'],
    idades=(18, 20),
    cidade='Osasco',
    estado='SP'
))