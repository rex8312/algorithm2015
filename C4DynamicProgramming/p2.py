__author__ = 'Hyunsoo'

import numpy as np
import timeit
#import pylab as pl


def evaluate(xs, ys):
    return np.sum((xs - ys) ** 2)


def digitize(xs, bins):
    ys = list()
    for x in xs:
        idx = find_the_closest(x, bins)
        ys.append(int(bins[idx]))
    return np.array(ys)


def find_the_closest(x, bins):
    idx, distance = None, 10e100
    for bin_idx, bin in enumerate(bins):
        if abs(x - bin) < distance:
            idx, distance = bin_idx, abs(x - bin)
    return idx


def bf_search(xs, s):
    min_n, max_n = min(xs), max(xs)

    def generate_bins(bins=list()):
        if len(bins) == s:
            yield bins
        else:
            for x in range(min_n, max_n):
                for b in generate_bins(bins[:] + [x]):
                    yield b

    min_error = 10e100
    min_bins = list()

    for bins in generate_bins():
        ys = digitize(xs, bins)
        error = evaluate(xs, ys)
        if error < min_error:
            min_error, min_bins = error, [set(bins)]
        elif error == min_error:
            if set(bins) not in min_bins:
                min_bins.append(set(bins))

    rs = [sorted([b for b in bins]) for bins in min_bins]
    return min_error, rs


def bf_search2(xs, s):
    min_n, max_n = min(xs), max(xs)
    hist = [0.0 for _ in range(max_n - min_n + 3)]
    errors = [float(max_n - min_n) for _ in range(max_n - min_n + 3)]

    def init():
        for x in xs:
            hist[min_n + x] += 1.0

    def apply_bin(errors, bin):
        new_errors = errors[:]
        for i, error in enumerate(errors):
            dist = float(abs(i - bin - min_n))
            new_errors[i] = min(error, dist)
        return new_errors

    def get_total_error(hist, errors):
        rs = []
        for h, e in zip(hist, errors):
            rs.append(h * e)
        return rs

    init()
    bins = list()
    for _ in range(s):
        _bins = list()
        for bin in range(max_n - min_n + 1):
            _errors = apply_bin(errors, bin)
            total_error = get_total_error(hist, _errors)
            _bins.append((sum(total_error), bin, _errors))
            _bins.sort()
        bins.append(_bins[0][1] + min_n)
        errors = _bins[0][2]

    bins = np.array(np.array(bins), dtype=int)
    ys = digitize(xs, bins)
    error = evaluate(xs, ys)
    return error, sorted(bins.tolist())


def k_means_search(xs, k):
    min_n, max_n = min(xs), max(xs)
    bins = np.linspace(min_n, max_n, k)
    n_items = [1.0] * k

    n_iter = 0
    cont = True
    cluster_idx = [None] * len(xs)

    while cont:
        n_iter += 1
        cont = False
        for i, x in enumerate(xs):
            c_idx = find_the_closest(x, bins)
            n = n_items[c_idx]
            new_c = n / (n+1.) * bins[c_idx] + 1. / (n+1.) * x
            if abs(new_c - bins[c_idx]) > 10e-6:
                cont = True
            bins[c_idx] = new_c

            if cluster_idx[i] != c_idx:
                cluster_idx[i] = c_idx
                cont = True
            n_items[c_idx] += 1.

    bins = np.array(bins + 0.5, dtype=int)
    ys = digitize(xs, bins)
    error = evaluate(xs, ys)

    return error, sorted(bins.tolist()), n_iter


def dp_search(xs, s):
    xs = sorted(xs)

    def func(start, end):
        error = 0.0
        for x in xs[start:end]:
            error += abs(x - xs[end]) ** 2
        return error

    def generate_ks(length, ks=list()):
        if length == 0:
            yield ks
        else:
            for i in range(len(xs)):
                for ks_ in generate_ks(length - 1, ks[:] + [i]):
                    yield ks_

    for ks in generate_ks(s):
        print ks

    exit()
    error_table = dict()
    min_k, min_error = -1, 10e6
    for k in range(len(xs)):
        if (0, k) not in error_table:
            error_table[(0, k)] = func(0, k)
        error_1 = error_table[(0, k)]

        if (k, len(xs)-1) not in error_table:
            error_table[(k, len(xs)-1)] = func(k, len(xs)-1)
        error_2 = error_table[(k, len(xs)-1)]

        error = error_1 + error_2

        if error < min_error:
            min_k, min_error = xs[k], error

    from pprint import pprint
    pprint(error_table)
    print min_k, min_error

    return



if __name__ == '__main__':
    xs = [1, 3, 2, 9, 10, 1, 2]
    s = 1
    ys = dp_search(xs, s)
    print ys
    exit()




    MIN, MAX, LENGTH, N_SYMBOL, N_ITER = 0, 10, 50, 3, 100
    xs = np.random.randint(MIN, MAX, LENGTH)
    print xs
    #print bf_search(xs, N_SYMBOL)
    #print bf_search2(xs, N_SYMBOL)
    #print k_means_search(xs, N_SYMBOL)

    correct0, error0 = 0, 0
    correct1, error1 = 0, 0

    for _ in range(N_ITER):
        xs = np.random.randint(MIN, MAX, LENGTH)
        s = 5
        ys0 = bf_search(xs, N_SYMBOL)

        ys1 = bf_search2(xs, N_SYMBOL)
        if ys0[0] == ys1[0]:
            correct0 += 1
        error0 += ys1[0] - ys0[0]

        ys1 = k_means_search(xs, N_SYMBOL)
        if ys0[0] == ys1[0]:
            correct1 += 1
        error1 += ys1[0] - ys0[0]

        if ys1[0] < ys0[0]:
            print 'ERROR:', xs
            print ys0
            print ys1

    print
    print 'BF SEARCH 2'
    print 'ACC:', correct0 / float(N_ITER)
    print 'ERR DIFF:', error0 / float(N_ITER)

    print
    print 'KM'
    print 'ACC:', correct1 / float(N_ITER)
    print 'ERR DIFF:', error1 / float(N_ITER)

    exit()
    setup_script = """
from __main__ import bf_search
from __main__ import bf_search2
from __main__ import k_means_search
import numpy as np
xs = np.random.randint(0, 50, 100)
s = 3
"""
    print 'BF:', timeit.timeit("bf_search(xs, s)", number=10, setup=setup_script)
    print 'BF2:', timeit.timeit("bf_search2(xs, s)", number=10, setup=setup_script)
    print 'KM:', timeit.timeit("k_means_search(xs, s)", number=10, setup=setup_script)
