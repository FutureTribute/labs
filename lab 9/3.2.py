# Засько Б., КНИТ16-А

from timeit import timeit

setup = '''
import numpy as np
choice = int(input("""Для рандомного заполнения массива введите 1, для ручного введите 2: """))
if choice == 1:
    n = int(input("Количество элементов в массиве: "))
    arr = np.random.randint(n, size=n)
elif choice == 2:
    n = int(input("Количество элементов в массиве (до 30): "))
    arr = np.zeros(n)
    for i in arr:
        x = int(input("Введите значение для элемента", i + 1, sep="", end=" "))
        arr[i] = x
abc = input("Выводить ли массив на экран? y/n: ")
if abc == "y":
    print("Массив:")
    print(arr)
'''


stmt = '''
def cocktail_sort(a):
    """Сортировка перемешиванием (cocktail sort)

        Развитие пузырьковой сортировки. Отличия от нее заключаются в том,
        что при прохождении части массива, происходит проверка, были ли перестановки.
        Если их не было, значит, эта часть массива уже упорядочена и она исключается из дальнейшей обработки.
        Кроме того, при прохождении массива от начала к концу, минимальные элементы перемещаются в самое начало,
        а максимальный элемент сдвигается к концу массива."""
    for k in range(len(a) - 1, 0, -1):
        flag = False
        for i in range(k, 0, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                flag = True
        for i in range(k):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        if not flag:
            return a
'''

time = timeit(stmt, setup, number=1)
print("Время выполнения cocktail_sort: {:f} секунд".format(time))

stmt1 = '''
def shell_sort(a):
    """Сортировка Шелла (shell sort)

        Алгоритм сортировки, являющийся усовершенствованным вариантом сортировки вставками.
        Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом,
        но и на определённом расстоянии друг от друга"""
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            val = a[i]
            j = i
            while j >= gap and a[j - gap] > val:
                a[j] = a[j - gap]
                j -= gap
            a[j] = val
        gap //= 2
    return a
'''

time1 = timeit(stmt1, setup, number=1)
print("Время выполнения shell_sort: {:f} секунд".format(time1))

stmt2 = '''
def heap_sort(a):
    """Пирамидальная сортировка (heap sort)

        Алгоритм сортировки, работающий в худшем, в среднем и в лучшем случае (то есть гарантированно)
        за Θ(n log n) операций при сортировке n элементов.
        Количество применяемой служебной памяти не зависит от размера массива (то есть, O(1))"""
    def sift_down (parent, limit):
        item = a[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and a[child] < a[child + 1]:
                child += 1
            if item < a[child]:
                a[parent] = a[child]
                parent = child
            else:
                break
        a[parent] = item

    length = len(a)
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    for index in range(length - 1, 0, -1):
        a[0], a[index] = a[index], a[0]
        sift_down(0, index)
        return a
'''

time2 = timeit(stmt2, setup, number=1)
print("Время выполнения heap_sort: {:f} секунд".format(time2))
