import functools
students={'john':80, "alice":95, "bob":75}
print(students)
result=dict(sorted(students.items(),key=lambda x:x[0]))
print(result)
<<<<<<< HEAD
=======
#sorted(students,key=lambda x:x[1])
>>>>>>> 96bab3c6334f4daa21158864506ea63d294fcd03
list1=[20,10,30,50,40]
map1=list(map(lambda x:x*2, list1))

print(map1)
reduce1=functools.reduce(lambda x,y:x*y, list1)
print(reduce1)
filter1=list(filter(lambda x:x%3 == 0, list1))
print(filter1)