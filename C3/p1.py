# -*- coding: utf-8 -*-

__author__ = 'Hyunsoo'

import numpy as np
from pprint import pprint

X = 2
W = 1
B = 0


def draw(tree):
    pass


def decode(code):
    # 코드를 입력받아 트리형태로 출력함
    root = list()
    stack = list()
    node = root

    for c in code:
        if len(node) == 4:
            # 현재 노드에 필요한 정보가 모두 입력되었다면, 부모 노드로 돌아감
            node = stack.pop()

        if c == X:
            # X가 나타나면, 새로운 리스트를 생성해서, 자식 노드를 만들고,
            # 부모노드는 자식노드의 정보가 다 입력될때까지 stack에 대기
            child = list()
            node.append(child)
            stack.append(node)
            node = child
        else:
            node.append(c)

    return root


def encode(tree):
    def is_leaf(node):
        for e in node:
            if isinstance(e, list):
                return False
        return True

    def flat(node):
        if is_leaf(node):
            return node[:]
        else:
            code = list()
            for i in range(4):
                if isinstance(node[i], list):
                    code += [X] + flat(node[i])
                else:
                    code.append(node[i])
            return code
    print tree
    return flat(tree[:])


def mirror(tree):
    def is_leaf(node):
        for e in node:
            if isinstance(e, list):
                return False
        return True

    def swap(node):
        if is_leaf(node):
            node[0], node[1], node[2], node[3] = node[2], node[3], node[0], node[1]
            return node
        else:
            for i in range(4):
                if isinstance(node[i], list):
                    node[i] = swap(node[i])
            node[0], node[1], node[2], node[3] = node[2], node[3], node[0], node[1]
            return node

    return swap(tree[:])


def print_code(code):
    for c in code:
        if c == X:
            print 'X',
        elif c == W:
            print 'w',
        elif c == B:
            print 'b',
    print


if __name__ == '__main__':
    code = [X, W, W, W, B, X, W, X, W, B, B, B, W, W, X, X, X, W, W, B, B, B, W, W, W, W, B, B]
    tree = decode(code)
    tree = mirror(tree)
    icode = encode(tree)

    print_code(code)
    print_code(icode)

