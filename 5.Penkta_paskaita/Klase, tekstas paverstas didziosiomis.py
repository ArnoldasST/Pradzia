class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def mazosios(self):
        self.tekstas = self.tekstas.upper()
        return self.tekstas


kintamasis = Sakinys("Ar turite obuoliu?")
print(kintamasis.tekstas)
print(kintamasis.mazosios())
