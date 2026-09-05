z=lambda x:lambda y: x*y
a=z(20)(30)
print(a)

z=lambda x,y:x*y
print(z(10,20))