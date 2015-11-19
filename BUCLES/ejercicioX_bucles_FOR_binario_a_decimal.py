#!/usr/bin/env python
# -*- coding: utf-8 -*-


string =raw_input("Codigo binario: ")
ini =0
num =7
for element in string:
    aux = int(element)*2**num
    num=num-1
    ini = ini+aux
print ini


