# Засько Б., КНИТ16-А


def rec(n, m):
    if m == 0:
        return n
    else:
        return rec(m, n % m)


def ite(n, m):
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
