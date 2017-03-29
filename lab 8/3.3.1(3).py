# Засько Б., КНИТ16-А
# Прямой поиск подстроки

from timeit import timeit

setup = '''
S = input("Введите строку: ")
subS = input("Введите подстроку: ")
'''

stmt = '''
i = -1
j = 0
while j < len(subS) and i < (len(S) - len(subS)):
    j = 0
    i += 1
    while j < len(subS) and subS[j] == S[i+j]:
        j += 1
if j == len(subS):
    print("Элемент найден в позиции", i+1)
else:
    print("Элемент не найден")
'''
time = timeit(stmt, setup, number=1)
print("Время выполнения алгоритма: {:f} секунд".format(time))
