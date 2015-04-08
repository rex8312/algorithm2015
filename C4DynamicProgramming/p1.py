__author__ = 'Hyunsoo'

import numpy as np
import timeit


def generate_random_seq(n_item):
    import random
    ns = list()
    while len(ns) < n_item:
        x = random.randint(0, 100)
        if x not in ns:
            ns.append(x)
    return ns


def evaluate(xs, select):
    ys = list()
    for x, s in zip(xs, select):
        if s:
            insert = True
            for y in ys:
                if x < y:
                    insert = False

            if insert:
                ys.append(x)
    return ys


def bf_search(xs):
    def generate_select(ss=list()):
        if len(ss) == len(xs):
            yield ss
        else:
            for x in [False, True]:
                for _x in generate_select(ss[:] + [x]):
                    yield _x

    max_len = 0
    rs = list()
    for select in generate_select():
        ys = evaluate(xs, select)
        if len(ys) > max_len:
            rs = [tuple(ys)]
            max_len = len(ys)
        elif len(ys) == max_len:
            if tuple(ys) not in rs:
                rs.append(tuple(ys))

    return len(rs[0]), rs


def n_square(xs):
    t = dict()

    for i1, x1 in enumerate(xs):
        for i2, x2 in enumerate(xs):
            if x1 < x2 and i1 < i2:
                t.setdefault(x1, list())
                t[x1].append(x2)

    def func(k, seq=list()):
        if k not in t:
            yield seq + [k]
        else:
            for v in t[k]:
                for y in func(v, seq[:] + [k]):
                    yield y

    max_length = 0
    rs = list()
    for x in xs:
        for y in func(x):
            if len(y) > max_length:
                rs = list()
                rs.append(tuple(y))
                max_length = len(y)
            elif len(y) == max_length:
                rs.append(tuple(y))

    return max_length, rs


if __name__ == '__main__':
    xs = generate_random_seq(10)
    #fx = f4
    print xs
    print 'BF:', bf_search(xs)
    print 'SQ:', n_square(xs)
    #print 'FX:', fx(xs)

    fx = n_square
    correct = 0
    for _ in range(1000):
        xs = generate_random_seq(10)
        if bf_search(xs)[0] == fx(xs)[0]:
            correct += 1
    print fx.__name__, 'ACC:', float(correct) / 1000

    exit()
    s = 10
    #print k_means_search(xs, s)
    #pl.hist(xs, bins=20)
    #pl.show()

    setup_script = """
from __main__ import bf_search
from __main__ import k_means_search
import numpy as np
xs = np.random.randint(0, 50, 100)
s = 3
"""
    print 'BF:', timeit.timeit("bf_search(xs, s)", number=10, setup=setup_script)
    print 'KM:', timeit.timeit("k_means_search(xs, s)", number=10, setup=setup_script)