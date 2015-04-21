__author__ = 'Hyunsoo'

import numpy as np


T = {
    1: [(1,)],
    2: [(1, 1), (2,)],
    }

S = {
    1: [(1,)],
    2: [(1, 1), (2,)],
    }


def is_symemetry(pre_code, post_code):
    if len(pre_code) == len(post_code):
        for v0, v1 in zip(pre_code, reversed(post_code)):
            if v0 != v1:
                return False
    elif len(pre_code) > len(post_code):
        if pre_code[-1] == 1 and len(pre_code[:-1]) == len(post_code):
            for v0, v1 in zip(pre_code[:-1], reversed(post_code)):
                if v0 != v1:
                    return False
        else:
            return False
    else:
        if post_code[0] == 1 and len(pre_code) == len(post_code[1:]):
            for v0, v1 in zip(pre_code, reversed(post_code[1:])):
                if v0 != v1:
                    return False
        else:
            return False
    return True


def counts(N):
    codes = list()
    ns_codes = list()
    prev_codes = T[N-1]

    for prev_code in prev_codes:
        new_code = prev_code[:] + (1,)
        if new_code not in codes:
            codes.append(new_code)

        new_code = (1,) + prev_code[:]
        if new_code not in codes:
            codes.append(new_code)

        if prev_code[-1] == 1:
            new_code = prev_code[:-1] + (2,)
            if new_code not in codes:
                codes.append(new_code)

    T[N] = codes
    S[N] = ns_codes


if __name__ == '__main__':
    MAX = 25
    SYMMETRY = True

    for i in range(3, MAX):
        print i
        counts(i)

    from pprint import pprint

    pprint(T[4])
    #pprint(S[5])
    #exit()
    for i in range(1, MAX):
        print i, '->', len(T[i]), ':', len(S[i])

