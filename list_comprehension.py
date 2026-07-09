matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for i in matrix:
    for j in i:
        print(j)
        
result = [j for i in matrix for j in i]
print(result)
print("**********"*3)

result = [[i*j for i in range(1,10)] for j in range(1,10)]
print(result)
print("**********"*3)

l=["mumbai","hyderabad","banglore","karnataka"]
max_len = max(len(word) for word in l)
result = [word for word in l if len(word) == max_len]
print(result)