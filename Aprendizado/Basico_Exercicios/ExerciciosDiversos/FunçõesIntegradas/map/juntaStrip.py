nomes = ["arthur", "maria", "joão"]
sobrenomes = ["resende", "silva", "oliveira"]

junta = map(lambda n, s: n.strip().title() + " " + s.strip().title(), nomes, sobrenomes)

print(list(junta))