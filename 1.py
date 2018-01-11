class Stack:
	def __init__(self):
		self.stack = []

	def __str__(self):
		return ', '.join(str(x) for x in self.stack)

	def push(self, val):
		return self.stack.append(val)

	def pop(self):
		if self.is_empty():
			return None
		return self.stack.pop()

	def is_empty(self):
		return len(self.stack) == 0

	def size(self):
		return len(self.stack)

	def peak(self):
		return self.stack[-1]
 		

class Queue:
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ', '.join(str(x) for x in self.queue)

	def enqueue(self, val):
		return self.queue.append(val)

	def dequeue(self):
		if not self.is_empty():
			return self.queue.pop(0)
		return None

	def size(self):
		return len(self.queue)

	def is_empty(self):
		return len(self.queue) == 0

	def front(self):
		if not self.is_empty():
			return self.queue[0]
		return None


def interleaved(stk):
	que = Queue()

	#enqueue all stack elements
	for i in range(stk.size()):
		que.enqueue(stk.pop())
	
	n = int(que.size()/2)
	m = que.size() - n

	#dequeue and enqueue half of the elements
	for i in range(n):
		que.enqueue(que.dequeue())

	#push the other half on to the stack
	for i in range(m):
		stk.push(que.dequeue())
	first = stk.peak()

	#interleave in the queue till stack is empty
	while not stk.is_empty():
		que.enqueue(stk.pop())
		if que.front() != first:
			que.enqueue(que.dequeue())

	#dequeue and push all elements onto original stack
	while not que.is_empty():
		stk.push(que.dequeue())

	#print stack
	print(stk)
	

if __name__ == '__main__':
	input_arr = [1,2,3,4,5,6,7,8]
	stk = Stack()
	for i in input_arr:
		stk.push(i)
	interleaved(stk)

'''
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwords from the end state.

'''

