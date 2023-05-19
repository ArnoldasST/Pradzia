import datetime


def praejes_laikas(data):
    dabar = datetime.datetime.now()
    prabeges_laikas = dabar - data

    metai = prabeges_laikas.days // 365
    menesiai = (prabeges_laikas.days - metai * 365) // 30
    dienos = prabeges_laikas.days - metai * 365 - menesiai * 30
    valandos = prabeges_laikas.total_seconds() // 3600
    minutes = (prabeges_laikas.total_seconds() - valandos * 3600) // 60
    sekundes = prabeges_laikas.total_seconds() - valandos * 3600 - minutes * 60

    print(
        f'{metai} metai, {menesiai} menesiai, {dienos} dienos, {valandos} valandos, {minutes} minutes, {sekundes} sekundes praejo nuo {data}')


data = datetime.datetime(2020, 2, 3, 10, 10, 10)
praejes_laikas(data)