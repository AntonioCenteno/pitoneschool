#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Ejercicio 9.- Dado un número natural umbral, escribe un programa que muestre los términos de la
sucesión de Fibonacci. El primer término de dicha sucesión es 0, el segundo es 1.
Sucesión de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
'''

umbral = abs(int(raw_input("Umbral: ")))
a,b = 1,1
print "Sucesion de Fibonacci:" ,
while umbral<>0:
    umbral = umbral -1
    a,b = b,a+b
    print a, ",",




