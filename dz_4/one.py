from collections import Counter
from www import vvod


def f(pl: list, k: int) -> list:
    k %= len(pl)
    return pl[-k:] + pl[:-k]


if __name__ == "__main__":
    print(f(vvod(input()), int(input())))