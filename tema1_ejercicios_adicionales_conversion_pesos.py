#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicios Python
# Ejercicio Adicionales: Conversor pesos
factor_libra=2.20462
factor_kilogramo=0.453592

kg=float(raw_input("Dame el peso en Kilogramos"))
conversor_libras = factor_libra*kg
print "Ejemplo para convertir kilogramos a libras: ",kg," kg son ", conversor_libras , "Libras"

libras=float(raw_input("Dame el peso en Libras"))
conversor_kilogramos = factor_kilogramo * libras
print "Ejemplo para convertir libras a kilogramos:", libras," libras son ", conversor_kilogramos , " Kilogramos"

'''
Convierte 120 kilos a libras
In [47]: libra=0.45359237
In [48]: kg=120
In [49]: conversor_libras=libra*kg
In [50]: conversor_libras
Out[50]: 54.4310844
'''


