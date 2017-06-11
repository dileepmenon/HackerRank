"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    head1 = head
    while head:
        if not head.next:
            head.next = Node(data, None)
            return head1
        head = head.next
    return Node(data, None)


