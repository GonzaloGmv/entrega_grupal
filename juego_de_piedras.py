#!/bin/python3 
import math
import os 
import random 
import re 
import sys 
# 
# # Complete the 'gameOfStones' function below. 
# 
# The function is expected to return a STRING. 
# The function accepts INTEGER n as parameter. 
#
def gameOfStones(n):
    turno = 0
    while n >= 1: 
        if turno % 2 == 0:
            if n == 1:
                n = n - 1
                result = 'P2 winner'
            elif n == 2:
                n = n - 2
                result = 'P1 winner'
            elif n == 3:
                n = n - 3
                result = 'P1 winner'
            elif n == 4:
                n = n - 3
                result = 'P1 winner'
            elif n == 5:
                n = n - 5
                result = 'P1 winner'
            elif n == 6:
                n = n - 5
                result = 'P1 winner'
            elif n == 7:
                a = random.randrange(3)
                if a == 0:
                    n = n - 2
                elif a == 1:
                    n = n - 3
                elif a == 2:
                    n = n - 5
            else:
                if n - 2 == 7:
                    n = n - 2
                elif n - 3 == 7:
                    n = n - 3
                elif n - 5 == 7:
                    n = n - 5
                elif n - 5 != 6 and n - 5 != 5 and n - 5 != 4 and n - 5 != 3:
                    n = n - 5
                elif n - 3 != 6 and n - 3 != 5:
                    n = n - 3
                elif n - 2 != 6:
                    n = n - 2
                else: 
                    a = random.randrange(3)
                    if a == 0:
                        n = n - 2
                    elif a == 1:
                        n = n - 3
                    elif a == 2:
                        n = n - 5
            turno += 1
        elif turno % 2 == 1:
            if n == 1:
                n = n - 1
                result = 'P1 winner'
            elif n == 2:
                n = n - 2
                result = 'P2 winner'
            elif n == 3:
                n = n - 3
                result = 'P2 winner'
            elif n == 4:
                n = n - 3
                result = 'P2 winner'
            elif n == 5:
                n = n - 5
                result = 'P2 winner'
            elif n == 6:
                n = n - 5
                result = 'P2 winner'
            elif n == 7:
                a = random.randrange(3)
                if a == 0:
                    n = n - 2
                elif a == 1:
                    n = n - 3
                elif a == 1:
                    n = n - 5
            else:
                if n - 2 == 7:
                    n = n - 2
                elif n - 3 == 7:
                    n = n - 3
                elif n - 5 == 7:
                    n = n - 5
                elif n - 5 != 6 and n - 5 != 5 and n - 5 != 4 and n - 5 != 3:
                    n = n - 5
                elif n - 3 != 6 and n - 3 != 5:
                    n = n - 3
                elif n - 2 != 6:
                    n = n - 2
                else: 
                    a = random.randrange(3)
                    if a == 0:
                        n = n - 2
                    elif a == 1:
                        n = n - 3
                    elif a == 2:
                        n = n - 5
            turno += 1
    return result

if __name__ == '__main__': 
    fptr = sys.stdout 
    t = int(input("Introduzca el numero de casos: ").strip()) 
    for t_itr in range(t): 
        n = int(input("Introduzca el numero de piedras para este caso: ").strip())
        result = gameOfStones(n) 
        fptr.write(result + '\n') 
    fptr.close()