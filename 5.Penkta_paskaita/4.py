class Sakinys:
    def __init__(self, tekstas):
        self.tekstas1 = tekstas

    def atbulai(self):
        return self.tekstas1[::-1]

    def mazosios(self):
        return self.tekstas1.lower()

    def didziosios(self):
        return self.tekstas1.upper()

    def pasirinktas_zodis(self):
        zodis = self.tekstas1.split()
        zodis1 = zodis[1]
        return zodis1

    def simboliai(self):
        zodis = self.tekstas1.split()
        zodis1 = len(zodis)

        zodis2 = self.tekstas1
        zodis3 = len(zodis2)
        return zodis1, zodis3

    def kiekis(self):
        kiekis = self.tekstas1
        for x in kiekis:
            x = kiekis.count(' ') + 1

        countl = 0
        countu = 0
        countn = 0

        for b in kiekis:
            if (b.islower()):
                countl = countl + 1
            elif (b.isupper()):
                countu = countu + 1
            elif (b.isdigit()):
                countn = countn + 1

        return x, countl, countu, countn

    def pakeist(self):
        pakeist = self.tekstas1
        pakeist1 = pakeist.replace('visi!', 'nevisi!')

        pakeist2 = pakeist1.replace('v', 'w')
        return pakeist1, pakeist2

    def __repr__(self):
        return f'{self.sakinys1}'


sakinys1 = Sakinys('Sveiki visi!')
print(sakinys1.atbulai())
print(sakinys1.mazosios())
print(sakinys1.didziosios())
print(sakinys1.pasirinktas_zodis())
print(sakinys1.simboliai())
print(sakinys1.kiekis())
print(sakinys1.pakeist())
print(sakinys1)
