#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 5.-

'''
Escribir un programa que tome como dato un número entero y presente al
usuario una lista con tres opciones identificadas mediante una letra, tal y como se
muestra en la tabla, para que éste elija una de ellas. En función de la opción elegida
realizar el cálculo correspondiente y mostrar el resultado obtenido.
'''

num=int(raw_input("Dame un numero"))
opciones=raw_input("Ahora, que hacemos con el ?\na) Calcular el cuadrado del numero\nb) Calcular el cubo del numero\nc) Calcular el doble del numero")

if opciones == 'a':
    print "El cuadrado del numero es %i " %  int(num**2)

elif opciones == 'b':
    print "El cubo del numero es %i " % int(num**3)

elif opciones == 'c':
    print "El doble del numero es %i " % int(num*2)
else:
    print "Escoge una opcion"
