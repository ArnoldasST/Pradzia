def zodziu_skaicius(stringas):
    return len(stringas.split())


def didziosios(stringas):
    return sum(1 for x in stringas if x.isupper())


def mazosios(stringas):
    return sum(1 for x in stringas if x.islower())


def skaiciai(stringas):
    return sum(1 for x in stringas if x.isdigit())


def analize(stringas):
    zodziai = zodziu_skaicius(stringas)
    dideles = didziosios(stringas)
    mazos = mazosios(stringas)
    skaiciukas = skaiciai(stringas)

    print(f'zodziu skaicius:  {zodziai}')
    print(f'didziuju raidziu skaicius: {dideles}')
    print(f'mazuju raidziu skaicius: {mazos}')
    print(f'skaiciu skaicius: {skaiciukas}')


stringas = "labas vakaras 123"
analize(stringas)
