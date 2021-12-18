import math 
import os
import random
import re
import sys

class coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def comparate(self,x,y):
        if(self.x == x and self.y == y):
            return True
        else:
            return False

class Tunel:
    def __init__(self, x1, y1, x2, y2):
        self.extremo1 = coordenadas(x1,y1)
        self.extremo2 = coordenadas(x2,y2)

def buscatunel(Casillax, Casillay, tuneles):
    coordenadas = coordenadas(Casillax, Casillay)
    for t in tuneles:
        if(t.extremo1.comparate(Casillax, Casillay) == True):
            coordenadas.x = t.extremo2.x
            coordenadas.y = t.extremo2.y
            break
        elif(t.extremo2.comparate(Casillax, Casillay) == True):
            coordenadas.x = t.extremo1.x
            coordenadas.y = t.extremo1.y
            break
        return coordenadas
