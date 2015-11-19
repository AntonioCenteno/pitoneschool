#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 1.- Dado un número entero n≥0, escribir un programa para obtener la suma de los n primeros
números naturales y escribir el resultado obtenido en la forma:
La suma de los 5 primeros números naturales es: 15
'''

n=abs(int(raw_input("Numero entero: ")))
suma = 0

for i in range(1,n+1):
    suma = suma + i

print "La suma de los",n, "primeros numeros naturales es:",suma



