dict_1={'a':1,'c':3,'d':4,'b':2}
sorted_dict=dict(sorted(dict_1.items(),key=lambda x:x[1]))
print(sorted_dict)