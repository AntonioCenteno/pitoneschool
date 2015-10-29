#!/usr/bin/env python
# -*- coding: utf-8 -*-

b=int(input("Introduce un numero: "))
num_len = len(str(abs(b)))

if num_len>=4 and num_len<=6:
    print "Tu numero tiene entre 4 y 6 cifras"
else:
    print "Tu numero NO tiene entre 4 y 6 cifras, tiene: " , num_len