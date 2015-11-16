#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 1.- Escribir un programa que lea del teclado carácter a carácter. La lectura de caracteres se
termina con ".". El programa debe mostrar el número de veces que se ha introducido el carácter "a".
'''
contador = 0;
buscado = "a"
texto = ''

while texto != ".":
    texto = raw_input('Dame el caracter:')
    for letra in texto:
        if letra == buscado:
            contador = contador + 1


print "El caracter 'a' se ha repetido " , contador, "veces"

