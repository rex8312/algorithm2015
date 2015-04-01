# -*- coding: utf-8 -*-

__author__ = 'rex8312'


def evaluate(xs, s, e):
    if e >= s:
        xs_ = xs[s:e+1]
        return len(xs_) * min(xs_), xs_
    else:
        return -1, []


def find_max(rs):
    biggest = rs[0]
    for r in rs:
        if r[0] > biggest[0]:
            if r[1] < biggest[1] and r[2] < biggest[2]:
                biggest = r
    return biggest


def search(xs):
    def partial_search(xs, start, end):
        # index의 양쪽 모두 포함함, eg([1, 2, 3], s=1, e=1 이라면 [2])
        #print '+', xs, start, end
        if len(xs) == 1:
            return (evaluate(xs, 0, 0)[0], start, end, xs)
        else:
            lower_xs, upper_xs = xs[:len(xs)/2], xs[len(xs)/2:]
            rs = [partial_search(lower_xs, start, start+len(xs)/2-1),
                  partial_search(upper_xs, start+len(xs)/2, end)]

            #print ':', xs, start, end
            for s in range((end-start)/2+1):
                for e in range((end-start)/2+1, (end-start)+1):
                    r = evaluate(lower_xs + upper_xs, s, e)
                    rs += [(r[0], start+s, start+e, r[1])]

            #print rs
            return find_max(rs)

    return partial_search(xs, 0, len(xs)-1)


def bf_search(xs):
    rs = list()
    for s, _ in enumerate(xs):
        for e, __ in enumerate(xs):
            fitness, xs_ = evaluate(xs, s, e)
            rs += [(fitness, s, e, xs_)]

    return find_max(rs)


def draw(xs):
    import numpy as np
    import pylab as pl
    img = np.zeros((len(xs), len(xs)))

    for s, _ in enumerate(xs):
        for e, __ in enumerate(xs):
            fitness, xs_ = evaluate(xs, s, e)
            img[s][e] = fitness
    pl.imshow(img, interpolation='none', cmap='gray')
    pl.show()


if __name__ == '__main__':
    ENABLE_DRAW = False
    xss = [
        [7, 1, 5, 9, 6, 7, 3],
        [1, 4, 4, 4, 4, 1, 1],
        [1, 8, 2, 2],
        [3, 1, 8, 6, 2, 4, 10, 1, 8, 7],
        [2, 3, 2, 1, 6]
    ]

    for xs in xss:
        r1 = bf_search(xs)
        r2 = search(xs)
        print xs
        print r1
        print r2
        print r1 == r2
        if ENABLE_DRAW:
            draw(xs)


    from random import randint
    correct = 0
    num = 10000
    int_max = 10
    print
    print "== Test {} times ==".format(num)

    for _ in range(num):
        xs = list()
        for x in range(randint(5, int_max)):
            xs.append(randint(0, int_max))
        if ENABLE_DRAW:
            draw(xs)
        if bf_search(xs) == search(xs):
            correct += 1
        else:
            print 'not pass:', xs
    print correct, '/', num

    """
    [7, 1, 5, 9, 6, 7, 3]
    (7, 0, 0, [7])
    (7, 0, 0, [7])
    True
    [1, 4, 4, 4, 4, 1, 1]
    (1, 0, 0, [1])
    (1, 0, 0, [1])
    True
    [1, 8, 2, 2]
    (1, 0, 0, [1])
    (1, 0, 0, [1])
    True
    [3, 1, 8, 6, 2, 4, 10, 1, 8, 7]
    (3, 0, 0, [3])
    (3, 0, 0, [3])
    True
    [2, 3, 2, 1, 6]
    (2, 0, 0, [2])
    (2, 0, 0, [2])
    True

    == Test 10000 times ==
    10000 / 10000
    """

