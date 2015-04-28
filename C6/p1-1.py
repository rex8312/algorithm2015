__author__ = 'Hyunsoo'

import numpy as np


def bf_search(W, items):

    def gen(seq=list(), length=len(items)):
        if length == 0:
            yield seq
        else:
            for s in (0, 1):
                for seq_s in gen(seq[:] + [s], length - 1):
                    yield seq_s

    def evaluation(items, select):
        total_value = 0
        total_weight = 0

        for sel, (weight, value) in zip(select, items):
            if sel == 1:
                total_weight += weight
                total_value += value

        return total_weight, total_value

    highest_value = 0
    best_selection = None
    for select in gen():
        weight, value = evaluation(items, select)
        if weight <= W:
            if value > highest_value:
                highest_value = value
                best_selection = select
    return highest_value, best_selection


def gen_test_case(n=15):
    import random
    items = np.zeros((n, 2))
    for i in range(n):
        items[i][0] = random.randint(1, 10)
        items[i][1] = random.randint(1, 10)
    W = np.sum(items, axis=0)[0] / 2
    return W, items


if __name__ == '__main__':
    items = np.array([[4, 7], [2, 10], [6, 6], [4, 7], [2, 5], [10, 4]])
    W = np.sum(items, axis=0)[0] / 2
    print bf_search(W, items)

    items = np.array([[10, 5], [15, 10], [1, 4]])
    W = np.sum(items, axis=0)[0] / 2
    print bf_search(W, items)

    w, items = gen_test_case()
    print bf_search(w, items)


