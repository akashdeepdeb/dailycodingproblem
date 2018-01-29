def balanceCheck(s):
	checker = {'}':'{', ']':'[', ')':'('}
	stack = []
	top = ''
	for i in s:
		if i == '(' or i == '[' or i == '{':
			stack.append(i)
		else:
			if len(stack):
				top = stack[-1] 
			if top != checker[i]:
				return False
			else:
				del stack[-1]
	if len(stack):
		return False
	return True


def main():
	tests = ["([])[]({})","([)]","((()","()","()[]{}","(]","([)]"]
	for t in tests:
		print(balanceCheck(t))


main()

'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''