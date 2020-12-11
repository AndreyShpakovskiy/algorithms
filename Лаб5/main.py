# РАЗРАБОТКА РЕКУРСИВНЫХ АЛГОРИТМОВ
# Цель работы:
#     Разработка программ, реализующих различные
#     рекурсивные алгоритмы, и оценка их временной и пространственной сложности.
# Алгоритм интерполирующего поиска целочисленного значения ключа в
# заданном массиве и вывода этого массива

import random
import time as t


def search(arr: list, low: int, high: int, to_find: int):

    if high < low:
        return None
    else:
        mid = low + (to_find - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[mid] > to_find:
            return search(arr, low, mid-1, to_find)
        elif arr[mid] < to_find:
            return search(arr, mid+1, high, to_find)
        else:
            return mid


n = 10000
array = [random.randint(0, 100) for a in range(n)]
array.sort()
arg = int(input())
start_time = t.time()
s = search(array, 0, n-1, arg)
finish_time = t.time()
print(finish_time-start_time)
print("ID=", s)
