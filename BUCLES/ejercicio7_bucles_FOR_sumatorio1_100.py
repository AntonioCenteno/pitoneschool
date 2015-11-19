#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 7.- Escribir un programa que calcule la siguiente expresión matemática:
        sumatorio de i=1 .. 100 (i**i+1)/i

'''

for i in range(1,101):
    print int((pow(i,2)+1)/i)

