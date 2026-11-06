#no need to define lst in call once procedure is defined lst(list) is created.
def add_item(item, lst=[]):#def add_item(item, lst=None)--wrong statement
    lst.append(item)
    return lst
print(add_item(4))
print(add_item(5))
print(add_item(6))



#isinstance method in python
x=10.2
if isinstance(x,(int,float,str)):
    print("x is valid")