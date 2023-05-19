class Sakinys:
    def __init__(self, zodis="LABAS vakaras", skaicius=1):
        self.skaicius = skaicius
        self.zodis = zodis

    def atbulas_zodis(self):
        atbulas = self.zodis[::-1]  # jei parasai tik zodi meta kl aida
        # print(atbulas)
        return atbulas

    # 2 dalis
    def mazosiomis_raidemis(self):
        mazosiomis = self.zodis.lower()  # jei parasai tik zodi meta kl aida
        return mazosiomis

    # trecia dalis

    def didziosiom_raidemis(self):
        didziosios = self.zodis.upper()  # jei parasai tik zodi be self meta kl aida
        # print(atbulas)
        return didziosios

    def zodzio_nr(self):
        tekstas_zodis = self.zodis.split()
        return tekstas_zodis[self.skaicius]

    # class simboliai_zodziai:
    #     def __init__(self, textas):
    #        self.textas = textas
    def zodzio_nr(self):
        tekstas_zodis = self.zodis.split()
        zodziu_kiekis = len(tekstas_zodis)
        simboliu_kiekis = len(self.zodis)
        return zodziu_kiekis, simboliu_kiekis

    def pakeisti_zodi(self, senas_zodis, naujas_zodis):
        pakeistas_zodis = self.zodis.replace(senas_zodis, naujas_zodis)
        return pakeistas_zodis

    def analize(self):
        zodziu_kiekis = len(self.zodis.split())
        didziuju = 0
        mazuju = 0
        skaiciu = 0
        for x in self.zodis:
            if x.isupper():
                didziuju += 1
            if x.islower():
                mazuju += 1
            if x.isdigit():
                skaiciu += 1
        return zodziu_kiekis, didziuju, mazuju, skaiciu


issaukimas = Sakinys()
print(issaukimas.atbulas_zodis())
print(issaukimas.mazosiomis_raidemis())
print(issaukimas.didziosiom_raidemis())
print(issaukimas.zodzio_nr())
print(issaukimas.pakeisti_zodi("vakaras", "rytas"))
print(issaukimas.analize())
