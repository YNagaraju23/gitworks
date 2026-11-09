# Example 1
def apply(func,x):
  return func(x)
def square(a):
  return a*a
print(apply(square,6))
print("*"*50)

#Example 2
def multiply(n):
    return lambda x:x*n
double=multiply(2)
triple=multiply(3)
print(double(5))
print(triple(5))
print("*"*50)

#Example 3
def create_counter(start):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = create_counter(5)
print(counter())
print(counter())
print(counter())