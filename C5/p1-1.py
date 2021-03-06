__author__ = 'Hyunsoo'

import numpy as np


T = {
    1: [(1,)],
    2: [(1, 1), (2,)],
    }


def counts(N):
    codes = list()
    for pre in sorted(T.keys(), reverse=True):
        post = N - pre
        for pre_detail in T[pre]:
            for post_detail in T[post]:
                new_code = pre_detail[:] + post_detail[:]
                if new_code not in codes:
                    codes.append(new_code)
    T[N] = codes


if __name__ == '__main__':
    for i in range(3, 6):
        counts(i)

    print 5, '->', len(T[5])

