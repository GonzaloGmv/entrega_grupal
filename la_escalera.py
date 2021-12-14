def staircase(n):
    for i in range(n):
        print(" " * (n - (i + 1)), '# ' *(i + 1))

def staircase2(n):
    for i in range(n):
        print(" " * (n - (i + 1)), '#' *(i + 1))

def staircase3(n):
    for i in range(n):
        print('#' *(i + 1), " " * (n - (i + 1)))

while True:
    n = input("Escriba un número entero: ")
    try:
        n = int(n)
        break
    except:
        pass

staircase(n)
staircase2(n)
staircase3(n)