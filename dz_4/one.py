from collections import Counter
from dz_3.one import vvod


def f(pl: list, k: int) -> list:
    k %= len(pl)
    return pl[-k:] + pl[:-k]


if __name__ == "__main__":
    print(f(vvod(input()), int(input())))
