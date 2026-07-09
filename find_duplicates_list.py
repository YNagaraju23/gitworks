lst=[1,2,3,2,4,5,1,6,3]
seen=set()
duplicates=set()
for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(list(duplicates))
print(list(seen))