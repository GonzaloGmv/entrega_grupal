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