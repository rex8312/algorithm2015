__author__ = 'Hyunsoo'

import pprint


def is_a_win(state=[3, 2, 1]):
    size = len(state)
    db = dict()
    aux_db = dict()
    q = list()
    end_state = [0 for _ in range(len(state))]
    q.append(end_state)
    db.setdefault(tuple(end_state), [False])

    while len(q) > 0:
        child = q.pop()
        #print current, win

        for i in range(size):
            for v in range(1, state[i] - child[i] + 1):
                parent = child[:]
                parent[i] += v
                q.append(parent)
                db.setdefault(tuple(parent), list())
                aux_db.setdefault(tuple(parent), list())
                parent_win = reduce(lambda x1, x2: x1 and x2, map(lambda x: not x, db[tuple(child)]))
                db[tuple(parent)].append(parent_win)
                aux_db[tuple(parent)].append((child,
                    reduce(lambda x1, x2: x1 or x2, db[tuple(child)]))
                )

    #print
    pprint.pprint(aux_db)
    print db[tuple(state)]
    return reduce(lambda x1, x2: x1 or x2, db[tuple(state)])
    #print reduce(lambda x1, x2: x1 and x2, map(lambda x: not x, [False, False, False]))
    #return not reduce(lambda x1, x2: not x1 and not x2, cache[tuple(state)], False)


if __name__ == '__main__':
    xs = [
        [1, 0, 0],
        [2, 1, 0],
        #[3, 2, 1],
        #[5, 6, 7, 8],
        #[10, 10, 10, 10],
        #[50, 50, 50, 50],
    ]

    for x in xs:
        print x, is_a_win(state=x)
        print