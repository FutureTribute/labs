# Засько Б., КНИТ16-А
# Дана непустая последовательность слов из строчных руссских букв; между соседними словами -
# - запятая, за последним словом - точка. Вывести на экран в алфавитном порядке все звонкие
# согласные буквы, которые входят в каждое нечетное слово и не входят ни в одно четное слово.

while True:
    alp = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя,")
    pr = {"б", "в", "г", "д", "ж", "з", "й", "л", "м", "н", "р"}
    pr2 = pr.copy()
    a = input("Введите последовательность слов из строчных русских букв через запятую \n"
              "без пробелов и с точкой в конце: ")
    if a != "":
        if a.__getitem__(-1) == ".":
            a = a.replace(a.__getitem__(-1), "")
            b = set(a)
            if b | alp == alp:
                n = 1
                d = a.find(",")
                if d == -1:
                    c = "0" + a
                else:
                    c = "0" + a[:d + 1]
                    while True:
                        d = a.find(",", d+1)
                        if d == -1:
                            c = c + str(n) + a[len(c) - n:]
                            break
                        c = c + str(n) + a[len(c) - n:d + 1]
                        n += 1
                b = set(c.split(","))
                s0 = set()
                s1 = set()
                for i in b:
                    if int(i.__getitem__(0)) % 2 == 0:
                        s0.add(i[1:])
                    else:
                        s1.add(i[1:])
                for j in s0:
                    for i in pr:
                        if i in j:
                            pr2.remove(i)
                ans = set()
                for i in pr2:
                    count = 0
                    for j in s1:
                       if i in j:
                           count += 1
                    if count == len(s1):
                        ans.add(i)
                print(sorted(ans))
            else:
                print("!Введены недопустимые символы/буквы")
        else:
            print("!Отсутствует точка в конце")
    else:
        print("!Последовательность должна быть непустая")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break
