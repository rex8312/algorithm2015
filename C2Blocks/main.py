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

print len(generate_case_s(seed))


def generate_case(seed):
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
def generate_case_q(seed):
    queue = seed[:]
    ys = []

    while True:
        x = queue.pop(0)
        if len(x) > target_length:
            break
        ys.append(x)
        for s in seed:
            queue.append(x + s)

    ys = filter(lambda x: len(x) == target_length, ys)
    return ys

print len(generate_case_q(seed))


if __name__ == '__main__':
    """
    puzzle = create_puzzle(8, 6)

    print place_block(puzzle, 0, 0, 0)
    print place_block(puzzle, 1, 0, 2, 2)
    print place_block(puzzle, 3, 0, 0, 3)
    print place_block(puzzle, 4, 0, 2, 4)
    print puzzle

    print is_full(puzzle)

    puzzle = [[1, 1], [1, 1]]
    print is_full(puzzle)
    """
    print '(0)'
    WIDTH, HEIGHT = 3, 2
    target_length = (WIDTH - 1) * (HEIGHT - 1)

    cases = generate_case_s(seed)
    for case in cases:
        puzzle = create_puzzle(WIDTH, HEIGHT)
        for idx, r in enumerate(case):
            x = idx % (WIDTH - 1)
            y = idx / (WIDTH - 1)
            place_block(puzzle, x, y, r, idx + 1)

        if is_full(puzzle):
            print puzzle
            print case

    print
    print '(a)'
    WIDTH, HEIGHT = 7, 3
    target_length = (WIDTH - 1) * (HEIGHT - 1)
    puzzle = np.array([
        [99, 0, 0, 0, 0, 0, 99],
        [99, 0, 0, 0, 0, 0, 99],
        [99, 99, 0, 0, 0, 99, 99],
        ])


    cases = generate_case_q(seed)
    for case in cases:
        print case
        """
        puzzle = puzzle[:]

        for idx, r in enumerate(case):
            x = idx % (WIDTH - 1)
            y = idx / (WIDTH - 1)
            #place_block(puzzle, x, y, r, idx + 1)

        if is_full(puzzle):
            print puzzle
            print case
        """
