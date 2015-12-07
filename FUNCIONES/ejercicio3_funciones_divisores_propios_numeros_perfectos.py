#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 3.- Utilizando la función definida en el ejercicio anterior, escribe un programa
que muestre en pantalla la secuencia de números perfectos comprendidos entre 2 y un
número entero positivo umbral que se solicitará por teclado.
Salida esperada para umbral = 10000 -> 6 28 496 8128

'''

umbral=abs(int(raw_input("divisores de ... : ")))

def suma_divisores_propios(umbral):
    suma=0
    for i in range (1,umbral):
        if umbral%i==0:
            suma=suma+i
    return suma

print "->", umbral ,":",

for i in range(1,umbral+1):
    if i == suma_divisores_propios(i):
        print i ,




