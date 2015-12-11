#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
2. Haga un programa que repetidamente pida una palabra y que muestre cuántas veces aparece en un fichero de tipo texto llamado "cuenta palabras.txt".
El programa finalizará cuando la palabra a buscar sea un punto a secas.
Nota: se considerará palabra toda secuencia de caracteres separada por espacios, por ejemplo la palabra "es" dentro de la frase "esto es un test" solamente aparece una vez.
Para simplificar suponga que no hay signos de puntuación ni caracteres no ASCII y considere palabra todo grupo de caracteres separado de otros por el espacio en blanco o fin de línea.
'''


# ejercicio 2

fichero=open('cuenta_palabras.txt')
lineas=fichero.readlines()
fichero.close()
def crea_listas(lista):
    """
    recibe la lista de las lineas y
    devuelve dos listas que contienen las palabras unicas
    y el numero de veces
    """
    lista_palabras=[]
    veces_palabra=[]
    for linea in lineas:
        for palabra in linea.split():
            if palabra not in lista_palabras:
                lista_palabras.append(palabra)
                veces_palabra.append(1)
            else:
                veces_palabra[lista_palabras.index(palabra)]+=1
    return lista_palabras,veces_palabra
palabras,veces=crea_listas(lineas)
palabra='no_punto'
while palabra !='.':
    palabra=raw_input('Introduce la palabra a buscar')
    if palabra=='.':
        break
    if palabra in palabras:
        print "La palabra",palabra,"aparece",veces[palabras.index(palabra)],"veces"
    else:
        print "La palabra",palabra,"no aparece"