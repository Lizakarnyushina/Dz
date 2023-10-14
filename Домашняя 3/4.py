from collections import Counter
from one import vvod


def f(lst):
    return Counter(lst).most_common()
    

lst = vvod()
a = f(lst)

output = ["Элемент | Частота"]

for e, c in a:
        output.append(f"{e.ljust(7)} | {c:4}")


print('\n'.join(output))