#Засько Б., КНИТ16-А
#По s-названию страны определить название ее континента

from enum import Enum
class country(Enum):
    Germany = 1
    Cuba = 2
    Laos = 3
    Monaco = 4
    Bangladesh = 5
    Ukraine = 6
class continent(Enum):
    Asia = 1
    America = 2
    Europe = 3
s = country[input("country: ")]