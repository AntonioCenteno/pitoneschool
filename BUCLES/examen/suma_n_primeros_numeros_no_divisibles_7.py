#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio:
1. Haga un programa que calcule y muestre la suma de los n primeros números naturales a partir del 1 (incluido) que no son múltiplos de 7 donde n se pide por teclado.
1+2+3+4+5+6 ...
'''

n = abs(int(raw_input("Numero n: ")))
suma = 0

for i in range(1,n+1):
    if n%7!=0:
        suma = suma + i

print "Suma: " , suma
