import datetime

ivesta_data = input("iveskite norima data ir laika (PVZ: MMMM-MM-DD HH:MM:SS) ")
data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
now = datetime.datetime.today()
skirtumas = now - data
metai = round(skirtumas.days / 365)
print("praeje metai nuo pasirinktos datos -", metai)
menesiai = round(skirtumas.days / 30)
print("praeje menesiai nuo pasirinktos datos -", menesiai)
print("praejusios dienos nuo pasirinktos datos -", skirtumas.days)
hours = round(skirtumas.total_seconds() / 3600)
print("praejusios valandos nuo pasirinktos datos -", hours)
minutes = round(skirtumas.total_seconds() / 60)
print("praejusios minutes nuo pasirinktos datos -", minutes)
print("praejusios sekundes nuo pasirinktos datos -", round(skirtumas.total_seconds()))