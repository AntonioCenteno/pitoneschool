#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio Adicionales: Movimiento uniformemente acelerado dos
import math

# Calculo: Velocidad inicial
a=9.8
t=30
D=5010
banner="="*50
V_i =  (2*D - a * pow(t,2))  / (2*t)
print "D =",D,"t =",t,"a =",a
print banner
print "Velocidad inicial:", V_i

# Calculo: Distancia
V_i = 20.00
a=9.8
t=30.00
D = V_i * t + (0.5 * a * pow(t,2))
print "V_i =",V_i,"t =",t,"a =",a
print banner
print  "Distancia: ", D

# Calculo: Aceleracion
V_i = 20.00
D=5010.00
t=30.00
a=2*(D-V_i*t)/pow(t,2)
print "V_i =",V_i,"t =",t,"D =",D
print banner
print "Aceleracion: ", float(a)

# Calculo: Tiempo
V_i = 20.00
D=5010.00
a=9.8
raiz=2*(D - V_i * t)/a
# raices positivas
if raiz>0:
    t=round(math.sqrt(raiz))
else:
    t=round(math.sqrt(abs(raiz)))


print "V_i =",V_i,"a =",a, "D =",D
print banner
print "Tiempo: ", t
print banner

'''
Velocidad inicial :
In [92]:  V_i =  (2*D - a * pow(t,2))  / (2*t)
In [93]: V_i
Out[93]: 20.0

Aceleración:
In [97]: a=2*(D-V_i*t)/pow(t,2)
In [98]: a
Out[98]: 9.8

Tiempo:
In [107]: t=round(math.sqrt(2*(D-V_i*t)/a))
In [108]: t
Out[108]: 30.0
'''


