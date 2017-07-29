#!bin/python2
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def find_ancestors(root, v):
    temp = root
    ancs = [root]
    while temp:
        if v > temp.data:
            temp = temp.right
            if temp:
                ancs.append(temp)
        elif v < temp.data:
            temp = temp.left
            if temp:
                ancs.append(temp)
        else:
            break
    return ancs


def lca(root, v1, v2):
    ancs1 = find_ancestors(root, v1)
    ancs2 = find_ancestors(root, v2)
    common_ancs = root
    for i in ancs1[-1::-1]:
        for j in ancs2[-1::-1]:
            if i == j:
                return i
    return common_ancs
