"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    head_0 = head
    pos = 0
    if pos == position and pos == 0:
        if head.next:
            nxt = head.next
            head.next = None
            return nxt
        else:
            return None
    while head:
        temp = head
        head = head.next
        if pos+1 == position:
            temp.next = head.next
            head.next = None
            return head_0
        pos += 1
