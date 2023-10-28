def f(n):
    if n < 2:
        return 1
    return n * f(n - 1)


print(f(int(input())))
