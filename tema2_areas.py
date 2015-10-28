#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejercicio 3 - Area del circulo
import math

num_pi = math.pi
print num_pi
radio=float(raw_input("Dime el radio del circulo: "))
circulo = float(num_pi * radio ** 2)
print "Area del circulo de radio %.2f = %.4f" % (radio, circulo)
