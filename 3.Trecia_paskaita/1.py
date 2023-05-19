import datetime

pradzios_data = input("iveskite pradzios data (MMMM-MM-DD HH:MM:SS) ")
pabaigos_data = input("iveskite pabaigos data (MMMM-MM-DD HH:MM:SS) ")

data1 = datetime.datetime.strptime(pradzios_data, "%Y-%m-%d %H:%M:%S")
data2 = datetime.datetime.strptime(pabaigos_data, "%Y-%m-%d %H:%M:%S")

skirtumas = (data2 - data1)
print("laiko skirtumas tarp datu sekundemis - ", skirtumas.total_seconds())