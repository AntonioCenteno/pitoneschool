#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejercicio 1
# Ejercicio 2

nombre=raw_input("Por favor, escribe tu nombre: ")
nota1=float(raw_input("Dame la nota 1: "))
nota2=float(raw_input("Dame la nota 2: "))
nota_media = float((nota1 + nota2) / 2)
print '#'*50
print  "La nota media de %s es %.2f "  % (nombre,nota_media)
print  "Aprueba la asignatura: " , ( (nota1+nota2) / 2 ) >= 5.0
print '#'*50



