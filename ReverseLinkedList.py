def reverseLinkedList(head):
	"""
	Args:
		{Node} head
	Returns:
		{Node} Head of the reversed linked list.
	"""
	# Write your code here.
	previous = None
	current = head
	
	while current is not None:
		next = current.next 	# n1 -> [n2] -> n3
		current.next = previous # [n1] -> n2 -> n3
		previous = current	# n1 -> n2 -> n3
		current = next	# n1 -> n2 -> n3
	head = previous
	
	return head