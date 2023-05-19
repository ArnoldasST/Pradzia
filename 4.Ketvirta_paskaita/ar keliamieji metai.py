def keliamieji(metai):
    if metai % 4 != 0:
        return False
    elif metai % 100 != 0:
        return True
    elif metai % 400 != 0:
        return False
    else:
        return True


print(keliamieji(2021))
