# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Для всех вариантов, №6

while True:
    try:
        day=input("Введите номер дня года: ")
        if day.isdigit():
            day=int(day)
            if day in range(1,366):
                number=day%7
                print("день недели -",number)
            else:
                print("Ошибка: день года не сответствует диапазону")
                continue
        else:
            day=float(day)
            print("Ошибка: день года должен быть целым числом")
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
