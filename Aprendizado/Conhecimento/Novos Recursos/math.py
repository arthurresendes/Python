import math


# Vai multiplicando os valores
num1 = [2,3,4]
print(math.prod(num1))

# Raiz quadrada exata(sqrt) e arredondando com isqrt para valor não raiz exata
print(math.isqrt(17))
print(math.sqrt(9))

# Soma mais a diferença de um pro outro
p3d1 = (12,50,40)
p3d2 = (6,7,13)
print(math.dist(p3d1,p3d2))

import statistics
# media
numReal = [1,2,3,4,5,6,7,8,9,10]
print(statistics.fmean(numReal))

# moda
numModa = [1,2,3,4,6,1,2,3,1]
print(statistics.multimode(numModa))

#mediana
numMediana = [1,2,5]
print(statistics.median(numMediana))

