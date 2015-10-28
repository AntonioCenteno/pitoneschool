#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 5.- Datos Representados en Cadenas
base=9
altura=5

area=str((base*altura)/2)
mensaje="El area del triangulo es igual a " +  area
print mensaje

base=5
altura=7
area=str((float(base)*float(altura))/2)
mensaje="El area del triangulo es igual a " +  area
print mensaje


'''
In [81]: base=9
In [82]: altura=5
In [83]: area=str((base*altura)/2)
In [88]: area
Out[88]: '22.5'
In [84]: mensaje="El area del triangulo es igual a" +  area
In [87]: mensaje
Out[87]: 'El area del triangulo es igual a: 22.5'

In [24]: base='5'
In [25]: altura='7'
In [26]: area=str((float(base)*float(altura))/2)
In [27]: mensaje="El area del triangulo es igual a" +  area
In [30]: mensaje
Out[30]: 'El area del triangulo es igual a: 17.5'
'''


