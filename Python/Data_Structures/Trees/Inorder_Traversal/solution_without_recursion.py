"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
#Using Stacks(without recursion)


def inOrder(root):
    if not root:
        return root.data
    temp = [root]
    ro = root.left
    while temp:
        while ro:
            temp.append(ro)
            ro = ro.left
        ro = temp.pop()
        print ro.data,
        if ro.right:
            temp.append(ro.right)
            ro = ro.right.left
        else:
            ro = ro.right
