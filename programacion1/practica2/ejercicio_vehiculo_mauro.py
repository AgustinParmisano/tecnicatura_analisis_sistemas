#!/usr/bin/python

vehiculo =int (raw_input ("cantidad de pasajeros: "))
if vehiculo ==1 and vehiculo<2:
	print "bicicleta"
elif vehiculo ==2 or vehiculo<3:
	print "moto"
elif vehiculo ==3 or vehiculo<5:
	print "auto"
elif vehiculo ==5 or vehiculo<13:
	print "camioneta"
elif vehiculo ==13 or vehiculo<41:
	print "micro"
elif vehiculo ==41 or vehiculo<201:
	print "avion"
else :
	print "no hay vehiculo" 






