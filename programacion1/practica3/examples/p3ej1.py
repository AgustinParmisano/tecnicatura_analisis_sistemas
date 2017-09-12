p1 = raw_input("Ingrese una palabra: ")
p2 = raw_input("Ingrese una palabra: ")

if (p1[-3:] == p2[-3:]):
    print "Las palabras %s y %s riman mucho!" % (p1,p2)
elif (p1[-2:] == p2[-2:]):
    print "Las palabras %s y %s riman poco!" % (p1,p2)
else:
    print "Las palabras %s y %s no riman!" % (p1,p2)

print "Salio del IF"