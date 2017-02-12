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
        if d in days and m in mounths and y in years:
            if m + 1 in mounths:
                if d + 1 in days:
                    print("Следующий день: ", d + 1, m, y)
                else:
                    print("Следующий день: ", 1, m + 1, y)
            else:
                print("Следующий день: ", 1, 1, y + 1)
        else:
            print("Введенные числа не соответствуют условию")
    except ValueError:
        print("Введены не целые числа")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break