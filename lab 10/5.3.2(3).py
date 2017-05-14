# Засько Б., КНИТ16-А
# Проверка текста на то, являеться ли он формулой, записанной в соответствии с синтаксисом EBNF


def formula(n):
    """Проверка текста на то, являеться ли он формулой
    
    :param n: передаваемый текст
    :return: 
    """

    def formula2(n):
        alph2 = '+-*'
        if ')' in n:
            for i in range(len(n)):
                if n[i] == ')':
                    j = i
                    if formula(n[1:j]) == 1:
                        if j == len(n)-1:
                            return 1
                        if n[j + 1] in alph2:
                            return formula(n[j + 2:])
                        else:
                            print("Не есть формулой")
                            return None
                    else:
                        print("Не есть формулой")
                        return None
        else:
            print("Не есть формулой")
            return None

    alph = '()+-*1234567890'
    if len(n) == 0:
        print("Не есть формулой")
        return None
    if n.__getitem__(-1) == '.':
        n = n[:-1]
    if len(n) == 0:
        print("Не есть формулой")
        return None
    for i in n:
        if i not in alph:
            print("Не есть формулой")
            return None
    alph2 = '+-*'
    alph3 = '0123456789'
    if n.__getitem__(0) in alph2 or n.__getitem__(0) == ')':
        print("Не есть формулой")
        return None
    if n[0] == '(':
        return formula2(n)
    for i in range(1, len(n)):
        if n[i] == '(':
            try:
                if n[i+1] not in alph3:
                    print("Не есть формулой")
                    return None
                else:
                    return formula2(n[i:])
            except IndexError:
                print("Не есть формулой")
                return None
    for i in range(len(n)):
        if n[i] in alph2:
            try:
                if n[i+1] == '(':
                    return formula(n[i:])
            except IndexError:
                print("Не есть формулой")
                return None
            return formula(n[i+1:])
    return 1

while True:
    m = input("Введите формулу: ")
    if m == 'n':
        break
    if formula(m) == 1:
        if m.__getitem__(-1) == '.':
            m = m[:-1]
        print(eval(m))
