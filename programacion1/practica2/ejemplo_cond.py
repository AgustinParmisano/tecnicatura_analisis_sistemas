#!/usr/bin/python

a = (3 > 1)
b = (3 > 3)
c = (5 % 2) == 0
d = "hola"[2] == "l"

if a and b:
	print("hola")
elif(not d or b):
	print("chau")
else:
	print("aloha")
