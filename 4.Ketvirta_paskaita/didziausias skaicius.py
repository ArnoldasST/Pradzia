def didziausias_skaicius(*args):
    didziausias = args[0]
    for skaicius in args:
        if skaicius > didziausias:
            didziausias = skaicius
    return didziausias


print(didziausias_skaicius(1, 15, 152, 22))
