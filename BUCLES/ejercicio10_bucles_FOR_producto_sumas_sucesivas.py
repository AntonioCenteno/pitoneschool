#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 10.- Dados dos enteros a≥0 y b≥0, escribir un programa que calcule su producto utilizando
para ello el método de sumas sucesivas y mostrar el resultado.

'''
a=abs(int(raw_input("a: ")))
b=abs(int(raw_input("b: ")))
suma_producto=0

for i in range(a):
    suma_producto += b

print suma_producto


