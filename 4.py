def missingFirstPositiveInt(inp):
	sz = len(inp)

	#i think this is O(n)
	for i, val in enumerate(inp):
		if val != '' and val > 0:
			curr = val
			while curr != '' and curr > 0:
				if curr > len(inp):
					inp[i] = 0
					break
				else:
					temp = inp[curr-1]
					inp[curr-1] = ''
					curr = temp

	for i in range(len(inp)):
		if inp[i] != '':
			return i+1
	return len(inp)+1

def main():
	tests = [[3,4,-1,1], [1,2,0], [], [1], [1,2], [2]]
	for t in tests:
		print(missingFirstPositiveInt(t))

main()

'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''