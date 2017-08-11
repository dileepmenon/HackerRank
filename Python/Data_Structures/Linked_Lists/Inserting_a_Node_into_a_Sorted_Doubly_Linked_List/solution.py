"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""


def SortedInsert(head, data):
    temp1 = head
    if temp1:
        if temp1.data > data:
            k = Node(data)
            k.next = temp1
            temp1.prev = k
            head = k
        else:
            while temp1 and temp1.data < data:
                temp = temp1
                temp1 = temp1.next
            if not temp1:
                temp1 = Node(data)
                temp.next = temp1
                temp1.prev = temp
                temp1.next = None
            else:
                k = Node(data)
                temp.next = k
                k.prev = temp
                k.next = temp1
                temp1.prev = k
    else:
        head = Node(data)
    return head
