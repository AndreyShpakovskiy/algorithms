# ИЗУЧЕНИЕ МЕТОДОВ ОЦЕНКИ АЛГОРИТМОВ
# Цель работы:
#    Изучение методов оценки алгоритмов и программ
#    и определение временной и емкостной сложности типовых алгоритмов и программ.

import random
import time as t
import plotly.express as px


def production(num: int, matr: list) -> int:
    product = 1
    for i in range(num):
        product *= matr[i][i]
    return product


def evaluate_results(repetitions: int) -> list:
    results = []
    for i in range(repetitions):
        n = random.randint(1000, 2000)
        matrix = [[random.randint(-10000000, 10000000) for a in range(n)] for b in range(n)]
        start_time = t.time()
        i = production(n, matrix)
        end_time = t.time()
        evaluated_time = end_time - start_time
        results.append((n, evaluated_time))
    return results


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


build_chart(sorted(evaluate_results(5), key=lambda tup: tup[0]))

