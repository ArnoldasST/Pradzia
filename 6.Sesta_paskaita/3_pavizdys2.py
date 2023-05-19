class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


class Biudzetas:
    def __init__(self):
        self.pajamu_irasai = []
        self.islaidu_irasai = []

    def ivesti_pajamas(self, suma, siuntejas, papildoma_informacija):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.pajamu_irasai.append(pajamu_irasas)
        print("Pajamos sėkmingai įvestos.")

    def ivesti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.islaidu_irasai.append(islaidu_irasas)
        print("Išlaidos sėkmingai įvestos.")

    def gauti_balansa(self):
        pajamu_suma = sum(irasas.suma for irasas in self.pajamu_irasai)
        islaidu_suma = sum(irasas.suma for irasas in self.islaidu_irasai)
        balansas = pajamu_suma - islaidu_suma
        return balansas

    def gauti_ataskaita(self):
        print("Pajamų įrašai:")
        for irasas in self.pajamu_irasai:
            print("Suma:", irasas.suma)
            print("Siuntėjas:", irasas.siuntejas)
            print("Papildoma informacija:", irasas.papildoma_informacija)
            print("-----------------")
        print("Išlaidų įrašai:")
        for irasas in self.islaidu_irasai:
            print("Suma:", irasas.suma)
            print("Atsiskaitymo būdas:", irasas.atsiskaitymo_budas)
            print("Įsigyta prekė/paslauga:", irasas.isigyta_preke_paslauga)
            print("-----------------")


def rodyti_menu():
    print("MINIBIUDŽETO PROGRAMA")
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Parodyti balansą")
    print("4. Parodyti biudžeto ataskaitą")
    print("5. Išeiti")


biudzetas = Biudzetas()

while True:
    rodyti_menu()
    pasirinkimas = input("Pasirinkite veiksmą (įveskite skaičių nuo 1 iki 5): ")

    if pasirinkimas == "1":
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_informacija = input("Įveskite papildomą informaciją: ")
        biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija)
    elif pasirinkimas == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įveskite įsigytą prekę/paslaugą: ")
        biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    elif pasirinkimas == "3":
        balansas = biudzetas.gauti_balansa()
        print("Balansas: ", balansas)
    elif pasirinkimas == "4":
        biudzetas.gauti_ataskaita()
    elif pasirinkimas == "5":
        print("Programa baigė darbą.")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
