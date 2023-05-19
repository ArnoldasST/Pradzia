class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas

    def vaziuoti(self):
        print("Vaziuoja")

    def stoveti(self):
        print("Priparkuota")

    def pilti_degalu(self):
        print("Degalai ipilti")


class Elektromobilis(Automobilis):
    def pilti_degalu(self):
        print("Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("Vaziuoja autonomiskai")


automobilis = Automobilis(2022, "Reno Twingo, ", "dyzelis")
print(automobilis.metai, automobilis.modelis, automobilis.kuro_tipas)

automobilis.vaziuoti()
automobilis.stoveti()
automobilis.pilti_degalu()

elektromobilis = Elektromobilis(2023, "Kia Sefija, ", "elektra")
print(elektromobilis.metai, elektromobilis.modelis, elektromobilis.kuro_tipas)

elektromobilis.vaziuoti()
elektromobilis.stoveti()
elektromobilis.pilti_degalu()
elektromobilis.vaziuoti_autonomiskai()
