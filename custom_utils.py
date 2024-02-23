import cmath
import math

import numpy as np


def count_to_digital_values(counts):
    data = list(counts.items())
    data = [(qbits[::-1], counts) for qbits, counts in data]
    sorted_by_bitstring = sorted(data, key=lambda tup: tup[0][:-1])

    print("INPUT------OUTPUT-----count----percent")
    suma_total = sum([e[1] for e in sorted_by_bitstring])
    for e in sorted_by_bitstring:
        print(e[0][:-1], "------", e[0][-1], "-----", e[1], "-----", e[1] / suma_total)
    print("shots totales", suma_total)


def get_probabilities(svector):
    return np.power(np.abs(svector.data), 2)


def get_phases(svector):
    return np.array([math.degrees(cmath.polar(c)[1]) for c in svector.data])
