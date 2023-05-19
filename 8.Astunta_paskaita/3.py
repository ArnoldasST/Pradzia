sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

suma = 0
for x in sarasas:
    if type(x) == int or type(x) == float:
        suma += x
print(suma)

for x in sarasas:
    if type(x) == str:
        print(x)

for x in sarasas:
    if type(x) == bool:
        print(x)
