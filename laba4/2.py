# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Для всех вариантов, №2

while True:
    try:
        x=float(input("x= "))
        d=int(x*10%10)
        print("d=",d)
        cont=input("Для продолжения введите yes, для завершения любое другое значение \n")
        if cont=="yes":
            print("")
            continue
        else:
            break
    except ValueError:
        print("Ошибка: введена строка")
        continue
