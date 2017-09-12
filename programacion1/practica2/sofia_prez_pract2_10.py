aome = input("ingrese edad")
while aome != 0:
    if aome <2:
        print "bebe"
    elif aome >2 and aome<=12:
        print "menor"
    elif aome >12 and aome<=18:
        print "adolescente"
    elif aome >18 and aome <=45:
        print "adulto"
    elif aome >45 and aome <=60:
        print "veterano"
    elif aome >60:
        print "abuelo"
    else:
        print "dios"
    aome = input("ingrese edad")    
