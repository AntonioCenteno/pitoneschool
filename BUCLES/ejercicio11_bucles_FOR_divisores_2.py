#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 8.- Dado un número entero n>0, escribe un programa que imprima sus cifras de la menos a la
más significativa.
Ejemplo de salida del programa para la entrada: 7249:
Las cifras del número 7249 de la menos a la más significativa son: 9 4 2 7
'''

numero = int(raw_input('Numero (Con 0 terminas): '))
ultima=0
division=0
salida=''

while numero > 0:
    ultima=numero%10
    numero=numero/10
    salida+=str(ultima)

print salida ," ",


