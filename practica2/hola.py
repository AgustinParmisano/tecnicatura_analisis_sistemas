def cambio_dialogo(texto):
     	diccionario={}
     	lista=[]
     	for linea in texto.split('\n'):
     		linea= linea.split(":")
    		if not(linea[0]) in diccionario:
     			diccionario[linea[0]]=[linea[1]]
     		else:
     			diccionario[linea[0]].append(linea[1])
    		lista.append({"actor":linea[0],"linea":diccionario[linea[0]].index(linea[1])})
            print linea[0]

		return (diccionario,lista)

def intercambiar_actores(dialog_dict, lista_dialogo, pers1, pers2):
    listAux= dialog_dict[pers2][:]
    dialog_dict[pers2]=dialog_dict[pers1][:]
    dialog_dict[pers1]=listAux[:]
    for dic in lista_dialogo:
		if( dic["actor"] == pers2):
			dic["actor"]=pers1
		else:
			dic["actor"]=pers2
		print(dic["actor"])

guion="""Carlos: Bienvenidos!
Luis: Gracias, por donde es?
Carlos: Pase por aca.
Eva: Muchas gracias!
Carlos: De nada.
Carlos: Cuanta cortesia!"""

dict_a, list_b = cambio_dialogo(guion)

intercambiar_actores(dict_a, list_b, 'Carlos', 'Luis')

print "Dict A"
print dict_a == {'Luis': [' Bienvenidos!', ' Pase por aca.', ' De nada.', ' Cuanta cortesia!'], 'Carlos': [' Gracias, por donde es?'], 'Eva': [' Muchas gracias!']} or dict_a == {'Luis': [' Bienvenidos!', 'Pase por aca.', ' De nada.', 'Cuanta cortesia!'], 'Carlos': ['Gracias, por donde es?'], 'Eva': ['Muchas gracias!']}
print "Dict B"
print list_b == [{'linea': 0, 'actor': 'Luis'}, {'linea': 0, 'actor': 'Carlos'}, {'linea': 1, 'actor': 'Luis'}, {'linea': 0, 'actor': 'Eva'}, {'linea': 2, 'actor': 'Luis'}, {'linea': 3, 'actor': 'Luis'}]
