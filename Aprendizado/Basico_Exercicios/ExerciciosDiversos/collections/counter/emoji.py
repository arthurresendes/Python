from collections import Counter as ct

emocoes = ["😀", "😂", "🥲", "😎", "😢", "😡", "😴","😀", "🤯", "🥶", "😱"]


result = ct(emocoes)

print(result.most_common(1))