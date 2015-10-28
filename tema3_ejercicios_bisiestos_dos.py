#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio 7.- Escribir un programa que lea un año y determine si es o no bisiesto.

# Ejercicio 8.-

'''Modificar el programa anterior para que además lea el número de un mes
(1 a 12) y muestre el número de días de ese mes en función del mes y del año
introducidos.
'''
anyo=int(raw_input("Introduce el anyo bisiesto:"))
mes = int(raw_input("Introduce el mes:"))
es_divisible_por_4 = (anyo % 4 == 0)
es_divisible_por_100 = (anyo % 100 == 0)
es_divisible_por_400 = (anyo % 400 == 0)
bisiesto = (anyo % 4 == 0) and (anyo % 100 != 0) or (anyo % 400 == 0)

par = mes%2==0
impar=mes%3==0

if (par) and mes != 2:
    dias=30
elif impar:
    dias=31
else:
    dias=28

print par , impar

if es_divisible_por_4 and not es_divisible_por_100:
        dias=29
        print anyo, " es BISIESTO ya que es divisible por 4 y no divisible por 100 "

if es_divisible_por_4 and es_divisible_por_100 and es_divisible_por_400:
        dias=29
        print anyo, " es BISIESTO ya que es divisible por 4, por 100 y por 400"

if es_divisible_por_4 and es_divisible_por_100 and not es_divisible_por_400:
        print anyo, " NO es BISIESTO ya que es divisible por 4, por 100 y no por 400"

if not es_divisible_por_4:
        print anyo, " NO es BISIESTO ya que no es divisible por 4"

print "Dias del mes %i: %i" %( mes, dias)


