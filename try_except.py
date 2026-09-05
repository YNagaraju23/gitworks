try:
    print("Hello, World!")
except Exception as e:
    print("An error occurred: {}".format(e))


slice = "Hello, World!"
print(slice[0:5])

a=[1, 2, 3, 4, 5]
b=[7, 8, 9, 10, 11]
mydict={a:b for (a,b) in  zip(a,b)}
print(mydict)


mylist = list(i for i in range(5))
print(mylist)