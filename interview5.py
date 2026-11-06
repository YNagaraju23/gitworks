import re
str1="nagaraju@gmail.com"
str2=re.split(str1,"@")
str3=str1.split("@")
print(str3)
if isinstance(str1,str) and isinstance(str3,str):
    print("str1 is a string")