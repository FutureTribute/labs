# Засько Б., КНИТ16-А

from time import clock
import numpy as np
from copy import deepcopy

# Если параметр c - 0, то массив сортируеться по неубыванию


def bubble_sort(a, c):
    """Сортировка простыми обменами(bubble sort)

        Простейший алгоритм сортировки, который основан на принципе
        сравнения и обмена пары соседних элементов до тех пор,
        пока не будут рассортированы все элементы массива

        :param a: исходный массив
        :param c: направление сортировки
        :return: отсортированый массив, число сравнений, число перестановок
    """
    s, p = 0, 0  # Счетчики
    n = len(a)
    i = 0
    flag = True
    s += 1
    if c == 0:
        while flag:
            s += 1
            flag = False
            for j in range(n - i - 1):
                s += 2
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    p += 1
                    flag = True
            i += 1
    else:
        while flag:
            s += 1
            flag = False
            for j in range(n - i - 1):
                s += 2
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    p += 1
                    flag = True
            i += 1
    return a, s, p


def selection_sort(a, c):
    """Сортировка выбором (selection sort)

        Простой алгоритм сортировки, который на каждом i-ом проходе
        по массивву (0<=i<=N-2) выполняет поиск минимального (максимального)
        элемента среди последних N - i неупорядоченых элементов в последующий
        обмен найденного элемента с i-ым элементом массива

        :param a: исходный массив
        :param c: направление сортировки
        :return: отсортированый массив, число сравнений, число перестановок
    """
    s, p = 0, 0  # Счетчики
    n = len(a)
    if c == 0:
        for i in range(n - 1):
            s += 1
            minimum = i
            for j in range(i + 1, n):
                s += 2
                if a[j] < a[minimum]:
                    minimum = j
            a[minimum], a[i] = a[i], a[minimum]
            p += 1
    else:
        for i in range(n - 1):
            s += 1
            minimum = i
            for j in range(i + 1, n):
                s += 2
                if a[j] > a[minimum]:
                    minimum = j
            a[minimum], a[i] = a[i], a[minimum]
            p += 1
    return a, s, p


def insertion_sort(a, c):
    """Сортировка вставками (insertion sort)

        Простой алгоритм сортировки, который заключается в том, что отдельно
        анализируется каждый конкректный элемент, который затем помещается в
        отсортированую часть массива. Место вставки в отсортированую часть
        массива определяется методом линейного поиска

        :param a: исходный массив
        :param c: направление сортировки
        :return: отсортированый массив, число сравнений, число перестановок
    """
    s, p = 0, 0  # Счетчики
    n = len(a)
    if c == 0:
        for i in range(1, n):
            s += 2
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                s += 2
                a[j + 1] = a[j]
                p += 1
                j -= 1
            a[j + 1] = key
            p += 1
    else:
        for i in range(1, n):
            s += 2
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] < key:
                s += 2
                a[j + 1] = a[j]
                p += 1
                j -= 1
            a[j + 1] = key
            p += 1
    return a, s, p


def cocktail_sort(a, c):
    """Сортировка перемешиванием (cocktail sort)

        Развитие пузырьковой сортировки. Отличия от нее заключаются в том,
        что при прохождении части массива, происходит проверка, были ли перестановки.
        Если их не было, значит, эта часть массива уже упорядочена и она исключается из дальнейшей обработки.
        Кроме того, при прохождении массива от начала к концу, минимальные элементы перемещаются в самое начало,
        а максимальный элемент сдвигается к концу массива.

        :param a: исходный массив
        :param c: направление сортировки
        :return: отсортированый массив, число сравнений, число перестановок
    """
    s, p = 0, 0  # Счетчики
    if c == 0:
        for k in range(len(a) - 1, 0, -1):
            s += 1
            flag = False
            for i in range(k, 0, -1):
                s += 2
                if a[i] < a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    p += 1
                    flag = True
            for i in range(k):
                s += 2
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    flag = True
            if not flag:
                return a, s, p
    else:
        for k in range(len(a) - 1, 0, -1):
            s += 1
            flag = False
            for i in range(k, 0, -1):
                s += 2
                if a[i] > a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    p += 1
                    flag = True
            for i in range(k):
                s += 2
                if a[i] < a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    flag = True
            if not flag:
                return a, s, p


def shell_sort(array, c):
    """Сортировка Шелла (shell sort)

        Алгоритм сортировки, являющийся усовершенствованным вариантом сортировки вставками.
        Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом,
        но и на определённом расстоянии друг от друга

        :param array: исходный массив
        :param c: направление сортировки
        :return: отсортированый массив, число сравнений, число перестановок
    """
    s, p = 0, 0  # Счетчики
    gap = len(array) // 2
    s += 1
    if c == 0:
        while gap > 0:
            s += 1
            for i in range(gap, len(array)):
                s += 2
                val = array[i]
                j = i
                while j >= gap and array[j - gap] > val:
                    s += 2
                    p += 1
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = val
                p += 1
            gap //= 2
    else:
        while gap > 0:
            s += 1
            for i in range(gap, len(array)):
                s += 2
                val = array[i]
                j = i
                while j >= gap and array[j - gap] < val:
                    s += 2
                    p += 1
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = val
                p += 1
            gap //= 2
    return array, s, p


