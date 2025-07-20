estudantesIngles = {'Arthur', 'Alice' , 'Jose' , 'Pedro' , 'Maria' , 'Escobar'}
estudantesEspanhol = {'Arthur', 'Ana' , 'Josef' , 'Kauan' , 'Hector' , 'Lalo' , 'Escobar'}

ambos = estudantesIngles.intersection(estudantesEspanhol)
print("Ambos matriculados em, inglês e espanhol: ")
print(ambos)

soIngles = estudantesIngles.difference(estudantesEspanhol)
soEspanhol = estudantesEspanhol.difference(estudantesIngles)
print("Matriculados apenas em ingles: ")
print(soIngles)
print("Matriculados apenas em espanhol: ")
print(soEspanhol)

uniao = estudantesIngles.union(estudantesEspanhol)

print("União dos estudantes: ")
print(uniao)