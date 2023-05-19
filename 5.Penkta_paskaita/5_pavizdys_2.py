class Minibiudzetas:
    def __init__(self):
        self.pajamos = 0
        self.islaidos = 0
        self.balansas = 0
        self.pajamu_irasai = []
        self.islaidu_irasai = []

    def ivesti_pajamas(self, suma):
        self.pajamos += suma
        self.balansas += suma
        self.pajamu_irasai.append(suma)
        print("Pajamos sėkmingai įvestos.")

    def ivesti_islaidas(self, suma):
        self.islaidos += suma
        self.balansas -= suma
        self.islaidu_irasai.append(suma)
        print("Išlaidos sėkmingai įvestos.")

    def parodyti_balansa(self):
        print("Pajamos: ", self.pajamos)
        print("Išlaidos: ", self.islaidos)
        print("Balansas: ", self.balansas)

    def parodyti_biudzeto_ataskaita(self):
        print("Pajamų įrašai:")
        for suma in self.pajamu_irasai:
            print(suma)
        print("Išlaidų įrašai:")
        for suma in self.islaidu_irasai:
            print(suma)

    def iseiti(self):
        print("Programa baigė darbą.")


def rodyti_menu():
    print("MINIBIUDŽETO PROGRAMA")
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Parodyti balansą")
    print("4. Parodyti biudžeto ataskaitą")
    print("5. Išeiti")


minibiudzetas = Minibiudzetas()

while True:
    rodyti_menu()
    pasirinkimas = input("Pasirinkite veiksmą (įveskite skaičių nuo 1 iki 5): ")

    if pasirinkimas == "1":
        suma = float(input("Įveskite pajamų sumą: "))
        minibiudzetas.ivesti_pajamas(suma)
    elif pasirinkimas == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        minibiudzetas.ivesti_islaidas(suma)
    elif pasirinkimas == "3":
        minibiudzetas.parodyti_balansa()
    elif pasirinkimas == "4":
        minibiudzetas.parodyti_biudzeto_ataskaita()
    elif pasirinkimas == "5":
        minibiudzetas.iseiti()
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
