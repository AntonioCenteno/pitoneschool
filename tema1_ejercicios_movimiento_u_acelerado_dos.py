#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio Adicionales: Movimiento uniformemente acelerado dos
import math

# Calculo: Velocidad inicial
a=float(raw_input("Aceleracion: "))
t=float(raw_input("Tiempo"))
D=float(raw_input("Distancia:"))
banner="="*50
V_i =  (2*D - a * pow(t,2))  / (2*t)
print "D =",D,"t =",t,"a =",a
print banner
print "Velocidad inicial:", V_i

# Calculo: Distancia
V_i=float(raw_input("Velocidad inicial: "))
t=float(raw_input("Tiempo"))
a=float(raw_input("Aceleracion:"))
D = V_i * t + (0.5 * a * pow(t,2))
print "V_i =",V_i,"t =",t,"a =",a
print banner
print  "Distancia: ", D

# Calculo: Aceleracion
V_i=float(raw_input("Velocidad inicial: "))
t=float(raw_input("Tiempo"))
D=float(raw_input("Distancia:"))

a=2*(D-V_i*t)/pow(t,2)
print "V_i =",V_i,"t =",t,"D =",D
print banner
print "Aceleracion: ", float(a)

# Calculo: Tiempo
V_i=float(raw_input("Velocidad inicial: "))
D=float(raw_input("Distancia"))
a=float(raw_input("Aceleracion:"))
t=((-V_i)+((V_i**2)-(4*(-a*D/2)))**(0.5))/a

print "V_i =",V_i,"a =",a, "D =",D
print banner
print "Tiempo: ", t
print banner


