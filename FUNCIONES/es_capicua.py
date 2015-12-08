#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Se desea hacer un programa que permita saber si un número es capicúa

'''
def es_capicua(numero):
    return str(abs(numero))==str(abs(numero))[::-1]


numero=int(raw_input('Introduce el numero'))
print numero,"es capicua:",es_capicua(numero)