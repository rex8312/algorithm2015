__author__ = 'Hyunsoo'

import pprint


def is_a_win(state):
    size = len(state)
    state = sorted(state)
    end_state = [0 for _ in range(len(state))]

    db = dict()
    q = list()
    hs = list()

    db.setdefault(tuple(end_state), False)
    q.append(end_state)

    while len(q) > 0:
        child = q.pop(0)
        if child in hs:
            print '.',
        if child not in hs:
            hs.append(child)

            for i in range(size):
                for v in range(1, state[i] - child[i] + 1):
                    parent = child[:]
                    parent[i] += v

                    db.setdefault(tuple(sorted(parent)), False)
                    if not db[tuple(sorted(child))]:
                        db[tuple(sorted(parent))] = True

                    q.append(parent)

    #pprint.pprint(db)
    return db[tuple(sorted(state))]


if __name__ == '__main__':
    xs = [
        [1, 0, 0],
        [2, 1, 0],
        [3, 2, 1],
        [1, 2, 3],
        [3, 1, 2],
        #[5, 6, 7, 8],
        #[10, 10, 10, 10],
        #[50, 50, 50, 50],
    ]

    for x in xs:
        print x
        print is_a_win(state=x)
        print