def product(*produtosTotal):
    result = 1
    for prod in produtosTotal:
        result = result * prod
    return result

print(product(1,2,3,4,5))