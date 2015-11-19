#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 4.- Escribir un programa que imprima todos los números comprendidos entre 20 y 10 en sentido
decreciente.
Salida del programa:
20
19
18
…
10
'''
n=abs(int(raw_input("Numero descendente: ")))

for i in range(10,n+1):
    print n
    n=n-1

