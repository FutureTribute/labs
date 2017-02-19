# Засько Б., КНИТ16-А
# Написать программу вычисления суммы тех элементов матрицы а,
# номера строк и столбцов которых принадлежат соответсвенно
# непустым множествам s_1 и s_2.

n = 10
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s_1 = {i for i in range(n)}
s_2 = {i for i in range(n)}
c = set()
try:
    for j in s_1:
        try:
            for k in s_2:
                c.add(a[j][k])
        except IndexError:
            pass
except IndexError:
    print()
print(sum(c))
