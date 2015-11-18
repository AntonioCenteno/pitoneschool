#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 7.- Escribe un programa que lea por teclado enteros positivos número a número y proporcione
el mayor de ellos y la posición en la que éste se introdujo. La lectura de números terminará si se introduce
el valor 0.
Ejemplo de salida para la entrada: 100 25 36 596 3 15 0
El mayor número es 596 y se proporcionó en la posición 4

'''

entrada = int(raw_input('Dame el numero A:'))
pos = 0
mayor = 0;
numeros = []
maxpos = 0

while entrada !=0:
    entrada = int(raw_input('Dame el numero A:'))
    pos = pos + 1
    numeros.append(entrada)
    if (max(numeros)):
        maxpos = pos

print str(numeros)
print "El mayor numero que se proporciono es ", max(numeros), "en la posicion ", pos





