#Засько Б., КНИТ16-А
#Значение переменной x, обозначающее некоторую длину в единицах p, заменить величиной этой же длины в метрах

from enum import Enum
class measure(Enum):
    decimetre = 1
    kilometre = 2
    metre = 3
    millimetre = 4
    centimetre = 5

class measure2(Enum):
    decimetre = 0.1
    kilometre = 1000
    metre = 1
    millimetre = 0.001
    centimetre = 0.01
while True:
    try:
        x = float(input("length: "))
        p = measure[input("measure: ")]
        print("Значение в метрах: ", x * measure2[p.name].value)
    except (ValueError, KeyError):
        print("Неверно введенное значение или ключ")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break