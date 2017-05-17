# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# 5c
# Программа. Дано не менее трех различных натуральных чисел, за которыми
# следует 0. Определить, сколько раз в этой последовательности меняется знак.
# Например, в последовательности 1, -34, 8, 14, -5 знак меняется 3 раза.

while True:
    f = True
    c = 0
    d = 0
    b = 0
    a = input()
    a = a.split(", ")
    if len(a) > 3 and a.__getitem__(-1) == "0":
        try:
            for i in a:
                c = int(i)
                if ((int(c) < 0) and (int(d) >= 0)) or ((int(c) >= 0) and (int(d) < 0)):
                    b += 1
                d = int(i)
            a.pop()
            for i in a:
                if i.startswith("-"):
                    f = True
                else:
                    f = False
                    break
            if f:
                b -= 1
            print(b)
        except ValueError:
            print("Введены не целые числа")
    else:
        print("Должно быть введено не менее 3 чисел и в конце 0")
