#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 11.- Dado un número entero n (n≥0), escribir un programa para obtener la cadena de caracteres
de unos y ceros correspondiente a su representación en binario sin utilizar la función predefinida bin.
'''

n=abs(int(raw_input("Numero entero: ")))
binario = ''
resultado=''

while n // 2 != 0:
    binario = str(n % 2) + binario
    n = n // 2
    resultado = str(n) +binario

print "El valor en binario del numero ", n , " es" ,resultado

