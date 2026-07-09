words = ["eat", "tea", "eattea"]
result={}
for word in words:
    key=''.join(sorted(word))
    if key not in result:
        result[key]=[]
    result[key].append(word)
print(list(result.values()))
