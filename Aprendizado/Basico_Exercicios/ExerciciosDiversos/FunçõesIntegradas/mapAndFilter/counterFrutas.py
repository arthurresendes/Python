from collections import Counter as cd
palavras = ["maçã", "pera", "uva", "kiwi", "banana"]

result = list(map(lambda n : cd(n) , filter(lambda n : 'a' in n, palavras)))
print(result)