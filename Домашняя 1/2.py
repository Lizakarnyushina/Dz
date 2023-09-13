print('Введите числа a,b,c,d,f')
a=int(input())
b=int(input())
c=int(input())
d=int(input())
f=int(input())
if (f-d) == 0:
    print('Делить на ноль нельзя')
else:
    x=(a*b-c)/(f-d)
    print(x)