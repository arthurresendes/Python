matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

todos_maiores_que_zero = all(all(n > 0 for n in linha) for linha in matriz)

print(todos_maiores_que_zero)