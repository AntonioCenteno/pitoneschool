#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 6.- Año Bisiesto
anyo=2012
bisiesto = (anyo % 4 == 0) and (anyo % 100 != 0) or (anyo % 400 == 0)

print "Año " , anyo , " es bisiesto? -> ", bisiesto

'''
In [32]: anyo=2011
In [33]: bisiesto=anyo % 4 == 0 and anyo % 100 != 0 or anyo % 400 == 0
In [34]: bisiesto
Out[34]: False
'''


