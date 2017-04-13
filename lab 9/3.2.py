# Засько Б., КНИТ16-А

from timeit import timeit
import random as rnd


def cocktail_sort(a):
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


def shell_sort(a):
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


def heap_sort(a):
    def heapify(a):
        start = int((len(a) - 2) / 2)
        while start >= 0:
            siftdown(a, start, len(a) - 1)
            start -= 1

    def siftdown(a, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if child <= end and a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return

    heapify(a)
    end = len(a) - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        siftdown(a, 0, end - 1)
        end -= 1
    return a

n = int(input("Количество элементов в массиве: "))
arr = []
for i in range(n):
    arr.append(rnd.randint(0, n * 2))
print("Массив:", arr)
print("cocktail_sort:", cocktail_sort(arr))
print("shell_sort:", shell_sort(arr))
print("heap_sort:", heap_sort(arr))

