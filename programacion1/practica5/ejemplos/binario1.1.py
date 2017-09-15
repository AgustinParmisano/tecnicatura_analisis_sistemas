#DRY = DONT REPEAT YOURSELF
def busqbin(e,l):
    pos = -1
    ok = False
    menor = 0
    mayor = len(l) - 1
    while (menor <= mayor) and not ok:
        mitad = (menor + mayor) / 2
        if e == l[mitad]:
            ok = True
            pos = mitad
        elif(l[mitad] > e):
            mayor = mitad - 1
        elif(l[mitad] < e):
            menor = mitad + 1
    return pos

print busqbin(3454, range(1000,99999,2))
