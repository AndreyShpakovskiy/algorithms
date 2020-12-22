from pandas import *
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import datetime as dt

p = 3  # число процессоров многопроцессорной системы
s = 4  # число  блоков структурированного программного ресурса
n = 12  # число конкурирующих процессов


def critical(matrix):
    i = j = 0
    time = matrix[0][0]

    while i < len(matrix) - 1:
        while j < len(matrix) - 1:
            if matrix[i][j + 1] > matrix[i + 1][j]:
                j += 1
                time += matrix[i][j]
                continue
            else:
                time += matrix[i + 1][j]
                break
        i += 1
    return time


matrix = [
    [1, 4, 3, 1, 3, 2, 4, 1, 4, 2, 4, 2, 2, 2, 2, 1],
    [3, 2, 4, 3, 3, 1, 2, 3, 3, 3, 1, 2, 3, 3, 1, 2],
    [1, 2, 4, 2, 4, 3, 2, 1, 2, 1, 4, 3, 4, 2, 3, 1],
    [3, 2, 4, 1, 4, 2, 4, 2, 2, 2, 2, 1, 0, 0, 0, 0],
    [3, 1, 2, 3, 3, 3, 1, 2, 3, 4, 2, 1, 0, 0, 0, 0],
    [4, 3, 2, 1, 2, 1, 4, 3, 4, 2, 3, 1, 0, 0, 0, 0],
    [4, 2, 4, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 3, 1, 2, 3, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 4, 3, 4, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

matrixTC = [
    [1, 4, 3, 1],
    [3, 2, 4, 3],
    [1, 2, 4, 2],

    [3, 2, 4, 1],
    [3, 1, 2, 3],
    [4, 3, 2, 1],

    [4, 2, 4, 2],
    [3, 3, 1, 2],
    [2, 1, 4, 3],

    [2, 2, 2, 1],
    [3, 4, 2, 1],
    [4, 2, 3, 1],
]

asyncMode = [

    # the 1st process

    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(1).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(1).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 1st 2nd
    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(23).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(23).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(28).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 1st 3rd
    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(38).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(34).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(40).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(38).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(40).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(46).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 1st 4th
    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(54).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(52).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(56).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(54).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(58).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(56).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(59).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(58).strftime('%Y-%m-%d %H:%M:%S')
    ),

    #   2 process

    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(4).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(1).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 2nd 2nd
    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(24).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(24).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(29).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(32).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(29).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 2nd 3rd
    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(41).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(38).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(41).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(45).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(48).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(46).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 2nd 4th
    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(57).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(54).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(61).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(57).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(63).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(61).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(64).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(63).strftime('%Y-%m-%d %H:%M:%S')
    ),

    #  3 process

    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(4).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 3rd 2nd
    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(28).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(24).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(31).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(28).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(33).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(31).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(34).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(33).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 3rd 3rd
    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(43).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(41).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(45).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(49).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(45).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(52).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(49).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 3rd 4th
    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(61).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(57).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(63).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(61).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(66).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(63).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(67).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(66).strftime('%Y-%m-%d %H:%M:%S')
    ),

]

asyncModeTwo = [

    # the 1st process

    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(1).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(1).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 1st 2nd
    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(14).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(21).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 1st 3rd
    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(28).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(32).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(28).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(34).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(32).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 1st 4th
    dict(
        process=1,
        block=1,
        end=dt.datetime.fromtimestamp(36).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(34).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=2,
        end=dt.datetime.fromtimestamp(38).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(36).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=3,
        end=dt.datetime.fromtimestamp(40).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(38).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=1,
        block=4,
        end=dt.datetime.fromtimestamp(41).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(40).strftime('%Y-%m-%d %H:%M:%S')
    ),

    #   2 process

    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(4).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(1).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(8).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 2nd 2nd
    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(15).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(19).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(20).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 2nd 3rd
    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(29).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(26).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(32).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(29).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(33).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(32).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(36).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(34).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 2nd 4th
    dict(
        process=2,
        block=1,
        end=dt.datetime.fromtimestamp(39).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(36).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=2,
        end=dt.datetime.fromtimestamp(43).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(39).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=3,
        end=dt.datetime.fromtimestamp(45).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(43).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=2,
        block=4,
        end=dt.datetime.fromtimestamp(46).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(45).strftime('%Y-%m-%d %H:%M:%S')
    ),

    #  3 process

    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(5).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(4).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(9).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(7).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(12).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(16).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 3rd 2nd
    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(18).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(22).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(25).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(28).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(27).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 3rd 3rd
    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(31).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(29).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(33).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(32).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(37).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(33).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(40).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(37).strftime('%Y-%m-%d %H:%M:%S')
    ),

    # 3rd 4th
    dict(
        process=3,
        block=1,
        end=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(40).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=2,
        end=dt.datetime.fromtimestamp(46).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(44).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=3,
        end=dt.datetime.fromtimestamp(48).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(46).strftime('%Y-%m-%d %H:%M:%S')
    ),
    dict(
        process=3,
        block=4,
        end=dt.datetime.fromtimestamp(49).strftime('%Y-%m-%d %H:%M:%S'),
        start=dt.datetime.fromtimestamp(48).strftime('%Y-%m-%d %H:%M:%S')
    ),

]

c_df = pd.DataFrame(asyncMode)
c_fig = px.timeline(c_df, x_start="start", x_end="end", y="process", color="block")
c_fig.show()

c_df = pd.DataFrame(asyncModeTwo)
c_fig = px.timeline(c_df, x_start="start", x_end="end", y="process", color="block")
c_fig.show()

print(DataFrame(matrix))
print(f"Время выполнения: {critical(matrix)}")