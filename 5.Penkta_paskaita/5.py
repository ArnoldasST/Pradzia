class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas}: {self.suma}"


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas("Išlaidos", suma)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            if irasas.tipas == "Išlaidos":
                suma -= irasas.suma
        print(f"{suma:.2f}")

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(f"{irasas.tipas}: {irasas.suma}")


def menu():
    while True:
        pasirinkimas = int(input(
            "1 - Įvesti pajamas, \n2 - Įvesti išlaidas, \n3 - Parodyti balansą, \n4 - Pajamų/išlaidų ataskaita, \n5 - Baigti "))
        if pasirinkimas == 1:
            suma = float(input("Įveskite pajamų sumą: "))
            print(suma)
            biudzetas.prideti_pajamu_irasa(suma)
        if pasirinkimas == 2:
            suma = float(input("Įveskite išlaidų sumą: "))
            print(suma)
            biudzetas.prideti_islaidu_irasa(suma)
        if pasirinkimas == 3:
            biudzetas.gauti_balansą()
        if pasirinkimas == 4:
            biudzetas.parodyti_ataskaita()
        if pasirinkimas == 5:
            print("Viso gero!")
            break


biudzetas = Biudzetas()
menu()
