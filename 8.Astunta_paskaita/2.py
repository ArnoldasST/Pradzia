from statistics import mean, median

sarasas = list(range(51))
print(sarasas)

naujas = map(lambda x: x * 10, sarasas)
print(list(naujas))

naujas2 = filter(lambda x: x % 7 == 0, sarasas)
print(list(naujas2))

naujas3 = map(lambda x: x ** 2, sarasas)
print(list(naujas3))

naujas3 = map(lambda x: x ** 2, sarasas)
print(sum(list(naujas3)))
naujas3 = map(lambda x: x ** 2, sarasas)
print(min(list(naujas3)))
naujas3 = map(lambda x: x ** 2, sarasas)
print(max(list(naujas3)))
naujas3 = map(lambda x: x ** 2, sarasas)
print(mean(list(naujas3)))
naujas3 = map(lambda x: x ** 2, sarasas)
print(median(list(naujas3)))
atbulai = map(lambda x: x ** 2, reversed(sarasas))
print(list(atbulai))
