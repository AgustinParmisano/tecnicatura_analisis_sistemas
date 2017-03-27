#!/usr/bin/python
# coding=utf-8

#llegan número del 1 al 4 imprimirlos en letras según el número

num = int(raw_input("Ingrese un numero del 1 al 4: "))

if num == "1": 
  print "Uno"

if num == "2":
  print "Dos"

if num == "3":
  print "Tres"

if num == "4":
  print "Cuatro"
else:
 print "El numero ingresado es incorrecto"
  
delunoalcuatro = {1,2,3,4}
