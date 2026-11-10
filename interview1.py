words = ["eat", "tea", "tan", "ate", "nat", "bat",'tab']
result={}
for word in words:
    key=''.join(sorted(word))
    if key not in result:
        result[key]=[]
    result[key].append(word)
print(list(result.values()))


#diff b/w sort and sorted
#words.sort() #sort changes that list
#print(words)

b=sorted(words) # sorted creates new list
print(b)
    
