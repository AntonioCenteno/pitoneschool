#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 2.- Escribir un programa que lea tres números enteros e indique si están o no en orden ascendente.

a=int(raw_input('a='))
b=int(raw_input('b='))
c=int(raw_input('c='))

# Ni ascendente ni descendente
if a==b and b==c:
    print "Ni ascendente ni descendente"
    exit()

# ascendente o descendente
if a<b and b<c and c>b:
    print "orden ascendente"
else:
    print "orden descendente"

