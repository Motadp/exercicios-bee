# Leia 3 valores de ponto flutuante e efetue o cáculo da equação de Bhaskara.
# Se não for possivel calcular a riaz mostar a menssagem "Impossivel Calcular".
#Ler 3 valores (double) A, B e C
"""
EX:Entrada
10.0 20.1 5.1            R1 = -0.29788     R2 = -1.71212

0.0 20.0 5.0             Impossivel calcular
"""


formula_bhas = (input())

formula_float = [float(x) for x in formula_bhas.split(" ")] #Esse metodo já deixa todos os valores em float.

a = formula_float[0]
b = formula_float[1]
c = formula_float[2]


delta = b**2 - 4*a*c

import math

sobre = 2*a

try:
    x1 = (-b + math.sqrt(delta)) / (sobre)
    x2 = (-b - math.sqrt(delta)) / (sobre)
 
    print("R1 = %0.5f" %x1)
    print("R2 = %0.5f" %x2)
except:
    print("Impossivel calcular")





