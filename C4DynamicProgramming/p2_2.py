__author__ = 'Hyunsoo'

import numpy as np


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

    print dp_search([1, 3, 2, 9, 10, 1, 2], 2)
    exit()
    MIN, MAX, LENGTH, N_SYMBOL, N_ITER = 0, 10, 50, 5, 100
    xs = np.random.randint(MIN, MAX, LENGTH)
    print bf_search(xs, N_SYMBOL)
    print dp_search(xs, N_SYMBOL)
