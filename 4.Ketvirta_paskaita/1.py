def skaiciu_suma(skaicius1, skaicius2, skaicius3):
    suma = skaicius1 + skaicius2 + skaicius3
    return suma


print(skaiciu_suma(10, 10, 10))


def saraso_suma(*args):
    suma = sum(args)

    return suma


print(saraso_suma(5, 5, 5, 5, 5, 5))


