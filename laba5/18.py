# Засько Богдан
# КНИТ16-А
# №18; Последовательность чисел Фибоначчи, конечное из которых не более чем
# целое число N

while True:
    N=input("Введите целый ограничитель для числа Фибоначчи: ")
    if N.isdigit():
        N=int(N)
        y=[1,1]
        for i in range(2,N):
            y.append(y[i-2]+y[i-1])
            if y[i]>=N:
                y.remove(y[i])
                break
        print("Последовательность Фибоначчи",y )
        print()
    else:
        print("Введите целое положительное число!")
    cont=input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont=="yes":
        print("")
        continue
    else:
        break