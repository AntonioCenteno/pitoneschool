#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 2.- Conversión de Temperaturas

c=float(raw_input('Temperatura en CELSIUS: '))
f=float(raw_input('Temperatura en FARENHEIT: '))
f_result=(c*9/5)+32
c_result=((f-32)*5)/9
print "Temperatura en grados celsius:" , c_result
print "Temperatura en grados farhenheit:" , f_result

'''
In [13]: C=30
In [14]: F=(C*9/5)+32
In [15]: F
Out[15]: 86
In [16]: F=77
In [17]: C=((F-32)*5)/9
In [18]: C
Out[18]: 25
'''


