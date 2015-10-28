data = [i.strip() for i in open("file.txt",'r')]
first = max(data)
data.remove(first)
second = max(data)
data.remove(second)
third =max(data)
print first
print second
print third
	
