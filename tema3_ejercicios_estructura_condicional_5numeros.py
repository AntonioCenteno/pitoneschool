#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 3.- Escribir un programa que lea cinco números enteros e indique cuál es el mayor de los cinco.

a=int(raw_input('a='))
b=int(raw_input('b='))
c=int(raw_input('c='))
d=int(raw_input('d='))
e=int(raw_input('e='))

# Ni ascendente ni descendente
if a==b and b==c and c==d and d==e:
    print "Son todos iguales! "
    exit()

print "El mayor introducido es %i" % max(a,b,c,d,e)

'''
mayor=0
a=int(raw_input("Numero 1"))
if(a>mayor):
    mayor=a
b=int(raw_input("Numero 2"))
if(b>mayor):
    mayor=b
c=int(raw_input("Numero 3"))
if(c>mayor):
    mayor=c
d=int(raw_input("Numero 4"))
if(d>mayor):
    mayor=d
e=int(raw_input("Numero 5"))
if(e>mayor):
    mayor=e

print "El mayor numero introducido es",mayor
''