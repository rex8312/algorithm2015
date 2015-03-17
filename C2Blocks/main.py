# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'


import numpy as np
import pylab as pl


blocks = [
    [[1, 0], [1, 1]],
    [[1, 1], [1, 0]],
    [[1, 1], [0, 1]],
    [[0, 1], [1, 1]],
    ]


def create_puzzle(width, height):
    return np.zeros((height, width))


def place_block(puzzle, x, y, rotation, value=1):
    if rotation < 4:
        block = np.array(blocks[rotation])

        def valid(block):
            r = True
            for dx, dy in ((0, 0), (0, 1), (1, 0), (1, 1)):
                if block[dy][dx] == 1:
                    if puzzle[y + dy][x + dx] != 0:
                        r = False
                        break
            return r

        def place(block):
            for dx, dy in ((0, 0), (0, 1), (1, 0), (1, 1)):
                if block[dy][dx] == 1:
                    puzzle[y + dy][x + dx] = value

        if valid(block):
            place(block)
            return True
        else:
            return False
    else:
        return True


def is_full(puzzle):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == 0:
                return False
    return True


# stack 사용
target_length = 3
seed = [[0], [1], [2], [3], [4]]


def generate_case_s(seed):
    def func(length, xs):
        if length == 1:
            return xs
        else:
            _xs = list()
            for x in xs:
                for s in seed:
                    _xs.append(x + s)
            return func(length - 1, _xs)

    ys = func(target_length, seed)
    return ys


# queue 사용
def depth_first_search(is_valid, target_length, seed):
    queue = seed[:]

    while True:
        x = queue.pop(0)
        if len(x) == target_length:
            yield x
        elif len(x) > target_length:
            break
        for s in seed:
            queue.append(x + s)


def generate_case(target_length, seed):
    stack = seed[:]

    while len(stack) > 0:
        x = stack.pop()
        if len(x) == target_length:
            yield x
        else:
            for s in seed:
                stack.append(x + s)


def print_ans(org_puzzle, width, height, verbose=False):
    import copy
    target_length = (width - 1) * (height - 1)
    n = 0

    for case in generate_case(target_length, seed):
        puzzle = copy.deepcopy(org_puzzle)
        for idx, r in enumerate(case):
            x = idx % (WIDTH - 1)
            y = idx / (WIDTH - 1)
            place_block(puzzle, x, y, r, idx + 1)

        if is_full(puzzle):
            n += 1
            if verbose:
                print n, case
                print puzzle
                print
    print 'Total n: {}'.format(n)


if __name__ == '__main__':
    print '(0)'
    WIDTH, HEIGHT = 3, 2
    puzzle = create_puzzle(WIDTH, HEIGHT)
    print_ans(puzzle, WIDTH, HEIGHT, True)

    exit()
    print
    print '(a)'
    WIDTH, HEIGHT = 7, 3
    puzzle = np.array([
        [99, 0, 0, 0, 0, 0, 99],
        [99, 0, 0, 0, 0, 0, 99],
        [99, 99, 0, 0, 0, 99, 99],
        ])

    print_ans(puzzle, WIDTH, HEIGHT)

    print
    print '(b)'
    WIDTH, HEIGHT = 7, 3
    puzzle = np.array([
        [99, 0, 0, 0, 0, 0, 99],
        [99, 0, 0, 0, 0, 0, 99],
        [99, 99, 0, 0, 99, 99, 99],
        ])

    print_ans(puzzle, WIDTH, HEIGHT)

    print
    print '(c)'
    WIDTH, HEIGHT = 8, 6
    puzzle = create_puzzle(WIDTH, HEIGHT)
    print_ans(puzzle, WIDTH, HEIGHT)
