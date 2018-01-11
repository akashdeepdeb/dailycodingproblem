def multiplyallbutone(arr):
	mul = 1
	for num in arr:
		mul *= num
	return [int(mul/i) for i in arr]

if __name__ == '__main__':
	tests = [[1,2,3,4,5],[1,2,3],[0,2,3,4,5]]
	for t in tests:
		print(multiplyallbutone(t))