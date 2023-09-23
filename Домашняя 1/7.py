print('Введите x, y')
x = int(input())
y = int(input())
a = 0
for i in range(x, y + 1):
    if i % 5 == 0:
        a += i
print(a)
