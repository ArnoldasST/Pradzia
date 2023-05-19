import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    def paskaiciuotos_dienos(self):
        dabar = datetime.datetime.today()
        pradzia = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        skirtumas = (dabar - pradzia).days
        return skirtumas

    def paskaiciuoti_atlyginima(self):
        dienu_skaicius = self.paskaiciuotos_dienos()
        pinigai = dienu_skaicius * 8 * self.valandos_ikainis
        return pinigai


class NormalusDarbuotojas(Darbuotojas):
    def paskaiciuotos_dienos(self):
        dabar = datetime.datetime.today()
        pradzia = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        skirtumas = (dabar - pradzia).days // 7 * 5
        return skirtumas


darbuotojas = Darbuotojas("Arnoldas", 10, "2023-01-01")
normalusdarbuotojas = NormalusDarbuotojas("Arnoldas", 10, "2023-01-01")
print(darbuotojas.vardas, darbuotojas.valandos_ikainis, darbuotojas.dirba_nuo)
print("Darbuotojas gaus ", darbuotojas.paskaiciuoti_atlyginima(), "pinigu")
print("normalus Darbuotojas gaus ", normalusdarbuotojas.paskaiciuoti_atlyginima(), "pinigu")
