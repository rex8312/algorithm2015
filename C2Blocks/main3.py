# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'

import copy
import shelve


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
    return [[0] * width for _ in range(height)]


def place_block(puzzle, x, y, rotation, value=1):
    if rotation < 4:
        block = blocks[rotation]

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

        for _y in range(y):
            for _x in range(width):
                if puzzle[_y][_x] == 0:
                    return False

        for _x in range(x):
            if puzzle[y][_x] == 0:
                return False

    return True


# queue 사용
def depth_first_search(org_puzzle, target_length, seed):
    queue = seed[:]

    iter = 0
    drop = 0
    found = 0
    while len(queue) > 0:
        x = queue.pop(0)
        if len(x) <= target_length:
            puzzle = copy.deepcopy(org_puzzle)
            if is_promising_case(puzzle, x):
                if is_full(puzzle):
                    found += 1
                    yield x, puzzle
                else:
                    for s in seed:
                        queue.append(x + s)
            else:
                drop += 1
        else:
            drop += 1

        max_iter = iter + len(queue)
        print '\rDrop:', drop, 'nSearch:', iter, 'nQueue: ', len(queue), 'Found: ', found, 'cmp: ', float(iter) / max_iter,
        iter += 1
    print


def print_ans(tag, org_puzzle, width, height, verbose=False):
    target_length = (width - 1) * (height - 1)
    n = 0

    db = shelve.open('results.pkl')

    for case, puzzle in depth_first_search(org_puzzle, target_length, seed):
        n += 1
        if verbose:
            print n, case
            print puzzle
            print
        db['{}-{}'.format(tag, n)] = puzzle
    db.close()
    print 'Total n: {}'.format(n)


if __name__ == '__main__':
    print '(0)'
    WIDTH, HEIGHT = 3, 2
    puzzle = create_puzzle(WIDTH, HEIGHT)
    print_ans('0', puzzle, WIDTH, HEIGHT, False)

    print
    print '(1)'
    WIDTH, HEIGHT = 7, 5
    puzzle = [
        [B, B, 0, B, B, 0, 0],
        [B, 0, 0, 0, 0, 0, 0],
        [B, 0, 0, 0, 0, B, B],
        [B, 0, 0, B, B, B, B],
        [B, B, B, B, B, B, B],
    ]

    print_ans('1', puzzle, WIDTH, HEIGHT, False)

    print
    print '(a)'
    WIDTH, HEIGHT = 7, 3
    puzzle = [
        [B, 0, 0, 0, 0, 0, B],
        [B, 0, 0, 0, 0, 0, B],
        [B, B, 0, 0, 0, B, B],
    ]

    print_ans('a', puzzle, WIDTH, HEIGHT, False)

    print
    print '(b)'
    WIDTH, HEIGHT = 7, 3
    puzzle = [
        [B, 0, 0, 0, 0, 0, B],
        [B, 0, 0, 0, 0, 0, B],
        [B, B, 0, 0, B, B, B],
    ]

    print_ans('b', puzzle, WIDTH, HEIGHT, False)

    print
    print '(c)'
    WIDTH, HEIGHT = 8, 6
    puzzle = create_puzzle(WIDTH, HEIGHT)
    print_ans('c', puzzle, WIDTH, HEIGHT, False)
