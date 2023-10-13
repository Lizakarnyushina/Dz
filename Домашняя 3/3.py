fib1 = 1
fib2 = 1
n = int(input("Номер элемента ряда Фибоначчи: "))
i = 0
while i < n - 2:
    sum = fib1 + fib2
    fib1 = fib2
    fib2 = sum
    i = i + 1
print("Значение этого элемента:", fib2)