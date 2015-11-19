#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 8.- Dados dos enteros a>0 y b, modificar el programa anterior para calcular la expresión
matemática
        sumatorio de i=a..b (i**i+1)/i

'''

for i in range(a,b+1):
    print float((pow(i,2)+1)/i)

