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
    n_miss = 0.
    n_search = 0.

    def get_avg(start, end):
        if start == end:
            return xs[start]
        else:
            return int((float(sum(xs[start:end])) / (end - start)) + 0.5)

    def func(start, end):
        error = 0.0
        avg = get_avg(start, end)
        for x in xs[start:end]:
            error += abs(x - avg) ** 2
        return error

    def generate_ks(length, ks=list()):
        if length == 0:
            yield ks
        else:
            for i in range(len(xs)):
                if len(ks) > 0 and ks[-1] > i:
                    continue
                else:
                    for ks_ in generate_ks(length - 1, ks[:] + [i]):
                        yield ks_

    error_table = dict()
    min_ks, min_error = None, 10e6

    for ks in generate_ks(s - 1):
        ks = [0] + ks + [len(xs)]
        error = 0.0

        for i in range(len(ks) - 1):
            start, end = ks[i], ks[i+1]

            n_search += 1.
            if (start, end) not in error_table:
                n_miss += 1.
                error_table[(start, end)] = func(start, end)
            error += error_table[(start, end)]

        if error < min_error:
            min_error = error
            min_ks = ks

    symbol = list()
    for i in range(s):
        start, end = min_ks[i], min_ks[i+1]
        symbol.append(get_avg(start, end))

    return min_error, symbol, 1.0 - (n_miss / n_search)


if __name__ == '__main__':
    #xs = [1, 3, 2, 9, 10, 1, 2]
    #N_SYMBOL = 2
    #print bf_search(xs, N_SYMBOL)
    #print k_means_search(xs, N_SYMBOL)
    #print dp_search(xs, N_SYMBOL)
    #exit()

    MIN, MAX, LENGTH, N_SYMBOL, N_ITER = 0, 10, 50, 5, 100
    xs = np.random.randint(MIN, MAX, LENGTH)
    print bf_search(xs, N_SYMBOL)
    #print bf_search2(xs, N_SYMBOL)
    #print k_means_search(xs, N_SYMBOL)
    print dp_search(xs, N_SYMBOL)
    #exit()

    correct0, error0 = 0, 0
    correct1, error1 = 0, 0

    for _ in range(N_ITER):
        xs = np.random.randint(MIN, MAX, LENGTH)
        ys0 = bf_search(xs, N_SYMBOL)
        ys1 = dp_search(xs, N_SYMBOL)
        if ys0[0] >= ys1[0]:
            correct0 += 1
        error0 += ys1[0] - ys0[0]

    print
    print 'ACC:', correct0 / float(N_ITER)
    print 'ERR DIFF:', error0 / float(N_ITER)
    #exit()

    setup_script = """
from __main__ import bf_search
from __main__ import dp_search
from __main__ import k_means_search
import numpy as np
xs = np.random.randint(0, 50, 100)
s = 3
"""
    print 'BF:', timeit.timeit("bf_search(xs, s)", number=10, setup=setup_script)
    print 'BF2:', timeit.timeit("dp_search(xs, s)", number=10, setup=setup_script)
    print 'KM:', timeit.timeit("k_means_search(xs, s)", number=10, setup=setup_script)
