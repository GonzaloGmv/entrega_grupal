# entrega_grupal

La dirección de github para nuestro repositorio es: [ github](https://github.com/GonzaloGmv/entrega_grupal)

### Ejercicio 1. Suma simple de una matriz
En este ejercicio hemos realizado una suma de los elementos de una matriz. Al principio hicimos la función para sumar los elementos, y pensábamos que con eso era sufuciente, pero a la hora de añadir el código que venía dado, no nos depuraba, por lo que tuvimos que crear un código para todo lo demás.

* El código de este ejercicio es el siguiente:
```
def simpleArraySum(ar):
    suma = 0
    n = len(ar)
    for i in range(n):
        for j in range(n):
            suma = suma + ar[i][j]
    print("La suma de todos los elementos de la matriz es: ", suma)

while True:
    n = input("Escriba el tamaño de su  matriz: ")
    try:
        n = int(n)
    except:
        pass
    else:
        break 

while True:
    elementos = input("Escriba los elementos de su matriz separados por espacios: ")
    elementos = elementos.split()
    try:
        for i in range(len(elementos)):
            elementos[i] = int(elementos[i])
    except:
        pass
    else:
        if len(elementos) == n ** 2:
            break

matriz = []
for i in range(n):
    matriz.append([''] * n)
    
k = 0
while k < len(elementos):
    for i in range(n):
        for j in range(n):
            matriz[i][j] = elementos[k]
            k = k + 1
print("La matriz de orden ", n, " es: ")
for i in range(n):
    print(matriz[i])
simpleArraySum(matriz)
```

## Ejercicio 2. Comparar problemas

La tarea consiste en encontrar los puntos de comparacion de dos personas teniendo en cuenta las nota que ham sacado. Cuando se pida hay que introducir las tres notas de la primera persona y mas tarde las tres notas de la segunda persona. La que mejor nota tenga recibira mas puntos que la otra. El ejercicio devuelve una matriz en funcion del resultado

* El código de este ejercicio es el siguiente:

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
            fptr = sys.stdout
            print("Escribe las notas de a: ")
            a = list(map(int, input().rstrip().split()))

            print("Escribe las notas de b: ")
            b = list(map(int, input().rstrip().split()))
            result = compareTriplets(a, b)

            fptr.write(' '.join(map(str, result)))
            fptr.write('\n')

            fptr.close()


### Ejercicio 3. Una suma muy grande
En este ejercicio hemos realizado la suma de los elementos de una matriz, teniendo en cuenta que estos elementos pueden ser muy grandes. Para hacer esto, nos dimos cuenta de que se hacía igual que el ejercicio 1, así que copiamos el ejercicio 1 y cambiamos alguna cosa como el nombre de la función, y la salida, para que coincidieran con el enunciado.

* El código de este ejercicio es el siguiente:
```
def aVeryBigSum(ar):
    suma = 0
    n = len(ar)
    for i in range(n):
        for j in range(n):
            suma = suma + ar[i][j]
    print("long: ", suma)

while True:
    n = input("Escriba el tamaño de su  matriz: ")
    try:
        n = int(n)
    except:
        pass
    else:
        break 

while True:
    elementos = input("Escriba los elementos de su matriz separados por espacios: ")
    elementos = elementos.split()
    try:
        for i in range(len(elementos)):
            elementos[i] = int(elementos[i])
    except:
        pass
    else:
        if len(elementos) == n ** 2:
            break

matriz = []
for i in range(n):
    matriz.append([''] * n)
    
k = 0
while k < len(elementos):
    for i in range(n):
        for j in range(n):
            matriz[i][j] = elementos[k]
            k = k + 1
print("La matriz de orden ", n, " es: ")
for i in range(n):
    print(matriz[i])
aVeryBigSum(matriz)
```
### Ejercicio 4. La escalera
En este ejercicio había que realizar una escalera de n filas utilizando "#" y espacios. Al hacer este ejercicio, nos hemos dado cuenta de que no se podía hacer una escalera centrada, ya que un "#" ocupa lo mismo que un espacio, por lo que siempre quedarían alineadas a un lado o al otro. La única forma que hemos encontrado de que quede centrado es con un espacio después de cada #.

+ El código de este ejercicio es el siguiente:

```
def staircase(n):
    for i in range(n):
        print(" " * (n - (i + 1)), '# ' *(i + 1))

while True:
    n = input("Escriba un número entero: ")
    try:
        n = int(n)
        break
    except:
        pass
staircase(n)
```
### Ejercicio 5. Juego de piedras
En este ejercicio había que realizar una simulación de un juego en el que hay 2 jugadores que tienen que eliminar unas piedras de un tablero, y pueden eliminar 2, 3 o 5. Pierde el que no pueda eliminar ninguna más.
Para realizar esto, hemos creado una función que contenía un bucle que dependiendo del número de piedras que haya, quitaba un número es estas u otro, haciendo todo lo posible por ganar.

* El código de este ejercicio es el siguiente:
```
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
``` 

# Ejercicio 6. La rana en el laberinto

La primera linea tiene que contener tres enteros separados por espacios (n, m y k), los cuales denotan las dimensiones del laberinto y el numero de tuneles que tiene. Para esta tarea usamos el codigo de la tarea del laberinto hecha previamente e incluimos la rana la cual puede saltar los tuneles y muros para intentar llegar a la salida.

* El código de este ejercicio es el siguiente:

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
            Coordenadas = coordenadas(Casillax, Casillay)
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

        def exploracion(Casillax, Casillay, laberinto, n, m, tuneles):
            num = 0
            den = 0
            probabilidad = 0.0
            if(Casillax > 0 and laberinto[Casillax - 1][Casillay] != "#"):
                den += 1
                if(laberinto[Casillax - 1][Casillay] == "%"):
                    num += 1
            if(Casillax < n-1 and laberinto[Casillax + 1][Casillay] != "#"):
                den += 1
                if(laberinto[Casillax + 1][Casillay] == "%"):
                    num += 1
            if(Casillay < m-1 and laberinto[Casillax][Casillay + 1] != "#"):
                den += 1
                if(laberinto[Casillax][Casillay + 1] == "%"):
                    num += 1
            if(Casillay > 0 and laberinto[Casillax][Casillay - 1] != "#"):
                den += 1
                if(laberinto[Casillax][Casillay - 1] == "%"):
                    num += 1
            if (den == 0):
                return probabilidad
            probabilidad = num / den

            if(Casillax > 0 and laberinto[Casillax - 1][Casillay] == "$"):
                laberintocopia = laberinto
                coordenadas = buscatunel(Casillax - 1, Casillay, tuneles)
                laberintocopia[Casillax][Casillay] = "#"
                probabilidad += exploracion(coordenadas.x, coordenadas.y, laberintocopia, n, m, tuneles)/den
            if(Casillax < n-1 and laberinto[Casillax + 1][Casillay] == "$"):
                laberintocopia = laberinto
                coordenadas = buscatunel(Casillax + 1, Casillay, tuneles)
                laberintocopia[Casillax][Casillay] = "#"
                probabilidad += exploracion(coordenadas.x, coordenadas.y, laberintocopia, n, m, tuneles)/den
            if(Casillay < m-1 and laberinto[Casillax][Casillay + 1] == "$"):
                laberintocopia = laberinto
                coordenadas = buscatunel(Casillax, Casillay + 1, tuneles)
                laberintocopia[Casillax][Casillay] = "#"
                probabilidad += exploracion(coordenadas.x, coordenadas.y, laberintocopia, n, m, tuneles)/den
            if(Casillay > 0 and laberinto[Casillax][Casillay - 1] == "$"):
                laberintocopia = laberinto
                coordenadas = buscatunel(Casillax, Casillay - 1, tuneles)
                laberintocopia[Casillax][Casillay] = "#"
                probabilidad += exploracion(coordenadas.x, coordenadas.y, laberintocopia, n, m, tuneles)/den
            return probabilidad

        if __name__ == "__main__":
            print("Dimensiones del laberinto y numero de tuneles: (filas columnas tuneles)")
            first_multiple_input = input().rstrip().split()

            n = int(first_multiple_input[0])

            m = int(first_multiple_input[1])

            k = int(first_multiple_input[2])

            laberinto = []
            for n_itr in range(n):
                print("Fila" + str(n_itr) + " del laberinto: (# muro, % salida, * bomba, $ vacia o tunel)")
                row = input()
                laberinto.append(list(row))
            tuneles=[]
            for k_itr in range(k):
                print("Coordenadas(i1 j1 i2 j2) del tunel "+ str(k_itr))
                second_multiple_input = input().rstrip().split()

                i1 = int(second_multiple_input[0])
                j1 = int(second_multiple_input[1])
                i2 = int(second_multiple_input[2])
                j2 = int(second_multiple_input[3])

                tuneles.append(Tunel(i1, j1, i2, j2))

        print("Coordenadas iniciales de la rana: ")
        third_multiple_input = input().rstrip().split()

        pos1 = int(third_multiple_input[0])
        pos2 = int(third_multiple_input[1])
        probabilidad = exploracion(pos1, pos2, laberinto, n, m, tuneles)
        print(probabilidad)


### Ejercicio 7. Estudiantes de calificación
En este ejercicio había que realizar un programa que redondé unas calificaciones siguiendo unos criterios establecidos. En este ejercicio hicimos rápido la parte de la función, pero a la hora de realizar el bucle con el input, se nos complicaba, ya que utilizamos un bucle *for* y al escribir *break* o *pass* se aplicaba al for.

* El código de este ejercicio es el siguiente:
```
def gradingStudents(calificaciones):
    for i in range(len(calificaciones)):
        if calificaciones[i] > 40:
            redondeo = int(calificaciones[i] / 5 + 1)
            if redondeo * 5 - calificaciones[i] < 3:
                calificaciones[i] = redondeo * 5
    print(calificaciones)

continuar = False
while True:
    notas = input("Escriba las calificaciones separadas por espacios: ")
    lista_notas = notas.split()
    try:
        for i in range(len(lista_notas)):
            lista_notas[i] = int(lista_notas[i])
    except:
        pass
    else:
        for i in range(len(lista_notas)):
            if lista_notas[i] < 0 or lista_notas[i] > 100:
                continuar = True
                break
        if continuar == True:
            pass
        else:
            break
        
gradingStudents(lista_notas)
```

# Ejercicio 8. Manzana y naranja

En este ejercicio tienes que trabajar con coordenadas. Tienes que introducir las coordenadas de los arboles y la de la casa que estará entre los dos arboles. Posteriormente deberás introducir cuantas manzanas y cuantas naranjas caen mas la distancia del arbol a la que cae cada una. El ejercicio te devuelve cuantas naranjas y manzanas caen dentro de la casa.

* El código para este ejercicio es el siguiente:

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
