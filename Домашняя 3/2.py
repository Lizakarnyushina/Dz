n = (int(input('Введите число от 1 до 12 ')))
def F(n):
    if n in (1, 2, 12):
        print('Зима')
    elif n in (3, 4, 5):
        print('Весна')
    elif n in (6, 7, 8):
        print('Лето')
    else:
        print('Осень')
F(n)