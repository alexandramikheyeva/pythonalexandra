#1

#2

#3
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a > b + c:
    print(a - b - c)
else:
    print('False')
#4
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a < b + c:
    print(b + c - a)
else:
    print('False')
#5
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a > 50 and b > a or c > a:
    print('Вася')
else:
    print('False')
#6
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a > 5 or b == 7 and c == 7:
    print('Петя')
else:
    print('False')