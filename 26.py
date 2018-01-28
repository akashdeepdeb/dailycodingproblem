class linked_list_node:
	def __init__(self, val):
		self.val = val
		self.next = None

def removeKthLast(head, k):
	k+=1
	temp = head
	while k > 0:
		temp  = temp.next
		k-=1
	p1 = temp
	p2 = head
	while p1 is not None:
		p1 = p1.next
		p2 = p2.next
	p3 = p2.next
	p2.next = p3.next
	del p3
	return head

def printList(head):
	temp = head
	while temp is not None:
		print(temp.val)
		temp = temp.next

def main():
	array = [2,4,5,9,8,3,67,23,45,87,15,7,3,64,12,32,49,40]
	head = linked_list_node(array[0])
	temp = head
	for i, element in enumerate(array[1:]):
		curr = linked_list_node(element)
		temp.next = curr
		temp = curr

	k = 4
	removeKthLast(head, k)
	printList(head)

main()

'''
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''
