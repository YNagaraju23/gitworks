<<<<<<< HEAD
=======
test_dict={'a':1,'b':2}
>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03
def test(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(f"{i}:{j}")
<<<<<<< HEAD
test([1,2,3],a=1,b=2)
=======
test([1,2,3],test_dict)
>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03


test_dict={'a':1,'b':2}
print(test_dict)