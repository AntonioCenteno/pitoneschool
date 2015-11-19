#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 11.- Dado un número natural n, escribir un programa que muestre todos sus divisores en la
forma:
Los divisores de 12 son: 1 2 3 4 6 12

'''
numero=abs(int(raw_input("a: ")))
divisores=''

for i in range(1,numero+1):
    if numero%i==0:
        divisores += str(i)+ " "

print divisores


