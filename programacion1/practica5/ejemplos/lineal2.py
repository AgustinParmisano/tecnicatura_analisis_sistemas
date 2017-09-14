import time
start_time = time.time()

lista=range(1,9999999)

def busqueda(a,l):
	pos=-1
	j=0
	fin= False
	while j < len(l) and not fin:
		if a== l[j]:
			pos = j
			fin=True
		j=j+1
	return pos

print busqueda(10000000,lista)
 
end_time = time.time()

print "El programa tardo %s " % (end_time - start_time)
