import random
print(random.random())
print(random.randint(20,30))
print(random.uniform(20,30))
fruits = ["apple", "banana", "cherry"]

print(random.choice(fruits))        # Single random item
print(random.choices(fruits,k=3))  # List of random items (with replacement)
print(random.sample(fruits, 2))     # Unique random items