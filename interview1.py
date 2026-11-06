<<<<<<< HEAD
words = ["eat", "tea", "eattea"]
=======
words = ["eat", "tea", "tan", "ate", "nat", "bat",'tab']
>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03
result={}
for word in words:
    key=''.join(sorted(word))
    if key not in result:
        result[key]=[]
    result[key].append(word)
print(list(result.values()))
