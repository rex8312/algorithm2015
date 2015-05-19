__author__ = 'Hyunsoo'

import pprint
import Queue


def is_a_win(state):
    size = len(state)
    state = sorted(state)
    end_state = [0 for _ in range(len(state))]

    db = dict()
    q = Queue.LifoQueue()
    hs = list()
    cnt = 0

    db.setdefault(tuple(end_state), False)
    db.setdefault(tuple(sorted(state)), False)
    q.put(end_state)

    while q.qsize() > 0:
        child = tuple(sorted(q.get()))

        if child not in hs:
            hs.append(child)
            #print child, db[child]
            cnt += 1
            print '\r', cnt, q.qsize(),

            parent_set = list()
            for i in range(size):
                for v in range(1, state[i] - child[i] + 1):
                    parent = list(child[:])
                    parent[i] += v
                    parent = tuple(sorted(parent))
                    if parent not in parent_set:
                        parent_set.append(parent)

            for parent in parent_set:
                db.setdefault(parent, None)
                if not db[child]:
                    db[parent] = True

                if parent not in hs:
                    q.put(parent)

                #print parent, db[parent]

        if db[tuple(sorted(state))]:
            return True

            #print
    #pprint.pprint(db)
    return db[tuple(sorted(state))]


if __name__ == '__main__':
    xs = [
        #[1, 0, 0],
        #[10, 10, 0],
        [2, 1, 0],
        [3, 2, 1],
        #[1, 2, 3],
        #[3, 1, 2],
        [5, 6, 7, 8],
        [10, 10, 10, 10],
        [50, 50, 50, 50],
    ]

    for x in xs:
        print x
        print is_a_win(state=x)
        print