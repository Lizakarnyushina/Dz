def f(n):
    if n < 2:
        return 1
    return n * f(n - 1)


if __name__ == "__main__":
    print(f(int(input())))