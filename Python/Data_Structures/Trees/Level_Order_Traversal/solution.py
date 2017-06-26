#!bin/python2
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

from collections import deque


def levelOrder(root):
	q = deque([root])
	while len(q) > 0:
		temp = q.pop()
        print temp.data,
		if temp.left:
			q.appendleft(temp.left)
        if temp.right:
			q.appendleft(temp.right)
