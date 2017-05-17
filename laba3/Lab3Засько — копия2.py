# Индивидуальное задание
# Засько Богдан
# КНИТ16-А
# Вариант 5

log=False;
print('{:>80}'.format("Enter your surname "))
surname = input()
print()
print('{:>80}'.format('Enter integer numbers '))
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('{:>55}'.format("Integer:"))
print('{:>80}'.format(" "*5+"Standart format"+" "*19+"Custom format"))
print('{:>80}'.format('{:10} {:d} {:d} {:d} {:d} {:24} {:} {:2d} {:} {:2d} {:} {:2d} {:} {:2d}'.format(" ",a,b,c,d," ","a=",a,"b=",b,"c=",c,"d=",d)))
print('{:>80}'.format("Enter real numbers "))
x, y = float(input()), float(input())
print('{:>55}'.format("Real:"));
print('{:>80}'.format(" "*5+"Standart format"+" "*19+"Custom format"))
print('{:>80}'.format('{:f} {:26} {} {:8f}'.format(x," ","x=",x)))
print('{:>80}'.format('{:f} {:26} {} {:8f}'.format(y," ","y=",y)))
print('{:>80}'.format('{:35} {} {:7.2f} {} {:7.2f}'.format(" ","x=",x," y=",y)))
print('{:>80}'.format('{:35} {} {:7.2g} {} {:7.2g}'.format(" ","x=",x," y=",y)))
print('{:>80}'.format('{:35} {} {:7.2e} {} {:7.2e}'.format(" ","x=",x," y=",y)))
print('{:>80}'.format('{:35} {} {:7.2E} {} {:7.2E}'.format(" ","x=",x," y=",y)))
print()
print('{:>55}'.format("Boolean:"));
print('{:>80}'.format(" "*5+"Standart format"+" "*19+"Custom format"));
print('{:>80}'.format('{:11} {} {:25} {} {:7}'.format(" ",log," ","log=",log)))
print('{:>80}'.format('{:11}{:d} {:28} {} {:7d}'.format(" ",log," ","log=",log)))
print()
print('{:>55}'.format("String:"));
print('{:>80}'.format(" "*5+"Standart format"+" "*19+"Custom format"));
print('{:>80}'.format('{:7} {} {:17} {} {:2}'.format(" ",surname," ","surname=",surname)))
