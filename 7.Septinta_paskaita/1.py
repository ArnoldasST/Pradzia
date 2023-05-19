import os
import datetime

with open("failas.txt", "w") as failas:
    failas.write("Zen of Python\n")

with open("failas.txt", "r") as failas:
    print(failas.read())

with open("failas.txt", "a", encoding="utf-8") as failas:
    tekstas = "Beautiful is better than ugly."
    tekstas2 = "Gražu yra geriau nei bjauru.\n"
    tekstas3 = tekstas.replace(tekstas, tekstas2)
    failas.write(tekstas3)

with open("failas.txt", "a") as failas:
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S\n")
    failas.write(data)

with open("failas.txt", "r") as failas:
    naujas = ""
    skaicius = 1
    for eilute in failas:
        naujas += str(skaicius) + " " + eilute
        skaicius += 1
with open("failas.txt", "w") as failas:
    failas.write(naujas)

with open("failas.txt", "r", encoding="utf-8") as failas:
    atbulai = naujas[::-1]
    print(atbulai)

with open("failas.txt", "r", encoding="utf-8") as failas:
    
