#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
a=int(input("Coeficiente a"))
b=int(input("Coeficiente b"))
c=int(input("Coeficiente c"))
disc=(b**2)-(4*a*c)

if(a!=0):
 if(disc<0):
  print("tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(disc)))/(2*a)
  x2=(-b-(math.sqrt(disc)))/(2*a)
  print("X1 = "+str(x1)+" X2 = "+str(x2))
else:
 print("coefiente cuadratico debe ser diferente de cero")

print 'La ecuacion tiene infinitas soluciones. '