__author__ = 'Hyunsoo'

import pprint


def is_a_win(state=[3, 2, 1]):
    size = len(state)
    rs = dict()
    q = list()
    q.append(([0 for _ in range(len(state))], False))

    while len(q) > 0:
        current, win = q.pop()
        #print current, win
        rs.setdefault(tuple(current), False)
        rs[tuple(current)] = win and rs[tuple(current)]
        #if current == state and rs[tuple(current)]:
        #    return rs[tuple(state)]

        for i in range(size):
            for v in range(1, state[i] - current[i] + 1):
                buff = current[:]
                buff[i] += v
                if not (tuple(buff) in rs and rs[tuple(buff)]):
                    buff_win = not win
                    q.append((buff, buff_win))

    #pprint.pprint(rs)
    return rs[tuple(state)]


if __name__ == '__main__':
    xs = [
        [3, 2, 1],
        [5, 6, 7, 8],
        #[10, 10, 10, 10],
        #[50, 50, 50, 50],
    ]

    for x in xs:
        print x, is_a_win(state=x)