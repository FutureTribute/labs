# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# 5b
# Дана последовательность, содержащая от 2 до 20 слов, в каждом
# из которых от 2 до 10 латинских букв; между соседними словами - не менее
# одного пробела, за последним словом - точка. Напечатать все слова, отличные
# от последнего слова, предварительно поменяв местами первую и последнюю букву
# каждого слова.

import re

while True:
    b = []
    inp = input()
    if inp.__getitem__(-1) == ".":
        inp = inp.replace(".", "")
        inp = inp.split()
        if 2 <= len(inp) <= 20:
            for i in inp:
                if 10 < len(i) < 2:
                    print("Слова должны иметь о 2 до 10 символов")
                    break
                else:
                    if i.isalpha():
                        if re.search("[A-Za-z]",i):
                            if i != inp.__getitem__(-1):
                                fa = i.__getitem__(0)
                                la = i.__getitem__(-1)
                                a=""
                                for j in range(1,len(i)-1):
                                    a+=i.__getitem__(j)
                                print(la,a,fa, sep="", end=", ")
                        else:
                            print("Слова должны состоять из латинских букв")
                            break
                    else:
                        print("Не должны присутствовать лишние пробелы и небуквы")
                        break
            else:
                print(inp.__getitem__(-1)+ ".")
        else:
            print("Нужно от 2 до 20 слов")
            continue
    else:
        print("Отсутствует точка в конце")
        continue
    
