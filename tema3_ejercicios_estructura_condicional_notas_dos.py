#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6.-

'''
Escribir un programa que lea 4 notas (tipo INT) entre 0 y 100, que calcule
la media aritmética de esas cuatro puntuaciones y visualice la media obtenida así como
su carácter asociado de acuerdo a la siguiente relación:
[90,100] A
[80,90) B
[70,80) C
[60,70) D
[0,60) E
'''
nota1=int(raw_input("Dame la nota 1: "))
nota2=int(raw_input("Dame la nota 2: "))
nota3=int(raw_input("Dame la nota 3: "))
nota4=int(raw_input("Dame la nota 4: "))

if nota1 in range(0,101) and nota2 in range(0,101) and nota3 in range(0,101) and nota4 in range(0,101):
    nota_media = int((nota1 + nota2 + nota3 + nota4) / 4)
    car = ''
    if nota_media in range(-1,61):
        car = 'E'
    elif nota_media in range(60-1,71):
        car = 'D'
    elif nota_media in range(70-1,81):
        car = 'C'
    elif nota_media in range(80-1,91):
        car = 'B'
    elif nota_media in range(90-1,101):
        car = 'A'

    print '#'*50
    print  "La nota media es %i "  % (nota_media)
    print  "El caracter asociado es %s "  % (car)
    print '#'*50

else:
    print "No estas en el rango pedido"

