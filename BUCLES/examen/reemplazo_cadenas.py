#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Haga un programa que pida una cadena de caracteres por teclado y que muestre otra pero conteniendo letras "e" donde antes había letras "a".
 Por ejemplo si la cadena de entrada es "una prueba", se debe mostrar por la salida "une pruebe".
 '''

cadena='ini'
buscada='a'
reemplazo='e'
i=0
while cadena<>'':
    cadena=raw_input("Cadena: ")
    i=i+1
    if buscada in cadena:
        print cadena, "pos " , i

