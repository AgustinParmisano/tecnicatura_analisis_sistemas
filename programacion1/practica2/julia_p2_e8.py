semana=("Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado")

dia=input("ingrese un numero del 1 al 7: ")

if dia>0 and dia<8:
    dia=dia-1
    print("el dia ingresado es %s" % (semana [dia]))
else:
    print("El numero que ingreso no corresponde a un dia de semana")

i=0
for ndia in semana:
    i+=1
    print("el for se ejecuto "+ str(i))
    print ndia
