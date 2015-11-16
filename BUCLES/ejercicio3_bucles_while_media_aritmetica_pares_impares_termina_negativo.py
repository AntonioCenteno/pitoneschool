#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 3.- Escribir un programa que lea del teclado número a número. La lectura de números termina
con un número negativo. El programa debe mostrar la media aritmética de los números pares leídos y la
media aritmética de los números impares leídos.
'''
numeros = 0
media_pares = 0
media_impares = 0
contador_pares = 0
contador_impares = 0
suma_pares = 0
suma_impares = 0

while numeros >= 0:
    numeros = int(raw_input('Dame el numero:'))
    if numeros >=0 and numeros%2==0:
        contador_pares = contador_pares + 1
        suma_pares = suma_pares + numeros

    if numeros >=0 and numeros%2!=0:
        contador_impares = contador_impares + 1
        suma_impares = suma_impares + numeros


media_pares = (suma_pares/contador)
media_impares = (suma_impares/contador)
print "La media de los numeros pares es ", suma_pares, " y la media " , media_pares
print "La media de los numeros impares es ", suma_impares, " y la media " , media_impares

