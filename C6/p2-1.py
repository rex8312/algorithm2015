__author__ = 'Hyunsoo'


def test_cases():
    xs = ['geo', 'oji', 'jing']
    n = len(xs)
    yield n, xs


def bf_search(n, xs):
    def find_unused_number(n, xs):
        ys = set(range(n)) - set(xs)
        return list(ys)

    def gen_seq(n, xs=list()):
        if len(find_unused_number(n, xs)) == 0:
            yield xs
        else:
            for x in find_unused_number(n, xs):
                for xs_ in gen_seq(n, xs[:] + [x]):
                    yield xs_

    strings = list()
    for orders in gen_seq(n):
        tx = [None for _ in range(len(orders))]
        for ord, x in zip(orders, xs):
            tx[ord] = x

        buff = ''
        for i, x in enumerate(tx):
            possible = list()
            for j in range(1, len(x)):
                if buff.endswith(x[:j]):
                    possible.append((j, x[:j]))

            if len(possible) == 0:
                buff += x
            else:
                possible = sorted(possible, key=lambda item: len(item[1]))
                j = possible[0][0]
                buff += x[j:]

        strings.append(buff)

    strings.sort(key=lambda x: len(x))
    return filter(lambda x: len(x) == len(strings[0]), strings)


if __name__ == '__main__':

    for n, xs in test_cases():
        print bf_search(n, xs)