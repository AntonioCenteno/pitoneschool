#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 12.- Dado un número natural n, escribe un programa que clasifique dicho número en:
perfecto, abundante, o, defectivo. Además, en este último caso, deberá indicarse si es o no primo.

Def.: Un número natural se dice que es perfecto si es igual a la suma de todos sus divisores propios
(exceptuando él mismo), abundante si la suma es mayor que él y defectivo si la suma es menor.
Ejemplo de salida del programa:

El número 6 es perfecto (ya que 1 + 2 + 3 = 6)
El número 12 es abundante (ya que 1 + 2 + 3 + 4 + 6 > 12)
El número 11 es defectivo y primo (ya que 1 < 11)

'''
numero=abs(int(raw_input("a: ")))
suma = 0
aux=''
resultado=''

for i in range(1,numero):
    if numero%i==0:
        aux+=str(i)+"+"
        suma += i
        if suma == numero:
            resultado = "El numero",numero," es perfecto (ya que ",aux,"=", numero ,")"
        elif suma > numero:
            resultado = "El numero",numero," es abundante (ya que ",aux,">", numero ,")"
        elif suma < numero:
            if numero%1==0 and numero%i==0:
                resultado = "El numero",numero," es defectivo Y primo (ya que ",aux,"<", numero ,")"
            else:
                resultado = "El numero",numero," es defectivo (ya que ",aux,"<", numero ,")"

print resultado
