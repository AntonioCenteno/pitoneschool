#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 2.- Define una función que retorne la suma de todos los divisores propios
positivos de un número dado, sin incluirse él mismo. Utiliza ésta para escribir un
programa que solicite por teclado un número entero positivo mayor que uno y muestre en
la pantalla si éste es o no perfecto.
Nota. Un número entero positivo es perfecto cuando es igual a la suma de todos sus
divisores propios positivos.
'''

def divisores_propios(numero):
    divisores=''
    for i in range(1,numero):
        if numero%i==0:
            divisores += str(i)+ " "
    return divisores

numero=abs(int(raw_input("divisores de ... : ")))
print "divisores de ",numero,":", divisores_propios(numero)