def F(n):
    s = []
    while n != '':
        s.append(n)
        n = input()
    return s
print(F(input()))