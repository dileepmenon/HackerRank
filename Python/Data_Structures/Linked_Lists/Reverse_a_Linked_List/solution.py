#!bin/python3


"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    head_0 = head
    nxt = head.next
    while head:
        temp = head
        head = nxt
        if head:
            nxt = head.next
            head.next = temp
        else:
            head_0.next = None
            return(temp)
    return None
