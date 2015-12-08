#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
En un fichero se encuentran los nombres de diversos ríos (pueden ser varias palabras) seguidos de su longitud en kilómetros.
Hay un río por cada línea del fichero y todos los datos están separados por espacios en blanco.
Se desea conocer el nombre y la longitud del río más largo así como la longitud media de todos los ríos contenidos en el fichero
'''

f=open("rios.txt","r")
rios=[]
longitudes=[]

def obtener_longitud(cadena):
	lista_cadena=cadena.split()
	numero_elementos=len(lista_cadena)
	longitud=float(lista_cadena[numero_elementos-1])
	return longitud

def obtener_nombre(cadena):
	lista_cadena=cadena.split()
	numero_elementos=len(lista_cadena)
	nombre = lista_cadena[0]
	for i in range(1,numero_elementos-1):
		nombre=nombre+" "+lista_cadena[i]
	return nombre

for linea in f:
	rios.append(obtener_nombre(linea))
	longitudes.append(obtener_longitud(linea))
f.close()

def media_longitudes(lista):
    suma=0
    total_items = len(lista)
    for dato in lista:
        suma=suma+dato
    return suma/total_items



longitud_max =  max(longitudes)
posicion =  longitudes.index(longitud_max)

print "El rio con mayor longitud es ", rios[posicion], "con", max(longitudes)
print "La media de longitudes de todos los rios es:" , media_longitudes(longitudes)

