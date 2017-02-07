#Засько Б., КНИТ16-А
#По s-названию страны определить название ее континента

from enum import Enum
class country(Enum):
    Germany = 3
    Cuba = 2
    Laos = 1
    Monaco = 3
    Bangladesh = 1
    Ukraine = 3
class continent(Enum):
    Asia = 1
    America = 2
    Europe = 3
while True:
    try:
        s = country[input("country: ")]C
        s2=continent(s.value)
        print(s2)
    except KeyError:
        print("Страна отсутствует в списке")