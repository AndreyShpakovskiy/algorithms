# ИССЛЕДОВАНИЕ И ОЦЕНКА АЛГОРИТМОВ ПОИСКА
# Цель работы:
#     Разработка программ, реализующих различные
#     алгоритмы поиска, и оценка их временной и пространственной сложности.

import random

n = random.randint(10000)
arr = [random.randint(0, 100) for a in range(n)]
arr.sort()
arg = int(input())


def search(to_find: int, a: list) -> int:
    low = 0
    high = len(a) - 1
    mid: int
    while a[low] < to_find < a[high]:
        if a[low] == a[high]:
            break
        mid = low + (to_find - a[low]) * (high - low) // (a[high] - a[low])
        if a[mid] < to_find:
            low = mid + 1
        else:
            if a[mid] > to_find:
                high = mid - 1
            else:
                return mid
    if a[low] == to_find:
        return low
    else:
        if a[high] == to_find:
            return high
        else:
            return -1


num = search(arg, arr)
print("ID=", num)
