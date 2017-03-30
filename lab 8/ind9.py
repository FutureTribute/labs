# Засько Б., КНИТ16-А
# Информация о заявках на склад в виде названия товара,
# его веса и допускаемой к обработке в этом магазине
# виду тары. Разработать программу, которая бы
# осуществляла расчет потребностей магазинов в
# заданом продукте в килограммах.

from enum import Enum
import numpy as np


class Shops(Enum):
    n111 = ["No", "Оболонь"]
    n112 = ["Yes", "Дарница"]
    n113 = ["No", "Троещина"]
    n114 = ["Yes", "Оболонь"]
    n115 = ["Yes", "Оболонь"]
    n116 = ["No", "Дарница"]


class Items(Enum):
    v1 = "onions"
    v2 = "tomatoes"
    f1 = "apples"
    f2 = "oranges"


class Requests(Enum):
    r7 = ["n114", "v1", 3]
    r21 = ["n116", "f1", 8]
    r70 = ["n111", "f2", 12]
    r135 = ["n113", "f1", 60]
    r222 = ["n112", "v1", 9]
    r500 = ["n115", "v2", 23]
    r501 = ["n111", "f1", 42]
    r634 = ["n113", "f1", 34]
    r789 = ["n116", "f2", 24]

y = list()
for i in Items.__members__.values():
    y.append(i.value)
z = set()
for i in Shops.__members__.values():
    z.add(i.value[1])
z = list(z)

while True:
    x = input("Введите наименование интересуемого товара (для получения списка товаров введите list):\n")
    if x == "list":
        print(y)
        continue
    elif x not in y:
        print("Введено неверное наименование товара\n")
        continue
    else:
        while True:
            x2 = input("\nДля вывода информации по раёнам введите его название, по всему городу - all\n"
                       "(для получения списка раёнов введите list2): ")
            if x2 == "list2":
                print(z)
                continue
            elif (x2 != "all") and (x2 not in z):
                print("Введено некоректное значение")
                continue
            else:
                countY = 0
                countN = 0
                for j in Items.__members__.values():
                    if j.value == x:
                        for k in Requests.__members__.values():
                            if k.value[1] == Items(x).name:
                                if x2 != "all":
                                    if Shops[k.value[0]].value[1] == x2:
                                        if Shops[k.value[0]].value[0] == "No":
                                            countN += k.value[2]
                                        else:
                                            countY += k.value[2]
                                else:
                                    if Shops[k.value[0]].value[0] == "No":
                                        countN += k.value[2]
                                    else:
                                        countY += k.value[2]
                count = "{:^5}".format(str(countN + countY) + " кг.")
                countN = "{:^19}".format(str(countN) + " кг.")
                countY = "{:^18}".format(str(countY) + " кг.")
                a = np.array([['Для тары типа "Да"', 'Для тары типа "Нет"', 'Всего'],
                             [countY, countN, count]])
                print("\nЗаявки на {} по {}".format(x, x2))
                print(a)
                break
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break
