# Засько Б., КНИТ16-А
# Для первого города найти найкратчайший путь в остальные города

import  numpy as np
import pickle


def dijkstra(s, n, a):
    wt_bool = [True] * n
    wt = [100] * n
    wt[s] = 0
    for i in range(n):
        min_wt = 101
        id_min_wt = -1
        for i in range(len(wt)):
            if wt_bool[i] and wt[i] < min_wt:
                min_wt = wt[i]
                id_min_wt = i
        for i in range(n):
            if wt[id_min_wt] + a[id_min_wt][i] < wt[i]:
                wt[i] = wt[id_min_wt] + a[id_min_wt][i]
        wt_bool[id_min_wt] = False
    return wt

while True:
    try:
        g = int(input("Количество городов: "))
        m = np.zeros((g, g), dtype=int)
        for i in range(0, g):
            m[i][i] = 0
            for j in range(i + 1, g):
                while True:
                    try:
                        r = int(input('Введите расстояние между городом {} и городом {}: '.format(i + 1, j + 1)))
                        break
                    except ValueError:
                        print("Введите целое число")
                m[i][j], m[j][i] = r, r
        f = open('bin.bin', 'wb')
        pickle.dump(m, f)
        f.close()
        with open('bin.bin', 'rb') as f:
            data = f.read()
        st = 1
        data_m = pickle.loads(data)
        print(data_m)
        res = dijkstra(st-1, g, data_m)
        for i in range(len(res)):
            if i == st - 1:
                continue
            print('Кратчайшее расстоияние от  {}-го к городу {}му = {}'.format(st, i+1, res[i]))
    except (ValueError, OverflowError):
        print("Некоректное знвчение")
