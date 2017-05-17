# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Для всех вариантов, №4

a=360
b=a/12
c=b/60
d=c/60
while True:
    try:
        hour=int(input("Часов - "))
        minute=int(input("Минут - "))
        second=int(input("Секунд - "))
        if hour not in range(0,12) or minute not in range(0,60) or second not in range(0,60):
            print("Ошибка: недопустимое значение времени")
            continue
        else:
            corner=b*hour+c*minute+d*second
            print("Угол равен",corner)
        cont=input("Для продолжения введите yes, для завершения любое другое значение \n")
        if cont=="yes":
            print("")
            continue
        else:
            break
    except ValueError:
        print("Ошибка: введено не целое число")
        continue
