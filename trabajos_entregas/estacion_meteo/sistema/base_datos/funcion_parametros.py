import datetime
import time
import random

def rjason(claves,valores):
    dicc = {}
    for c in claves:
            dicc[c] = valores[claves.index(c)]
    return dicc

def alertador(variables, valores_alerta):
	print "Alertando"
	time.sleep(1)
        #for a in range(0,60):
        if "temperatura" in variables:
            print "La temperatura es: " + str(variables['temperatura'])
            if variables["temperatura"] < 20:
                print "la temperatura es baja: " + str(variables['temperatura'])

def seteador_variables():
	lista = []
	opcion = raw_input("Ingrese el nombre de la variable (Ingrese salir para terminar) : ")
	while opcion != "salir":
		lista.append(opcion)
		print "usted fue agregando"
		print lista
		opcion = raw_input("Ingrese el nombre de la variable (Ingrese salir para terminar) : ")
	return lista

def configurador(lista_variables):
	variables = {}
	for var in lista_variables:
		valor = input("Ingrese el valor numerico para la variable " + str(var) + " : ")
		discriminador = raw_input("Ingrese el discriminador (mayor o menor) de la variable: " + str(var) + " : ")
		variables[var] = {"valor":valor,"discriminador":discriminador}
	
	return variables

lista1 = seteador_variables()

print configurador(lista1)

lista1.append("fecha")

"""
for i in range(0,60):
    print "Generando datos"
    #time.sleep(1)
    #Hacer funcion que lea de gpio y retorne una lista con los valores
    lista2=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(500,1200),datetime.datetime.now()]
    print ""
    datos = rjason(lista1,lista2)
    alertador(datos)
"""
