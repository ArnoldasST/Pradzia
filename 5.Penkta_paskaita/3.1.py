import datetime


class Sukaktis:
    def __init__(self, metai=1974, menesis=6, diena=17, valanda=0, minute=0, sekunde=0):
        self.data = datetime.datetime(metai, menesis, diena, valanda, minute, sekunde)

    def kiek_laiko_praejo(self):
        # sukaktuviu_data = input("iveskite sukaktuviu data" "(Pvz. 2000-01-01)")
        # sukaktuviu_data_dt = datetime.datetime.strptime(sukaktuviu_data, "%Y-%m-%d")
        dabartine_data = datetime.datetime.now()
        skirtumas = dabartine_data - self.data
        print(skirtumas)
        print("Praejo ", round(skirtumas.days / 365), " m.")
        print("Praejo ", round(skirtumas.days / 30), " mėn.")
        print("Praejo ", skirtumas.days, " d.")
        print("Praejo ", round(skirtumas.total_seconds() / 3600), " val.")
        print("Praejo ", round(skirtumas.total_seconds() / 60), " min.")
        print("Praejo ", round(skirtumas.total_seconds()), " s.")
        return skirtumas

    def ar_metai_keliamieji(self):
        metai = self.data.year
        if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
            print('Keliamieji metai')
        else:
            print('Nekelemieji metai')

    def atimti(self, dienos):
        nauja_data = self.data - datetime.timedelta(days=dienos)
        print(nauja_data)

    def prideti(self, dienos):
        nauja_data = self.data + datetime.timedelta(days=dienos)
        print(nauja_data)


sukaktis = Sukaktis()
sukaktis.kiek_laiko_praejo()
sukaktis.ar_metai_keliamieji()
sukaktis.atimti(10)
sukaktis.prideti(10)
