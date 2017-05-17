# Засько Богдан
# КНИТ16-А
# №19; Выполните по шагам с фиксацией пошаговых значений основных переменных
# программу нахождения суммы и произведения положительных вещественных
# элементов квадратной матрицы размерности 3. Внутреннее представление
# матрицы А организовать в виде вложенных списков.

while True:
    matr= [[], [], []]
    sm=0
    mm=1
    for f in range(0,len(matr)):
        for s in range(0, len(matr)):
            while True:
                try:
                    matr[f].append(float(input("Введите элемент а{}{}: ".format(f+1, s+1))))
                    break
                except ValueError:
                    print("Введено не число")
            if matr[f][s]>=0:
                sm += matr[f][s]
                mm *= matr[f][s]
    else:
        print(matr[0])
        print(matr[1])
        print(matr[2])
        print("Сумма положительных элеметов матрицы = ",sm,"\nПроизведение положительных членов матрицы = ",mm)
        print()
        cont=input("Для продолжения введите yes, для завершения любое другое значение \n")
        if cont=="yes":
            print("")
            continue
        else:
            break
