from random import randint

x = randint(0, 100) 
y = int(input("Введите число от 0 до 100: "))
while y >= 0:
    if x > y:
        print("Загаданное число больше!")    
    elif x < y:
        print("Загаданное число меньше!")
    else:
        print("Вы угадали число!")
        break
    y = int(input("Введите число от 1 до 100: "))