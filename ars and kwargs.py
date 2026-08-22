test_dict={'a':1,'b':2}
def test(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(f"{i}:{j}")
test([1,2,3],test_dict)


test_dict={'a':1,'b':2}
print(test_dict)