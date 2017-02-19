# Засько Б., КНИТ16-А
# Дано натуральное число n. Вывести на экран все простые делители этого числа.

while True:
    try:
        n = int(input("Введите натуральное число: "))
        if n < 1:
            print("Натуральное число - целое и неотрицательное")
        else:
            a = {i for i in range(1, n+1) if n % i == 0}
            print(a)
    except ValueError:
        print("Натуральное число - целое и неотрицательное")
    if cont == "yes":
        print("")
        continue
    else:
        break