#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 11.- Dado un número natural n, escribir un programa que muestre todos sus divisores en la
forma:
Los divisores de 12 son: 1 2 3 4 6 12

'''
a=abs(int(raw_input("a: ")))
b=abs(int(raw_input("b: ")))
suma_producto=0

for i in range(a):
    suma_producto += b

print suma_producto


