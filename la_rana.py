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
        self.extremo1 = Coordenadas(x1,y1)
        self.extremo2 = Coordenadas(x2,y2)

def buscatunel(Casillax, Casillay, tuneles):