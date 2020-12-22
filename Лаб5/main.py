# РАЗРАБОТКА РЕКУРСИВНЫХ АЛГОРИТМОВ
# Цель работы:
#     Разработка программ, реализующих различные
#     рекурсивные алгоритмы, и оценка их временной и пространственной сложности.
# Алгоритм интерполирующего поиска целочисленного значения ключа в
# заданном массиве и вывода этого массива

import random
import time as t
import plotly.express as px


def search(arr: list, low: int, high: int, to_find: int):
    if high < low:
        return None
    else:
        mid = low + (to_find - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[mid] > to_find:
            return search(arr, low, mid - 1, to_find)
        elif arr[mid] < to_find:
            return search(arr, mid + 1, high, to_find)
        else:
            return mid


def build_chart(raw):
    chart_data = []

    for (nn, time) in raw:
        chart_data.append(
            dict(
                size=nn,
                evaluation=time
            )
        )
    fig = px.line(chart_data, x="size", y="evaluation")
    fig.show()


def evaluate_results(repetitions: int) -> list:
    meta = []
    for m in range(repetitions):
        random.seed(t.time())
        i = random.randint(100, 20000)
        sus = [random.randint(0, 100) for a in range(i)]
        sus.sort()
        argument = 25
        start_time1 = t.time()
        m = search(sus, 0, i-1, argument)
        finish_time1 = t.time()
        meta.append((len(sus), finish_time1 - start_time1))
    return meta


build_chart(sorted(evaluate_results(15), key=lambda x: x[0]))
