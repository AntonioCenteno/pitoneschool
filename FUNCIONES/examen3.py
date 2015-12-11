#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Se dispone de una lista con valores de puntos (x,y,z) de la forma [x1, y1, z1, x2, y2, z2, ... xn, yn, zn]. Se pide hacer una función que permita obtener tres listas: [x1, x2, ... xn] [y1, y2, ... yn] y [z1, z2, ... zn].
La función debe tener cuatro parámetros, el primero será la lista original que no debe modificarse y los otros tres serán sendas listas inicialmente vacías que tras la llamada tendrán lo pedido anteriormente.

Ejemplo de llamada:

puntos=[11,23,40,5,8,3,27,15,9,7,1,12]
X=[]
Y=[]
Z=[]

extraer(puntos,X,Y,Z)
# X debe ser [11,5,27,7]
# Y debe ser [23,8,15,1]
# Z debe ser [40,3,9,12]
'''

def extraer(puntos, X,Y,Z):
    for i in range(0,len(puntos),3):
        X.append(puntos[i])
    for i in range(1,len(puntos),3):
        Y.append(puntos[i])
    for i in range(2,len(puntos),3):
        Z.append(puntos[i])

    return X,Y,Z

puntos=[11,23,40,5,8,3,27,15,9,7,1,12]
X=[]
Y=[]
Z=[]

print extraer(puntos,X,Y,Z)