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