# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Для всех вариантов, №5

import math
a=30
while True:
    try:
        corner=float(input("Введите значение угла: "))
        if 0<corner<360:
            hour=math.floor(corner//a)
            minute=math.floor((corner%(hour*a))*2)
            print("Время - ",hour,":","%02d" % minute,sep="")
        else:
            print("Ошибка: градус не сответствует диапазону")
            continue
        cont=input("Для продолжения введите yes, для завершения любое другое значение \n")
        if cont=="yes":
            print("")
            continue
        else:
            break
    except ValueError:
        print("Ошибка: введена строка")
        continue
