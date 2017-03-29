# Засько Б., КНИТ16-А
# Алгоритм Кнута-Морриса-Пратта

from timeit import timeit

S = input("Введите строку: ")
subS = input("Введите подстроку: ")

t = [0] * len(subS)
j = 0
for i in range(1, len(subS)):
    while j > 0 and subS[i] != subS[j]:
        j = t[j-1]
    if subS[i] == subS[j]:
        j += 1
    t[i] = j

m = k = 0
while k < len(S) and m < len(subS):
    if subS[m] == S[k]:
        m += 1
        k += 1
    elif m == 0:
        k += 1
    else:
        m = t[m - 1]
else:
    if m == len(subS):
        print("Элемент найден в позиции", k - m)
    else:
        print("Элемент не найден")
