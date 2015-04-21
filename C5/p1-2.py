__author__ = 'Hyunsoo'

import numpy as np


T = {
    1: [(1,)],
    2: [(1, 1), (2,)],
    }


def counts(N):
    codes = list()
    for pre in [N / 2, N / 2 + 1]:
        post = N - pre
        for pre_detail in T[pre]:
            for post_detail in T[post]:
                new_code = pre_detail[:] + post_detail[:]
                if new_code not in codes:
                    codes.append(new_code)
    T[N] = codes


if __name__ == '__main__':
    MAX = 50

    for i in range(3, MAX):
        print i
        counts(i)

    from pprint import pprint

    #pprint(T)
    #exit()
    for i in range(1, MAX):
        print i, '->', len(T[i])

