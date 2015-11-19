#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 9.- Dados dos números enteros a y b, escribir un programa que muestre los números enteros
pares e impares del intervalo [a, b] en la forma:
10 (par)
11 (impar)
12 (par)
'''
a=int(raw_input("a: "))
b=int(raw_input("b: "))

for i in range(a,b+1):
    if i%2==0:
        print i,"(par)"
    else:
        print i,"(impar)"

