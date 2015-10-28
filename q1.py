def is_perfect(n):
	i = sum(i for i in range(1,n/2+1) if n%i==0)
	if i==n:
		return True
	else:
		return False

n = raw_input()
print is_perfect(int(n))



