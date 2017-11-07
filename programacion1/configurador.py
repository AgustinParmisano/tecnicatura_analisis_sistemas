#Funcion que genera las variables de la estacion, las mismas las va pidiendo por teclado al humanoide.
def seteador_variables(): # funcion sin parametros.
        
	lista = [] #Seteamos la lista.
        opcion = raw_input("Ingrese el nombre de la variable (Ingrese salir para terminar) : ") #Pedimos variable por teclado, tambien variable de While.
        while opcion != "salir": # While.
                print "usted fue agregando"
                lista.append(opcion) #Agregamos la variable ingresada.
                opcion = raw_input("Ingrese el nombre de la variable (Ingrese salir para terminar) : ") #Pedimos la siguiente Variable y la guardamos en variable opcion.
                print "Usted fue agregando"
		print lista
        return lista


#Funcion que recibe la lista creada por  funcion seteador_variables, y devuelve un diccionario.
def configurador(lista_variables):
        variables = {} #seteamos el diccionario interno
        for var in lista_variables: # For que  recorre la lista ingresada por parametro.
                valor = input("Ingrese el valor numerico para la variable " + str(var) + " : ") #pedimos por teclado los valores para elemento de lista_variables 
                discriminador = raw_input("Ingrese el discriminador (mayor o menor) de la variable: " + str(var) + " : ") #pedimos por teclado el tag de mayor o menor.
                variables[var] = {"valor":valor,"discriminador":discriminador} # armamos el diccionario con las variables valor y discriminador.

        return variables # devuelve un diccionario.

lista = seteador_variables() # variable que contiene la lista que devolvio la funcion "seteador_variables". 

json = configurador(lista) #Variable que contiene el diccionario que devolvio la funcion 2configurador".

f = open("meteo_vars.conf", 'w') #Creamos el archivo "meteo_vars.conf" con la opcion de escritura.

f.write(str(json)) # Escribimos en el archivo lo que contiene la variable json.

print "El Archivo meteo_vars.conf fue creado exitosamente." #Aviso de que el archivo fue creado.

f.close() #Cerramos el archivo.





