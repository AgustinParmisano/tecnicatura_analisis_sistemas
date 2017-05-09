# Bucle

salir = False
while not salir:
    entrada = raw_input("Hola! ")
    if entrada == "chau":
        print("Hasta la proxima!")
        salir = True
    else:
        print("Escribiste: %s" % (entrada))
print("Salgo del while")