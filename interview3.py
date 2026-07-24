a=[1,3,5]
b=[2,4,6]
list1=[(i,j) for i,j in zip(a,b)]
list1=[i for row in list1 for i in row]

#result = [num for row in matrix for num in row]
print(list1)
#o/p: [1, 2, 3, 4, 5, 6]