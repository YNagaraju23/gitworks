dict_1={"a":1,"c":3,"b":2}
result={value:key for key,value in dict_1.items()}
print(result)
#print(dict(result.items()))
print("****************")

converted = dict(sorted(result.items()))
print(converted)
result={value:key for key,value in converted.items()}
print(result)

print("****************")
dict_1={"a":1,"c":3,"b":2}
result = dict(sorted(dict_1.items()))
print(result)

print("****************")
dict_1={"a":1,"raju":3,"b":2}
result = {key:value for key,value in dict_1.items() if "a" in key }
print(result)

print("****************")
a=['a','b','c','d','e']
b=(1,2,3,4,5)
finaldict={keys:values for keys,values in zip(a,b)}
print(finaldict)
