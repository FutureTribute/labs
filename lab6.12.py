#Засько Б., КНИТ16-А
#Значение переменной x, обозначающее некоторую длину в единицах p, заменить величиной этой же длины в метрах

from enum import Enum
class measure(Enum):
    decimetre = 0.1
    kilometre = 1000
    metre = 1
    millimetre = 0.001
    centimetre = 0.01

try:
    x = float(input("length: "))
    p = measure[input("measure: ")]
    print("Значение в метрах: ", x*p.value)
except ValueError:
    print("Длина должна быть числом")