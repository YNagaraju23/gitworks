# When you write my_object[index], 
# Python internally intercepts the operation and calls my_object.__getitem__(index).
lst=[1,2,300,4,5]
print(lst.__getitem__(3))
dictionary={"a":2,"b":3,"c":4}
dictionary.__setitem__("b",300)
print(dictionary)
dictionary._delitem__(b)
print(dictionary)