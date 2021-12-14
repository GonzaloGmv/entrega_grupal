import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
    puntosA = 0
    puntosB = 0
    for i in range(0,3):
        if a[i] < b[i]:
            puntosB += 1
        elif a[i] > b[i]:
            puntosA += 1

    puntosTotales = [puntosA, puntosB]
    return puntosTotales


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("Escribe las notas de a: ")
    a = list(map(int, input().rstrip().split()))

    print("Escribe las notas de b: ")
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()