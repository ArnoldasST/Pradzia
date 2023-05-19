from operator import attrgetter


class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f"({self.vardas}, {self.amzius})"


zmogus1 = Zmogus("Petras", 30)
zmogus2 = Zmogus("Jonas", 40)
zmogus3 = Zmogus("Jurate", 72)
zmogus4 = Zmogus("Agne", 25)

sarasas = [zmogus1, zmogus2, zmogus3, zmogus4]


def rusiavimas(vardas):
    return vardas.vardas


surusiuotas = sorted(sarasas, key=rusiavimas)
print(surusiuotas)
print(surusiuotas[::-1])


def rusiavimas1(amzius):
    return amzius.amzius


print("-----------------------------------------------------")

suvarduotas = sorted(sarasas, key=rusiavimas1)
print(suvarduotas)
print(suvarduotas[::-1])
print("-----------------------------------------------------")
surusiuotas2 = sorted(sarasas, key=attrgetter("vardas"))
print(surusiuotas2)
suvarduotas2 = sorted(sarasas, key=attrgetter("amzius"))
print(suvarduotas2)