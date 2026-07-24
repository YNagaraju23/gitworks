#flatten list
lst = [1, 2, [3, 4], [5, 6, [7, 8, [9]]], 10]
def flatten(data):
    result=[]
    for i in data:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
print(flatten(lst))
#o/p:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]