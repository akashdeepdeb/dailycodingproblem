def missingFirstPositiveInt(inp):
	sz = len(inp)
	for idx, elem in enumerate(inp):
		if i < sz:
			inp[elem] = 1


if '__name__' == __main__:
	tests = [[3,4,-1,1], [1,2,0]]
	for t in tests:
		print(missingFirstPositiveInt(t))