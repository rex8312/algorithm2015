# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'


import numpy as np
import pylab as pl
import copy
import time


blocks = [
    [[1, 0],
     [1, 1]],

    [[1, 1],
     [1, 0]],

    [[1, 1],
     [0, 1]],

    [[0, 1],
     [1, 1]],
]

seed = [[0], [1], [2], [3], [4]]

B = -1


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


def is_promising_case(puzzle, case):
    width = len(puzzle[0])
    for idx, r in enumerate(case):
        x = idx % (width - 1)
        y = idx / (width - 1)
        if not place_block(puzzle, x, y, r, idx + 1):
            return False
    return True


# queue 사용
def depth_first_search(org_puzzle, target_length, seed):
    queue = seed[:]

    while True:
        x = queue.pop(0)
        if len(x) > target_length:
            break
        puzzle = copy.deepcopy(org_puzzle)
        if is_promising_case(puzzle, x):
            if is_full(puzzle):
                yield x, puzzle
            else:
                for s in seed:
                    queue.append(x + s)


def print_ans(tag, org_puzzle, width, height, verbose=False):
    target_length = (width - 1) * (height - 1)
    n = 0

    for case, puzzle in depth_first_search(org_puzzle, target_length, seed):
        n += 1
        if verbose:
            print n, case
            print puzzle
            print
        pl.imshow(puzzle, interpolation='none', cmap='gray')
        pl.savefig('data/{}-{}.png'.format(tag, n))
    print 'Total n: {}'.format(n)


if __name__ == '__main__':
    print '(0)'
    WIDTH, HEIGHT = 3, 2
    puzzle = create_puzzle(WIDTH, HEIGHT)
    print_ans('0', puzzle, WIDTH, HEIGHT, True)

    print
    print '(1)'
    WIDTH, HEIGHT = 7, 5
    puzzle = np.array([
        [B, B, 0, B, B, 0, 0],
        [B, 0, 0, 0, 0, 0, 0],
        [B, 0, 0, 0, 0, B, B],
        [B, 0, 0, B, B, B, B],
        [B, B, B, B, B, B, B],
    ])

    print_ans('1', puzzle, WIDTH, HEIGHT, True)

    print
    print '(a)'
    WIDTH, HEIGHT = 7, 3
    puzzle = np.array([
        [B, 0, 0, 0, 0, 0, B],
        [B, 0, 0, 0, 0, 0, B],
        [B, B, 0, 0, 0, B, B],
    ])

    print_ans('a', puzzle, WIDTH, HEIGHT, True)

    print
    print '(b)'
    WIDTH, HEIGHT = 7, 3
    puzzle = np.array([
        [B, 0, 0, 0, 0, 0, B],
        [B, 0, 0, 0, 0, 0, B],
        [B, B, 0, 0, B, B, B],
    ])

    print_ans('b', puzzle, WIDTH, HEIGHT, True)

    print
    print '(c)'
    WIDTH, HEIGHT = 8, 6
    puzzle = create_puzzle(WIDTH, HEIGHT)
    print_ans('c', puzzle, WIDTH, HEIGHT, True)
