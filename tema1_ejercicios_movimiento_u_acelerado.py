#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 3.- Movimiento uniformemente acelerado

a=float(raw_input('Aceleracion: '))
t=float(raw_input('Tiempo m/s: '))
V_f = 314
V_i = V_f - (a*t)
print "Velocidad inicial: ", V_i

V_i = 20
V_f = V_i + (a*t)
print "Velocidad final: ", V_f

'''
V_f = V_i + a t
In [28]: a=9.8
In [29]: t=30
In [30]: Vi=Vf-(a*t)
In [31]: Vi
Out[31]: 20.0
'''


