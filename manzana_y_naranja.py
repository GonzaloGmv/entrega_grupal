import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    manzanasdentro = 0
    naranjasdentro = 0
    for manzana in apples:
        if(a+manzana >=s and a+manzana<=t):
            manzanasdentro += 1
    for naranja in oranges:
        if(b+naranja >=s and b+naranja<=t):
            naranjasdentro += 1
    print("Han caido " + str(manzanasdentro) + " manzanas dentro.")
    print("Han caido " + str(naranjasdentro) + " naranjas dentro.")

if __name__ == '__main__':
    print("Introduce dos valores separados por un espacio que seran la cordenada incial y final de la casa")
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    print("Introduce dos numeros separados por un espacio que son las coordenadas del manzano y el naranjo")
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    print("Introduce cuantas manzanas caen y cuantas naranjas caen")
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    print("Introduce a que distancia cae cada manzana")
    apples = list(map(int, input().rstrip().split()))

    print("Introduce a que idstancia cae cada naranja")
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)