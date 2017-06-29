f = open('archivo3.txt', 'w')                
pal = -1                                      
while pal != "salir":                           
    pal = raw_input("Escriba: ")
    f.write(pal)
 
f.close()

