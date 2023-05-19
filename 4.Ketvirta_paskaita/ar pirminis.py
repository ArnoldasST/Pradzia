def atsakymas(skaicius):
    if skaicius < 2:
        return False
    for x in range(2, int(skaicius ** 0.5) + 1):
        if skaicius % x == 0:
            return False
    return True


print(atsakymas(11))
