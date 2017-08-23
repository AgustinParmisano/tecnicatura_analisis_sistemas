cadena = "esto es una cadena"
def inversa(cadena):
    variable = ""
    for i in range(len(cadena)-1,-1,-1):
        variable += cadena[i]
        #print cadena[i]
    return variable
print(inversa(cadena))

def inversa2(cadena):
    variable = ""
    for i in cadena:
        variable = i + variable

        #print cadena[i]
    return variable
print(inversa2(cadena))
