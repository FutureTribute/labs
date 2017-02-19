# Засько Б., КНИТ16-А
# Дано натуральное число n. Вывести на экран все простые делители этого числа.

while True:
    try:
        n = int(input("Введите натуральное число: "))
        if n < 1:
            print("Натуральное число - целое положительное")
        else:
            a = {i for i in range(1, n+1) if n % i == 0}
            print(sorted(a))
    except ValueError:
        print("Натуральное число - целое положительное")
    cont = input("Для продолжения введите yes, для завершения любое другое значение \n")
    if cont == "yes":
        print("")
        continue
    else:
        break
