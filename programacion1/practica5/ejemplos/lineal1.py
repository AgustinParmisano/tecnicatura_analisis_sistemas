import time
start_time = time.time()

lista=range(1,9999999)

def busqueda(a,l):
	pos=-1
	for j in range(0,len(l)):
		if a== l[j]:
			pos = j
	return pos

print lista[busqueda(1,lista)]
 
end_time = time.time()

print "El programa tardo %s " % (end_time - start_time)
