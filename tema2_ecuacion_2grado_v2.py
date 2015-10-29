#!/usr/bin/python
# -*- coding: latin-1 -*-

# Ejercicio 4 - Ecuacion de segundo grado
a=float(raw_input("Introduce coeficiente a"))
b=float(raw_input("Introduce coeficiente b"))
c=float(raw_input("Introduce coeficiente c"))

radicando=((b**2)-(4*a*c))

solucion_real=radicando>=0
solucion_unica=radicando==0

if solucion_real:
    if solucion_unica:
        print "La ecuacion tiene una solucion real doble"

    else:
        print "La ecuacion tiene dos soluciones reales"

else:
    print "Dos soluciones complejas conjugadas"