#!/usr/bin/python
# coding=utf-8

'''
Realizar un  programa  que lea  dos números enteros desde  teclado  e  informe
en pantalla cuál de  los  dos  números  es  el  mayor. Si  son  iguales
debe  informar  en pantalla lo siguiente: “Los números leídos son iguales”.
'''

num1 = int(raw_input('Ingrese un número: '))
num2 = int(raw_input('Ingrese otro número: '))

if num1 > num2:
    print(" El número %s es mayor que %s" % (num1, num2))
elif num1 < num2:
    print("El número %s es mayor que %s" % (num2, num1))
else:
    print("Los números %s y %s son iguales" % (num1, num2))
