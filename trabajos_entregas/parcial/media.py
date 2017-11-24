def pos(pal,let):
	l=[]
	i=0
	for e in pal:
		if str(e) == str(let):
			l.append(i)
		i+=1
	if len(l) == 0:
		return -1
	else:
		return l


pal = raw_input("Palabra: ")
letra = raw_input("Letra: ")
print pos(pal,letra)
