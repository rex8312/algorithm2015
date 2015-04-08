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



if __name__ == '__main__':
    xs = np.random.randint(0, 20, 100)
    s = 5
    print bf_search(xs, s)
    print k_means_search(xs, s)
    #pl.hist(xs, bins=20)
    #pl.show()

    correct = 0
    error = 0
    for _ in range(1000):
        xs = np.random.randint(0, 20, 100)
        s = 5
        ys0 = bf_search(xs, s)
        ys1 = k_means_search(xs, s)
        if ys0[0] == ys1[0]:
            correct += 1
        error = ys1[0] - ys0[0]
    print 'ACC:', correct / 1000.
    print 'ERR:', error / 1000.

    setup_script = """
from __main__ import bf_search
from __main__ import k_means_search
import numpy as np
xs = np.random.randint(0, 50, 100)
s = 3
"""
    print 'BF:', timeit.timeit("bf_search(xs, s)", number=10, setup=setup_script)
    print 'KM:', timeit.timeit("k_means_search(xs, s)", number=10, setup=setup_script)
