import gc
gc.enable()
print(gc.isenabled())
class A:
    pass   
obj1=A()
obj2=A()
obj1.friend=obj2
obj2.friend=obj1
collected_objects=gc.collect()
print(collected_objects)

