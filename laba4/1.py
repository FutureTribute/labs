# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Для всех вариантов, №1

while True:
    try:
        x=input("x= ")
        y=input("y= ")
        if x.isdigit() and y.isdigit():
            x=int(x)
            y=int(y)
            x,y = y,x
            print("x=",x)
            print("y=",y)
        else:
            x=float(x)
            y=float(y)
            print("Введите целые числа")
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
