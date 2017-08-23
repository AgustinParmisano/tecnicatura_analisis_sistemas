persona = ["valeria", "maza", 33112447, 1987, "florencio varela",0]
clave_personal = persona[2]* persona[3]
print "clave_personal"
print(clave_personal)
persona[-1] = clave_personal
print "persona"
print(persona)

dictic = {"nombre":"valeria","apellido":"maza","DNI":33112447,"nacimiento":1987,"lugar":"florencio varela","cp":persona[-1]}
print(dictic)
print("cp")
print(dictic["cp"])
dictic["mascota"]="perro"
print(dictic)
