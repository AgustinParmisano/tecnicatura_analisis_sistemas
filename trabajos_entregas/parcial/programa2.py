def poscad(a,b):
	cont = 0
	lista = []
	for i in a:
		cont = cont+1
		if i == b:
			lista.append(cont-1)

	return lista
	if cont == 0:
		nomatch = -1
		return nomatch

palabra = "ferrocarril"
print poscad(palabra,"r")
