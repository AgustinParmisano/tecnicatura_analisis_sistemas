#!/usr/bin/python

palabra = raw_input ("ingrese la palabra: ")

def contar_vocales (palabra):
	a = 0
	e = 0
	ii = 0
	o = 0
	u = 0
	for i in palabra: 
		if i == "a":
			a +=1
		if i == "e": 
                        e +=1   
                if i == "i": 
                       ii +=1   
		if i == "o": 
                        o +=1
		if i == "u": 
                        u +=1
  
	print a; print e; print ii; print o; print u

	return 0

contar_vocales (palabra)

