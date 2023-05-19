class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def zodis_eileje(self, eile):
        zodziai = self.tekstas.split()
        if eile > len(zodziai) or eile < 1:
            return None
        else:
            return zodziai[eile-1]


kintamasis = Sakinys("Ar turite skaniu obuoliu?")
print(kintamasis.tekstas)
print(kintamasis.zodis_eileje(2))
