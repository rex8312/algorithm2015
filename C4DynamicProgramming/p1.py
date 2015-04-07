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


def f1(xs):
    max_length = 0
    start = None

    for i, x1 in enumerate(xs):
        n_count = 1
        lower_limit = x1
        for j, x2 in enumerate(xs):
            if i < j and lower_limit < x2:
                n_count += 1
                lower_limit = x2

        if n_count >= max_length:
            max_length = n_count
            start = x1
    return max_length, start


def f2(xs):
    def func(xs):
        if len(xs) > 1:
            xs1_valid, xs1 = func(xs[:len(xs)/2])
            xs2_valid, xs2 = func(xs[len(xs)/2:])
            if xs1_valid and xs2_valid and xs1[-1] < xs2[0]:
                return True, xs1 + xs2
            elif xs1_valid and xs2_valid and xs1[-1] >= xs2[0]:
                if len(xs1) > len(xs2):
                    return True, xs1
                else:
                    return True, xs2
            elif xs1_valid and not xs2_valid:
                return True, xs1
            elif not xs1_valid and xs2_valid:
                return True, xs2
            else:
                return False, []
        else:
            return True, xs

    valid, ys = func(xs)
    return len(ys), ys


def f3(xs):

    max_length = 0

    def func(xs):
        if len(xs) == 1:
            yield xs
        else:
            ys_list = list()
            m_length = 0
            for i, x in enumerate(xs):
                for ys in func(xs[i + 1:]):
                    if len(ys) > 0 and x < ys[0]:
                        ys_list.append([x] + ys)
                        if len([x] + ys) > m_length:
                            m_length = len([x] + ys)

            for ys in ys_list:
                if len(ys) == m_length:
                    yield ys

    for ys in func(xs):
        if len(ys) > max_length:
            max_length = len(ys)
            print ys, len(ys)

    return (max_length, )


if __name__ == '__main__':
    xs = generate_random_seq(10)
    fx = f3
    print xs
    print 'BF:', bf_search(xs)
    print 'FX:', fx(xs)

    exit()
    correct = 0
    for _ in range(1000):
        xs = generate_random_seq(10)
        if bf_search(xs)[0] == fx(xs)[0]:
            correct += 1
    print 'ACC:', float(correct) / 1000

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