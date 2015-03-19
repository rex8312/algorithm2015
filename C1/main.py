__author__ = 'Hyunsoo'


import numpy as np
import pylab as pl


def generate_xs(n, lower_bound=-10, upper_bound=10):
    return np.random.randint(lower_bound, upper_bound, n)


def evaluate(xs, start, end):
    xs = xs[start:end]
    return sum(xs)

xs = generate_xs(10)
ys = evaluate(xs, 4, 5)
print xs
print ys



N = 10
LB = -10
UB = 10

def draw_surface(xs, n=N):
    img = np.zeros((N, N))
    for x in range(N):
        for y in range(N):
            img[y][x] = evaluate(xs, x, y)
    print img
    pl.imshow(img, cmap='gray', interpolation='none', origin='upper')


xs = generate_xs(N, LB, UB)
print xs
draw_surface(xs)


from operator import itemgetter

N = 10
LB = -10
UB = 10


def bf_search(xs, n=N):
    rs = list()
    for x in range(N):
        for y in range(N):
            if x <= y:
                rs.append((x, y, evaluate(xs, x, y)))
    rs.sort(key=itemgetter(2), reverse=True)
    rs = filter(lambda x: x[2] == rs[0][2], rs)
    return sorted(rs)


xs = generate_xs(N, LB, UB)
print xs
draw_surface(xs)
bf_search(xs)


N = 10
LB = -10
UB = 10


def search(xs, n=N):
    rs = list()
    for x in range(N-1):
        rs.append((x, N, evaluate(xs, x, N)))

    rs.sort(key=itemgetter(2), reverse=True)
    rs = filter(lambda x: x[2] == rs[0][2], rs)
    best_xs = map(lambda r: r[0], rs)

    print 'best', best_xs
    rs = list()
    for x in best_xs:
        for y in range(N):
            if x <= y:
                rs.append((x, y, evaluate(xs, x, y)))

    rs.sort(key=itemgetter(2), reverse=True)
    rs = filter(lambda x: x[2] == rs[0][2], rs)
    return rs[0]

xs = generate_xs(N, LB, UB)
print xs
draw_surface(xs)
print bf_search(xs)
print search(xs)


