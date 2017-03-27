#!/usr/bin/python
# coding=utf-8

'''
Realizar un  programa  que  lea  números  enteros  desde  teclado.
La  lectura  debe finalizar  cuando  se  ingrese el  número 100,
el  cual debe  procesarse. Informar en pantalla:
a. El número máximo leído.
b. El número mínimo leído.
c.La suma total de los números leídos.
'''

nummin = 999999999
maxnum = -99999999
tot = 0
num = int(raw_input("Ingrese un número: "))

while num != 100:
    print("El número ingresado es %s" % (num))
    if num < nummin:
        nummin = num
    if num > maxnum:
        maxnum = num
    tot = tot + num
    print("El número mínimo es %s el máximo es %s y el total es %s" % (nummin, maxnum, tot))
    num = int(raw_input("Ingrese un número: "))
