cadena = raw_input('Ingrese una cadena de caracteres ')
letra = raw_input('Ingrese una letra ')
lista = []

def buscar(cadena,letra,lista):
    indice = 0

    while (indice < len(cadena)):
        if cadena[indice] == letra:
            lista.append(indice)
            ok = True
        indice = indice + 1

    if(ok == True):
        return lista

    else:
        return -1

print(buscar(cadena,letra,lista))
