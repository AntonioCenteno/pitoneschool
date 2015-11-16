#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 2.- Escribir un programa que lea del teclado número a número. La lectura de números termina
con un número negativo. El programa debe mostrar la media aritmética de los números introducidos.
'''

numeros = 0
media = 0
contador = 0
suma = 0

while numeros >= 0:
    numeros = int(raw_input('Dame el numero:'))
    if numeros >= 0:
        contador = contador + 1
        suma = suma + numeros

media = (suma/contador)
print "La media de los numeros es ", suma, " y la media " , media





