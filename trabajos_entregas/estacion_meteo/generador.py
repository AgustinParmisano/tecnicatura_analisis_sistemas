# -*- coding: utf-8 -*- 
import ast
import random
valrandom = {}

def rjason(claves,valores):
	dicc = {}
	for c in claves:
		dicc[c] = valores[claves.index(c)]
	return dicc

f=open("meteo_vars.conf","r") #Abrimos el archivo

for i,linea in enumerate(f):
	dicc = ast.literal_eval(str(linea))

variables = dicc.keys()
while True:	
	for k in variables:
		valrandom[k]=random.randint(0,100)
	print valrandom



