'''
Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing links between nodes.

Examples:

Input : Head of following linked list
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL

Input : Head of following linked list
       1->2->3->4->5->NULL
Output : Linked list should be changed to,
       5->4->3->2->1->NULL

Input : NULL
Output : NULL

Input  : 1->NULL
Output : 1->NULL
'''

def reverse_linked_list(self, head_ptr):
       # Set previous = None, Current = head, next = current
       # iterate until current = None
       # within each Iteration, set the next node of current = previous
       # Previous = current, current = next, next = next node

       return