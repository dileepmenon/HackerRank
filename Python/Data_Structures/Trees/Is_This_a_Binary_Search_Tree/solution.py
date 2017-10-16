""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
s = []
def inord(root):
    if root is None:
        return
    if root.left:
        inord(root.left)
    s.append(root.data)
    if root.right:
        inord(root.right)


def check_binary_search_tree_(root):
    inord(root)
    return s == sorted(s) and len(set(s)) == len(s)
