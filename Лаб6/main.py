# ИССЛЕДОВАНИЕ И ОЦЕНКА АЛГОРИТМОВ СОРТИРОВКИ
# Цель работы. Разработка программ, реализующих различные
# алгоритмы сортировки, и оценка их временной и пространственной сложности
#
# Составить две программы, которые реализуют алгоритмы
# простой сортировки «пузырьком» и выбором. Исходные данные
# задавать с помощью датчика случайных чисел

import time as t
from random import randint
from random import seed
import plotly.express as px


def bubbled(arr: list) -> list:
    sus = arr.copy()
    n = len(sus)
    for k in range(n - 1):
        for i in range(n - k - 1):

            if sus[i] > sus[i+1]:
                sus[i], sus[i+1] = sus[i+1], sus[i]
    return sus


def inserted(arr: list) -> list:
    sus = arr.copy()
    n = len(sus)
    for i in range(1, n):
        key = sus[i]
        j = i - 1
        while j >= 0 and key < sus[j]:
            sus[j+1] = sus[j]
            j -= 1
        sus[j+1] = key
    return sus


array = [randint(-100, 100) for n in range(randint(1, 2000))]

start_time = t.time()
bubble = bubbled(array)
finish_time = t.time()
bubble_time = finish_time - start_time

start_time = t.time()
insert = inserted(array)
finish_time = t.time()
insert_time = finish_time - start_time

print(f"bubble: {bubble_time}")
print(f"insertion: {insert_time}")


def build_chart(raw):
    chart_data = []

    for (n, time) in raw:
        chart_data.append(
            dict(
                size=n,
                evaluation=time
            )
        )
    fig = px.line(chart_data, x="size", y="evaluation")
    fig.show()


def evaluate_results(repetitions: int, func) -> list:
    meta = []
    for _ in range(repetitions):
        seed(t.time())
        sus = [randint(-100, 100) for _ in range(randint(1, 2000))]
        start_time1 = t.time()
        _ = func(sus)
        finish_time1 = t.time()
        meta.append((len(sus), finish_time1 - start_time1))
    return meta


build_chart(sorted(evaluate_results(10, bubbled), key=lambda x: x[1]))
build_chart(sorted(evaluate_results(10, inserted), key=lambda x: x[1]))
