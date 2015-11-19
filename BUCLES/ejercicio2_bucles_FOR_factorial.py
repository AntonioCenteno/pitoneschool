#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 2.- Dado un número entero n≥0, escribir un programa para calcular el factorial del número n
(n!) y escribir el resultado obtenido en la forma:
4 ! = 24

'''

n=abs(int(raw_input("Numero entero: ")))
aux=n
factorial = 1

for i in range(1,n):
    factorial = factorial * n
    n=n-1

print aux, "!",factorial



