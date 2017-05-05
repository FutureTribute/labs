# Засько Б., КНИТ16-А

import numpy as np
import sys

sys.setrecursionlimit(10000)


def ackermann(n, m):
    if n == 0:
        return m+1
    elif m == 0 and n > 0:
        return ackermann(n - 1, 1)
    elif n > 0 and m > 0:
        return ackermann(n - 1, ackermann(n, m - 1))


def ackermann2(n, m):
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
        f = int(input("Первое число: "))
        f1 = int(input("Второе число: "))
        print(ackermann(f, f1))
        print(ackermann2(f, f1))
    except ValueError:
        print("Введены некоректные данные")
