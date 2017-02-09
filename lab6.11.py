#Засько Б., КНИТ16-А
#По дате d, m, y определить дату следующего дня

days = range(1, 32)
mounths = range(1, 13)
years = range(1901, 2016)
while True:
    try:
        d = int(input("day: "))
        m = int(input("mounth: "))
        y = int(input("year: "))
        if d not in days or m not in mounths or y not in years:
            print("Введенные числа не соответствуют условию")
        else:
            if d+1 == 32:
                if m+1 == 13:
                    print("Следующий день: ", 1, 1, y + 1)
                else:
                    print("Следующий день: ", 1, m + 1, y)
            else:
                print("Следующий день: ", d + 1, m, y)
    except ValueError:
        print("Введены не целые числа")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break