print('введите x, y')
x = float(input())
y = float(input())
if x == 0 and y != 0:
    print('Точка лежит на ординате')
elif x != 0 and y == 0:
    print('Точка лежит на абсциссе')
elif x > 0 and y > 0:
    print('Точка лежит в первойчервети')
elif x < 0 and y > 0:
    print('Точка лежит во второй четверти')
elif x < 0 and y < 0:
    print('Точка лежит в третьей четверти')
elif x > 0 and y < 0:
    print('Точка лежит в четвёртой чертвети')
else:
    print('Точка лежит в начале координат')
