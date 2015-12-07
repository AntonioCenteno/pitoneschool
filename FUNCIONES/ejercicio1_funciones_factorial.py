#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 1.- Define una función que retorne el factorial de un número entero no negativo
dado y escribe un programa que solicite un número entero no negativo y muestre en
pantalla éste y su factorial.
'''

def factorial(n):
    factorial=1
    for i in range(1,n):
        factorial = factorial * n
        n=n-1
    return factorial

num = abs(int(raw_input("numero factorial")))
aux = num
print "factorail de ",aux, "!", factorial(num)


