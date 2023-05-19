class Sakinys:
    def __init__(self, tekstas, ):
        self.tekstas = tekstas

    def zodziu_skaicius(self, skaicius):
        print(self.tekstas.count(skaicius))

    def pakeisti_simbolius(self, senas, naujas):
        self.tekstas = "".join(self.tekstas).replace(senas, naujas)
        print(self.tekstas)

kintamasis = Sakinys("Ar turite skaniu obuoliu?")
print(kintamasis.tekstas)
kintamasis.zodziu_skaicius(" ")
kintamasis.pakeisti_simbolius("t", "o")
