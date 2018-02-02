class Codec:
	def encode(self, string):
		ans = ''
		j = 0
		while j < len(string):
			curr = string[j]
			count = 0
			while j < len(string) and string[j] == curr:
				count+=1
				j+=1
			ans += str(count)+curr
		return ans


	def decode(self, string):
		ans = ''
		for i in range(0, len(string), 2):
			ans += int(string[i])*string[i+1]
		return ans


def main():
	tests = ['AAAABBBCCDAA', '']
	for t in tests:
		obj = Codec()
		print(True) if obj.decode(obj.encode(t)) == t else print(False)

main()