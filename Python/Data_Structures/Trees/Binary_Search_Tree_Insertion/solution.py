#!bin/python2
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


def insert(r,val):
    temp = r
    if r:
        while temp:
            if val > temp.data:
                ins_node = temp
                temp = temp.right
            elif val < temp.data:
                ins_node = temp
                temp = temp.left
        if val > ins_node.data:
            ins_node.right = Node(val)
        elif val < ins_node.data:
            ins_node.left = Node(val)
        return r
    else:
        return Node(val)
