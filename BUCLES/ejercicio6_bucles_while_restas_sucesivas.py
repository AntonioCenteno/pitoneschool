#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 6.- Dados dos enteros a≥0 y b>0, escribe un programa que calcule el cociente y el resto de su
división entera utilizando para ello el método de restas sucesivas y mostrar el resultado en la forma:
Cociente: 17 / 3 = 5
Resto: 17 % 3 = 2

'''
a = int(raw_input('Dame el numero A:'))
b = int(raw_input('Dame el numero B:'))
resto=0
cont=0
a1=a
b1=b

hacer_resta = a>=0 and b>0

if (hacer_resta == False):
    exit('Esperamos la condicion a>=0 y b>0, no se cumple')

while a>=b:
    a=a-b
    cont=cont+1

resto=a
print "Cociente ", a1, "/", b1,"=", cont
print "Resto ", a1, "%", b1,"=", resto





