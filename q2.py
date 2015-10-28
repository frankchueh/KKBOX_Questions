with open("file.txt",'r') as f:
	first, second, third = 0, 0, 0
	for line in f:
		if line > first:
			first, second, third = line, first, second
		elif line > second:
			second, third = line, second
		elif line > third:
			third = line
	
	print first
	print second
	print third
	
