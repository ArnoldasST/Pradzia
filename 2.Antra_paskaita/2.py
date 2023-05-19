skaiciu_sarasas = []
skaiciu_suma = 0
while True:
    ivestas = int(input("Įveskite skaičių "))
    if ivestas < 0:
        break
    else:
        skaiciu_sarasas.append(ivestas)
for suma in skaiciu_sarasas:
    skaiciu_suma += suma
print(skaiciu_suma)
print(skaiciu_sarasas)
