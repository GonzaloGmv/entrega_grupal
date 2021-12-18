# entrega_grupal

La dirección de github para nuestro repositorio es: [ github](https://github.com/GonzaloGmv/entrega_grupal)

### Ejercicio 1. Suma simple de una matriz
En este ejercicio hemos realizado una suma de los elementos de una matriz. Al principio hicimos la función para sumar los elementos, y pensábamos que con eso era sufuciente, pero a la hora de añadir el código que venía dado, no nos depuraba, por lo que tuvimos que crear un código para todo lo demás.

El código de este ejercicio es el siguiente:
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
### Ejercicio 3. Una suma muy grande
En este ejercicio hemos realizado la suma de los elementos de una matriz, teniendo en cuenta que estos elementos pueden ser muy grandes. Para hacer esto, nos dimos cuenta de que se hacía igual que el ejercicio 1, así que copiamos el ejercicio 1 y cambiamos alguna cosa como el nombre de la función, y la salida, para que coincidieran con el enunciado.

El código de este ejercicio es el siguiente:
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

El código de este ejercicio es el siguiente:

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

El código de este ejercicio es el siguiente:
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
### Ejercicio 7. Estudiantes de calificación
En este ejercicio había que realizar un programa que redondé unas calificaciones siguiendo unos criterios establecidos. En este ejercicio hicimos rápido la parte de la función, pero a la hora de realizar el bucle con el input, se nos complicaba, ya que utilizamos un bucle *for* y al escribir *break* o *pass* se aplicaba al for.

El código de este ejercicio es el siguiente:
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
