# Засько Б., КНИТ16-А
# Функция Аккермана

import sys

print("Устанавливаеться глубина рекурсии...")
i = 0
while True:
    try:
        i += 100
        sys.setrecursionlimit(i)
    except OverflowError:
        sys.setrecursionlimit(i - 100)
        break
print("Максимальная глубина рекурсии:", sys.getrecursionlimit())


def ackermann(n, m, lvl = 0):
    """Рекурсивное вычисление функции Аккермана
    
    :param n: первое число
    :param m: второе число
    :return: функция Аккермана
    """
    global c
    c = lvl
    if n == 0:
        return m+1
    elif m == 0 and n > 0:
        return ackermann(n - 1, 1, lvl=c+1)
    elif n > 0 and m > 0:
        return ackermann(n - 1, ackermann(n, m - 1, lvl=c+1), lvl=c+1)


def ackermann2(n, m):
    """Итерационное вычисление функции Аккермана, имитируя стек
    
    :param n: первое число
    :param m: второе число
    :return: функция Аккермана
    """
    stack = []
    while True:
        if not n:
            if not stack:
                return m + 1
            n, m = stack.pop(), m + 1
        elif not m:
            n, m = n - 1, 1
        else:
            stack.append(n - 1)
            m -= 1


while True:
    try:
        c = None
        f = int(input("Первое число: "))
        f1 = int(input("Второе число: "))
        print("Результат рекурсивно: {}, глубина рекурсии: {}".format(ackermann(f, f1), c))
        print("Результат итерационно: {}".format(ackermann2(f, f1)))
    except ValueError:
        print("Введены некоректные данные")
