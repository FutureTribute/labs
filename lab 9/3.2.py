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
                    p += 1
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
                    p += 1
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

while True:
    try:
        ch = int(input("Для сортировки случайного массива введите 1, для отсортированого по возрастанию - 2,\n"
                       "для отсортированого по убыванию - 3, для ручного ввода массива - 4: "))
        if ch == 1:
            try:
                n = int(input("Количество элементов в массиве: "))
                if n > 100000:
                    raise MemoryError
                arr = np.random.randint(n, size=n)

                print("Сортировка по НЕУБЫВАНИЮ. Массив:")
                print(arr)
                t = clock()
                x = bubble_sort(deepcopy(arr), 0)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr), 0)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr), 0)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr), 0)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr), 0)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr), 0)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])

                print("===============================================================")
                print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
                print(arr)

                t = clock()
                x = bubble_sort(deepcopy(arr), 1)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr), 1)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr), 1)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr), 1)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr), 1)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr), 1)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])
            except MemoryError:
                print("Слишком много элеметов")
        elif ch == 2:
            try:
                n = int(input("Количество элементов в массиве: "))
                if n > 100000:
                    raise MemoryError
                arr1 = np.arange(n)
                print("Сортировка по НЕУБЫВАНИЮ. Массив:")
                print(arr1)
                t = clock()
                x = bubble_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])

                print("===============================================================")
                print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
                print(arr1)
                t = clock()
                x = bubble_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])
            except MemoryError:
                print("Слишком много элеметов")
        elif ch == 3:
            try:
                n = int(input("Количество элементов в массиве: "))
                if n > 100000:
                    raise MemoryError
                arr1 = np.arange(n - 1, -1, -1)
                print("Сортировка по НЕУБЫВАНИЮ. Массив:")
                print(arr1)
                t = clock()
                x = bubble_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr1), 0)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])

                print("===============================================================")
                print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
                print(arr1)
                t = clock()
                x = bubble_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr1), 1)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])
            except MemoryError:
                print("Слишком много элеметов")
        elif ch == 4:
            try:
                n = int(input("Количество элементов в массиве (до 30): "))
                if n > 30 or n < 1:
                    raise ValueError
                arr3 = np.zeros(n, dtype=int)
                for i in range(n):
                    while True:
                        try:
                            arr3[i] = int(input("Введите значение для элемента {}: ".format(int(i+1))))
                            break
                        except ValueError:
                            print("Неверный ввод")
                print("Сортировка по НЕУБЫВАНИЮ. Массив:")
                print(arr3)
                t = clock()
                x = bubble_sort(deepcopy(arr3), 0)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr3), 0)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr3), 0)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr3), 0)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr3), 0)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr3), 0)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])

                print("===============================================================")
                print("Сортировка по НЕВОЗРАСТАНИЮ. Массив:")
                print(arr3)
                t = clock()
                x = bubble_sort(deepcopy(arr3), 1)
                t = clock() - t
                print("Время выполнения bubble_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = selection_sort(deepcopy(arr3), 1)
                t = clock() - t
                print("Время выполнения selection_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                insertion_sort(deepcopy(arr3), 1)
                t = clock() - t
                print("Время выполнения insertion_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = cocktail_sort(deepcopy(arr3), 1)
                t = clock() - t
                print("Время выполнения cocktail_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = shell_sort(deepcopy(arr3), 1)
                t = clock() - t
                print("Время выполнения shell_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))

                t = clock()
                x = heap_sort(deepcopy(arr3), 1)
                t = clock() - t
                print("Время выполнения heap_sort: {:f} секунд, перестановок: {}, сравнений: {}".format(t, x[2], x[1]))
                print("Отсортированый массив:")
                print(x[0])
            except MemoryError or ValueError:
                print("Слишком много элеметов")
        else:
            print("Неверный ввод")
    except ValueError:
        print("Неверный ввод")
