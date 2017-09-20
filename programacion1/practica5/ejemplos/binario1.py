import time

def busqbin(a,l):
	pos = -1
	menor = 0
	mayor = len(l)-1
	fin = False
	while menor <= mayor and not fin:
		mitad = (menor + mayor)/2
		if l[mitad] == a:
			fin = True
			pos = mitad
		elif l[mitad] > a:
			mayor = mitad -1
		elif l[mitad] < a:
			menor = mitad +1
	return pos

lista = range(1,9999999)
n = input("Ingrese un numero de 8 cifras: ")
start_time = time.time()
print busqbin(n,lista)

end_time = time.time()

print (end_time - start_time)
