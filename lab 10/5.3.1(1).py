# Засько Б., КНИТ16-А
# Найти наибольший общий делитель


def rec(n, m):
    """Рекурсивное нахождение НОД
    
    :param n: первое число
    :param m: второе число
    :return: НОД
    """
    if m == 0:
        return n
    else:
        return rec(m, n % m)


def ite(n, m):
    """Итерационное нахождение НОД
    
    :param n: первое число
    :param m: второе число
    :return: НОД
    """
    while n != 0 and m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n + m

f = int(input("Первое число: "))
f1 = int(input("Второе число: "))
print(rec(f, f1))
print(ite(f, f1))
