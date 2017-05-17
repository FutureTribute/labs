# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Вариант 5

import math
while True:
    try:
        r=float(input("r= "))
        C=2*r*math.pi
        S=math.pi*r**2
        V=4/3*math.pi*r**3
        print("Длина окружности =",C)
        print("Площадь круга =",S)
        print("Объем шара =",V)
        cont=input("Для продолжения введите yes, для завершения любое другое значение \n")
        if cont=="yes":
            print("")
            continue
        else:
            break
    except ValueError:
        print("Ошибка: введено не число!")
        continue
