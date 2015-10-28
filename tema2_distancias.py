#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Convertidor de metros a yardas, pies, pulgadas ... ")
metros = float(raw_input("Escriba una distancia en metros: "))

# equivalencias a metros de yardas, pies y pulgadas
yarda = 1.0936 # 1 m
pie = 3.2808 # 1 m
pulgada = 39.370 # 1m

print '#'*50
print " %s metros equivalen a %s yardas " % (metros, float(metros*yarda))
print " %s metros equivalen a %s pies " % (metros, float(metros*pie))
print " %s metros equivalen a %s pulgadas " % (metros, float(metros*pulgada))
print '#'*50

