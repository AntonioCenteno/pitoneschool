#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Haga un programa que pida una cadena de caracteres por teclado y que muestre otra pero conteniendo letras "e" donde antes había letras "a".
Por ejemplo si la cadena de entrada es "una prueba", se debe mostrar por la salida "une pruebe".

'''
cadena="esta es una cadena muy largo para reemplazarla"
aux=''
buscada='a'
rem='e'

for i in range(len(cadena)):
    if cadena[i]==buscada:
        aux+=rem
    else:
        aux+=cadena[i]

print aux