# -*-coding: utf-8 -*-

__author__ = 'Hyunsoo'

VERBOSE = False


def mirror(code, depth=0, idx=0):
    xs = code.lower()

    if len(xs) < 1:
        return ''
    else:
        if xs[0] == 'x':
            if VERBOSE:
                print ' ' * depth, code[0]
            start_index = 1
            end_index = 2
            curr_index = start_index
            rs = list()
            for i in range(4):
                try:
                    while curr_index < end_index:
                        if xs[curr_index] == 'x':
                            end_index += 4
                        curr_index += 1
                    r0 = mirror(code[start_index: end_index], depth+1)
                    rs.append(r0)
                    start_index = end_index
                    end_index = start_index + 1
                except IndexError:
                    print 'code:', code[start_index: end_index]
                    print code, curr_index
                    exit()

            rs[0], rs[1], rs[2], rs[3] = rs[2], rs[3], rs[0], rs[1]
            return 'X' + ''.join(rs)
        elif len(xs) == 1:
            if VERBOSE:
                print ' ' * depth, xs
            return xs
        else:
            r0 = mirror(code[0], depth)
            rs = mirror(code[1:], depth)
            return r0 + rs


if __name__ == '__main__':
    code = "Xwwbb"
    code = "XwXwwbbbw"
    code = "XwXwXwwbbbbbw"
    code = "XXwwwbXwXwbbbwwXXXwwbbbwwwwbb"

    print code
    rcode = mirror(code)
    print rcode
    ccode = mirror(rcode)
    print ccode