# Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    if not headA or not headB:
        return 0
    while headA and headB:
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    if not headA and not headB:
        return 1
    else:
        return 0
