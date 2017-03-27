#!/usr/bin/python
# coding=utf-8

#Pedimos al usuario un número, si es par impirmir "par" si no imprimir "impar"

num = float(raw_input("Ingrese un número: "))
divisor = int(raw_input("Ingrese el divisor: "))

mod = num % divisor

if mod == 0:
    print("El número %s es divisible por %s porque el mod es %s" % (num, divisor, mod))
else:
    print("El número %s NO es divisible por %s porque el mod es %s" % (num, divisor, mod))
