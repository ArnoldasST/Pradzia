class Irasas:
    def __init__(self, tipas, suma):
        self.suma = suma
        self.tipas = tipas

    def __str__(self):
        return f"suma: {self.suma}, tipas: {self.tipas}"


class PajamuIrasas(Irasas):
    def __init__(self, tipas, suma, siuntejas, papildoma_informacija):
        super().__init__(tipas, suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def siuntejas(self):
        self.siuntejas = siuntejas
        input("Siuntejas: ")

    def papildoma_informacija(self):
        self.papildoma_informacija = papildoma_informacija
        input("Papildoma informacija: ")

    def __str__(self):
        return f"Suma: {self.suma}, tipas: {self.tipas}, siuntejas: {self.siuntejas}, papildoma informacija:" \
               f" {self.papildoma_informacija}"


class IslaiduIrasas(Irasas):
    def __init__(self, tipas, suma, isigyta_preke_paslauga, atsiskaitymo_budas):
        super().__init__(tipas, suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def atsiskaitymo_budas(self):
        self.atsiskaitymo_budas = atsiskaitymo_budas
        input("Atsiskaitymo budas: ", )

    def isigyta_preke_paslauga(self):
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        input("Isigyta preke/paslauga: ")

    def __str__(self):
        return f"Suma: {self.suma}, tipas: {self.tipas}, atsiskaitymo budas: {self.atsiskaitymo_budas}, isigyta preke" \
               f"/paslauga: {self.isigyta_preke_paslauga}"


biudzetas = []
irasas1 = PajamuIrasas
irasas2 = IslaiduIrasas
biudzetas.append(irasas1)
biudzetas.append(irasas2)
pajamu_skaiciai = []
islaidu_skaiciai = []
while True:
    pasirinkimas = int(input("Pasirinkite:\n1 - Ivesti pajamas\n2 - Ivesti islaidas\n3 - Pajamu/islaidu balansas\n4 - "
                             "Biudzeto ataskaita\n5 - Patikrinti biudzeto likuti\n6 - Iseiti is programos"
                             "\nPasirinkimas: "))
    if pasirinkimas == 1:
        suma = int(input("Iveskite suma: "))
        tipas = input("Iveskite pajamos tipa: ")
        siuntejas = input("Siuntejas: ")
        papildoma_informacija = input("Papildoma informacija: ")
        pajama = PajamuIrasas(tipas, suma, siuntejas, papildoma_informacija)
        biudzetas.append(pajama)
        pajamu_skaiciai.append(suma)
    if pasirinkimas == 2:
        suma = int(input("Iveskite suma: "))
        tipas = input("Iveskite islaidos tipa: ")
        isigyta_preke_paslauga = input("Isigyta preke/paslauga: ")
        atsiskaitymo_budas = input("Atsiskaitymo budas: ")
        islaida = IslaiduIrasas(tipas, suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        biudzetas.append(islaida)
        islaidu_skaiciai.append(suma)
    if pasirinkimas == 3:
        pasirinkimas2 = int(input(f"Pasirinkite:\n1 - Pajamu balansas:\n2 - Islaidu balansas:\nPasirinkimas: "))
        if pasirinkimas2 == 1:
            print(f"Jusu pajamu balansas yra:\n {sum(pajamu_skaiciai)}")
        if pasirinkimas2 == 2:
            print(f"Jusu islaidu balansas yra:\n {sum(islaidu_skaiciai)}")
    if pasirinkimas == 4:
        print("Jusu biudzeto ataskaita:")
        print(f"Bendras pajamu balansas:\n {sum(pajamu_skaiciai)}")
        for x in biudzetas:
            if isinstance(x, PajamuIrasas):
                print(x)
        print("Cia yra pajamos.")
        print("---------------------")
        print(f"Bendras islaidu balansas:\n {sum(islaidu_skaiciai)}")
        for x in biudzetas:
            if isinstance(x, IslaiduIrasas):
                print(x)
        print("Cia yra islaidos.")
        print("---------------------")
        print(f"Jums liko:\n {sum(pajamu_skaiciai) - sum(islaidu_skaiciai)} Eur.")
    if pasirinkimas == 5:
        print(f"Jums liko:\n {sum(pajamu_skaiciai) - sum(islaidu_skaiciai)} Eur.")
    if pasirinkimas == 6:
        print("Programa baigiasi.")
        break
