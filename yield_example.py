a=[[1,2],[3,4],[5,6]]
a=[i for j in a for i in j]
print(a)


def return_fun(a):
    for i in a:
        yield i
b=[1,2,3,4,5]
print(list(return_fun(b)))