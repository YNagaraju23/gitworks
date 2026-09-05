data={ "name": "Jake", "age": 22 }
print(data)
b=dict(name="Jake", age= 22)
print(b)

#accessing values
print(b["name"])
print(b.get("name"))
del b["name"]
print(b)

#list of dictionaries
print("list of dictionaries")
data1=[{ "name": "Jake", "age": 22 },{"name": "ram", "age": 25 }]
print(data1)
for i in data1:
    print(i.get("age"))

#remove items
data1={ "name": "Jake", "age": 22 }
data1.pop("name")
print(data1)
#remove items
data1={ "name": "Jake", "age": 22 }
val=data1.pop("age")
print("value is :",val)
print(dat1)