def heap_sort(sequence, c):
    """Пирамидальная сортировка (heap sort)

        Алгоритм сортировки, работающий в худшем, в среднем и в лучшем случае (то есть гарантированно)
        за Θ(n log n) операций при сортировке n элементов.
        Количество применяемой служебной памяти не зависит от размера массива (то есть, O(1))

        :param sequence: исходный массив
        :param c: направление сортировки
        :return: отсортированый массив, число сравнений, число перестановок
    """
    s, p = 0, 0  # Счетчики

    def sift_down(parent, limit):
        nonlocal s, p
        item = sequence[parent]
        s += 1
        while True:
            s += 4
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and sequence[child] < sequence[child + 1]:
                s += 1
                child += 1
            if item < sequence[child]:
                s += 1
                p += 1
                sequence[parent] = sequence[child]
                parent = child
            else:
                break
        sequence[parent] = item
        p += 1

    def sift_down2(parent, limit):
        nonlocal s, p
        item = sequence[parent]
        s += 1
        while True:
            s += 4
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and sequence[child] > sequence[child + 1]:
                s += 1
                child += 1
            if item > sequence[child]:
                s += 1
                p += 1
                sequence[parent] = sequence[child]
                parent = child
            else:
                break
        sequence[parent] = item
        p += 1

    if c == 0:
        length = len(sequence)
        for index in range((length >> 1) - 1, -1, -1):
            s += 1
            sift_down(index, length)
        for index in range(length - 1, 0, -1):
            s += 1
            p += 1
            sequence[0], sequence[index] = sequence[index], sequence[0]
            sift_down(0, index)
    else:
        length = len(sequence)
        for index in range((length >> 1) - 1, -1, -1):
            s += 1
            sift_down2(index, length)
        for index in range(length - 1, 0, -1):
            s += 1
            p += 1
            sequence[0], sequence[index] = sequence[index], sequence[0]
            sift_down2(0, index)
    return sequence, s, p

arr = np.random.randint(10000, size=10000)
lst = [deepcopy(arr)] * 12
a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = lst
print("Сортировка по НЕУБЫВАНИЮ. Массив:")
print(arr)
t = clock()
x = bubble_sort(a0, 0)
t = clock() - t
print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = selection_sort(a1, 0)
t = clock() - t
print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
insertion_sort(a2, 0)
t = clock() - t
print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = cocktail_sort(a3, 0)
t = clock() - t
print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = shell_sort(a4, 0)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(a5, 0)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
print(arr)

t = clock()
x = bubble_sort(a6, 1)
t = clock() - t
print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = selection_sort(a7, 1)
t = clock() - t
print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
insertion_sort(a8, 1)
t = clock() - t
print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = cocktail_sort(a9, 1)
t = clock() - t
print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = shell_sort(a10, 1)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(a11, 1)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
arr1 = np.arange(10000)
lst = [deepcopy(arr1)] * 12
ar0, ar1, ar2, ar3, ar4, ar5, ar6, ar7, ar8, ar9, ar10, ar11 = lst
print("Сортировка по НЕУБЫВАНИЮ. Массив:")
print(arr1)
t = clock()
x = bubble_sort(ar0, 0)
t = clock() - t
print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = selection_sort(ar1, 0)
t = clock() - t
print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
insertion_sort(ar2, 0)
t = clock() - t
print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = cocktail_sort(ar3, 0)
t = clock() - t
print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = shell_sort(ar4, 0)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(ar5, 0)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
print(arr1)
t = clock()
x = bubble_sort(ar6, 1)
t = clock() - t
print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = selection_sort(ar7, 1)
t = clock() - t
print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
insertion_sort(ar8, 1)
t = clock() - t
print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = cocktail_sort(ar9, 1)
t = clock() - t
print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = shell_sort(ar10, 1)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(ar11, 1)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
arr10 = np.random.randint(100000, size=100000)
lst = [deepcopy(arr10)] * 4
a100, a101, a102, a103 = lst
print("Сортировка по НЕУБЫВАНИЮ. Массив:")
print(arr10)

t = clock()
x = shell_sort(a100, 0)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(a101, 0)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
print(arr10)

t = clock()
x = shell_sort(a102, 1)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(a103, 1)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
arr11 = np.arange(100000)
lst = [deepcopy(arr11)] * 4
a110, a111, a112, a113 = lst
print("Сортировка по НЕУБЫВАНИЮ. Массив:")
print(arr11)

t = clock()
x = shell_sort(a110, 0)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(a111, 0)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
print(arr11)

t = clock()
x = shell_sort(a112, 1)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(a113, 1)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
n = int(input("Количество элементов в массиве (до 30): "))
arr3 = np.zeros(n, dtype=int)
for i in range(n):
    arr3[i] = int(input("Введите значение для элемента {}: ".format(int(i+1))))
lst = [deepcopy(arr3)] * 12
ar30, ar31, ar32, ar33, ar34, ar35, ar36, ar37, ar38, ar39, ar310, ar311 = lst
print("Сортировка по НЕУБЫВАНИЮ. Массив:")
print(arr3)
t = clock()
x = bubble_sort(ar30, 0)
t = clock() - t
print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = selection_sort(ar31, 0)
t = clock() - t
print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
insertion_sort(ar32, 0)
t = clock() - t
print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = cocktail_sort(ar33, 0)
t = clock() - t
print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = shell_sort(ar34, 0)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(ar35, 0)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])

print("===============================================================")
print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
print(arr3)
t = clock()
x = bubble_sort(ar36, 1)
t = clock() - t
print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = selection_sort(ar37, 1)
t = clock() - t
print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
insertion_sort(ar38, 1)
t = clock() - t
print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = cocktail_sort(ar39, 1)
t = clock() - t
print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = shell_sort(ar310, 1)
t = clock() - t
print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

t = clock()
x = heap_sort(ar311, 1)
t = clock() - t
print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
print("Отсортированый массив:")
print(x[0])
