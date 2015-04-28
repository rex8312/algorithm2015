__author__ = 'Hyunsoo'


def test_cases():
    xs = ['geo', 'oji', 'jing']
    n = len(xs)
    yield n, xs


def bf_search(n, xs):
    for x1 in xs:
        for x2 in xs:
            if x1 != x2:
                for i in range(len(x1)):
                    pre_x1, post_x1 = x1[:i], x1[i:]
                    if x2.startswith(post_x1):
                        print pre_x1 + x2, '=', x1, '+', x2


if __name__ == '__main__':

    for n, xs in test_cases():
        bf_search(n, xs)