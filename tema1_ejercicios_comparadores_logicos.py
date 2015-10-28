#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 4.- Comparadores lógicos
a=int(raw_input("Dame un numero a:"))
b=int(raw_input("Dame un numero b:"))

c = a in range (5,30) and (b%2==0)
print "Valor de c True/False? ", c
print "Tipo de dato para c: ", type(c)

d = a not in range(5,30) and not (b%2==0)
print "Valor de d True/False? ", d
print "Tipo de dato para d: ", type(d)

'''
In [47]: a=10
In [48]: b=12
In [49]: c= a in range(5,30) and (b%2==0)
In [50]: c
Out[50]: True
In [51]: type(c)
Out[51]: bool
In [57]: d= a not in range(5,30) and not (b%2==0)
In [58]: d
Out[58]: False
In [62]: a=15
In [63]: b=26
In [64]: c= a in range(5,30) and (b%2==0)
In [65]: d= a not in range(5,30) and not (b%2==0)
In [66]: c
Out[66]: True
In [67]: d
Out[67]: False
'''


