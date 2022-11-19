"""
PROYECTO FINAL 
ECUACIONES DIFERENCIALES

PROGRAMA PARA MEDIR EL TIEMPO DEL ALGORITMO QUCKSORT CON DISTINTAS LONGITUDES DE ARRAY

ROBERTO RIOS 20979
JOSE SANTISTEBAN 21153
"""

import time
import random
from quicksort import *
import sys

sys.setrecursionlimit(10**6)

print("Bienvenido a la medición de tiempo de quicksort")
print("-----------------------------------------------")
print("Ingrese el tamaño de array a generar:")
n = int(input())
data = [0] * n

#generar array de numeros aleatorios
for i in range(n):
    data[i] = random.randint(0,10000)


size = len(data)

st = time.time()
quickSort(data, 0, size - 1)

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

