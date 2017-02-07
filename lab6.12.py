#Засько Б., КНИТ16-А
#Значение переменной x, обозначающее некоторую длину в единицах p, заменить величиной этой же длины в метрах

class measure(Enum):
    decimetre = 1
    kilometre = 2
    metre = 3
    millimetre = 4
    centimetre = 5
x = float(input("length: "))
p = measure[input("measure: ")]
