doble = input("ingrese un entero: ")
while doble != 0:
    d = doble / 2
    mitad = d % 2

    if (mitad != 0):
        print "es el doble de un impar"
    else:
        print "no es el doble de un impar"
    doble = input("ingrese unn entero: ")
