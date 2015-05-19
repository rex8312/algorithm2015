__author__ = 'rex8312'


def is_win(state):
    parent = tuple(sorted(filter(lambda x: x != 0, state)))
    if parent in bb:
        return bb[parent]

    for i in range(len(parent)):
        for v in range(1, parent[i] + 1):
            child = list(parent[:])
            child[i] -= v
            child = tuple(child)
            if not is_win(child):
                bb[parent] = True
                return True

    bb[parent] = False
    return False


if __name__ == '__main__':
    bb = dict()
    bb[tuple()] = False
    bb[tuple([0])] = False

    xs = [
        [1, 0, 0],
        [2, 1, 0],
        [3, 2, 1],
        [10, 10, 0],
        [1, 2, 3],
        [3, 1, 2],
        [5, 6, 7, 8],
        [10, 10, 10, 10],
        [50, 50, 50, 50],
        [83, 1, 2],
    ]

    import pprint
    import time
    import datetime

    for x in xs:
        stime = time.clock()
        print x
        print is_win(x)
        etime = time.clock()
        print datetime.timedelta(seconds=etime-stime)
        #pprint.pprint(bb)
        print
