
str1=["Kolkata", "Pune", "Chennai", "Bengaluru"]
n=0
for i in str1:
	lenth = len(i)
	if lenth > n:
		n=lenth
		long_str = i
print(n)
print(long_str)