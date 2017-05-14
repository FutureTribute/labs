# Засько Б.
# Найти количество различных представлений натурального числа в виде суммы не менее двух
# попарно различных натуральных слагаемых


def part(n, k):
    """Функция подсчета количества различных представлений числа

    :param n: число для разбиений
    :param k: количество слагаемых
    :return: представление натурального числа в ввиде сумы
    """

    def part2(n, k, pre):
        if n <= 0:
            return []
        if k == 1 and n <= pre:
            return [[n]]
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [[i] + sub for sub in part2(n - i, k - 1, i)]
        return ret

    return part2(n, k, n)


while True:
    try:
        a = input("Введите число для разложений: ")
        if a == 'n':
            break
        a = int(a)
        count = 0
        for i in range(1, a + 1):
            k = part(a, i)
            for j in k:
                if len(j) == len(set(j)):
                    print(j)  #
                    count += 1
        print(count)
    except ValueError:
        print("Введите корректное значение!")
