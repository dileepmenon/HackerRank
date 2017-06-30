#!bin/python3

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def MergeLists(headA, headB):
	#Without Recursion
    temp0 = None
    temp1 = headA
    temp2 = headB
    if temp1 and temp2:
        if temp1.data >= temp2.data:
            temp0 = temp2
            temp2 = temp2.next
            head = headB
        else:
            temp0 = temp1
            temp1 = temp1.next
            head = headA
        while temp1 and temp2:
            if temp1.data >= temp2.data:
                temp0.next = temp2
                temp0 = temp2
                temp2 = temp2.next
            else:
                temp0.next = temp1
                temp0 = temp1
                temp1 = temp1.next
        while temp1:
            temp0.next = temp1
            temp0 = temp1
            temp1 = temp1.next
        while temp2:
            temp0.next = temp2
            temp0 = temp2
            temp2 = temp2.next
        temp0.next = None
        return head
    else:
        if temp1:
            return temp1
        else:
            return temp2
