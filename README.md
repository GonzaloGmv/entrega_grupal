# entrega_grupal

La dirección de github para nuestro repositorio es: [ github](https://github.com/GonzaloGmv/entrega_grupal)

### Ejercicio 1
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
### Ejercicio 3
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
