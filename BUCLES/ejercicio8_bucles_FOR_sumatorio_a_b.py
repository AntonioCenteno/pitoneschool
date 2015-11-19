#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 8.- Dados dos enteros a>0 y b, modificar el programa anterior para calcular la expresión
matemática

sumatorio de i=1..b (i**i+1)/i

'''
a=int(raw_input("a: "))
b=int(raw_input("b: "))

for i in range(a,b+1):
    print int((pow(i,2)+1)/i)

