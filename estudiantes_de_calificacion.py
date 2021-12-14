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