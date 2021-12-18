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

