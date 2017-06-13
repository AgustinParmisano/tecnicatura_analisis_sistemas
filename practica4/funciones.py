# def nombre_func(parametro1, parametro2, parametro3):
# 	bloque_de_codigo
#	return

n = input("Ingrese un numero: ")

def es_par(num):
	if (num % 2) == 0:
		return 1
	else:
		return 0

if es_par(n) == 1:
	print("El numero %s es par " % (n))
else:
	print("El numero %s no es par" % (n))

print(es_par(n))

resul = es_par(n)
print("El resultado es %s: " % (resul))

a = 2

def por_num(num):
	
	return a * num

a = por_num(n)

print(a) 
