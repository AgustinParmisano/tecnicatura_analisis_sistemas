#Iteracion

semana = ['lunes','martes','miercoles','jueves','viernes']
responsable = ['Joaquin','Julia','Mauro','Adan','Pablo']

for dia in semana:
    indice_dia = semana.index(dia)
    responsable_dia = responsable[indice_dia]
    print("El responsable de los %s es %s." % (dia, responsable_dia))
print("Un gran poder conlleva una gran responsabilidad")