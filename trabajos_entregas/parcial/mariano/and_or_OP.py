#1)
#a)Realice una funcion que dado los numeros pasados por parametro retorne si A=1 y B=1 Res=1, Res=0 en cualquier otro caso.

A = input("Ingrese un numero: ")
B = input("Ingrese otro numero: ")

def andfun(A,B):
	if A == 1 and B == 1:
		return 1
	else:
		return 0

print(andfun(A,B))

#b)Realice una funcion que simule una compuerta OR dados 2 numeros pasados por parametro y retorne el Res

C = input("ingrese un numero binario: ")
D = input ("ingrese otro numero binario: ")

def orfun(C,D):
	if C == 1 or D == 1:
		return 1
	else:
		return 0

print(orfun(C,D))

#2)Realice una funcion que dado dos numeros binarios de 8 bits (ej: "01010101") retorne el resultado de Operacion AND

n_1 = raw_input("Ingrese un numero binario de 8 bits: ")

n_2 = raw_input("Ingrese otro numero binario de 8 bits: ")

def andop(n_1,n_2):

	lista = []
	conteo = 0

	for i in n_1:
		result = andfun(int(i),int(n_2[conteo]))
		conteo = conteo + 1
		lista.append(result)

	return lista

print(andop(n_1,n_2))

