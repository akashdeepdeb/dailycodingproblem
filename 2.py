def multiplyallbutone(arr):
	mul = 1
	for num in arr:
		mul *= num
	return [int(mul/i) for i in arr]

if __name__ == '__main__':
	tests = [[1,2,3,4,5],[1,2,3],[0,2,3,4,5]]
	for t in tests:
		print(multiplyallbutone(t))


'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''