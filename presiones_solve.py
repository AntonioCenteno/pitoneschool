#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 3
# Presión de los neumaticos
# Deben estar dentro de unos limites (25 y 45 ) y tener holgura de 3 psi.
UMBRAL_PSI = 3
PSI_MIN = 25
PSI_MAX = 45
correcto_delanteras = False
correcto_traseras = False

rueda_a = float(raw_input("Indica la presion de la rueda delantera derecha (0.00)"))
rueda_b = float(raw_input("Indica la presion de la rueda delantera izquierda (0.00)"))
rueda_c = float(raw_input("Indica la presion de la rueda trasera derecha (0.00)"))
rueda_d = float(raw_input("Indica la presion de la rueda trasera izquierda (0.00)"))

# eje delantero
if (rueda_a >= PSI_MIN and rueda_a <= PSI_MAX) and (abs(rueda_b-rueda_a) <= UMBRAL_PSI):
    if (rueda_b >= PSI_MIN and rueda_b <= PSI_MAX):
        correcto_delanteras = True

# eje trasero
if (rueda_c >= PSI_MIN and rueda_c <= PSI_MAX)  and (abs(rueda_d-rueda_c) <= UMBRAL_PSI):
    if (rueda_d >= PSI_MIN and rueda_d <= PSI_MAX):
        correcto_traseras = True

if correcto_delanteras and correcto_traseras:
    print "Las presiones son CORRECTAS"
    print "Presion rueda delantera derecha:",rueda_a
    print "Presion rueda delantera izquierda:",rueda_b
    print "Presion rueda trasera derecha:",rueda_c
    print "Presion rueda trasera izquierda:",rueda_d
else:
    print "Las presiones son INCORRECTAS"

