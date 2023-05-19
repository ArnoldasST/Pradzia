class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def atbulai(self):
        print(self.tekstas[::-1])

    def mazosios(self):
        print(self.tekstas.lower())

    def didziosios(self):
        print(self.tekstas.upper())

    def zodis_eileje(self, eile):
        zodziai = self.tekstas.split()
        print(zodziai[eile - 1])

    def zodziu_skaicius(self, skaicius):
        print(self.tekstas.count(skaicius))

    def pakeisti_simbolius(self, senas, naujas):
        self.tekstas = "".join(self.tekstas).replace(senas, naujas)
        print(self.tekstas)




kintamasis = Sakinys("Ar turite obuoliu, o gal turite baranku?")
print(kintamasis.tekstas)
(kintamasis.atbulai())
(kintamasis.mazosios())
(kintamasis.didziosios())
(kintamasis.zodis_eileje(2))
(kintamasis.zodziu_skaicius("turite"))
(kintamasis.pakeisti_simbolius("b", "L"))
