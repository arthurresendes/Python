from collections import deque

# Criando um deque vazio

meu_deque = deque()

# Adicionando elementos
meu_deque.append(1)  # Adiciona no final
meu_deque.appendleft(2) # Adiciona no inicio
meu_deque.extend([3, 4, 5]) # Adiciona varios elementos no final
meu_deque.extendleft([6, 7, 8]) # Adiciona varios elementos no inicio
print(meu_deque)  # Saída: deque([8, 7, 6, 2, 1, 3, 4, 5])

# Removendo elementos
meu_deque.pop()   # Remove o último elemento
meu_deque.popleft() # Remove o primeiro elemento
print(meu_deque)  # Saída: deque([7, 6, 2, 1, 3, 4])

# Outras operações
meu_deque.rotate(2) # Rotaciona para a direita
print(meu_deque) # Saída: deque([3, 4, 7, 6, 2, 1])

meu_deque.reverse() # Inverte a ordem dos elementos
print(meu_deque) # Saída: deque([1, 2, 6, 7, 4, 3])

meu_deque.clear() # Limpa o deque
print(meu_deque)  # Saída: deque([])