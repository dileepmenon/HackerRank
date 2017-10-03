#!bin/python2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


def topView(root):
    temp = root
    r = [root.data]
    left_st = []
    right_st = []
    while temp.left:
        if temp.left:
            left_st.append(temp.left.data)
        temp = temp.left
    temp = root
    while temp.right:
        if temp.right:
            right_st.append(temp.right.data)
        temp = temp.right
    for i in left_st[::-1] + r + right_st:
        print i,
