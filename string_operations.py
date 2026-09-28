import re
str="hyderabad%#$banglore"
symbol="~!@#$%^&*()_+"
#method=f'[a-z]'
#result=re.findall(method,str) # ['h', 'y', 'd', 'e', 'r', 'a', 'b', 'a', 'd']

#method=r'[^\w]'
#result=re.findall(method,str)
#print("".join(result))   # %#$


method=r'[a-z]+'
result=re.findall(method,str)
print(result)  #  ['h', 'y', 'd', 'e', 'r', 'a', 'b', 'a', 'd']
#print("".join(result))   # hyderabad

#print(result)