"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def ReversePrint(head):
	node_data = []
	while head:
		node_data.append(head.data)
		head = head.next
	if node_data:
		for i in node_data[::-1]:
			print(i)
