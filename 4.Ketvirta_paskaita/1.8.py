def atbulai(sakinys):
    zodziai = sakinys.split()
    atbulas_sakinys = ' '.join(reversed(zodziai))
    return atbulas_sakinys


print(atbulai("saulute sviecia , vejelis pucia"))
