#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 10.- Dados dos números enteros n (n≥0) y a (a>0) encontrar, si existe, el menor entero x del
intervalo [0, n] para el que se cumpla lo siguiente: la diferencia entre las sumas de los valores enteros
de los intervalos [n-x, n] y [0, x] coincide con a
'''

def suma(a,b):
    #suma de a a b ambos inclusive
    s=0
    for i in range(a,b+1):
        s=s+i
        print s
    return s


def busca(a,b):
    for i in range(n/2+1):
        if a==suma(n-x,n):
            return x,True
        return -1, False

n=int(raw_input("Valor de n:"))
x=int(raw_input("Valor de a"))
encontrado = False


x,encontrado = busca(a,n)

if encontrado:
    print "encontrado x valor " , x
else:
    print "No encontrado"
