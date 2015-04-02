# -*-coding: utf-8 -*-

__author__ = 'Hyunsoo'


def mirror(code, depth=0, idx=0):
    xs = code.lower()

    if len(xs) < 1:
        return ''
    else:
        if xs[0] == 'x':
            print ' ' * depth, code[0]
            start_index = 1
            end_index = 4
            curr_index = start_index

            while curr_index <= end_index:
                if xs[curr_index] == 'x':
                    end_index += 4
                curr_index += 1

            r0 = 'X' + mirror(code[start_index: end_index+1], depth+1)
            r1 = mirror(code[end_index+1:], depth)
            return r0 + r1
        elif len(xs) == 1:
            print ' ' * depth, xs
            return xs
        else:
            r0 = mirror(code[0], depth)
            rs = mirror(code[1:], depth)
            return r0 + rs


if __name__ == '__main__':
    code = "Xwwwb"
    code = "XwXwwwbwb"
    code = "XXwwwbXwXwbbbwwXXXwwbbbwwwwbb"

    print code
    rcode = mirror(code)
    print rcode

    """
    code = [X, W, W, W, B, X, W, X, W, B, B, B, W, W, X, X, X, W, W, B, B, B, W, W, W, W, B, B]

    tree = decode(code)
    draw(tree, 'original')
    tree = mirror(tree)
    icode = encode(tree)

    print_code(code)
    print_code(icode)
    draw(tree, 'inverted')
    """

