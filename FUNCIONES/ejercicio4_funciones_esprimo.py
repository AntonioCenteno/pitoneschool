#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio 4.- Define una función, es_primo, que retorne cierto si un número entero dado
es primo y falso en caso contrario. En la definición, se considerará que el número 1 no es
primo. Escribe un programa que de forma repetitiva solicite por teclado un número entero mayor
que cero y muestre en pantalla si es o no primo, en la forma: El número 100 no es primo.
El programa deberá finalizar cuando el dato que se introduzca por teclado no cumpla el requisito de ser un entero mayor que cero

'''

def es_primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return True

numero=1

while numero>0:
    try:
        numero = abs(int(raw_input("Dame el numero primo")))
        if numero<=0:
            break
        if es_primo(numero):
            print "El numero %s es primo" % numero
        else:
            print "El numero %s NO es primo" % numero
    except:
        print "No entiendo, para salir debes escribir 0 o algo negativo"


