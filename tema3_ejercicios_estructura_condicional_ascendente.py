#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 2.- Escribir un programa que lea tres números enteros e indique si están o no en orden ascendente.

a=abs(int(raw_input('a=')))
b=abs(int(raw_input('b=')))
c=abs(int(raw_input('c=')))

# Ni ascendente ni descendente
if a==b and b==c:
    print "Ni ascendente ni descendente"
    exit()

# ascendente o descendente
if c>b:
    print "orden ascendente"
else:
    print "orden descendente"

