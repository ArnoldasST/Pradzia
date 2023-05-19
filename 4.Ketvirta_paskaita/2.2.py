elementas = str(55)

def gretimi_skaiciai():
    for x in elementas:
        if x.isdigit() == True:
            a = int(x)
            b = a - 1
            c = a + 1
        print(a, "-",b,c)

gretimi_skaiciai()