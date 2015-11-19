#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 3.- Dado un número entero n≥0, escribir un programa para obtener una cadena de caracteres
que contenga n asteriscos y escribir el resultado obtenido.
Ejemplo de salida del programa para n = 3: ***

'''

n=abs(int(raw_input("Numero asteriscos: ")))
asteriscos=''

for i in range(1,n):
    asteriscos = '*'*n


print "n=",n ,":",asteriscos



