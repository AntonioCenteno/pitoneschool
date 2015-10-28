#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 4.- Escribir un programa que lea cinco números enteros e indique cuál es el mayor de los cinco.
'''
Escribir un programa que resuelva cualquier ecuación de 1er grado de la
forma: ax+b=0, donde x es la incógnita y a y b son dos números reales que leerá el
programa. Contemplar el caso en el que a es 0.
'''

a=float(raw_input("a="))
b=float(raw_input("b="))
if a<0:
    a=abs(a)
if b<0:
    b=abs(b)

if a>0:
    a=-a
if b>0:
    b=-b

x=b/a

print "a: %i" % a
print "b: %i" % b
print "Solucion: %.4f" % x
