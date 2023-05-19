import pickle

sarasas = []
pajamos = []
islaidos = []
balansas = 0
with open("a.pkl", "ab") as pickle_fail:
    while True:
        try:
            skaicius = int(input("Įveskite skaičių: \njei pajamos teigiamas skaičius\njei neigiamos su minuso ženklu"))
            balansas += skaicius
            sarasas.append(skaicius)
            print("sąskaitos likutis", balansas)  ## iki čia pildo pickle failą
        except ValueError:
            pickle.dump(sarasas, pickle_fail)
        break

with open("a.pkl", "rb") as pickle_fail:  ## nuo čia iš failo spausdina
    while True:
        try:
            print(pickle.load(pickle_fail))
        except EOFError:
            break
