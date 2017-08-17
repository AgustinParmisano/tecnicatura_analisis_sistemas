def dni_checker(num):
	count = 0
	if num < 100:
		return False
	else:
		snum = str(num)
		for n in snum:
			if (int(n) % 2) != 0:
				count += 1
		return (count >= 3)

if dni_checker(input("Ingrese un DNI: ")):
	print "El dni ingresado es valido"

