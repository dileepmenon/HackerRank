"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    head_0 = head
    pos = 0
    if pos == position and pos == 0:
        head = Node(data, head)
        return head
    while head:
        temp = head
        head = head.next
        if pos+1 == position:
            if not head:
                temp.next = Node(data, None)
                return head_0
            else:
                temp.next = Node(data, head)
                return head_0
        pos += 1
