# Засько Б., КНИТ16-А


def bubble_sort(a):
    """Сортировка простыми обменами(bubble sort)

        Простейший алгоритм сортировки, который основан на принципе
        сравнения и обмена пары соседних элементов до тех пор,
        пока не будут рассортированы все элементы массива"""
    n = len(a)
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        i += 1
    return a


def selection_sort(a):
    """Сортировка выбором (selection sort)

        Простой алгоритм сортировки, который на каждом i-ом проходе
        по массивву (0<=i<=N-2) выполняет поиск минимального (максимального)
        элемента среди последних N - i неупорядоченых элементов в последующий
        обмен найденного элемента с i-ым элементом массива"""
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[m], a[i] = a[i], a[m]
    return a


def insertion_sort(a):
    """Сортировка вставками (insertion sort)


    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
