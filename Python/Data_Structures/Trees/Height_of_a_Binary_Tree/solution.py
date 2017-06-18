#!bin/python2
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

from collections import deque


def height(root):
    t = 0
    q = deque([(root, 0)])
    while q:
        temp, num = q.pop()
        if temp.left:
            q.appendleft((temp.left, num+1))
            t = num + 1
        if temp.right:
            q.appendleft((temp.right, num+1))
            t = num + 1
    return t
