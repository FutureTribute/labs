# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Для всех вариантов, №3

while True:
    try:
        second=input("second=")
        if second.isdigit():
            second=int(second)
            hour=second//3600
            minute=(second-hour*3600)//60
            print("hour=",hour)
            print("minute=",minute)
        else:
            second=float(second)
            print("Число секунд должно быть целым")
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
