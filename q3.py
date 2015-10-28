with open("file3.txt") as f:
	factor = 1
	result = 0;
	A_to_Z = [chr(i) for i in range(65,91)]
	data = f.readline()
	for c in data:
		if c in A_to_Z:
			result += (ord(c)-64)*factor
		elif c is ',':
			factor+=1
	print result