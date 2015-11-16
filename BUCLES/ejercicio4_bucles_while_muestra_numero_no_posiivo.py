#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 4.- Escribir un programa que solicite un número entero n mientras que éste no sea positivo y
que muestre el dato proporcionado.
'''
numeros = -1

while numeros < 0:
    numeros = int(raw_input('Dame el numero:'))
    if numeros < 0:
        print numeros



