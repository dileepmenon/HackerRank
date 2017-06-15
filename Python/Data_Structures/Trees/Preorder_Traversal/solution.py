#!bin/python2
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def preOrder(root):
        st = [root]
        data = []
        while len(st) > 0:
            temp = st.pop()
            data.append(temp.data)
            if temp.right:
                st.append(temp.right)
            if temp.left:
                st.append(temp.left)
        for i in data:
            print i,
