# Засько Б., КНИТ16-А
# В основу древнеяпонского календаря был положен 60-летний цикл, состоящий из пяти 12-летних подциклов.
# Подциклы обозначались названиями цвета: зелёный, красный, желтый, белый и черный.
# Внутри каждого подцикла, годы носили названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади,
# овцы, обезьяны, курицы, собаки и свиньи. 1984 год (год зеленой крысы) - начало очередного цикла.
# Разработать программу, которая вводит номер некоторого года нашей эры и
# печатает его название по древнеяпонскому календарю.

from enum import Enum
class colors(Enum):
    green = 0
    red = 1
    yellow = 2
    white = 3
    black = 4
class animals(Enum):
    rat = 4
    cow = 5
    tiger = 6
    hare = 7
    dragon = 8
    snake = 9
    horse = 10
    sheep = 11
    monkey = 0
    chicken = 1
    dog = 2
    pig = 3
while True:
    try:
        x = int(input("Введите год нашей эры: "))
        if x < 0:
            print("Неверное значение года")
        else:
            c = (x - 4) % 60
            c2 = 0
            while c >= 12:
                c -= 12
                c2 += 1
            c3 = colors(c2).name
            a = x % 12
            a2 = animals(a).name
            print(x, "год по древнеяпонскому календарю -", c3, a2)
    except ValueError:
        print("Неверное значение года")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break