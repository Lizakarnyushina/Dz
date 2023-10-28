def f(x) -> bool:
    x = [(i, type(i)) for i in x]
    return len(x) == len(set(x))


print(f(input().split()))
