import time

gen_inicio = time.time()
print(sum(num for num in range(100000)))

gen_tempo = time.time() - gen_inicio

li_inicio = time.time()

print(sum([num for num in range(100000)]))

li_tempo = time.time() - li_inicio

print(gen_tempo)
print(li_tempo)