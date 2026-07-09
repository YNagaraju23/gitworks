str="nagaraju"
len=len(str)
count=0
for i in str:
    if i in "aeiou":
        #print(i)
        count+=1
print("vowels count is: ",count)
print("consonants count is: ",len-count)