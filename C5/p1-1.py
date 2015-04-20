__author__ = 'Hyunsoo'

import numpy as np


def gen_cods(length, code=list()):
    if length == 0:
        yield code
    else:
        for c in [0, 1, 2]:
            for new_code in gen_cods(length - 1, code + [c]):
                yield new_code


def evaluat(code):
    surface = np.zeros((2, N))

    for i, c in enumerate(code):
        y, x = i / N, i % N
        if c == 1:
            if surface[y][x] == 0:
                surface[y][x] = i + 1
                if x + 1 < N and surface[y][x + 1] == 0:
                    surface[y][x + 1] = i + 1
                else:
                    return False, surface
            else:
                return False, surface
        elif c == 2:
            if surface[y][x] == 0:
                surface[y][x] = i + 1
                if y + 1 < 2 and surface[y + 1][x] == 0:
                    surface[y + 1][x] = i + 1
                else:
                    return False, surface
            else:
                return False, surface

    if not surface.all():
        return False, surface

    return True, surface


if __name__ == '__main__':
    N = 5

    T = dict()
    count = 0

    for code in gen_cods(2 * N):
        valid, surface = evaluat(code)
        if valid:
            print code
            print surface
            count += 1

    print "N: ", N, " -> ", count